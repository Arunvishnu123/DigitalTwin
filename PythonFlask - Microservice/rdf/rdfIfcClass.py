from rdflib import Graph, URIRef, Literal, BNode, Namespace
from rdflib.namespace import RDF, XSD, OWL, RDFS, BRICK

class IFCClass:
    def __init__(self):
        self.ifcC = Graph()
        # props Namespace
        self.props = Namespace("http://127.0.0.1:5000/test")
        self.ifcC.bind("props", self.props)
        # bot namespace
        bot = Namespace("https://w3id.org/bot#")
        self.ifcC.bind("bot", bot)
        self.url = URIRef("http://127.0.0.1:5000/IfcClass")

    def ifcClassRDFGeneration(self):
        self.ifcC.add((self.url , RDF.type ,    ))


