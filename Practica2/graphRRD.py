import time
import rrdtool
#from main import host

host = "192.168.105.1"

rrdtool.dump(f"Datos_{host}.rrd", f"Datos_{host}.xml")

tiempo_inicial = int(time.mktime((2022,11,10,16,57,0,0,0,0)))
tiempo_final = int(time.mktime((2022,11,10,18,3,0,0,0,0)))



ret = rrdtool.graphv(f"Unicast_{host}.png",
                            "--start", str(tiempo_inicial),
                            "--end", str(tiempo_final),
                            "--vertical-label=Bytes/s",
                            "--title=Paquetes Unicast recibidos",
                            f"DEF:datosUnicast=Datos_{host}.rrd:inUcast:AVERAGE",
                            "CDEF:escala=datosUnicast,5,*",
                            "LINE1:escala#00FFFF:datosUnicast")
ret = rrdtool.graphv(f"IPv4_{host}.png",
                      "--start", str(tiempo_inicial),
                      "--end", str(tiempo_final),
                      "--vertical-label=Bytes/s",
                      "--title=Paquetes recibidos a protocolos IP",
                      f"DEF:datosIPv4=Datos_{host}.rrd:inIPv4:AVERAGE",
                      "CDEF:IPv4=datosIPv4,5,*",
                      "LINE1:IPv4#A52A2A:datosIPv4")

ret = rrdtool.graphv(f"ICMP_{host}.png",
                        "--start", str(tiempo_inicial),
                        "--end", str(tiempo_final),
                        "--vertical-label=Bytes/s",
                        "--title=Mensajes ICMP echo enviados",
                        f"DEF:datosICMPecho=Datos_{host}.rrd:ICMPecho:AVERAGE",
                        "CDEF:ICMP=datosICMPecho,5,*",
                        "LINE1:ICMP#0000FF:datosICMP")

ret = rrdtool.graphv(f"segmentosTCP_{host}.png",
                       "--start", str(tiempo_inicial),
                       "--end", str(tiempo_final),
                       "--vertical-label=Bytes/s",
                       "--title=Segmentos TCP recibidos",
                       f"DEF:datosTCP=Datos_{host}.rrd:segTCP:AVERAGE",
                       "CDEF:TCP=datosTCP,5,*",
                       "LINE1:TCP#DC143C:segmentosTCP")

ret = rrdtool.graphv(f"UDP_{host}.png",
                       "--start", str(tiempo_inicial),
                       "--end", str(tiempo_final),
                       "--vertical-label=Bytes/s",
                       "--title=Datagramas entregados a usuarios UDP",
                       f"DEF:datosUDP=Datos_{host}.rrd:dataUDP:AVERAGE",
                       "CDEF:UDP=datosUDP,5,*",
                       "LINE1:UDP#006400:dataUDP")

