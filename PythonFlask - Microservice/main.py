from flask import Flask, send_from_directory,send_file
from flask import render_template
from rdf.ontology import Ontology
from rdflib import Graph, URIRef, Literal, BNode ,Namespace
from rdflib.namespace import RDF ,XSD , OWL ,RDFS ,BRICK ,FOAF
from ifc.readIFC import  IFCInformationExtratcion

t = IFCInformationExtratcion(r"C:\Users\ARUN\OneDrive\Desktop\MINESIFC.ifc" , r"C:\Users\ARUN\OneDrive\Desktop\New folder (31)")
g = t.propSetExtraction()
app = Flask(__name__)

ontology = Ontology()
# get request to send the rdf graphs
@app.route('/test',methods=['GET'])
def createdOntology():
    return ontology.createdOntology()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)


