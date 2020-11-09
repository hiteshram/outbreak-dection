import networkx as nx
import datetime
import pandas as pd
import operator
import pylab as plt
import csv
from visit import Visit
import matplotlib.pyplot as mplt



def update_infection_rate(count,g):

    blue_list=list()
    red_list=list()
    green_list=list()

    for node in g.nodes:
        if g.nodes[node]["color"]=="BLUE":
            blue_list.append(node)
        elif g.nodes[node]["color"]=="RED":
            red_list.append(node)
        elif g.nodes[node]["color"]=="GREEN":
            green_list.append(node)


    with open('SIR_Outputs/betweenness_centrality/sir_infection_status.csv','a',newline='') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow([count,len(blue_list),len(red_list),len(green_list)])
        
    return


def plot_infection_rates():
    infection_df=pd.read_csv('SIR_Outputs/betweenness_centrality/sir_infection_status.csv')
    #ax = plt.gca()

    fig = plt.figure()

    ax = fig.add_subplot(2,1,1)


    infection_df.plot(kind='line',x='Time',y='Susceptible',color='blue',ax=ax)
    infection_df.plot(kind='line',x='Time',y='Infected', color='red',ax=ax)
    infection_df.plot(kind='line',x='Time',y='Recovered', color='green',ax=ax)
    
    #fig=plt.figure()
    plt.savefig('SIR_Outputs/betweenness_centrality/graph_sir_plot.png')

    return 




#Code starts from here


g=nx.DiGraph()

visit_df=pd.read_csv('visit_place_SIR.csv')

for index,row in visit_df.iterrows():
    start=datetime.datetime.strptime(row['StartTime'],'%Y-%m-%dT%H:%M:%S')
    end=datetime.datetime.strptime(row['EndTime'],'%Y-%m-%dT%H:%M:%S')
    time_spent=(end-start).total_seconds()//60
    g.add_edge(row['PersonId'],row['PlaceId'],weight=time_spent)


quarantine_nodes=list()
node_count=len(g.nodes)//2
while len(quarantine_nodes)<node_count:
    centrality_dict=nx.betweenness_centrality(g)
    central_node=max(centrality_dict.items(), key=operator.itemgetter(1))[0]
    quarantine_nodes.append(central_node)
    g.remove_node(central_node)
    

print(quarantine_nodes)

g=nx.DiGraph()

visit_df=pd.read_csv('visit_place_SIR.csv')

for index,row in visit_df.iterrows():
    start=datetime.datetime.strptime(row['StartTime'],'%Y-%m-%dT%H:%M:%S')
    end=datetime.datetime.strptime(row['EndTime'],'%Y-%m-%dT%H:%M:%S')
    time_spent=(end-start).total_seconds()//60
    g.add_edge(row['PersonId'],row['PlaceId'],weight=time_spent)



options = {"node_size": 500, "alpha": 0.8}
pos = nx.spring_layout(g)

#Creating the nodes and edges
nx.draw_networkx_nodes(g, pos,list(visit_df['PersonId']), node_color="b", **options)
nx.draw_networkx_edges(g, pos, width=1.0, alpha=0.5)


#Creating Edge Labels dictionary
edge_labels=nx.get_edge_attributes(g,'weight')

#Creating Node Labels dictionary
node_labels=dict()
for node in visit_df['PersonId']:
    node_labels[node]=node[-1:]

nx.draw_networkx_labels(g, pos,labels=node_labels,font_size=10,font_color="w")

e_labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,pos,edge_labels=e_labels,font_size=6)
plt.savefig('SIR_Outputs/betweenness_centrality/graph_sir_0.png')


for node in g.nodes:
    g.nodes[node]["color"]="BLUE"
    g.nodes[node]["distance"]=-1
    g.nodes[node]["parent"]=None

for node in quarantine_nodes:
    g.nodes[node]["color"]="YELLOW"


with open('SIR_Outputs/betweenness_centrality/sir_infection_status.csv','w',newline='') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow(['Time','Susceptible','Infected','Recovered'])



count=0
blue_list=list(g.nodes)
red_list=list()
green_list=list()
yellow_list=list()

update_infection_rate(count,g)


root='3'
root="Person_"+root
g.nodes[root]["color"]="RED"
g.nodes[root]["distance"]=0
g.nodes[root]["parent"]=None
queue=list()
queue.append(root)
count=1


update_infection_rate(count,g)



for node in g.nodes:
    if g.nodes[node]["color"]=="BLUE":
        blue_list.append(node)
    elif g.nodes[node]["color"]=="RED":
        red_list.append(node)
    elif g.nodes[node]["color"]=="GREEN":
        green_list.append(node)
    elif g.nodes[node]["color"]=="YELLOW":
        yellow_list.append(node)


nx.draw_networkx_nodes(g, pos,blue_list,node_color="b", **options)
nx.draw_networkx_nodes(g, pos,red_list,node_color="r", **options)
nx.draw_networkx_nodes(g, pos,green_list,node_color="g", **options)
nx.draw_networkx_nodes(g, pos,green_list,node_color="y", **options)

plt.savefig('SIR_Outputs/betweenness_centrality/graph_sir_'+str(count)+'.png')
count=count+1

update_infection_rate(count,g)


while queue:
    u=queue.pop(0)
    for v in list(g.neighbors(u)):
        
        if g.nodes[v]["color"]=="BLUE":
            if e_labels[(u,v)] >= 100 and g.nodes[u]["color"]=="RED":
                g.nodes[v]["color"]="RED"
                red_list.append(v)
            else:
                g.nodes[v]["color"]="BLUE"

            g.nodes[v]["distance"]=g.nodes[u]["distance"]+1
            g.nodes[v]["parent"]=u
            queue.append(v)
    
    if g.nodes[u]["color"]=="RED": 
        g.nodes[u]["color"]="GREEN"

    blue_list=list()
    red_list=list()
    green_list=list()

    for node in g.nodes:
        if g.nodes[node]["color"]=="BLUE":
            blue_list.append(node)
        elif g.nodes[node]["color"]=="RED":
            red_list.append(node)
        elif g.nodes[node]["color"]=="GREEN":
            green_list.append(node)


    nx.draw_networkx_nodes(g, pos,blue_list,node_color="b", **options)
    nx.draw_networkx_nodes(g, pos,red_list,node_color="r", **options)
    nx.draw_networkx_nodes(g, pos,green_list,node_color="g", **options)
    nx.draw_networkx_nodes(g, pos,yellow_list,node_color="y", **options)
    plt.savefig('SIR_Outputs/betweenness_centrality/graph_sir_'+str(count)+'.png')
    count=count+1
    update_infection_rate(count,g)

plot_infection_rates()
