

from write import write_move,write_sp, auth
thr=float(raw_input("Enter threshold (recommended 0.0001) : "))
auth()
path="/home/ubuntu/Desktop/trajectory_clone/data"
#path=raw_input("Enter full input path (root directory of the files) : ")

'''
##test
thr=0.0001
#path="/home/mehul/1/2"
#path ="/home/ubuntu/Desktop/trajectory_clone/data2/peace"
path = "/home/ubuntu/Desktop/trajectory_clone/data3"
def write_move(taxino,lat,lon,starttime,endtime,count,hy):
   print(starttime,endtime,count,lat,lon,"move")
   global counter
def write_sp(taxino,lat,lon,starttime,endtime,count,hy):
   print(starttime,endtime,count,lat,lon,"sp")
   global counter
##test end
'''
import os
import psycopg2

from write import time_difference
os.chdir(path)
counter=0





#from writepos import write
taxi={}

folderlist=os.listdir(os.getcwd())
totnum=0
for folder in folderlist:
  os.chdir(path+"/"+folder)
  filelist=os.listdir(os.getcwd())
  for files in filelist:
    totnum+=1

numnow=0; pumbalines=0; pumbanow=0
prec=1
#precision=6 
for folder in folderlist:
  os.chdir(path+"/"+folder)
  filelist=os.listdir(os.getcwd())
  for files in filelist:
    os.system("clear")
    print "Scanned file("+files+") "+str(numnow)+" of "+str(totnum)+"."
    print "% complete: "+str(numnow*100/totnum)
    try:
    	print "The last file was compressed by: "+str(pumbanow*100.0/pumbalines)
    except: pass
    numnow+=1
    f=open(files,"r")
    pumbalines=0; pumbanow=0
    global records
    records=[]
    flag=1 
    while(1):
      line=f.readline()
      pumbalines+=1
      if not line: break
      data=line.strip('\n').split(",")
      dates=data[1].strip(" ").split(" ")
      date=dates[0].split("-")
      time=dates[1].split(":")
      day, month, year =int(date[2]), int(date[1]), int(date[0])
      hr, mins, sec = int(time[0]), int(time[1]), int(time[2])
      lat=float(data[2])
      lon=float(data[3])
      #global records  
      #print([[day,month,year,hr,mins,sec],lat,lon]) 
      
      #print(len(records))
      if prec:	precision=len(str(lat).split(".")[1]); prec=0
      taxino=int(data[0])
      templat=0; templon=0
      
      try:
      	#count=len(taxi[taxino])-1
        pass
      	#print("count changed   : "+str(count))
      except:
      	#print("except")
      	taxi[taxino]=[]
      	taxi[taxino]=[[day,month,year,hr,mins,sec],lat,lon]
      	count=1
      try:
      	i=1
        
        while(1):
           try:
            templat+=taxi[taxino][i]
            templon+=taxi[taxino][i+1]
            i+=2
      	   except:
      	    count=(len(taxi[taxino])-1)*0.5
            #count = Count + 1
            #print(count)
      	    break
      	#print("try")
        #count = float(count)+float(1.0)
      	dist=(((templat/(count))-lat)**2)+(((templon/(count))-lon)**2)
      	#print(str(templat/count)+"  "+str(templon/count)+" "+str(lat)+" "+str(lon))
      	#print "dist: "+str(dist)
        if(flag):
           starpos=[lat,lon]
           starTIE=[day,month,year,hr,mins,sec]
           flag=0
      	if (dist<thr**2):
            global stemp
            stemp=[day,month,year,hr,mins,sec]
            stemppos=[lat,lon]
            taxi[taxino].append(lat)
            taxi[taxino].append(lon)
            records.append([[day,month,year,hr,mins,sec],lat,lon])
            
            #print("if")
      	else:
            flag=1
            i=len(records)-1
            timeELAPSED=time_difference(starTIE,stemp)
            precision = 6
            #print(timeELAPSED," sec")
            if ( count >= 10 or timeELAPSED >= 60 ):
                write_move(taxino,starpos[0],starpos[1], starTIE,starTIE,-1,precision)
          	write_sp(taxino,(templat+lat)/(count+float(1.0)),(templon+lon)/(count+float(1.0)), taxi[taxino][0],stemp,count,precision)
                write_move(taxino,stemppos[0],stemppos[1], stemp,stemp,count,precision)
		pumbanow+=3
                while len(records) > 0 : records.pop()
            else:
                #records.pop();records.pop();records.pop();
                p=len(records)
                for i in range(len(records)):
                        
                        try:
		                record1=records.pop(0)
		                #record2=records.pop(0)
		       		write_move(taxino,record1[1],record1[2], record1[0],record1[0],0,precision)
				pumbanow+=1
                        except:
                        	while len(records) > 0 : records.pop()
                while len(records) > 0 : records.pop()
                
                #print(len(records),p)	
                #global records	
                #records=[]
	    '''			#print(len(records))   
            else :
          	write_sp(taxino,(templat+lat)/count,(templon+lon)/count, taxi[taxino][0],stemp,count,precision)
            '''
            #write_move(taxino,lat,lon, [day,month,year,hr,mins,sec],[day,month,year,hr,mins,sec],0,precision)          
            #write(taxino,lat,lon, [day,month,year,hr,mins,sec],[day,month,year,hr,mins,sec],count,"move")
            counter+=1
            taxi[taxino]=[[day,month,year,hr,mins,sec],lat,lon]
      		#print("else")
      except Exception, e:
      	#print e
      	taxi[taxino]=[]
      	taxi[taxino]=[[day,month,year,hr,mins,sec],lat,lon]	
      	#print("oexceptf")
  #os.chdir(path)
