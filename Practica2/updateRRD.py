import rrdtool
import time
from getSNMP import consultaSNMP
#from main import comunidad,host

comunidad = "Chavz"
host = "192.168.105.1"

while 1:

  input_UCast = int(consultaSNMP(comunidad,host,
                                 '1.3.6.1.2.1.2.2.1.11.4'))
  input_IPv4 = int(consultaSNMP(comunidad,host,
                                '1.3.6.1.2.1.4.3.0'))
  send_ICMPecho = int(consultaSNMP(comunidad,host,
                                   '1.3.6.1.2.1.5.21.0'))
  input_segTCP = int(consultaSNMP(comunidad,host,
                                  '1.3.6.1.2.1.6.10.0'))
  dataUDP = int(consultaSNMP(comunidad,host,
                             '1.3.6.1.2.1.7.1.0'))

  valor = "N:" + str(input_UCast) + ':' + str(input_IPv4) + ':' + str(send_ICMPecho) + ':' + str(
    input_segTCP) + ':' + str(dataUDP)
  print(valor)
  rrdtool.update(f"Datos_192.168.105.1.rrd", valor)
  time.sleep(1)

if ret:
  print(rrdtool.error())
  time.sleep(300)