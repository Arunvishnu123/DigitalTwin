from rdflib import Graph, URIRef, Literal, BNode, Namespace
from rdflib.namespace import RDF, XSD, OWL, RDFS, BRICK

class IFCClassTriple:
    def __init__(self ,ifcClass):
        self.ifcClassG = Graph()
        self.urlRef = URIRef("http://127.0.0.1:3000/" + ifcClass )
        # bot namespace
        self.bot = Namespace("https://w3id.org/bot#")
        self.ifcClassG.bind('bot',self.bot)
        # props Namespace
        self.props = Namespace("http://127.0.0.1:5000/test")
        self.ifcClassG.bind("props", self.props)
        self.ifcClass = ifcClass

    def createIFCClassTriple(self):
        self.ifcClassG.add((self.urlRef , RDF.type ,self.bot.Element))

    def addIFCClassNumber(self,number):
        self.ifcClassG.add((self.urlRef , self.props.hasTotalElements,Literal(number,datatype=XSD['integer'])))

    def addIFCElementLink(self,ifcGuid):
        type = URIRef("http://127.0.0.1:3000/" + self.ifcClass + "/" + ifcGuid)
        self.ifcClassG.add((self.urlRef ,self.bot.containsElements ,  type ))

    def createFile(self , location ):
        self.ifcClassG.serialize(location + "/" + self.ifcClass + ".ttl" , format="ttl" )

