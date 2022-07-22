from rdflib import Graph, URIRef, Literal, BNode ,Namespace
from rdflib.namespace import RDF ,XSD , OWL ,RDFS ,BRICK ,SKOS


class ThingDescription:
    def __init__(self):
        self.thingGraph =  Graph()
        #thing description
        td = Namespace("https://www.w3.org/2019/wot/td#")
        self.thingGraph("td" , td)
        # thing description
        jsonschema = Namespace("https://www.w3.org/2019/wot/hypermedia#")
        self.thingGraph("jsonschema", jsonschema)
        # thing description
        mqv = Namespace("@prefix td: <https://www.w3.org/2019/wot/td#>")
        self.thingGraph("mqv", mqv)
        # thing description
        td = Namespace("@prefix td: <https://www.w3.org/2019/wot/td#>")
        self.thingGraph("td", td)


    def rdfCreation(self):
        pass
