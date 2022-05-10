var categorySubfolder = "category-pages/";

function addCategory(name) {
    var categoryBinding = _createCategoryJSBinding(name)
    $('#navbar-categories').append(`<li id = ${categoryBinding.name}><a href="${"/" + categorySubfolder + categoryBinding.id + ".php"}"> ${categoryBinding.name} </a></li>`)
}

function _createCategoryJSBinding(name) {
    return {
        name: name,
        // Replace space with nothing
        id: name.replace(/\s+/g, '')
    }
}

$(document).ready(function () {
	addCategory("Temperature");
	addCategory("Humidity");
	addCategory("CO2");
});


//API Call
var apiUrlRoot = "http://"+location.host+"/bridge.php";
console.log("API URL: "+apiUrlRoot)

function _getData(type, gateway, worker, topic, from = 0, to = Number.MAX_SAFE_INTEGER) {
    var actualUrl = apiUrlRoot + "?type="+type+"&gateway="+gateway+"&topic="+worker+"&topic="+worker+"&from="+from+"&to="+to;
    console.log(actualUrl)
    return new Promise((resolve, reject) => {
        $.ajax({
            url: actualUrl,
            type: 'GET',
            data: {},
            success: function (data) {
                resolve(JSON.parse(data))
            },
            error: function (error) {
                reject(error)
            },
        })
    })
}

//MQTT!
var isTestingLocally = true;
var mqtt;
var reconnectTimeout = 2000;
var host = location.host
var port = 8081
var username = "kristian"
var pw = "1234"

console.log("MQTT");
console.log("Host: "+host);
console.log("Port: "+port);

function _onConnect(callback = null) {
    console.log("Connected to MQTT!");
    // Subscribe to topics

    callback(mqtt);
}

function MQTTConnect(callback) {
    mqtt = new Paho.MQTT.Client(host, port, "/ws", "kristian");
    var options = {
        timeout: 5,
        onSuccess: () => _onConnect(callback),
        onFailure: () => {
            console.log("MQTT Failed to connect..");
        },
        userName: username,
        password: pw
    }

    mqtt.connect(options)
}

function MQTTSend(topic, message) {
    console.log("Sending message");
    console.log("Topic: " + topic);
    console.log("Message: " + message);

    // Connect and send
    MQTTConnect((x) => {
        message = new Paho.MQTT.Message(message);
        message.destinationName = topic;

        mqtt.send(message)
    })
}
