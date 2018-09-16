#!/usr/bin/env python
if __name__ == "__main__":

        import time
        import BME280
        import pigpio

        pi = pigpio.pi()

        if not pi.connected:
                exit(0)

        s = BME280.sensor(pi,BME280.OVER_SAMPLE_1,BME280.SPI)
	day= time.strftime("%m-%d-%Y", )
        time= time.strftime("%H:%M:%S",)
       
        t, p, h = s.read_data()
        t = t*9/5+32

        with open('sensor_data', 'w') as file:
                #file.write("{{ 'id':'rpiX', 'time':'{}', 'temp':'{:.2f}', 'pres':'{:.1f}', 'h':'{:.2f}' }}".format(timeStamp, t, p/100.0, h))
                #file.write('{{ "sensorData": {{\n"id":"rpiX",\n"time":"{}",\n"temp":"{:.2f}",\n"pres":"{:.1f}",\n"hum":"{:.2f}"}}\n}}'.format(timeStamp, t, p/133.322, h))
                #file.write('{{"id":"rpiX","time":"{}","temp":"{:.2f}","pres":"{:.1f}","hum":"{:.2f}"}}'.format(timeStamp, t, p/100.0, h))
		file.write("INSERT INTO sensor_data2 (username, device_id, day, time, temp, humid, press) VALUES ('slayton_tom','Raspi','{}','{}', '{:.2f}', '{:.2f}', '{:.1f}')".format(day, time, t, h, p/100))
        s.cancel()

        pi.stop()

