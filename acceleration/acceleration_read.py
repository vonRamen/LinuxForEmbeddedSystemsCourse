#!/usr/bin/env python3

from asyncore import read
import spidev, subprocess, time
class accelorometer_service():

    def __init__(self) -> None:
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz=1000000
        self.x=0
        self.y=0
        self.z=0

    def _read_adc(self, channel):
        adc = self.spi.xfer2 ([1 ,(8 + channel) << 4 , 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    def _send_values_to_things_speak(self):
        subprocess.call(["curl", 'https://api.thingspeak.com/update?api_key=HES1NSKC27QJ5DMP&field1='+str(self.x)+'&field2='+str(self.y)+'&field3='+str(self.z)])

    def run(self):
        while 1:
            x_new = self._read_adc(0)
            y_new = self._read_adc(1)
            z_new = self._read_adc(2)
            if(self.x != x_new or self.y != y_new or self.z != y_new):
                self.x = x_new
                self.y = y_new
                self.z = z_new
                self._send_values_to_things_speak()
                time.sleep(1)

if __name__=="__main__":
    inst = accelorometer_service()
    inst.run()