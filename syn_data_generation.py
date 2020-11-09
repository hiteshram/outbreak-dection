import random
import datetime
import csv
import networkx as nx
import pandas as pd


'''
person_limit=int(input("Enter number of persons : "))
person_list=dict()
for i in range(1,person_limit+1):
    temp=random.randint(1,person_limit//3)
    temp_list=list()
    while len(temp_list)<=temp:
        temp_num=random.randint(1,person_limit)
        if temp_num != i and temp_num not in temp_list:
            temp_list.append(temp_num)
    
    person_list[i]=temp_list
'''
count=0

#g=g=nx.Graph()
#g=nx.read_gml('karate.gml')


with open('visit_place_SIR.csv','w',newline='') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow(['VisitId','PersonId','PlaceId','StartTime','EndTime'])
    
    #For Random Data Generation
    '''
    for k,v in person_list.items():
        for i in v:
            count=count+1
            person_id="Person_"+str(k)
            place_id="Person_"+str(i)
            start_time_obj = datetime.datetime.now()
            start_time_str = start_time_obj.strftime('%Y-%m-%dT%H:%M:%S')
            rand_minutes=random.randint(5,240)
            end_time_obj = datetime.datetime.now()+datetime.timedelta(minutes=rand_minutes)
            end_time_str = end_time_obj.strftime('%Y-%m-%dT%H:%M:%S')
            
            newFileWriter.writerow([count,person_id,place_id,start_time_str,end_time_str])
    
    '''
    #For a predefined graph or data
    '''
    for edge in g.edges:
        count=count+1
        person_id="Person_"+str(edge[0])
        place_id="Person_"+str(edge[1])
        start_time_obj = datetime.datetime.now()
        start_time_str = start_time_obj.strftime('%Y-%m-%dT%H:%M:%S')
        rand_minutes=random.randint(5,240)
        end_time_obj = datetime.datetime.now()+datetime.timedelta(minutes=rand_minutes)
        end_time_str = end_time_obj.strftime('%Y-%m-%dT%H:%M:%S')
        newFileWriter.writerow([count,person_id,place_id,start_time_str,end_time_str])
    '''
    #For a directed contact network

    contact_df=pd.read_csv('visit_place_dataset.csv')
    for index,row in contact_df.iterrows():
        count=count+1
        person_id="Person_"+str(row[0])
        place_id="Person_"+str(row[1])
        start_time_obj = datetime.datetime.now()
        start_time_str = start_time_obj.strftime('%Y-%m-%dT%H:%M:%S')
        rand_minutes=0
        
        if row[2]==1:
            rand_minutes=14
        elif row[2]==2:
            rand_minutes=15
        elif row[2]==3:
            rand_minutes=60
        else:
            rand_minutes=61

        end_time_obj = datetime.datetime.now()+datetime.timedelta(minutes=rand_minutes)
        end_time_str = end_time_obj.strftime('%Y-%m-%dT%H:%M:%S')
        #print(count,person_id,place_id,start_time_str,end_time_str)
        newFileWriter.writerow([count,person_id,place_id,start_time_str,end_time_str])
        
    