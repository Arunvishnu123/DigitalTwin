import ifcopenshell.util
import ifcopenshell.util.element
import os
from ifcopenshell.util.selector import Selector

from rdf.rdfTriple import RDFGraph
from rdf.rdfTripleIFCClass import IFCClassTriple

mainArray = {}
j = {}
propArray = []
z = {}


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
        for i in self.finalIFCClass:
            print(i)
            ifcClassTriple = IFCClassTriple(i)
            ifcClassTriple.createIFCClassTriple()
            path = os.path.join(self.tripleStoreDirectory, i)
            os.mkdir(path)
            products = ifc_file.by_type(i)
            ifcClassTriple.addIFCClassNumber(len(products))

            for product in products:
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

                self.test.createRDFGraph(i, product.GlobalId, propJson, path, self.relatedElementList)
            ifcClassTriple.createFile(self.tripleStoreDirectory)
