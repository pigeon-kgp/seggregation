import psycopg2
import getpass
def auth():
	global dbs,usr,passw, db_con, cursor
        dbs="trajectory"
	dbss=raw_input("Enter database name:  trajectory ")
        dbs=dbs+"_"+dbss
	usr=raw_input("Enter user name : (ubuntu) ")
	print("Enter password : (lion) ")
	passw=getpass.getpass()
	db_con = psycopg2.connect(database=dbs, user=usr, password=passw, host="127.0.0.1", port="5432")
	cursor = db_con.cursor()
	cursor.execute("ROLLBACK")
	
def write(taxino,lat,lon,starttime,endtime,count,precision=6):
	global cursor
	startTime='\''+str(starttime[2])+"-"+str(starttime[1])+"-"+str(starttime[0])+" "+str(starttime[3])+":"+str(starttime[4])+":"+str(starttime[5])+"\'"
	endTime='\''+str(endtime[2])+"-"+str(endtime[1])+"-"+str(endtime[0])+" "+str(endtime[3])+":"+str(endtime[4])+":"+str(endtime[5])+"\'"
	if(count < 10):
		dataa=str(taxino)+",'move',"+str(round(lat,precision))+","+str(round(lon,precision))+",NULL,"+startTime+",NULL"
		
	else:
		dataa=str(taxino)+",'SP',"+str(round(lat,precision))+","+str(round(lon,precision))+",NULL,"+startTime+","+endTime
	
	try:
		cursor.execute("INSERT INTO a"+str(taxino)+" VALUES ("+dataa+");")
		#cursor.execute("INSERT INTO a1 VALUES ( 11, \'abc\', 1,1,\'ab\',\'2016-11-11 01:01:01\',\'2016-11-11 01:01:01\');")
	except Exception, e:
		#print e
		cursor.execute("CREATE TABLE a"+str(taxino)+" (id INTEGER,type VARCHAR,lat FLOAT,lon FLOAT,poi VARCHAR,stime TIMESTAMP,etime TIMESTAMP);")

