from rdflib import Graph, URIRef, Literal, BNode ,Namespace
from rdflib.namespace import RDF ,XSD , OWL ,RDFS ,BRICK
class Ontology:

    def createdOntology(self):
        onto = Graph()
        # bot namespace
        bot = Namespace("https://w3id.org/bot#")
        onto.bind("bot", bot)

        # custom namespace
        myOnto = Namespace("http://10.103.1.173:8080/test.ttl")
        onto.bind("myOnto", myOnto)

        # ifc window class
        onto.add((myOnto.IFCWindow, RDF.type, OWL.Class))
        onto.add((myOnto.IFCWindow, RDFS.comment, Literal("total number of windows", lang="en")))
        onto.add((myOnto.IFCWindow, RDFS.label, Literal("ifcWindow", lang="en")))
        onto.add((myOnto.IFCWindow, RDFS.subClassOf, bot.Element))

        # ifc Building class
        onto.add((myOnto.IfcBuilding, RDF.type, OWL.Class))
        onto.add((myOnto.IfcBuilding, RDFS.comment, Literal("Building information Class", lang="en")))
        onto.add((myOnto.IfcBuilding, RDFS.label, Literal("IfcBuilding", lang="en")))
        onto.add((myOnto.IfcBuilding, RDFS.subClassOf, bot.Element))

        # ifc BuildingElement Proxy
        onto.add((myOnto.IfcBuildingElementProxy, RDF.type, OWL.Class))
        onto.add((myOnto.IfcBuildingElementProxy, RDFS.comment, Literal("Building Element Proxy Class", lang="en")))
        onto.add((myOnto.IfcBuildingElementProxy, RDFS.label, Literal("IfcBuildingElementProxy", lang="en")))
        onto.add((myOnto.IfcBuildingElementProxy, RDFS.subClassOf, bot.Element))

        # ifc element id creation
        onto.add((myOnto.hasIFCguid, RDF.type, RDF.Property))
        onto.add((myOnto.hasIFCguid, RDFS.comment, Literal("unique id of each element", lang="en")))
        onto.add((myOnto.hasIFCguid, RDFS.label, Literal("IFCguid", lang="en")))
        onto.add((myOnto.hasIFCguid, RDFS.range, XSD.string))
        onto.add((myOnto.hasIFCguid, RDFS.subPropertyOf, bot.Element))

        # ifc element reference
        onto.add((myOnto.hasReference, RDF.type, RDF.Property))
        onto.add((myOnto.hasReference, RDFS.comment, Literal("measurement reference of the elements", lang="en")))
        onto.add((myOnto.hasReference, RDFS.label, Literal("elementReference", lang="en")))
        onto.add((myOnto.hasReference, RDFS.range, XSD.string))
        onto.add((myOnto.hasReference, RDFS.subPropertyOf, bot.Element))

        # ifc element thermal tranmittance
        onto.add((myOnto.hasThermalTransmittance, RDF.type, RDF.Property))
        onto.add(
            (myOnto.hasThermalTransmittance, RDFS.comment, Literal("the value of thermal transmittance", lang="en")))
        onto.add((myOnto.hasThermalTransmittance, RDFS.label, Literal("elementThermalTransmittance", lang="en")))
        onto.add((myOnto.hasThermalTransmittance, RDFS.range, XSD.float))
        onto.add((myOnto.hasThermalTransmittance, RDFS.subPropertyOf, bot.Element))

        # ifc element height
        onto.add((myOnto.hasHeight, RDF.type, RDF.Property))
        onto.add((myOnto.hasHeight, RDFS.comment, Literal("height of the element", lang="en")))
        onto.add((myOnto.hasHeight, RDFS.label, Literal("elementHeight", lang="en")))
        onto.add((myOnto.hasHeight, RDFS.range, XSD.float))
        onto.add((myOnto.hasHeight, RDFS.subPropertyOf, bot.Element))

        # ifc element width
        onto.add((myOnto.hasWidth, RDF.type, RDF.Property))
        onto.add((myOnto.hasWidth, RDFS.comment, Literal("width of the element", lang="en")))
        onto.add((myOnto.hasWidth, RDFS.label, Literal("elementWidth", lang="en")))
        onto.add((myOnto.hasWidth, RDFS.range, XSD.float))
        onto.add((myOnto.hasWidth, RDFS.subPropertyOf, bot.Element))

        # ifc element area
        onto.add((myOnto.hasArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasArea, RDFS.comment, Literal("area of the element", lang="en")))
        onto.add((myOnto.hasArea, RDFS.label, Literal("elementArea", lang="en")))
        onto.add((myOnto.hasArea, RDFS.range, XSD.float))
        onto.add((myOnto.hasArea, RDFS.subPropertyOf, bot.Element))

        # ifc element sill height
        onto.add((myOnto.hasSillHeight, RDF.type, RDF.Property))
        onto.add((myOnto.hasSillHeight, RDFS.comment, Literal("sill height  of the element", lang="en")))
        onto.add((myOnto.hasSillHeight, RDFS.label, Literal("elementSillHeight", lang="en")))
        onto.add((myOnto.hasSillHeight, RDFS.range, XSD.float))
        onto.add((myOnto.hasSillHeight, RDFS.subPropertyOf, bot.Element))

        # ifc element storey type
        onto.add((myOnto.belongToLevel, RDF.type, RDF.Property))
        onto.add((myOnto.belongToLevel, RDFS.comment, Literal("element belong to which level", lang="en")))
        onto.add((myOnto.belongToLevel, RDFS.label, Literal("elementLevel", lang="en")))
        onto.add((myOnto.belongToLevel, RDFS.range, XSD.string))
        onto.add((myOnto.belongToLevel, RDFS.subPropertyOf, bot.Element))

        # ifc element volume
        onto.add((myOnto.hasVolume, RDF.type, RDF.Property))
        onto.add((myOnto.hasVolume, RDFS.comment, Literal("element has volume", lang="en")))
        onto.add((myOnto.hasVolume, RDFS.label, Literal("elementVolume", lang="en")))
        onto.add((myOnto.hasVolume, RDFS.range, XSD.float))
        onto.add((myOnto.hasVolume, RDFS.subPropertyOf, bot.Element))

        # ifc element head height
        onto.add((myOnto.hasHeadHeight, RDF.type, RDF.Property))
        onto.add((myOnto.hasHeadHeight, RDFS.comment, Literal("element has head height", lang="en")))
        onto.add((myOnto.hasHeadHeight, RDFS.label, Literal("elementHeadHeight", lang="en")))
        onto.add((myOnto.hasHeadHeight, RDFS.range, XSD.float))
        onto.add((myOnto.hasHeadHeight, RDFS.subPropertyOf, bot.Element))



        return onto.serialize( r"C:\Users\ARUN\OneDrive\Desktop\New folder (21)\tet.ttl" , format='ttl')
