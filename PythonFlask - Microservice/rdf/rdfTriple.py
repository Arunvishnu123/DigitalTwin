from rdflib import Graph, URIRef, Literal, BNode ,Namespace
from rdflib.namespace import RDF ,XSD , OWL ,RDFS ,BRICK ,SKOS

class RDFGraph:
    def __init__(self):
        pass

    def createRDFGraph(self, ifcClass, ifcGuid ,test , path , relatedElementList  , vertices , faces):
        rdfG = Graph()
        # rdfG.parse("https://w3id.org/bot#")
        # props namespace
        props = Namespace("http://127.0.0.1:5000/test")
        rdfG.bind("props", props)
        # bot namespace
        bot = Namespace("https://w3id.org/bot#")
        rdfG.bind('bot', bot)
        # seas namespace
        seas = Namespace("https://w3id.org/seas/")
        rdfG.bind("seas" , seas)
        # ifc owl ontology
        ifcowl = Namespace("https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2_TC1/OWL")
        rdfG.bind("ifcowl" , ifcowl)
        geometry = BNode()
        url = URIRef("http://127.0.0.1:3000/" + ifcClass + "/" + ifcGuid)
        rdfG.add((url, RDF.type, bot.Element))
        rdfG.add((url,RDF.type , ifcowl[ifcClass]))
        rdfG.add((url,props.hasGeometryType ,  geometry))
        rdfG.add((url, props.hasGeometryType,  geometry))
        rdfG.add(( geometry , props.hasVertices, Literal(vertices)))
        rdfG.add(( geometry  ,props.hasFaces, Literal(faces)))
        for i in test:
            propertyName = i.replace(" ", "")
            propertyNameVoca = "has" + propertyName
            if(type(test[i]) == str):
              rdfG.add((url , props[propertyNameVoca] , Literal(test[i], datatype=XSD['string'])))
            if (type(test[i]) == int):
              rdfG.add((url, props[propertyNameVoca], Literal(test[i], datatype=XSD['integer'])))
            if (type(test[i]) == float):
                rdfG.add((url, props[propertyNameVoca], Literal(test[i], datatype=XSD['decimal'])))
            if (type(test[i]) == bool):
                rdfG.add((url, props[propertyNameVoca], Literal(test[i], datatype=XSD['boolean'])))
            if ifcClass == "IfcSpace":
                for k in relatedElementList:
                    containsElementLink = "http://127.0.0.1:3000/" + k[0] + "/" + k[1]
                    rdfG.add((url , bot.containsElement , URIRef(containsElementLink)))
            if ifcClass == "IfcBuildingStorey":
                for h in relatedElementList:
                    storeyElementList = "http://127.0.0.1:3000/" + h[0] + "/" + h[1]
                    rdfG.add((url, bot.containsElement, URIRef(storeyElementList)))
        return rdfG.serialize(path+"/" + ifcGuid + ".ttl" ,format="ttl")
