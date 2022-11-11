import os
import rrdtool

bandera = True
update = False

os.system('clear')
print('Administraciòn de Contabilidad')
print('----Agregar dispositivo----')
print('\n\tIndica los siguienes datos: \n')
host = input('Indica el nombre o host: ')
comunidad = input('Indica la comunidad ')

ret = rrdtool.create(f"Datos_{host}.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:inUcast:COUNTER:120:U:U",
                     "DS:inIPv4:COUNTER:120:U:U",
                     "DS:ICMPecho:COUNTER:120:U:U",
                     "DS:segTCP:COUNTER:120:U:U",
                     "DS:dataUDP:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:1:500")

if ret:
  print (rrdtool.error())


