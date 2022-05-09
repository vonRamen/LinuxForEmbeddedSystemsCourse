import gtts
from time import sleep
import speech_recognition as sr
import pyttsx3
import os
import requests
import time
from datetime import datetime, time, date
from pygame import mixer
import json
import threading

# Spotify 
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials


# Dialogflow
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToDict
from google.cloud import dialogflow_v2beta1 as dialogflow

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

mixer.init() 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

DIALOGFLOW_PROJECT_ID = 'alexa-elxq'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'
global alarmSoundPath
alarmSoundPath = "/static_files/generic_alarm.mp3"
global dateTimeForNextAlarm
dateTimeForNextAlarm = None

dayoftheweekToString = {0: "Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}

def playsound(path, block=True):
    mixer.init()
    mixer.music.load(ROOT_DIR+path)
    mixer.music.play()
    while mixer.music.get_busy() == True and block == True:
        continue

def sayToAgent(sentence):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=sentence, language_code=DIALOGFLOW_LANGUAGE_CODE)
    print("User: "+sentence)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    
    return handleQueryResults(response)

def say(sentence):
    try:
        print("Kjeld: "+sentence)
        tts = gtts.gTTS(text=sentence, tld='co.uk', lang="en", slow=False)
        tts.save("temp.mp3")
        playsound("temp.mp3")
        os.remove("temp.mp3")
        return True
    except(e):
        print(e)
        return False


# Returns true for followup intent
def handleQueryResults(response):
    displayName = response.query_result.intent.display_name
    text = response.query_result.fulfillment_text
    
    #print(response.query_result)

    if(displayName == "Alarm clock setup"):
        if len(response.query_result.parameters["date"]) == 0 or len(response.query_result.parameters["time"]) == 0:
            say(text)
            return True

        time = response.query_result.parameters["time"]
        date = response.query_result.parameters["date"]

        time_split = time.split("T")[1].split("+")[0].split(":")
        date_split = date.split("T")[0].split("-")

        global dateTimeForNextAlarm
        dateTimeForNextAlarm = datetime(int(date_split[0]), int(date_split[1]), int(date_split[2]), int(time_split[0]), int(time_split[1]), 0)
        
        today = datetime.today()

        weekday = dateTimeForNextAlarm.weekday()
        delta = dateTimeForNextAlarm - today
        if(delta.days == 0):
            wordForDateOfNextAlarm = "Today"
        elif(delta.days == 1):
                wordForDateOfNextAlarm = "Tomorrow"
        else:
            wordForDateOfNextAlarm = dayoftheweekToString[weekday] +" the date of " + "%s-%s-%s" % (date_split[2], date_split[1], date_split[0])

        timeString = "%s:%s" % (time_split[0], time_split[1])
        say("Alright, setting an alarm for: "+wordForDateOfNextAlarm +  " at "+timeString)

        return False
        
    elif(displayName == "SpotifyPlayer"):
        say(text)
        song = response.query_result.parameters["SongTitle"][0]
        if(len(response.query_result.parameters["music-artist"]) != 0):
            artist = response.query_result.parameters["music-artist"][0]
            playSong(artist, song)
        else:
            playSong("", song)

        return False

    say("Sorry, I did not get that. Try again!")
    return True

soundsLikeKjeld = ["sharon", "karen", "kim", "cute", "kill", "chill", "carol", "shelby", "google", "shut up"]

def shouldStartNextListen(sentence):
    nextCouldBeKjeld = False
    for word in sentence.split():
        if nextCouldBeKjeld:
            nextCouldBeKjeld = False
            if word in soundsLikeKjeld:
                return True

        if word == "ok":
            nextCouldBeKjeld = True
    
    return False

 

SPOTIPY_CLIENT_ID='da237a0330024c4aabfbcfde568ddba3'
SPOTIPY_CLIENT_SECRET='b89ba1fb3fcc4ad78a48f528468e7c97'

spotify = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))


def playSong(artist, track=""):
    searchQuery = track + ' ' + artist

    searchResults = spotify.search(q=searchQuery, type="track")
    for track in searchResults['tracks']['items']:
        if(track['preview_url'] == None):
            continue

        print('audio    : ' + track['preview_url'])
        URL = track['preview_url']
        response = requests.get(URL)
        open("temp.mp3", "wb").write(response.content)
        mixer.music.load('temp.mp3') # loads the music, can be also mp3 file.
        mixer.music.play() # plays the music
        return
    
    say("Could not find the requested song: "+track)

     
#say("Starting alarm clock.")

#
listening = False
listenerThreadInUse = False
def listeningThread(listenImmediately = False):
    # Initialize the recognizer
    r = sr.Recognizer()
    # Loop infinitely for user to
    # speak
    listening = True
    listeningForNextSentence = listenImmediately
    listenerThreadInUse = True
    print("Listening...")
    while(listening):   
        
        # Exception handling to handle
        # exceptions at the runtime
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input
                print("Listening for audio")
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                sentence = r.recognize_google(audio2)
                sentence = sentence.lower()

                
                global alarmIsRinging
                if(alarmIsRinging == True and "stop" in sentence):
                    # Reset for the following day
                    global dateTimeForNextAlarm
                    dateTimeForNextAlarm = dateTimeForNextAlarm + 24*60*60*1000

                    # Make it stop by overriding the sound with another one. 
                    alarmIsRinging = False
                    playsound("static_files/listening.wav", False)

    
                if listeningForNextSentence:
                    listeningForNextSentence = sayToAgent(sentence)

                    if listeningForNextSentence:
                        playsound("static_files/listening.wav", False)

                else:
                    listeningForNextSentence = shouldStartNextListen(sentence)
                    if(listeningForNextSentence):
                        mixer.music.stop()
                        playsound("static_files/listening.wav", False)
                    pass
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occured")
        
        # For some reason it doesn't recognize speach after some time. Maybe this fixes the issue.
        r = sr.Recognizer()

    listenerThreadInUse = False

global alarmIsRinging
alarmIsRinging = False

alarmIsOn = True
def alarmThread():
    print("Starting alarm thread")
    while alarmIsOn:
        sleep(1)

        if dateTimeForNextAlarm == None:
            continue
        else:
            print("Alarm is set")

        today = datetime.today()

        while today > dateTimeForNextAlarm:
            global alarmIsRinging
            alarmIsRinging = True
            print("Starting alarm")
            playsound(alarmSoundPath)

global micThread
def restartMicThread():
    listening = False
    print("Restarting mic thread")
    while(listenerThreadInUse):
        pass
        
    micThread = threading.Thread(target=listeningThread, args=(True,))
    micThread.start()
    print("Mic Thread restarted")

isOn = True
if __name__ == "__main__":
    playsound("static_files/start_up.mp3")

    # say("Hi there! My name is Kjeld and I am your personal alarm clock.")
    micThread = threading.Thread(target=listeningThread, args=())
    micThread.start()

    alarmThread = threading.Thread(target=alarmThread, args=())
    alarmThread.start()

    # Simulate button on alarm pressed:
    while isOn:
        sleep(1)
        pass

    listening = False
    alarmIsOn = False