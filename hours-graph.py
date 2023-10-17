import networkx as nx

# Directed multigraphs: 
# - uphill vs downhill, rough roads vs fast, sneaky vs walking plainly, teleporting

# Set up Hours
Hours = nx.DiGraph()
for i in range(1, 12):
    Hours.add_edges_from([(i, i+1)])
Hours.add_edge(12, 1)

### Switch to match case?
for i in range(1, 7):
    Hours.nodes[i]['dayhalf'] = 'rising'
for i in range(7, 13):
    Hours.nodes[i]['dayhalf'] = 'setting'
for i in [1, 2, 11, 12]:
    Hours.nodes[i]['daypart'] = 'night'
for i in [3, 4]:
    Hours.nodes[i]['daypart'] = 'morning'
for i in [5, 6, 7, 8]:
    Hours.nodes[i]['daypart'] = 'day'
for i in [9, 10]:
    Hours.nodes[i]['daypart'] = 'evening'

day_count = 1
current_hr = Hours.nodes[1]

print(f"""
Day: {day_count}, hour: "some way to get node". 
It is {current_hr['daypart']}. 
The sun is {current_hr['dayhalf']}.
""")


# pass in current hr?
def advance_hour():
    pass
# assert list(DG.predecessors('Forest')) == ['Town']  #  going backwards
