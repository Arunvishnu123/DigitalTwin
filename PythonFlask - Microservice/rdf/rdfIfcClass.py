from rdflib import Graph, URIRef, Literal, BNode, Namespace
from rdflib.namespace import RDF, XSD, OWL, RDFS, BRICK

class IFCClass:
    def __init__(self , location):
        self.ifcC = Graph()
        # props Namespace
        self.props = Namespace("http://127.0.0.1:5000/test")
        self.ifcC.bind("props", self.props)
        # bot namespace
        bot = Namespace("https://w3id.org/bot#")
        self.ifcC.bind("bot", bot)
        self.url = URIRef("http://127.0.0.1:5000/IfcClass")
        self.location  =location
        # ifc owl ontology
        ifcowl = Namespace("https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2_TC1/OWL")
        self.ifcC .bind("ifcowl", ifcowl)

    def ifcBNodeGeneration(self ,ifcClassName  , bNode , number):
        self.ifcC.add((bNode , RDF.type , self.ifcowl[ifcClassName] ))
        self.ifcC.add((bNode , self.props.hasTotalElements , Literal(number, datatype=XSD['integer'])))


    def ifcClassGeneration(self , ifcClassObject):
        for  i in ifcClassObject:
            bNodeName = BNode()
            self.ifcC.add((self.url , RDF.Property , bNodeName))
            self.ifcBNodeGeneration(i["ifcClassName"] , bNodeName , i["elementsCount"])
        print(self.location)
        return self.ifcC.serialize(self.location + "/"+ "IfcClass.ttl" , format="ttl")

