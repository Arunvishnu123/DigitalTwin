from flask import Flask, send_from_directory,send_file ,request
from flask import render_template
from rdf.ontology import Ontology
from flask_cors import CORS
from rdflib import Graph, URIRef, Literal, BNode ,Namespace
from rdflib.namespace import RDF ,XSD , OWL ,RDFS ,BRICK ,FOAF
from ifc.readIFC import  IFCInformationExtratcion

#t = IFCInformationExtratcion(r"C:\Users\ARUN\OneDrive\Desktop\MINESIFC.ifc" , r"C:\Users\ARUN\OneDrive\Desktop\New folder (42)")
#g = t.propSetExtraction()
app = Flask(__name__)
DEBUG = True
CORS(app)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
ontology = Ontology()
# get request to send the rdf graphs
@app.route('/',methods=['GET'])
def createdOntology():
    return "Welcome to RDF Graph Generator"


@app.route('/updateknowledge' , methods=['GET' , 'POST'])
def updateKnowledge():
    if request.method == 'GET':
        return "Helo"

    if request.method == 'POST':
        sparql  =  request.form['sparqlQuery']
        restLink  =  request.form['restLink']

        print(sparql)
        print(restLink)
        return sparql



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
