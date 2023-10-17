import networkx as nx

temple = nx.MultiDiGraph()
temple.add_nodes_from([
    ("Entry", {"desc": "The entryway to the ruined temple"}),
    ("Hall", {"desc": "A big hall"}),
    ("Kitchen", {"desc": "An ancient kitchen"}),
    ("Library", {"desc": "An old library overlooking some gardens"}),
    ("Study", {"desc": "A small study"}),
    ("Bedroom", {"desc": "A broken down room with beds"}),
    ("Ledge", {"desc": "A small ledge"}),
    ("Garden", {"desc": "A nice garden, you probably died falling here"})
])

# Each height difference on stairs: 0.1
# Easier to go down stairs
# Just walking is weight 1
# Falling any height is 0.5... Maybe want heights somewhere
temple.add_edges_from([
    ("Kitchen", "Library", {'weight': 1.2, 'type': 'stairs'}), 
    ("Library", "Kitchen", {'weight': 0.8, 'type': 'stairs'}),
    ("Study", "Bedroom", {'weight': 1.3, 'type': 'stairs'}),
    ("Bedroom", "Study", {'weight': 0.7, 'type': 'stairs'})])

#  Doors
temple.add_edges_from([("Entry", "Hall"), ("Hall", "Entry"),
                       ("Hall", "Study"), ("Study", "Hall")], weight=1, type='door')

#  Falls
temple.add_edges_from([("Hall", "Kitchen"), 
                       ("Library", "Hall"),
                       ("Bed", "Ledge"),
                       ("Ledge", "Library")], weight=0.5, type='fall')
