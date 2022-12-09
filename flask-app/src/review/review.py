from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

# Wireframe #1 for Customer
review_cust = Blueprint('review', __name__)

# Post a review for a product
@review_cust.route('/review')
def get_form():
    return """
    <h2>HTML Forms</h2>

    <form action="/ramen_oneclick/customer/review" method="POST">
    <label for="custID">Customer ID:</label><br>
    <input type="text" id="custID" name="custID"><br>
    <label for="targetID">Product ID:</label><br>
    <input type="text" id="targetID" name="targetID"><br>
    <label for="rating">Rating ID:</label><br>
    <input type="text" id="rating" name="rating"><br>
    <br>
    <input type="submit" value="Post">
    </form> 
    """

@review_cust.route('/review', methods=['POST'])
def post_form():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    custID = request.form['custID']
    targetID = request.form['targetID']
    rating = request.form['rating']
    query = f'INSERT INTO cust_review_ramen(custID, targetID, rating) VALUES (\"{custID}\", \"{targetID}\", \"{rating}\")'
    cursor.execute(query)
    db.get_db().commit()
    return f'<h1>Successfully posted a review!</h1><h2>Target = {targetID}</h2>'