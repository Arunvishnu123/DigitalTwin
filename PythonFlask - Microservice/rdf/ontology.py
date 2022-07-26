from rdflib import Graph, URIRef, Literal, BNode ,Namespace
from rdflib.namespace import RDF ,XSD , OWL ,RDFS ,BRICK
class Ontology:

    def __init__(self):
        pass


    def createdOntology(self):
        onto = Graph()
        # bot namespace
        bot = Namespace("https://w3id.org/bot#")
        onto.bind("bot", bot)

        # custom namespace
        myOnto = Namespace("http://10.103.1.173:8080/test.ttl")
        onto.bind("", myOnto)

        #########################################################################################################################

        # ifc element id creation
        onto.add((myOnto.hasIFCguid, RDF.type, RDF.Property))
        onto.add((myOnto.hasIFCguid, RDFS.isDefinedBy, Literal("The IFC specification uses an unique identifier for object instances that follows the universal unique identifier standard UUID with its implementation as a globally unique identifier GUID. The generated GUID is compressed for exchange purpose following a published compression function.", lang="en")))
        onto.add((myOnto.hasIFCguid, RDFS.label, Literal("IFCguid", lang="en")))
        onto.add((myOnto.hasIFCguid , RDFS.comment ,Literal("" , lang="en")))
        onto.add((myOnto.hasIFCguid, RDFS.range, XSD.string))
        onto.add((myOnto.hasIFCguid, RDFS.subPropertyOf, bot.Element))

        # ifc element reference
        onto.add((myOnto.hasReference, RDF.type, RDF.Property))
        onto.add((myOnto.hasReference, RDFS.isDefinedBy, Literal("Reference is a relationship between objects in which one object designates, or acts as a means by which to connect to or link to, another object.", lang="en")))
        onto.add((myOnto.hasReference, RDFS.label, Literal("Reference", lang="en")))
        onto.add((myOnto.hasReference , RDFS.comment ,Literal("show the reference" , lang="en")))
        onto.add((myOnto.hasReference, RDFS.range, XSD.string))
        onto.add((myOnto.hasReference, RDFS.subPropertyOf, bot.Element))

        # ifc element thermal tranmittance
        onto.add((myOnto.hasThermalTransmittance, RDF.type, RDF.Property))
        onto.add((myOnto.hasThermalTransmittance, RDFS.isDefinedBy, Literal("Thermal transmittance (U-value) defines the ability of an element of structure to transmit heat under steady-state conditions. It is a measure of the quantity of heat that will flow through unit area in unit time per unit difference in temperature of the individual environments between which the structure intervenes.", lang="en")))
        onto.add((myOnto.hasThermalTransmittance, RDFS.label, Literal("elementThermalTransmittance", lang="en")))
        onto.add((myOnto.hasThermalTransmittance , RDFS.comment ,Literal("unit of thermal transmittance is W/m²K" , lang="en")))
        onto.add((myOnto.hasThermalTransmittance, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasThermalTransmittance, RDFS.subPropertyOf, bot.Element))

        # ifc element height
        onto.add((myOnto.hasHeight, RDF.type, RDF.Property))
        onto.add((myOnto.hasHeight, RDFS.isDefinedBy, Literal("The measurement of the distance of an object from the base to the top.", lang="en")))
        onto.add((myOnto.hasHeight, RDFS.label, Literal("elementHeight", lang="en")))
        onto.add((myOnto.hasHeight , RDFS.comment ,Literal("Measurements in Meters" , lang="en")))
        onto.add((myOnto.hasHeight, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasHeight, RDFS.subPropertyOf, bot.Element))

        # ifc element width
        onto.add((myOnto.hasWidth, RDF.type, RDF.Property))
        onto.add((myOnto.hasWidth, RDFS.isDefinedBy, Literal("The distance from side to side.", lang="en")))
        onto.add((myOnto.hasWidth, RDFS.label, Literal("elementWidth", lang="en")))
        onto.add((myOnto.hasWidth, RDFS.comment ,Literal("Measurements are in Meters" , lang="en")))
        onto.add((myOnto.hasWidth, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasWidth, RDFS.subPropertyOf, bot.Element))

        # ifc element area
        onto.add((myOnto.hasArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasArea, RDFS.isDefinedBy, Literal("The area is the region bounded by the shape of an Ifc element.", lang="en")))
        onto.add((myOnto.hasArea, RDFS.label, Literal("elementArea", lang="en")))
        onto.add((myOnto.hasArea , RDFS.comment ,Literal("Measurements are in Meter Square" , lang="en")))
        onto.add((myOnto.hasArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasArea, RDFS.subPropertyOf, bot.Element))

        # ifc element sill height
        onto.add((myOnto.hasSillHeight, RDF.type, RDF.Property))
        onto.add((myOnto.hasSillHeight, RDFS.isDefinedBy, Literal("The height between the base of the window and floor level is known as sill height. ", lang="en")))
        onto.add((myOnto.hasSillHeight, RDFS.label, Literal("elementSillHeight", lang="en")))
        onto.add((myOnto.hasSillHeight , RDFS.comment ,Literal("Measurement are in meters" , lang="en")))
        onto.add((myOnto.hasSillHeight, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasSillHeight, RDFS.subPropertyOf, bot.Element))

        # ifc element storey type
        onto.add((myOnto.belongToLevel, RDF.type, RDF.Property))
        onto.add((myOnto.belongToLevel, RDFS.isDefinedBy, Literal("A part of a building comprising all the rooms that are on the same level.", lang="en")))
        onto.add((myOnto.belongToLevel, RDFS.label, Literal("elementLevel", lang="en")))
        onto.add((myOnto.belongToLevel , RDFS.comment ,Literal("represent the floor level" , lang="en")))
        onto.add((myOnto.belongToLevel, RDFS.range, XSD.string))
        onto.add((myOnto.belongToLevel, RDFS.subPropertyOf, bot.Element))

        # ifc element volume
        onto.add((myOnto.hasVolume, RDF.type, RDF.Property))
        onto.add((myOnto.hasVolume, RDFS.isDefinedBy, Literal("Volume is a mathematical quantity that shows the amount of three-dimensional space occupied by an object or a closed surface.", lang="en")))
        onto.add((myOnto.hasVolume, RDFS.label, Literal("elementVolume", lang="en")))
        onto.add((myOnto.hasVolume , RDFS.comment ,Literal("Measurements of the volumn ir represented in m3" , lang="en")))
        onto.add((myOnto.hasVolume, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasVolume, RDFS.subPropertyOf, bot.Element))

        # ifc element head height
        onto.add((myOnto.hasHeadHeight, RDF.type, RDF.Property))
        onto.add((myOnto.hasHeadHeight, RDFS.isDefinedBy, Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasHeadHeight, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasHeadHeight , RDFS.comment ,Literal("" , lang="en")))
        onto.add((myOnto.hasHeadHeight, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasHeadHeight, RDFS.subPropertyOf, bot.Element))

        # ifc element Slope
        onto.add((myOnto.hasSlope, RDF.type, RDF.Property))
        onto.add((myOnto.hasSlope, RDFS.isDefinedBy, Literal("Slope means the steepest slope across building footprint measured from one side of the building to another.", lang="en")))
        onto.add((myOnto.hasSlope, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasSlope , RDFS.comment ,Literal("slope is unitless" , lang="en")))
        onto.add((myOnto.hasSlope, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasSlope, RDFS.subPropertyOf, bot.Element))

        # ifc element Span
        onto.add((myOnto.hasSpan, RDF.type, RDF.Property))
        onto.add((myOnto.hasSpan, RDFS.isDefinedBy,Literal("Span is the distance between two intermediate supports for a structure, e.g. a beam or a bridge.", lang="en")))
        onto.add((myOnto.hasSpan, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasSpan, RDFS.comment, Literal("Measurements of span is in Meters", lang="en")))
        onto.add((myOnto.hasSpan, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasSpan, RDFS.subPropertyOf, bot.Element))

        # ifc element CrossSectionArea
        onto.add((myOnto.hasCrossSectionArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasCrossSectionArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasCrossSectionArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasCrossSectionArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasCrossSectionArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasCrossSectionArea, RDFS.subPropertyOf, bot.Element))

        # ifc element head height
        onto.add((myOnto.hasHeadHeight, RDF.type, RDF.Property))
        onto.add((myOnto.hasHeadHeight, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasHeadHeight, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasIFCguid, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasHeadHeight, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasHeadHeight, RDFS.subPropertyOf, bot.Element))

        # ifc element OuterSurfaceArea
        onto.add((myOnto.hasOuterSurfaceArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasOuterSurfaceArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasOuterSurfaceArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasOuterSurfaceArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasOuterSurfaceArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasOuterSurfaceArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossSurfaceArea
        onto.add((myOnto.hasGrossSurfaceArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossSurfaceArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossSurfaceArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossSurfaceArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossSurfaceArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasHGrossSurfaceArea, RDFS.subPropertyOf, bot.Element))

        # ifc element NetSurfaceArea
        onto.add((myOnto.hasNetSurfaceArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasNetSurfaceArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasNetSurfaceArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasNetSurfaceArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasNetSurfaceArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasNetSurfaceArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossVolume
        onto.add((myOnto.hasGrossVolume, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossVolume, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossVolume, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossVolume, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossVolume, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossVolume, RDFS.subPropertyOf, bot.Element))

        # ifc element NetVolume
        onto.add((myOnto.hasNetVolume, RDF.type, RDF.Property))
        onto.add((myOnto.hasNetVolume, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasNetVolume, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasNetVolume, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasNetVolume, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasNetVolume, RDFS.subPropertyOf, bot.Element))

        # ifc element Cross-Section Rotation
        onto.add((myOnto.hasCrossSectionRotation, RDF.type, RDF.Property))
        onto.add((myOnto.hasCrossSectionRotation, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasCrossSectionRotation, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasCrossSectionRotation, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasCrossSectionRotation, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasCrossSectionRotation, RDFS.subPropertyOf, bot.Element))

        # ifc element ReferenceLevelElevation
        onto.add((myOnto.hasReferenceLevelElevation, RDF.type, RDF.Property))
        onto.add((myOnto.hasReferenceLevelElevation, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasReferenceLevelElevation, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasReferenceLevelElevation, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasReferenceLevelElevation, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasEnReferenceLevelElevation, RDFS.subPropertyOf, bot.Element))

        # ifc element Start Level Offset
        onto.add((myOnto.hasStartLevelOffset, RDF.type, RDF.Property))
        onto.add((myOnto.hasStartLevelOffset, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasStartLevelOffset, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasStartLevelOffset, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasStartLevelOffset, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasStartLevelOffset, RDFS.subPropertyOf, bot.Element))

        # ifc element Elevation at Bottom
        onto.add((myOnto.hasElevationatBottom, RDF.type, RDF.Property))
        onto.add((myOnto.hasElevationatBottom, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasElevationatBottom, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasElevationatBottom, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasElevationatBottom, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasElevationatBottom, RDFS.subPropertyOf, bot.Element))

        # ifc element Elevation at Top
        onto.add((myOnto.hasElevationatTop, RDF.type, RDF.Property))
        onto.add((myOnto.hasElevationatTop, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasElevationatTop, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasElevationatTop, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasElevationatTop, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasElevationatTop, RDFS.subPropertyOf, bot.Element))

        # ifc element Cut Length
        onto.add((myOnto.hasCutLength, RDF.type, RDF.Property))
        onto.add((myOnto.hasCutLength, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasCutLength, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasCutLength, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasCutLength, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasCutLength, RDFS.subPropertyOf, bot.Element))

        # ifc element Join Status
        onto.add((myOnto.hasJoinStatus, RDF.type, RDF.Property))
        onto.add((myOnto.hasJoinStatus, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasJoinStatus, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasJoinStatus, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasJoinStatus, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasJoinStatus, RDFS.subPropertyOf, bot.Element))

        # ifc element y Justification
        onto.add((myOnto.hasYJustification, RDF.type, RDF.Property))
        onto.add((myOnto.hasYJustification, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasyJustification, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasyJustification, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasyJustification, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasyJustification, RDFS.subPropertyOf, bot.Element))

        # ifc element y Offset Value
        onto.add((myOnto.hasyOffsetValue, RDF.type, RDF.Property))
        onto.add((myOnto.hasyOffsetValue, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasyOffsetValue, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasyOffsetValue, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasyOffsetValue, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasyOffsetValue, RDFS.subPropertyOf, bot.Element))

        # ifc elementyz Justification
        onto.add((myOnto.hasyzJustification, RDF.type, RDF.Property))
        onto.add((myOnto.hasyzJustification, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasyzJustification, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasyzJustification, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasyzJustification, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasyzJustification, RDFS.subPropertyOf, bot.Element))

        # ifc element z Justification
        onto.add((myOnto.haszJustification, RDF.type, RDF.Property))
        onto.add((myOnto.haszJustification, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.haszJustification, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.haszJustification, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.haszJustification, RDFS.range, XSD.decimal))
        onto.add((myOnto.haszJustification, RDFS.subPropertyOf, bot.Element))

        # ifc element zOffsetValue
        onto.add((myOnto.haszOffsetValue, RDF.type, RDF.Property))
        onto.add((myOnto.haszOffsetValue, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.haszOffsetValue, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.haszOffsetValue, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.haszOffsetValue, RDFS.range, XSD.decimal))
        onto.add((myOnto.haszOffsetValue, RDFS.subPropertyOf, bot.Element))

        # ifc element familytype
        onto.add((myOnto.belongtoFamilyType, RDF.type, RDF.Property))
        onto.add((myOnto.belongtoFamilyType, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.belongtoFamilyType, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.belongtoFamilyType, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.belongtoFamilyType, RDFS.range, XSD.decimal))
        onto.add((myOnto.belongtoFamilyType, RDFS.subPropertyOf, bot.Element))

        # ifc element number of storey
        onto.add((myOnto.storeyNumber, RDF.type, RDF.Property))
        onto.add((myOnto.storeyNumber, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.storeyNumber, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.storeyNumber, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.storeyNumber, RDFS.range, XSD.decimal))
        onto.add((myOnto.storeyNumber, RDFS.subPropertyOf, bot.Element))

        # ifc element depth
        onto.add((myOnto.hasDepth, RDF.type, RDF.Property))
        onto.add((myOnto.hasDepth, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasDepth, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasDepth, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasDepth, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasDepth, RDFS.subPropertyOf, bot.Element))

        # ifc element DEF_Level
        onto.add((myOnto.hasDEFLevel, RDF.type, RDF.Property))
        onto.add((myOnto.hasDEFLevel, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasDEFLevel, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasDEFLevel, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasDEFLevel, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasDEFLevel, RDFS.subPropertyOf, bot.Element))

        # ifc element Computation Height
        onto.add((myOnto.hasComputationHeight, RDF.type, RDF.Property))
        onto.add((myOnto.hasComputationHeight, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasComputationHeight, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasComputationHeight, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasComputationHeight, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasComputationHeight, RDFS.subPropertyOf, bot.Element))

        # ifc element length
        onto.add((myOnto.hasLength, RDF.type, RDF.Property))
        onto.add((myOnto.hasHeadLength, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasLength, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasLength, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasHLength, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasLength, RDFS.subPropertyOf, bot.Element))

        # ifc element TotalThickness
        onto.add((myOnto.hasTotalThickness, RDF.type, RDF.Property))
        onto.add((myOnto.hasTotalThickness, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasTotalThickness, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasTotalThickness, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasTotalThickness, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasTotalThickness, RDFS.subPropertyOf, bot.Element))

        # ifc element Roughness
        onto.add((myOnto.hasRoughness, RDF.type, RDF.Property))
        onto.add((myOnto.hasRoughness, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasRoughness, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasRoughness, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasRoughness, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasRoughness, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

###############################################
        # ifc element Perimeter
        onto.add((myOnto.hasPerimeter, RDF.type, RDF.Property))
        onto.add((myOnto.hasPerimeter, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasPerimeter, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasPerimeter, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasPerimeter, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasPerimeter, RDFS.subPropertyOf, bot.Element))


        # ifc element UnconnectedHeight
        onto.add((myOnto.hasUnconnectedHeight, RDF.type, RDF.Property))
        onto.add((myOnto.hasUnconnectedHeight, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasUnconnectedHeight, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasUnconnectedHeight, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasUnconnectedHeight, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasUnconnectedHeight, RDFS.subPropertyOf, bot.Element))

        # ifc element Angle
        onto.add((myOnto.hasHorizontalGridAngle, RDF.type, RDF.Property))
        onto.add((myOnto.hasHorizontalGridAngle, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasHorizontalGridAngle, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasHorizontalGridAngle, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasHorizontalGridAngle, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasHorizontalGridAngle, RDFS.subPropertyOf, bot.Element))

        # ifc element Justification
        onto.add((myOnto.hasHorizontalGridJustification, RDF.type, RDF.Property))
        onto.add((myOnto.hasHorizontalGridJustification, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasHorizontalGridJustification, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasHorizontalGridJustification, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasHorizontalGridJustification, RDFS.range, XSD.string))
        onto.add((myOnto.hasHorizontalGridJustification, RDFS.subPropertyOf, bot.Element))

        # ifc element offset
        onto.add((myOnto.hasHorizontalGridOffset, RDF.type, RDF.Property))
        onto.add((myOnto.hasHorizontalGridOffset, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasHorizontalGridOffset, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasHorizontalGridOffset, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasHorizontalGridOffset, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasHorizontalGridOffset, RDFS.subPropertyOf, bot.Element))

        # ifc element number
        onto.add((myOnto.hasHorizontalGridNumber, RDF.type, RDF.Property))
        onto.add((myOnto.hasHorizontalGridNumber, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasHorizontalGridNumber, RDFS.label,
                  Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasHorizontalGridNumber, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasHorizontalGridNumber, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasHorizontalGridNumber, RDFS.subPropertyOf, bot.Element))

        # ifc element Angle
        onto.add((myOnto.hasVerticalGridAngle, RDF.type, RDF.Property))
        onto.add((myOnto.hasVerticalGridAngle, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasVerticalGridAngle, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasVerticalGridAngle, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasVerticalGridAngle, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasVerticalGridAngle, RDFS.subPropertyOf, bot.Element))

        # ifc element Justification
        onto.add((myOnto.hasVerticalGridJustification, RDF.type, RDF.Property))
        onto.add((myOnto.hasVerticalGridJustification, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasVerticalGridJustification, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasVerticalGridJustification, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasVerticalGridJustification, RDFS.range, XSD.string))
        onto.add((myOnto.hasVerticalGridJustification, RDFS.subPropertyOf, bot.Element))

        # ifc element offset
        onto.add((myOnto.hasVerticalGridOffset, RDF.type, RDF.Property))
        onto.add((myOnto.hasVerticalGridOffset, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasVerticalGridOffset, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasVerticalGridOffset, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasVerticalGridOffset, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasVerticalGridOffset, RDFS.subPropertyOf, bot.Element))

        # ifc element number
        onto.add((myOnto.hasVerticalGridNumber, RDF.type, RDF.Property))
        onto.add((myOnto.hasVerticalGridNumber, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasVerticalGridNumber, RDFS.label,
                  Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasVerticalGridNumber, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasVerticalGridNumber, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasVerticalGridNumber, RDFS.subPropertyOf, bot.Element))

        # ifc element angle
        onto.add((myOnto.hasAngle, RDF.type, RDF.Property))
        onto.add((myOnto.hasAngle, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasAngle, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasAngle, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasAngle, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasAngle, RDFS.subPropertyOf, bot.Element))

        # ifc element Bend Radius
        onto.add((myOnto.hasBendRadius, RDF.type, RDF.Property))
        onto.add((myOnto.hasBendRadius, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasBendRadius, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasBendRadius, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasBendRadius, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasBendRadius, RDFS.subPropertyOf, bot.Element))

        # ifc element Path height
        onto.add((myOnto.hasPathHeight, RDF.type, RDF.Property))
        onto.add((myOnto.hasPathHeight, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasPathHeight, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasPathHeight, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasPathHeight, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasPathHeight, RDFS.subPropertyOf, bot.Element))

        # ifc element Path width
        onto.add((myOnto.hasPathwidth, RDF.type, RDF.Property))
        onto.add((myOnto.hasPathwidth, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasPathwidth, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasPathwidth, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasPathwidth, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasPathwidth, RDFS.subPropertyOf, bot.Element))

        # ifc element Path length
        onto.add((myOnto.hasPathLength, RDF.type, RDF.Property))
        onto.add((myOnto.hasPathLength, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasPathLength, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasPathLength, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasPathLength, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasPathLength, RDFS.subPropertyOf, bot.Element))

        # ifc element Size
        onto.add((myOnto.hasSize, RDF.type, RDF.Property))
        onto.add((myOnto.hasSize, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGSize, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasSize, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasSize, RDFS.range, XSD.string))
        onto.add((myOnto.hasGSize, RDFS.subPropertyOf, bot.Element))

        # ifc element Extrmit Center
        onto.add((myOnto.hasExtrmitCenter, RDF.type, RDF.Property))
        onto.add((myOnto.hasExtrmitCenter, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasExtrmitCenter, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasExtrmitCenter, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasExtrmitCenter, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasExtrmitCenter, RDFS.subPropertyOf, bot.Element))

        # ifc element radius of curvature
        onto.add((myOnto.hasRadiusofCurvature, RDF.type, RDF.Property))
        onto.add((myOnto.hasRadiusofCurvature, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasRadiusofCurvature, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasRadiusofCurvature, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasRadiusofCurvature, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasRadiusofCurvature, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))


        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))

        # ifc element GrossCeilingArea
        onto.add((myOnto.hasGrossCeilingArea, RDF.type, RDF.Property))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.isDefinedBy,
                  Literal("The position of something when level with the height of a person's head.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.label, Literal("Measurements of the head height in Meters.", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.comment, Literal("", lang="en")))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.range, XSD.decimal))
        onto.add((myOnto.hasGrossCeilingArea, RDFS.subPropertyOf, bot.Element))




        return onto.serialize( r"C:\Users\ARUN\OneDrive\Desktop\ontologyfolder\tet.ttl" , format='ttl')
