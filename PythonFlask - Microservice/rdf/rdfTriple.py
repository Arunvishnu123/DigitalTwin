from rdflib import Graph, URIRef, Literal, BNode ,Namespace
from rdflib.namespace import RDF ,XSD , OWL ,RDFS ,BRICK ,SKOS


class RDFGraph:
    def __init__(self):
        pass

    def createRDFGraph(self, ifcClass, ifcGuid ,test , path , relatedElementList):
        rdfG = Graph()
        # rdfG.parse("https://w3id.org/bot#")
        # props namespace
        props = Namespace("http://127.0.0.1:5000/test")
        rdfG.bind("props", props)
        # bot namespace
        bot = Namespace("https://w3id.org/bot#")
        rdfG.bind('bot', bot)

        type = URIRef("http://127.0.0.1:3000/" + ifcClass + "/" + ifcGuid)
        rdfG.add((type, RDF.type, bot.Element))
        if (ifcClass == "ifcWindow" or ifcClass == "IFCWindow" or ifcClass == "ifcwindow"):
            rdfG.add((type, RDF.type, props.IfcWindow))
        if (ifcClass == "ifcDoor" or ifcClass == "IFCDoor" or ifcClass == "ifcdoor"):
            rdfG.add((type, RDF.type, props.IfcDoor))
        if (ifcClass == "IfcWall"):
            rdfG.add((type, RDF.type, props.IfcWall))
        if (ifcClass == "IfcBeam"):
            rdfG.add((type, RDF.type, props.IfcBeam))
        if(ifcClass == "IfcBuilding"):
            rdfG.add((type,RDF.type , props.IfcBuilding))
        for i in test:
            if(i == "Level"):
                rdfG.add((type, props.belongToLevel, Literal(test["Level"], datatype=XSD["string"])))
            if(i == "Area"):
                rdfG.add((type, props.hasArea, Literal(test["Area"], datatype=XSD['float'])))
            if(i == "Head Height"):
                rdfG.add((type, props.hasHeadHeight, Literal(test["Head Height"], datatype=XSD['float'])))
            if(i == "Height"):
               rdfG.add((type, props.hasHeight, Literal(test["Height"], datatype=XSD['float'])))
            if (i == "IFCguid"):
               rdfG.add((type, props.hasIFCguid, Literal(test["IFCguid"], datatype=XSD["string"])))
            if (i == "Reference"):
                rdfG.add((type, props.hasReference, Literal(test["Reference"], datatype=XSD["string"])))
            if (i == "Sill Height"):
               rdfG.add((type, props.hasSillHeight, Literal(test["Sill Height"], datatype=XSD['float'])))
            if ( i == "ThermalTransmittance"):
               rdfG.add((type, props.hasThermalTransmittance, Literal(test["ThermalTransmittance"], datatype=XSD['float'])))
            if ( i == "Volumn"):
               rdfG.add((type, props.hasVolume, Literal(test["Volume"], datatype=XSD['float'])))
            if ( i == "Width"):
               rdfG.add((type, props.hasWidth, Literal(test["Width"], datatype=XSD['float'])))
            if(i == "Length"):
                rdfG.add((type,props.hasLength,Literal(test["Length"], datatype=XSD['float'])))
            if(i == "GrossFootprintArea"):
                rdfG.add((type,props.hasGrossFootprintArea , Literal(test["GrossFootprintArea"] ,datatype=XSD["float"])))
            if(i == "NetVolume"):
                rdfG.add((type ,props.hasNetVolume , Literal(test["NetVolume"] ,datatype=XSD['float'] )))
            if(i == "NetSideArea"):
                rdfG.add((type ,props.hasNetSideArea , Literal(test["NetSideArea"] , datatype=XSD['float'])))
            if(i == "Type"):
                rdfG.add((type ,props.belongsToType , Literal(test["Type"] , datatype=XSD['string'])))
            if(i == "Unconnected Height"):
                rdfG.add((type ,props.hasUnconnectedHeight, Literal(test["Unconnected Height"] , datatype=XSD["float"])))
            if(i == "Location Line"):
                rdfG.add((type ,props.locationLine , Literal(test["Location Line"] , datatype=XSD['string'])))
            if(i == "Roughness"):
                rdfG.add((type , props.hasRoughness, Literal(test["Roughness"] , datatype=XSD["float"])))
            if(i == "Slope"):
                rdfG.add((type , props.hasSlop ,Literal(test["Slope"] ,datatype=XSD["float"])))
            if(i == "Span"):
                rdfG.add((type , props.hasSpan , Literal(test["Span"] , datatype=XSD["float"])))
            if(i == "CrossSectionArea"):
                rdfG.add((type , props.hasCrossSectionArea , Literal(test["CrossSectionArea"] ,datatype=XSD["float"] )))
            if (i == "OuterSurfaceArea"):
                rdfG.add((type, props.hasOuterSurfaceArea, Literal(test["OuterSurfaceArea"], datatype=XSD["float"])))
            if (i == "GrossSurfaceArea"):
                rdfG.add((type, props.hasGrossSurfaceArea, Literal(test["GrossSurfaceArea"], datatype=XSD["float"])))
            if (i == "NetSurfaceArea"):
                rdfG.add((type, props.hasNetSurfaceArea, Literal(test["NetSurfaceArea"], datatype=XSD["float"])))
            if (i == "GrossVolume"):
                rdfG.add((type, props.hasGrossVolume, Literal(test["GrossVolume"], datatype=XSD["float"])))
            if (i == "End Level Offset"):
                rdfG.add((type, props.hasEndLevelOffset, Literal(test["End Level Offset"], datatype=XSD["float"])))
            if (i == "Cross-Section Rotation"):
                rdfG.add((type, props.hasCrossSectionRotation, Literal(test["Cross-Section Rotation"], datatype=XSD["float"])))
            if (i == "Reference Level"):
                rdfG.add((type, props.hasReferencLevel, Literal(test["Reference Level"], datatype=XSD["string"])))
            if (i == "Reference Level Elevation"):
                rdfG.add((type, props.hasReferenceLevelElevation, Literal(test["Reference Level Elevation"], datatype=XSD["float"])))
            if (i == "Start Level Offset"):
                rdfG.add((type, props.hasStartLevelOffset, Literal(test["Start Level Offset"], datatype=XSD["float"])))
            if (i == "Elevation at Bottom"):
                rdfG.add((type, props.hasElevationatBottom, Literal(test["Elevation at Bottom"], datatype=XSD["float"])))
            if (i == "Elevation at Top"):
                rdfG.add((type, props.hasElevationatTop, Literal(test["Elevation at Top"], datatype=XSD["float"])))
            if (i == "Elevation at Bottom"):
                rdfG.add((type, props.hasElevationatBottom, Literal(test["Elevation at Bottom"], datatype=XSD["float"])))
            if (i == "Cut Length"):
                rdfG.add((type, props.hasCutLength, Literal(test["Cut Length"], datatype=XSD["float"])))
            if (i == "NumberOfStoreys"):
                rdfG.add((type, props.hasTotalStoreys, Literal(test["NumberOfStoreys"], datatype=XSD["float"])))
            if (i == "Building Name"):
                rdfG.add((type, props.BuildingName, Literal(test["Building Name"], datatype=XSD["string"])))
            if (i == "Project Address"):
                rdfG.add((type, props.Address, Literal(test["Project Address"], datatype=XSD["string"])))
            if (i == "DEF_Adresse"):
                rdfG.add((type, props.Address, Literal(test["DEF_Adresse"], datatype=XSD["string"])))
            if (i == "Name"):
                rdfG.add((type, props.storeyName, Literal(test["Name"], datatype=XSD["string"])))
            if (i == "Elevation"):
                rdfG.add((type, props.hasElevation, Literal(test["Elevation"], datatype=XSD["string"])))




            if ifcClass == "IfcSpace":
                for k in relatedElementList:
                    containsElementLink = "http://127.0.0.1:3000/" + k[0] + "/" + k[1]
                    rdfG.add((type , bot.containsElement , URIRef(containsElementLink)))
            if ifcClass == "IfcBuildingStorey":
                for h in relatedElementList:
                    storeyElementList = "http://127.0.0.1:3000/" + h[0] + "/" + h[1]
                    rdfG.add((type, bot.containsElement, URIRef(storeyElementList)))
        return rdfG.serialize(path+"/" + ifcGuid + ".ttl" ,format="ttl")