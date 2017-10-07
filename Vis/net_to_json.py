import random
from xml.dom import minidom
import os
import hex

os.environ['SUMO_HOME'] = "/usr/share/sumo"

import sys
if 'SUMO_HOME' in os.environ:
 tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
 sys.path.append(tools)
else:   
 sys.exit("please declare environment variable 'SUMO_HOME'")
import sumolib

net = sumolib.net.readNet('sumo/map.net.xml')

xmldoc = minidom.parse('/home/ubuntu/Desktop/trajectory_clone/Vis/sumo/map.net.xml')
junclist= xmldoc.getElementsByTagName('junction')
junctions={}
for junc in junclist:
	idno=str(junc.attributes['id'].value)
	try:
		x=float(junc.attributes['x'].value)
		y=float(junc.attributes['y'].value)
	except: continue
	junctions[idno]=[x,y]
itemlist = xmldoc.getElementsByTagName('edge')
output={}
hexmap={}
for item in itemlist:
	idno=str(item.attributes['id'].value)
	try:
		fr=str(item.attributes['from'].value)
		to=str(item.attributes['to'].value)
	except:  continue
	lanes=item.getElementsByTagName('lane')
	dist=0
	for lane in lanes:
		dist+=float(lane.attributes['length'].value)
	from_lat_lon = net.convertXY2LonLat(junctions[fr][0],junctions[fr][1])
	to_lat_lon = net.convertXY2LonLat(junctions[to][0],junctions[to][1])
	hex_here = hex.pixel_to_hex(float(from_lat_lon[0]+to_lat_lon[0])/2,float(from_lat_lon[1] + to_lat_lon[1])/2)
	try:
		hexmap[str(hex_here)].append(idno)
	except:
		hexmap[str(hex_here)]=[idno]
	output[idno]={"from":from_lat_lon,"to":to_lat_lon, "hex":hex_here,\
	"distance":float(dist), "traffic":random.randrange(1,6)}
	print output[idno]
# print output
import json
string=json.dumps(output, indent=2)
print string
f=open("/home/ubuntu/Desktop/trajectory_clone/Vis/out.json","w")
f.write(string)

string=json.dumps(hexmap, indent=2)
print string
f=open("/home/ubuntu/Desktop/trajectory_clone/Vis/hexmap.json","w")
f.write(string)

os.system('rm /home/ubuntu/Desktop/trajectory_clone/Vis/tables/*')