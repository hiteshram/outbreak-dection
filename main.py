import pandas as pd
import networkx as nx
import pylab as plt 

from place import Place
from person import Person
from visit import Visit


g=nx.Graph()
place_df=pd.read_csv('place.csv')
place_dict=dict()
for index,row in place_df.iterrows():
    t=Place(row['PlaceId'],row['PlaceName'],row['PlaceType'],row['Lat'],row['Long'])
    place_dict[row['PlaceId']]=t
    g.add_node('Place_'+str(row['PlaceId']))    

person_df=pd.read_csv('person.csv')
person_dict=dict()
for index,row in person_df.iterrows():
    t=Person(row['PersonId'],row['PersonName'],row['HealthStatus'],row['ConfirmedTime'],row['AddressLat'],row['AddressLong'])
    person_dict[row['PersonId']]=t
    g.add_node('Person_'+str(row['PersonId']))    

visit_df=pd.read_csv('visit.csv')
visit_dict=dict()
for index,row in visit_df.iterrows():
    v=Visit(row['VisitId'],row['PersonId'],row['PlaceId'],row['StartTime'],row['EndTime'])
    g.add_edge('Person_'+str(row['PersonId']),'Place_'+str(row['PlaceId']))

nx.draw(g,with_labels=True)
plt.savefig('graph.png')


'''
t=Place(1,'Place nr 1','Theater','51.21552663','4.405887211')
t.print_place_details()

p=Person(1,'Landyn Greer','Healthy','2020-10-09T16:42:55','51.21156341','4.40950761')
p.print_person_details()

v=Visit(1,p,t,'2020-10-16T06:45:53','2020-10-16T08:04:41')

v.print_visit_details()
'''