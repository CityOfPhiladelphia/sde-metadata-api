# SDE Metadata API
Provides a REST API for accessing metadata from ArcSDE

## Installation
1. Clone this repository
2. Optionally, create a virtual environment using `virtualenv --system-site-packages venv` and activate it via `venv/Scripts/activate`
3. Install dependencies via `pip install -I -r requirements.txt`
4. Copy `.env.sample` to `.env` and fill in environment variables

## Usage
Run the server via `python app.py`

### /feature-classes
Gets a list of feature class names
```json
{
  "feature_classes": [
    "FPC_Tree_Inventory_1996",
    "Planning_Parcel",
    "FPC_Fairmount_Park",
    "FPC_Buildings_All",
    "FPC_Recreation_Facilities",
	//...
}
```
### /feature-classes/{item}
Get basic info about feature class: name, file, shape type, fields
```json
{
  "fields": [
    {
      "aliasName": "OBJECTID",
      "length": 4,
      "name": "OBJECTID",
      "type": "OID"
    },
    {
      "aliasName": "SHAPE",
      "length": 0,
      "name": "SHAPE",
      "type": "Geometry"
    },
    {
      "aliasName": "NAME",
      "length": 255,
      "name": "NAME",
      "type": "String"
    },
    {
      "aliasName": "ADDRESS",
      "length": 255,
      "name": "ADDRESS",
      "type": "String"
    },
    {
      "aliasName": "ZIP",
      "length": 8,
      "name": "ZIP",
      "type": "Double"
    }
  ],
  "file": "Healthy_Chi_Takeout_rev",
  "name": "Healthy_Chi_Takeout_rev",
  "shapeType": "Point"
}
```
### /feature-classes/{item}/metadata
Get feature class metadata as XML. Uses METADATA_TRANSLATOR environment
variable for metadata schema.
```xml
<?xml version="1.0" encoding="utf-8"?>
<MD_Metadata xmlns="http://www.isotc211.org/2005/gmd" xmlns:gml="http://www.opengis.net/gml" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:gco="http://www.isotc211.org/2005/gco" xmlns:gts="http://www.isotc211.org/2005/gts" xmlns:srv="http://www.isotc211.org/2005/srv" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <language>
        <LanguageCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#LanguageCode" codeListValue="eng" codeSpace="ISO639-2">eng</LanguageCode>
    </language>
    <hierarchyLevel>
        <MD_ScopeCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_ScopeCode" codeListValue="dataset" codeSpace="ISOTC211/19115">dataset</MD_ScopeCode>
    </hierarchyLevel>
    <hierarchyLevelName>
        <gco:CharacterString>dataset</gco:CharacterString>
    </hierarchyLevelName>
    <dateStamp>
        <gco:Date>2015-11-27</gco:Date>
    </dateStamp>
    <metadataStandardName>
        <gco:CharacterString>ISO 19139 Geographic Information - Metadata - Implementation Specification</gco:CharacterString>
    </metadataStandardName>
    <metadataStandardVersion>
        <gco:CharacterString>2007</gco:CharacterString>
    </metadataStandardVersion>
    <spatialRepresentationInfo>
        <MD_VectorSpatialRepresentation>
            <topologyLevel>
                <MD_TopologyLevelCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_TopologyLevelCode" codeListValue="geometryOnly" codeSpace="ISOTC211/19115">geometryOnly</MD_TopologyLevelCode>
            </topologyLevel>
            <geometricObjects>
                <MD_GeometricObjects>
                    <geometricObjectType>
                        <MD_GeometricObjectTypeCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_GeometricObjectTypeCode" codeListValue="point" codeSpace="ISOTC211/19115">point</MD_GeometricObjectTypeCode>
                    </geometricObjectType>
                    <geometricObjectCount>
                        <gco:Integer>181</gco:Integer>
                    </geometricObjectCount>
                </MD_GeometricObjects>
            </geometricObjects>
        </MD_VectorSpatialRepresentation>
    </spatialRepresentationInfo>
    <referenceSystemInfo>
        <MD_ReferenceSystem>
            <referenceSystemIdentifier>
                <RS_Identifier>
                    <code>
                        <gco:CharacterString>2272</gco:CharacterString>
                    </code>
                    <codeSpace>
                        <gco:CharacterString>EPSG</gco:CharacterString>
                    </codeSpace>
                    <version>
                        <gco:CharacterString>8.6.2</gco:CharacterString>
                    </version>
                </RS_Identifier>
            </referenceSystemIdentifier>
        </MD_ReferenceSystem>
    </referenceSystemInfo>
    <identificationInfo>
        <MD_DataIdentification>
            <citation>
                <CI_Citation>
                    <title>
                        <gco:CharacterString>Healthy Chinese Takeout</gco:CharacterString>
                    </title>
                    <date gco:nilReason="missing" />
                    <presentationForm>
                        <CI_PresentationFormCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_PresentationFormCode" codeListValue="mapDigital" codeSpace="ISOTC211/19115">mapDigital</CI_PresentationFormCode>
                    </presentationForm>
                </CI_Citation>
            </citation>
            <abstract>
                <gco:CharacterString>Data Development: Data provided by Temple's Center for Asian Health (based on their compliance check data and Chinese Restaurant Association updates) and then geocoded.Coordinate System: NAD_1983_StatePlane_Pennsylvania_South_FIPS_3702_Feet</gco:CharacterString>
            </abstract>
            <purpose>
                <gco:CharacterString>Healthy Chinese Takeout participants as of July 2015. The Philadelphia Healthy Chinese Take-out Initiative is working to prevent and control high blood pressure in Philadelphia residents by 1) reducing the sodium content in Chinese take-out dishes by 10-15% and 2) decreasing access to tobacco products. The initiative is a joint effort among Temple University’s Center for Asian Health, the Asian Community Health Coalition, the Philadelphia Chinese Restaurant Association, and the Philadelphia Department of Public Health. Excess consumption of sodium (salt) and tobacco use are two major contributors to hypertension, heart disease and stroke. Chinese take-out restaurant dishes can have large amounts of sodium mainly due to the sauces used in preparation and cooking. And Chinese take-out restaurants tend to have higher rates of illegal tobacco sales to minors than other retailers. To date, 200 Chinese take-out restaurants have enrolled in the initiative, participated in a low-sodium healthy cooking training with a professional chef, and received education about complying with the Tobacco Youth Sales Law. Features updated: 7/29/15 Attributes updated: 7/29/15 Metadata updated: 7/29/15 Update frequency: as needed Public = Y</gco:CharacterString>
            </purpose>
            <credit>
                <gco:CharacterString>Amory Hillengas, MUSA Geospatial Analyst Get Healthy Philly</gco:CharacterString>
            </credit>
            <descriptiveKeywords>
                <MD_Keywords>
                    <keyword>
                        <gco:CharacterString>Chinese Takeout</gco:CharacterString>
                    </keyword>
                    <keyword>
                        <gco:CharacterString>Get Healthy Philly</gco:CharacterString>
                    </keyword>
                    <keyword>
                        <gco:CharacterString>City of Philadelphia</gco:CharacterString>
                    </keyword>
                    <keyword>
                        <gco:CharacterString>PDPH</gco:CharacterString>
                    </keyword>
                </MD_Keywords>
            </descriptiveKeywords>
            <resourceConstraints>
                <MD_Constraints>
                    <useLimitation>
                        <gco:CharacterString>The City of Philadelphia reserves all rights in the GIS database and any data contained therein, and the end user’s use of the data does not constitute a transfer of, nor does the end user receive, any title or interest in the database or any other City data. The City of Philadelphia makes no representation about the accuracy of any specific information in this GIS data and is provided “as is” and without Warranty of any kind. The user of this data will assume complete responsibility for any and all occurrences resulting from its use or display and will hold the City of Philadelphia harmless from any and all claims, demands, liabilities, obligations, damages, suits, judgments or settlements, including reasonable costs and attorneys' fees that arise from use of this data.</gco:CharacterString>
                    </useLimitation>
                </MD_Constraints>
            </resourceConstraints>
            <spatialRepresentationType>
                <MD_SpatialRepresentationTypeCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_SpatialRepresentationTypeCode" codeListValue="vector" codeSpace="ISOTC211/19115">vector</MD_SpatialRepresentationTypeCode>
            </spatialRepresentationType>
            <language>
                <LanguageCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#LanguageCode" codeListValue="eng" codeSpace="ISO639-2">eng</LanguageCode>
            </language>
            <environmentDescription>
                <gco:CharacterString>Version 6.2 (Build 9200) ; Esri ArcGIS 10.3.1.4959</gco:CharacterString>
            </environmentDescription>
            <extent>
                <EX_Extent>
                    <geographicElement>
                        <EX_GeographicBoundingBox>
                            <extentTypeCode>
                                <gco:Boolean>true</gco:Boolean>
                            </extentTypeCode>
                            <westBoundLongitude>
                                <gco:Decimal>-75.25432</gco:Decimal>
                            </westBoundLongitude>
                            <eastBoundLongitude>
                                <gco:Decimal>-75.067795</gco:Decimal>
                            </eastBoundLongitude>
                            <southBoundLatitude>
                                <gco:Decimal>39.917531</gco:Decimal>
                            </southBoundLatitude>
                            <northBoundLatitude>
                                <gco:Decimal>40.08172</gco:Decimal>
                            </northBoundLatitude>
                        </EX_GeographicBoundingBox>
                    </geographicElement>
                </EX_Extent>
            </extent>
        </MD_DataIdentification>
    </identificationInfo>
    <distributionInfo>
        <MD_Distribution>
            <distributionFormat>
                <MD_Format>
                    <name>
                        <gco:CharacterString>File Geodatabase Feature Class</gco:CharacterString>
                    </name>
                    <version>
                        <gco:CharacterString>unknown</gco:CharacterString>
                    </version>
                </MD_Format>
            </distributionFormat>
        </MD_Distribution>
    </distributionInfo>
</MD_Metadata>
```