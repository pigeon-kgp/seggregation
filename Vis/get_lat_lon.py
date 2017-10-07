import json
f=open("/home/ubuntu/Desktop/trajectory_clone/Vis/out.json", "r")
lat_lon_json = json.load(f)
abc = open("/home/ubuntu/Desktop/trajectory_clone/Vis/out_path","r")
fout = open("/home/ubuntu/Desktop/trajectory_clone/Vis/out_path_lat_lon", "w")
while(1):
	line=abc.readline()
	if not line: break
	my_pos = lat_lon_json[str(line).strip()]['from']
	fout.write(str(my_pos[0])+","+str(my_pos[1])+"\n")
