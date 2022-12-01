import sys
import rrdtool
from Notify import send_alert_attached
import time
from getSNMP import consultaSNMP
rrdpath = '/home/osvaldo/Documents/redes/Introduccion_SNMP/6-AdministraciónDeRendimiento/RRD/'
imgpath = '/home/osvaldo/Documents/redes/Introduccion_SNMP/6-AdministraciónDeRendimiento/IMG/'

umbral75 = umbral80 = umbral90 = True
umbral = 0



def getInfo():
  sistemaOp = consultaSNMP("Chavz", "localhost", "1.3.6.1.2.1.1.1.0")
  dispositivo = consultaSNMP("Chavz", "localhost", "1.3.6.1.2.1.1.5.0")
  contacto = consultaSNMP("Chavz", "localhost", "1.3.6.1.2.1.1.4.0")
  ubicacion = consultaSNMP("Chavz", "localhost", "1.3.6.1.2.1.1.6.0")
  body = ("\t-----Información del agente SNMP-----"+
          f"\nSistema Operativo: {sistemaOp}"+
          f"\nNombre del dispositivo: {dispositivo}"+
          f"\nContacto: {contacto}"+
          f"\nUbicación: {ubicacion}")
  return body


def generarGrafica(ultima_lectura,i):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 2500


    ret = rrdtool.graphv( imgpath+f"Rendimiento_CPU{i}.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     f"--vertical-label=Cpu load{i}",
                     '--lower-limit', '0',
                     '--upper-limit', '100',
                     "--title=Carga del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales",
                     f"DEF:cargaCPU{i}=" + rrdpath + f"Umbrales3.rrd:CPUload{i}:AVERAGE",
                     f"CDEF:umbral75_0=cargaCPU{i},75,LT,0,cargaCPU{i},IF",
                     f"CDEF:umbral80_0=cargaCPU{i},80,LT,0,cargaCPU{i},IF",
                     f"CDEF:umbral90_0=cargaCPU{i},90,LT,0,cargaCPU{i},IF",
                     f"AREA:cargaCPU{i}#000000:Carga del CPU {i}",
                     f"AREA:umbral75_0#2E8C1E:Carga CPU {i} mayor de 75",
                     f"AREA:umbral80_0#E5D833:Carga CPU {i} mayor de 80",
                     f"AREA:umbral90_0#FF0000:Carga CPU {i} mayor de 90",
                     "HRULE:75#2E8C1E:Umbral  75%",
                     "HRULE:80#E5D833:Umbral  80%",
                     "HRULE:90#FF0000:Umbral  90%")
    '''
    ret = rrdtool.graphv(imgpath + f"RAM.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         f"--vertical-label=RAM",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "--title=Carga de la RAM del agente Usando SNMP y RRDtools \n Detección de umbrales",
                         f"DEF:cargaRAM=" + rrdpath + f"Umbrales2.rrd:CPUload{i}:AVERAGE",
                         f"CDEF:umbral75_0=cargaCPU{i},75,LT,0,cargaCPU{i},IF",
                         f"CDEF:umbral80_0=cargaCPU{i},80,LT,0,cargaCPU{i},IF",
                         f"CDEF:umbral90_0=cargaCPU{i},90,LT,0,cargaCPU{i},IF",
                         f"AREA:cargaCPU{i}#000000:Carga del CPU {i}",
                         f"AREA:umbral75_0#2E8C1E:Carga CPU {i} mayor de 75",
                         f"AREA:umbral80_0#E5D833:Carga CPU {i} mayor de 80",
                         f"AREA:umbral90_0#FF0000:Carga CPU {i} mayor de 90",
                         "HRULE:75#2E8C1E:Umbral  75%",
                         "HRULE:80#E5D833:Umbral  80%",
                         "HRULE:90#FF0000:Umbral  90%")
    '''
    print (ret)

while (1):
  i=0
  ultima_actualizacion = rrdtool.lastupdate(rrdpath + "Umbrales3.rrd")
  timestamp = ultima_actualizacion["date"].timestamp()
  print(i)
  print("Dentro de while")
  for i in range(4):
    print("Dentro de for")
    print(i)
    print(f"CPULoad{i}",ultima_actualizacion["ds"][f"CPUload{i}"])
    registro = ultima_actualizacion["ds"][f"CPUload{i}"]

    #Analizamos que umbral sobrepaso el registro

    if registro > 75 and registro < 80 and umbral75:
      umbral = 75
      generarGrafica(int(timestamp), i)
      send_alert_attached(f"El CPU {i} sobrepasa el umbral del {umbral}% con {registro}%", i, getInfo())
      print(f"El CPU {i} sobrepasa el umbral del {umbral}% con {registro}%")
      umbral75 = False

    elif registro > 80 and registro < 90 and umbral80:
      umbral = 80
      generarGrafica(int(timestamp), i)
      send_alert_attached(f"El CPU {i} sobrepasa el umbral del {umbral}% con {registro}%", i, getInfo())
      print(f"El CPU {i} sobrepasa el umbral del {umbral}% con {registro}%")
      umbral80 = False

    elif registro > 90 and umbral90:
      umbral = 90
      generarGrafica(int(timestamp), i)
      send_alert_attached(f"El CPU {i} sobrepasa el umbral del {umbral}% con {registro}%", i, getInfo())
      print(f"El CPU {i} sobrepasa el umbral del {umbral}% con {registro}%")
      umbral90=False

    time.sleep(5)

