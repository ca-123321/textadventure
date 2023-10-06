class Room:
    def __init__(self, name, desc_long, desc_short, attributes):
        self.name = name
        self.desc_long = desc_long
        self.desc_short = desc_short
        self.attributes = attributes
        self.entries = attributes["entries"]
        self.exits = attributes["exits"]
        self.lighting = attributes["lighting"]
        self.interactable = attributes["interactable"]
        self.discoverable = attributes["discoverable"]

class Item:
    def __init__(self, name, desc_long, desc_short, attributes):
        self.name = name
        self.desc_long = desc_long
        self.desc_short = desc_short
        self.attributes = attributes
