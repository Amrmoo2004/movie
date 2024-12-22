from flask import Blueprint, request, jsonify
from data import add_review

api = Blueprint('api', __name__)

@api.route('/api/review', methods=['POST'])
def handle_review():
    data = request.json
    movie_id = data.get('movie_id')
    review = {
        "title": data.get('title'),
        "body": data.get('comment'),
        "rating": data.get('rating'),
        "author": data.get('user')
    }
    if add_review(movie_id, review):
        return jsonify({"success": True, "message": "Review added successfully!", "review": review}), 201
    return jsonify({"success": False, "message": "Movie not found!"}), 404