from flask import Blueprint, request, jsonify
from data import add_review
from data import add_to_watchlist, remove_from_watchlist


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



@api.route('/api/watchlist/<int:movie_id>', methods=['POST'])
def add_to_watchlist_route(movie_id):
    if add_to_watchlist(movie_id):
        return jsonify({"success": True, "message": "Movie added to watchlist!"}), 201
    return jsonify({"success": False, "message": "Movie already in watchlist or not found!"}), 400


@api.route('/api/watchlist/<int:movie_id>', methods=['DELETE'])
def remove_from_watchlist_route(movie_id):
    if remove_from_watchlist(movie_id):
        return jsonify({"success": True, "message": "Movie removed from watchlist!"}), 200
    return jsonify({"success": False, "message": "Movie not found in watchlist!"}), 404
