from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,letter
import time
import rrdtool
#from main import comunidad,host

tiempo_inicial = int(time.mktime((2022,11,10,16,57,0,0,0,0)))
tiempo_final = int(time.mktime((2022,11,10,18,3,0,0,0,0)))


host = "192.168.105.1"
SO = "Windows"

info_rdd = rrdtool.info(f'Datos_{host}.rrd')


data = rrdtool.fetch(f"Datos_{host}.rrd", "AVERAGE","-s,"+str(tiempo_inicial),'-e'+str(tiempo_final))[2]

nUCast = ndataUDP = nIPv4 = nICMPecho = nsegTCP = 0


for i in data:
  if None not in i:
    nUCast+= i[0]
    nIPv4 += i[1]
    nICMPecho += i[2]
    nsegTCP += i[3]
    ndataUDP += i[4]




  x, y = letter

  archivo = canvas.Canvas(host + ".pdf", pagesize=letter)
  archivo.drawImage("IPN.jpg", 50, y - 100, width=75, height=75)
  archivo.drawImage("ESCOM.png", x - 150, y - 100, width=75, height=75)
  archivo.drawString(180, y - 75, "INSTITUTO POLITÉCNICO NACIONAL")
  archivo.drawString(200, y - 95, "Escuela Superior de Cómputo")
  archivo.drawString(75, y-150, "Administraciòn de Servicios en Red \t Pràctica 2")
  archivo.drawString(75, y - 163, "Chàvez Àvila Osvaldo Antonio")
  archivo.drawString(75, y - 175, f"Sistema Operativo: {SO}")
  archivo.drawImage(f"{SO}.jpg", x - 350, y - 240, width=80, height=65)
  archivo.drawString(170, y-270, "------------ Informaciòn de RRD ------------")
  archivo.drawString(75, y - 285, f"Versiòn de rrd: {info_rdd['rrd_version']}")
  archivo.drawString(75, y - 300, f"Fecha: {time.ctime(info_rdd['last_update'])}")
  archivo.drawString(170, y - 320, "------------ Informaciòn obtenida con el agente ------------")
  archivo.drawString(75, y - 335, f"Paquetes Unicast recibidos por una interfaz: {nUCast}")
  archivo.drawString(75, y - 350, f"Paquetes recibidos a protocolos IP: {nIPv4}")
  archivo.drawString(75, y - 365, f"Mensajes ICMP echo enviados: {nICMPecho}")
  archivo.drawString(75, y - 380, f"Segmentos TCP recibidos: {nsegTCP}")
  archivo.drawString(75, y - 395, f"Datagramas entregados a usuarios UDP: {ndataUDP}")
  archivo.drawString(185, y - 415, "------------ Gràficas ------------")
  archivo.drawImage(f"Unicast_{host}.png", 145, y - 575, width=320, height=150)
  archivo.drawImage(f"IPv4_{host}.png", 145, y - 735, width=320, height=150)
  archivo.showPage()
  archivo.drawImage(f"ICMP_{host}.png", 145, y - 180, width=320, height=150)
  archivo.drawImage(f"segmentosTCP_{host}.png", 145, y - 350, width=320, height=150)
  archivo.drawImage(f"UDP_{host}.png", 145, y - 505, width=320, height=150)
  archivo.showPage()
  archivo.save()

