import time
import rrdtool
from getSNMP import consultaSNMP
rrdpath = '/home/osvaldo/Documents/redes/Introduccion_SNMP/6-AdministraciónDeRendimiento/RRD/'
carga_CPU0=carga_CPU1=carga_CPU2=carga_CPU3 = 0

rrdtool.dump(rrdpath+'Umbrales3.rrd','Umbrales3.xml')

total_RAM = int(consultaSNMP('Chavz', 'localhost', '1.3.6.1.4.1.2021.4.5.0'))
umbral_Entrada = 300000000
umbral_Salida = 20000000
'''
print(f"\nTOTAL: {total_RAM} Bytes"+
f"\nTotal: {int(consultaSNMP('Chavz', 'localhost', '1.3.6.1.4.1.2021.4.5.0'))} kbs"+
f"\nLibre: {int(consultaSNMP('Chavz', 'localhost', '1.3.6.1.4.1.2021.4.6.0'))*8} bytes"+
f"\nLibre: {int(consultaSNMP('Chavz', 'localhost', '1.3.6.1.4.1.2021.4.6.0'))} kbs")

'''
while 1:

    carga_CPU0 = int(consultaSNMP('Chavz','localhost','1.3.6.1.2.1.25.3.3.1.2.196608'))

    carga_CPU1 = int(consultaSNMP('Chavz', 'localhost', '1.3.6.1.2.1.25.3.3.1.2.196609'))

    carga_CPU2 = int(consultaSNMP('Chavz', 'localhost', '1.3.6.1.2.1.25.3.3.1.2.196610'))

    carga_CPU3 = int(consultaSNMP('Chavz', 'localhost', '1.3.6.1.2.1.25.3.3.1.2.196611'))
    '''
    free_RAM = int(consultaSNMP('Chavz', 'localhost', '1.3.6.1.4.1.2021.4.6.0'))

    entradaOctetos = int(consultaSNMP('Chavz', 'localhost', '1.3.6.1.2.1.2.2.1.10.2'))

    salidaOctetos = int(consultaSNMP('Chavz', 'localhost', '1.3.6.1.2.1.2.2.1.16.2'))

    RAM = (free_RAM*100/total_RAM)

    inOctetos = (entradaOctetos*100/umbral_Entrada)

    outOctetos = (salidaOctetos*100/umbral_Salida)
    '''

    #valor = "N:" + str(RAM) + ':' + str(inOctetos) + ':' + str(outOctetos)
    valor = "N:" + str(carga_CPU0) + ':' + str(carga_CPU1) + ':' + str(carga_CPU2) + ':' + str(carga_CPU3)
    print (valor)
    rrdtool.update(rrdpath+'Umbrales3.rrd', valor)
    rrdtool.dump(rrdpath + 'Umbrales3.rrd', 'Umbrales3.xml')
    time.sleep(5)

if ret:
    print(rrdtool.error())
    time.sleep(300)