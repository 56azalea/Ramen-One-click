from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

# Wireframe #1 for Admin
register_prod_admin = Blueprint('register_prod', __name__)

# Get all registered products from the DB
@register_prod_admin.route('/register_prod', methods=['GET'])
def get_prod():
    cursor = db.get_db().cursor()
    cursor.execute('select productName, price from ramen_product_table')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get a product's detail for that with a particular productID
@register_prod_admin.route('/register_prod/<productID>', methods=['GET'])
def get_regist_prod(productID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from ramen_product_table where productID = {0}'.format(productID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Post a new ramen
@register_prod_admin.route('/register_prod/new')
def get_form():
    return """
    <h2>HTML Forms</h2>

    <form action="/ramen_oneclick/register_prod_admin/new" method="POST">
    <label for="productID">Product ID:</label><br>
    <input type="text" id="productID" name="productID"><br>
    <label for="packStyle">Pack Style:</label><br>
    <input type="text" id="packStyle" name="packStyle"><br>
    <label for="productName">Product Name:</label><br>
    <input type="text" id="productName" name="productName"><br>
    <label for="price">Price:</label><br>
    <input type="text" id="price" name="price"><br>
    <label for="company">Company:</label><br>
    <input type="text" id="company" name="company"><br>
    <label for="uploadedBy">Uploaded By:</label><br>
    <input type="text" id="uploadedBy" name="uploadedBy"><br>
    <br>
    <input type="submit" value="Register">
    </form> 
    """

@register_prod_admin.route('/register_prod/new', methods=['POST'])
def post_form():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    productID = request.form['productID']
    packStyle = request.form['packStyle']
    productName = request.form['productName']
    price = request.form['price']
    company = request.form['company']
    uploadedBy = request.form['uploadedBy']
    query = f'INSERT INTO ramen_product_table(productID, packStyle, productName, price, avgRating, company, uploadedBy) VALUES (\"{productID}\", \"{packStyle}\", \"{productName}\", \"{price}\", 0, \"{company}\", \"{uploadedBy}\")'
    cursor.execute(query)
    db.get_db().commit()
    return f'<h1>New product added successfully!</h1><h2>ProductID = {productID}, PackStyle = {packStyle}, ProductName = {productName}, price = {price}, company = {company}, uploadedBy = {uploadedBy}</h2>'

# Get companies info for AppSmith dropdown
@register_prod_admin.route('/register_prod/companies')
def get_companies():
    cursor = db.get_db().cursor()
    query = 'select companyID as value, companyName as label from ramen_company_table'
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response