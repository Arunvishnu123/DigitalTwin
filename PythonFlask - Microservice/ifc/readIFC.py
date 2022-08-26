import ifcopenshell.util
import ifcopenshell.util.element
import os
import ifcopenshell.geom
from ifcopenshell.util.selector import Selector

from rdf.rdfTriple import RDFGraph
from rdf.rdfTripleIFCClass import IFCClassTriple
from rdf.rdfIfcClass import IFCClass

class IFCInformationExtratcion:

    def __init__(self, location, tripleStoreDirectory):
        self.location = location
        self.ifcClasses = []
        self.finalIFCClass = []
        self.test = RDFGraph()
        self.tripleStoreDirectory = tripleStoreDirectory
        self.relatedElementList = []
        self.selector  =  Selector()



    def getUniqueItems(self, iterable):
        seen = set()
        result = []
        for item in iterable:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result



    def propSetExtraction(self):
        ifc_file = ifcopenshell.open(self.location)
        products = ifc_file.by_type('IfcProduct')
        for product in products:
            self.ifcClasses.append(product.is_a())
        self.finalIFCClass = self.getUniqueItems(self.ifcClasses)
        t = []
        print(self.finalIFCClass)
        for i in self.finalIFCClass:
            ifcClassNumber = {}
            print(i)
            ifcClassNumber["ifcClassName"] = i
            ifcClassTriple = IFCClassTriple(i)
            ifcClassTriple.createIFCClassTriple()
            path = os.path.join(self.tripleStoreDirectory, i)
            os.mkdir(path)
            products = ifc_file.by_type(i)
            ifcClassTriple.addIFCClassNumber(len(products))
            ifcClassNumber["elementsCount"] = len(products)
            t.append(ifcClassNumber)
            print()
            for product in products:
                #settings = ifcopenshell.geom.settings()
                #try:
                 #shape = ifcopenshell.geom.create_shape(settings,product)
                 #faces = shape.geometry.faces
                 #verts = shape.geometry.verts
                 #grouped_verts = [[verts[i], verts[i + 1], verts[i + 2]] for i in range(0, len(verts), 3)]
                 #grouped_faces = [[faces[i], faces[i + 1], faces[i + 2]] for i in range(0, len(faces), 3)]
                #except:
                    #continue
                propJson = {"IFCguid": product.GlobalId}
                line1 = ifcopenshell.util.element.get_psets(product)
                ifcClassTriple.addIFCElementLink(product.GlobalId)
                for main in line1:
                    for properties in line1[main]:
                        propJson[properties] = line1[main][properties]
                if i == "IfcSpace":
                    self.relatedElementList = []
                    self.selector = Selector()
                    elements = self.selector.parse(ifc_file, "@ #" + product.GlobalId)
                    for element in elements:
                        relatedElement = (element.is_a(), element.GlobalId)
                        self.relatedElementList.append(relatedElement)
                if i == "IfcBuildingStorey":
                    self.relatedElementList =  []
                    storeyElements = self.selector.parse(ifc_file ,"@ #" + product.GlobalId)
                    for storeyElement in storeyElements:
                        relatedStoreyElement = (storeyElement.is_a() , storeyElement.GlobalId)
                        self.relatedElementList.append(relatedStoreyElement)
                grouped_verts = []
                grouped_faces = []
                print(propJson)
                self.test.createRDFGraph(i, product.GlobalId, propJson, path, self.relatedElementList , grouped_verts ,  grouped_faces  )
            ifcClassTriple.createFile(self.tripleStoreDirectory)
            print(ifcClassNumber)
            ifcClass = IFCClass(self.tripleStoreDirectory)
            print(t)
            ifcClass.ifcClassGeneration(t)
