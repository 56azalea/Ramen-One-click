from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

# Wireframe #1 for Customer Service
one_pick_serivce = Blueprint('one_pick', __name__)

# Get all public posts from the DB
@one_pick_serivce.route('/one_pick', methods=['GET'])
def get_post():
    cursor = db.get_db().cursor()
    cursor.execute('select postTitle from post_table')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get a post's detail for that with a particular postID
@one_pick_serivce.route('/one_pick/<postID>', methods=['GET'])
def get_published_post(postID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from post_table where postID = {0}'.format(postID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Make a new post
@one_pick_serivce.route('/one_pick/new')
def get_form():
    return """
    <h2>HTML Forms</h2>

    <form action="/ramen_oneclick/service/one_pick/new" method="POST">
    <label for="postID">Post ID:</label><br>
    <input type="text" id="postID" name="postID"><br>
    <label for="authorID">Author ID:</label><br>
    <input type="text" id="authorID" name="authorID"><br>
    <label for="postTitle">Post Title:</label><br>
    <input type="text" id="postTitle" name="postTitle"><br>
    <br>
    <input type="submit" value="Post">
    </form> 
    """

@one_pick_serivce.route('/one_pick/new', methods=['POST'])
def post_form():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    postID = request.form['postID']
    authorID = request.form['authorID']
    postTitle = request.form['postTitle']
    query = f'INSERT INTO post_table(postID, authorID, postTitle) VALUES (\"{postID}\", \"{authorID}\", \"{postTitle}\")'
    cursor.execute(query)
    db.get_db().commit()
    return f'<h1>Successfully made a new post!</h1><h2>PostTitle = {postTitle}</h2>'