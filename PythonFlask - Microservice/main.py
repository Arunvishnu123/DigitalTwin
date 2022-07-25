from flask import Flask, send_from_directory,send_file ,request
from flask import render_template
from rdf.ontology import Ontology
from flask_cors import CORS
from rdflib import Graph, URIRef, Literal, BNode ,Namespace
from rdflib.namespace import RDF ,XSD , OWL ,RDFS ,BRICK ,FOAF
from ifc.readIFC import  IFCInformationExtratcion
from ThingRDF.thingRDFModeling import ThingDescriptionRDF
from ThingRDF.ThingDirectory import ThingDirectory
import time
start_time = time.time()
#t = IFCInformationExtratcion(r"C:\Users\ARUN\OneDrive\Desktop\MINESIFC.ifc" , r"C:\Users\ARUN\OneDrive\Desktop\finaltest")
#g = t.propSetExtraction()
app = Flask(__name__)
DEBUG = True
CORS(app)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
ontology = Ontology()
print("--- %s seconds ---" % (time.time() - start_time))

# get request to send the rdf graphs
@app.route('/',methods=['GET'])
def createdOntology():
    return "Welcome to RDF Graph Generator"


@app.route('/updateknowledge' , methods=['GET' , 'POST'])
def updateKnowledge():
    if request.method == 'POST':
        thingDirectoryPath =  r"C:\Users\ARUN\OneDrive\Desktop\ThingDirectory"
        thingRDFModeling  =  ThingDescriptionRDF()
        thingDirectoryCreation =  ThingDirectory()
        data  = request.json
        print(data["IfcClass"])
        path = thingDirectoryCreation.creation( data["IfcClass"] , data["IfcGuid"],thingDirectoryPath )
        print(path)
        thingRDFModeling.rdfCreation(path,data["IfcClass"] ,data["IfcGuid"] ,  data["sensorType"] ,data["thingType"],data["thingEventDescription"] , data["thingHistroicalDescription"] , data["eventContentType"] ,  data["historicalContentType"] , data["eventBasedTarget"] , data["historicalTarget"] , data["eventTargetType"] ,data["historicalTargetType"])
        print(request.json)

        #update RDF graphs

        graph =  Graph()
        graph.parse("http://localhost:4000/" + data["IfcClass"] + "/" + data["IfcGuid"])

        url = URIRef("http://127.0.0.1:3000/" + data["IfcClass"] + "/" + data["IfcGuid"])
        urlLocal = url + "/" + data["thingType"] + "#"
        dogont = Namespace("http://elite.polito.it/ontologies/dogont.owl")
        graph.bind("dogont",dogont)
        saref = Namespace("https://saref.etsi.org/core/v3.1.1/")
        graph.bind("saref", saref)
        hctl = Namespace("https://www.w3.org/2019/wot/hypermedia#")
        graph.bind("hctl", hctl)

        graph.add((url, dogont.hasSensor, Literal(urlLocal)))
        graph.add((urlLocal,saref.hasSensorType ,Literal(data["thingType"])) )
        graph.add((urlLocal,hctl.hasTarget ,URIRef(url + '/' + data["thingType"])))
        graph.serialize(r"C:/Users/ARUN/OneDrive/Desktop/finaltest" + "/" + data["IfcClass"] + "/" + data["IfcGuid"] + ".ttl" , format="ttl" )
        return "test"





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
