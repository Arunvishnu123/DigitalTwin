from rdflib import Graph, URIRef, Literal, BNode ,Namespace
from rdflib.namespace import RDF ,XSD , OWL ,RDFS ,BRICK ,SKOS,FOAF

class EmployeeRDf:
    def __init__(self):
        pass

    def creation(self , ifcClass , ifcGuid ,firstName,lastName,position,email,imageLink,location):
        employeeGraph = Graph()
        url = URIRef(ifcClass + "/" + ifcGuid + "/" + "employee")
        employeeGraph.add((url,RDF.type,FOAF.Person))
        employeeGraph.add((url, FOAF.firstName, Literal(firstName)))
        employeeGraph.add((url,FOAF.lastName,Literal(lastName)))
        employeeGraph.add((url, FOAF.title, Literal(position)))
        employeeGraph.add((url,FOAF.mbox , Literal(email)))
        employeeGraph.add((url,FOAF.img , Literal(imageLink)))
        employeeGraph.serialize(location +"/" + firstName + ".ttl",format="ttl")

