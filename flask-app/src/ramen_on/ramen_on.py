from flask import Blueprint, request, jsonify, make_response
import json
from src import db

# Wireframe #2 for Customer
ramen_on_cust = Blueprint('ramen_on', __name__)

# Get all mukbang shows from the DB
@ramen_on_cust.route('/ramen_on', methods=['GET'])
def get_show():
    cursor = db.get_db().cursor()
    cursor.execute('select showTitle from show_table')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get a show's detail for that with a particular showID
@ramen_on_cust.route('/ramen_on/<showID>', methods=['GET'])
def get_mukbang_show(showID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from show_table where showID = {0}'.format(showID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response