import psycopg2
import getpass
import calendar,time
def auth():
	global dbs,usr,passw, db_con, cursor
        #dbs="trajectory_"
	dbs=raw_input("Enter database name:  trajectory_thres ")
	usr=raw_input("Enter user name : ubuntu ")
	print("Enter password : lion ")
	passw=getpass.getpass()
	db_con = psycopg2.connect(database=dbs, user=usr, password=passw, host="127.0.0.1", port="5432")
	cursor = db_con.cursor()
	cursor.execute("ROLLBACK")
	
def write_sp(taxino,lat,lon,starttime,endtime,count,precision=6):
	global cursor
	startTime='\''+str(starttime[2])+"-"+str(starttime[1])+"-"+str(starttime[0])+" "+str(starttime[3])+":"+str(starttime[4])+":"+str(starttime[5])+"\'"
	endTime='\''+str(endtime[2])+"-"+str(endtime[1])+"-"+str(endtime[0])+" "+str(endtime[3])+":"+str(endtime[4])+":"+str(endtime[5])+"\'"

	dataa=str(taxino)+",'SP',"+str(round(lat,precision))+","+str(round(lon,precision))+",NULL,"+startTime+","+endTime
	
	try:
		cursor.execute("INSERT INTO a"+str(taxino)+" VALUES ("+dataa+");")
		#cursor.execute("INSERT INTO a1 VALUES ( 11, \'abc\', 1,1,\'ab\',\'2016-11-11 01:01:01\',\'2016-11-11 01:01:01\');")
	except :
		#print e
		cursor.execute("CREATE TABLE a"+str(taxino)+" (id INTEGER,type VARCHAR,lat FLOAT,lon FLOAT,poi VARCHAR,stime TIMESTAMP,etime TIMESTAMP);")
		cursor.execute("INSERT INTO a"+str(taxino)+" VALUES ("+dataa+");")

	
def write_move(taxino,lat,lon,starttime,endtime,count,precision=6):
	global cursor
	startTime='\''+str(starttime[2])+"-"+str(starttime[1])+"-"+str(starttime[0])+" "+str(starttime[3])+":"+str(starttime[4])+":"+str(starttime[5])+"\'"
	endTime='\''+str(endtime[2])+"-"+str(endtime[1])+"-"+str(endtime[0])+" "+str(endtime[3])+":"+str(endtime[4])+":"+str(endtime[5])+"\'"
	dataa=str(taxino)+",'move',"+str(round(lat,precision))+","+str(round(lon,precision))+",NULL,"+startTime+",NULL"	
	try:
		cursor.execute("INSERT INTO a"+str(taxino)+" VALUES ("+dataa+");")
		#cursor.execute("INSERT INTO a1 VALUES ( 11, \'abc\', 1,1,\'ab\',\'2016-11-11 01:01:01\',\'2016-11-11 01:01:01\');")
	except :
		#print e
		cursor.execute("CREATE TABLE a"+str(taxino)+" (id INTEGER,type VARCHAR,lat FLOAT,lon FLOAT,poi VARCHAR,stime TIMESTAMP,etime TIMESTAMP);")
		cursor.execute("INSERT INTO a"+str(taxino)+" VALUES ("+dataa+");")

def time_difference(starTIE,stemp):
	#[day,month,year,hr,mins,sec]
	#calendar.timegm(time.strptime('Jul 9, 2010 @ 20:02:45 UTC', '%b %d, %Y @ %H:%M:%S UTC'))
	t1=str(starTIE[3])+":"+str(starTIE[4])+":"+str(starTIE[5])+' UTC'
	t2=str(stemp[3])+":"+str(stemp[4])+":"+str(stemp[5])+' UTC'
	t1=calendar.timegm(time.strptime(t1,'%H:%M:%S UTC'))
	t2=calendar.timegm(time.strptime(t2,'%H:%M:%S UTC'))
	return abs(t1-t2)
