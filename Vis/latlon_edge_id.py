# x1, y1 = raw_input().strip().split()
# x2, y2 = raw_input().strip().split()
# x1 =  88.36337056410642
# y1 = 22.571993398604974


import sys
import json
from numpy import inf

x1, y1, x2, y2 = sys.argv[1:]
x1, y1, x2, y2 = map(float,[x1,y1,x2,y2])
f=open("/home/ubuntu/Desktop/trajectory_clone/Vis/out.json", "r")
lat_lon_json = json.load(f)

def distance(a,b):
	a = map(float,a)
	b = map(float,b)
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.2

def return_edge_id(ini, fin):
	x1, y1 = ini[0], ini[1]
	x2, y2 = fin[0], fin[1]
	key_ini = key_fin = 0
	min_i = min_f = inf

	for key in lat_lon_json.keys():
		p1 = lat_lon_json[key]['from']
		# print(key,distance(p1,[x1,y1]))
		if(distance(p1,[x1,y1]) < min_i):
			min_i = distance(p1,[x1,y1])
			key_ini = key

		p2 = lat_lon_json[key]['to']
		if(distance(p2,[x2,y2]) < min_f):
			min_f = distance(p2,[x2,y2])
			key_fin = key

	return key_ini, key_fin


a, b = return_edge_id([x1,y1], [x2,y2])
print a.strip()
print b.strip()