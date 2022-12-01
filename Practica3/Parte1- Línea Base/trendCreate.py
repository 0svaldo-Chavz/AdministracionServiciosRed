import rrdtool




ret = rrdtool.create("/home/osvaldo/Documents/redes/Introduccion_SNMP/6-AdministraciónDeRendimiento/RRD/Umbrales3.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:CPUload0:GAUGE:60:0:100",
                    "DS:CPUload1:GAUGE:60:0:100",
                    "DS:CPUload2:GAUGE:60:0:100",
                    "DS:CPUload3:GAUGE:60:0:100",
                     "RRA:AVERAGE:0.5:1:50")
'''
ret = rrdtool.create("/home/osvaldo/Documents/redes/Introduccion_SNMP/6-AdministraciónDeRendimiento/RRD/Umbrales2.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:RAM:GAUGE:60:0:100",
                    "DS:inOctects:GAUGE:60:0:100",
                    "DS:outOctects:GAUGE:60:0:100",
                     "RRA:AVERAGE:0.5:1:50")
'''
if ret:
    print (rrdtool.error())
