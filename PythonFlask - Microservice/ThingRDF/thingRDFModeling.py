from rdflib import Graph, URIRef, Literal, BNode ,Namespace
from rdflib.namespace import RDF ,XSD , OWL ,RDFS ,BRICK ,SKOS


class ThingDescriptionRDF:
    def __init__(self):
        pass

    def rdfCreation(self,directory,ifcClass , ifcGuid , sensorType , parameterName, eventDescription , historicalDescritpion , eventContentType,historicalContentType,eventTarget , historicalTarget, eventType, historicalType):
        thingGraph = Graph()
        # thing description
        td = Namespace('https://www.w3.org/2019/wot/td#')
        thingGraph.bind("td", td)
        # thing description
        hctl = Namespace("https://www.w3.org/2019/wot/hypermedia#")
        thingGraph.bind("hctl", hctl)
        # thing description
        jsonSchema = Namespace("https://www.w3.org/2019/wot/json-schema#")
        thingGraph.bind("jsonSchema", jsonSchema)
        # thing description
        mqv = Namespace("http://www.example.org/mqtt-binding#")
        thingGraph.bind("mqv", mqv)
        # thing description
        htv = Namespace("http://www.w3.org/2011/http#")
        thingGraph.bind("htv", htv)
        # thing description
        dct = Namespace("http://purl.org/dc/terms/")
        thingGraph.bind("dct", dct)
        url = URIRef(ifcClass + "/" + ifcGuid + "/" + sensorType )
        thingGraph.add((url, RDF.type, td.Thing))
        eventAffordance = BNode()
        thingGraph.add((url, td.hasEventAffordance, eventAffordance))
        thingGraph.add((eventAffordance, dct.title, Literal(parameterName)))
        thingGraph.add((eventAffordance, dct.description,
                        Literal(eventDescription)))
        thingGraph.add((eventAffordance, dct.name, Literal(parameterName +"_current")))
        schema = BNode()
        thingGraph.add((eventAffordance, td.hasNotificationSchema, schema))
        thingGraph.add((schema, RDF.type, jsonSchema.NumberSchema))
        form = BNode()
        thingGraph.add((eventAffordance, td.hasForm, form))
        thingGraph.add((form, hctl.hasTarget, URIRef(eventTarget)))
        thingGraph.add((form, mqv.controlPacketValue, Literal(eventType)))
        thingGraph.add((form, hctl.hasOperationType, td.subscribeEvent))
        thingGraph.add((form, hctl.forContentType, Literal(eventContentType)))
        propertyAffordance = BNode()
        thingGraph.add((url, td.hasPropertyAffordance, propertyAffordance))
        thingGraph.add((propertyAffordance, RDF.type, jsonSchema.ObjectSchema))
        thingGraph.add((propertyAffordance, dct.title, Literal(parameterName+ "-(HTTP binding)")))
        thingGraph.add((propertyAffordance, dct.description,
                        Literal(historicalDescritpion)))
        thingGraph.add((propertyAffordance, td.name, Literal(parameterName+ "_history")))
        historyForm = BNode()
        thingGraph.add((propertyAffordance, td.hasForm, historyForm))
        thingGraph.add((historyForm, hctl.hasTarget,
                        URIRef(historicalTarget)))
        thingGraph.add((historyForm, htv.methodName, Literal(historicalType)))
        thingGraph.add((historyForm, hctl.hasOperationType, td.readProperty))
        thingGraph.add((historyForm, hctl.forContentType, Literal(historicalContentType)))
        print(thingGraph.serialize())
        thingGraph.serialize(directory + "/"+parameterName+".ttl" ,format="ttl")


