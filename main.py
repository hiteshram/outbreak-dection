import pandas as pd
import networkx as nx
import pylab as plt 
import datetime

from place import Place
from person import Person
from visit import Visit


g=nx.DiGraph()

#Reading the list of places and creating an object and adding to the dictionary
place_df=pd.read_csv('place.csv')
place_dict=dict()
for index,row in place_df.iterrows():
    t=Place(row['PlaceId'],row['PlaceName'],row['PlaceType'],row['Lat'],row['Long'])
    place_dict[row['PlaceId']]=t
    #g.add_node('Place_'+str(row['PlaceId']))    

#Reading the person details and creating an object for each person and adding to the dictionary
person_df=pd.read_csv('person.csv')
person_dict=dict()
for index,row in person_df.iterrows():
    t=Person(row['PersonId'],row['PersonName'],row['HealthStatus'],row['ConfirmedTime'],row['AddressLat'],row['AddressLong'])
    person_dict[row['PersonId']]=t
    #g.add_node('Person_'+str(row['PersonId']))    

#Reading the visit details of each person and creating the object for each visit and adding to the dictionary
visit_df=pd.read_csv('visit_place.csv')
visit_dict=dict()
for index,row in visit_df.iterrows():
    v=Visit(row['VisitId'],row['PersonId'],row['PlaceId'],row['StartTime'],row['EndTime'])
    person_dict[row['VisitId']]=v


labels=dict()
#Adding the nodes of persons based on the visit file, simultaneosuly adding their names to the labels 
for node in visit_df['PersonId']: 
    g.add_node(node)
    labels[node]=person_dict[node].get_person_name()
    
#Adding the nodes of places based on the visit file, simultaneosly adding their names to the labels
for node in visit_df['PlaceId']:
    g.add_node(node)
    labels[node]=place_dict[node].get_place_name()

#Fetching the start and end time of each visit and add it as weight to the edge 
#Conditions if person to person 15 mins 
# If person to workplace or any location 4 hours 
for index,row in visit_df.iterrows():
    start=datetime.datetime.strptime(row['StartTime'],'%Y-%m-%dT%H:%M:%S')
    end=datetime.datetime.strptime(row['EndTime'],'%Y-%m-%dT%H:%M:%S')
    time_spent=(end-start).total_seconds()//60
    g.add_edge(row['PersonId'],row['PlaceId'],weight=time_spent)


hotspot_list=list()
for node in visit_df['PlaceId']:
    if g.in_degree(node)>1 and node not in hotspot_list:
        hotspot_list.append(node)

hotspot_edge_list=list()

for node in hotspot_list:
    for edge in g.edges:
        if node in edge and g[edge[0]][edge[1]]["weight"]>=240:
            hotspot_edge_list.append(edge)

options = {"node_size": 500, "alpha": 0.8}
pos = nx.spring_layout(g)

#Creating Labels dictionary
edge_labels=nx.get_edge_attributes(g,'weight')

nx.draw_networkx_nodes(g, pos,list(visit_df['PersonId']), node_color="r", **options)
nx.draw_networkx_nodes(g, pos,list(visit_df['PlaceId']), node_color="b", **options)
nx.draw_networkx_edges(g, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(g, pos, edgelist=hotspot_edge_list, width=2.0)
nx.draw_networkx_labels(g, pos,labels=labels,font_size=6)

e_labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,pos,edge_labels=e_labels,font_size=6)
plt.savefig('graph.png')