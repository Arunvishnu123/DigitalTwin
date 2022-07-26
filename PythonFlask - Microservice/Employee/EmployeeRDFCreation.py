from rdflib import Graph, URIRef, Literal, BNode ,Namespace
from rdflib.namespace import RDF ,XSD , OWL ,RDFS ,BRICK ,SKOS,FOAF

class EmployeeRDf:
    def __init__(self):
        pass

    def creation(self , ifcClass , ifcGuid ,firstName,lastName,position,email,imageLink,location):
        employeeGraph = Graph()
        # props namespace
        props = Namespace("http://127.0.0.1:5000/test")
        employeeGraph.bind("props", props)
        hctl = Namespace("https://www.w3.org/2019/wot/hypermedia#")
        employeeGraph.bind("hctl", hctl)
        url = URIRef(ifcClass + "/" + ifcGuid + "/" + "employee")
        employeeGraph.add((url,RDF.type,FOAF.Person))
        employeeGraph.add((url, FOAF.firstName, Literal(firstName)))
        employeeGraph.add((url,FOAF.lastName,Literal(lastName)))
        employeeGraph.add((url, FOAF.title, Literal(position)))
        employeeGraph.add((url,FOAF.mbox , Literal(email)))
        employeeGraph.add((url,FOAF.img , Literal(imageLink)))
        employeurl = url + "#" + "element"
        employeeGraph.add((url,props.hasElement,URIRef(employeurl)))
        employeeGraph.add((employeurl,RDF.type ,props[ifcClass]))
        employeeGraph.add((employeurl,hctl.hasTarget,URIRef("http://127.0.0.1:3000/" + ifcClass + "/" + ifcGuid)))
        employeeGraph.serialize(location +"/" + firstName + ".ttl",format="ttl")

