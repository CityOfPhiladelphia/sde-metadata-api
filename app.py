import os

import arcpy
from flask import Flask, jsonify, Response
from dotenv import load_dotenv

# Load and set environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
METADATA_TRANSLATOR = os.environ.get('METADATA_TRANSLATOR')
arcpy.env.workspace = os.environ.get('WORKSPACE')

app = Flask(__name__)

def dict_from_obj(obj, keys):
	""" Helper to construct dict from object """
	dict_ = {}
	for key in keys:
		dict_[key] = getattr(obj, key)
	return dict_

@app.route('/feature-classes')
def get_feature_classes():
	"""
	Get list of feature class names
	"""
	return jsonify(feature_classes=arcpy.ListFeatureClasses())

@app.route('/feature-classes/<item>')
def describe(item):
	"""
	Get basic info about feature class: name, file, shape type, fields
	"""
	desc = arcpy.Describe(item)
	desc_dict = dict_from_obj(desc, ['name', 'file', 'shapeType'])
	desc_dict['fields'] = []
	for field in desc.fields:
		desc_dict['fields'].append(dict_from_obj(field, ['name', 'length', 'aliasName', 'type']))
	return jsonify(desc_dict)
	
@app.route('/feature-classes/<item>/metadata')
def metadata(item):
	"""
	Get feature class metadata as XML. Uses METADATA_TRANSLATOR environment
	variable for metadata schema
	"""
	output_file = './tmp/' + item + '.xml'
	try:  # Make sure file doesn't exist already (can't overwrite)
		os.remove(output_file)
	except OSError:
		pass
		
	arcpy.ExportMetadata_conversion(item, METADATA_TRANSLATOR, output_file)
	with open(output_file) as f:
		file_contents = f.read()
	return Response(file_contents, mimetype='text/xml')

if __name__ == '__main__':
	app.run(debug=False)
