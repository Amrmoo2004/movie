from flask import Flask, render_template
from data import get_movie_by_id, movies
from api_routes import api
from flask import Flask, render_template, request, redirect, url_for
from data import get_watchlist

# Create app instance first
app = Flask(__name__, template_folder='templates')

# Then register blueprint
app.register_blueprint(api)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('login.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # ... your signup logic ...
    return render_template('signup.html')
    
@app.route('/watchlist', methods=['GET'])
def watchlist_page():
    return render_template('watchlist.html', watchlist=get_watchlist())

@app.route('/')
def home():
    movies = [
        {'id': 1, 'title': 'Bat-man', 'image': 'images/movies/bat-man.jpg', 'rating': 4.5, 'genre': 'Action'},
        {'id': 2, 'title': 'Blood-shot', 'image': 'images/movies/blood-shot.jpg', 'rating': 4.2, 'genre': 'Sci-fi'},
        {'id': 3, 'title': 'Call', 'image': 'images/movies/call.jpg', 'rating': 4.0, 'genre': 'Thriller'},
        {'id': 4, 'title': 'Captain Marvel', 'image': 'images/movies/captain-marvel.png', 'rating': 4.7, 'genre': 'Action'},
        {'id': 5, 'title': 'End Game', 'image': 'images/movies/end-game.jpg', 'rating': 4.8, 'genre': 'Action'},
        {'id': 6, 'title': 'Hunter Killer', 'image': 'images/movies/hunter-killer.jpg', 'rating': 4.3, 'genre': 'Action'},
        {'id': 7, 'title': 'Insidious', 'image': 'images/movies/insidious.jpg', 'rating': 4.1, 'genre': 'Horror'},
        {'id': 8, 'title': 'Love-roise', 'image': 'images/movies/love-roise.jpg', 'rating': 4.6, 'genre': 'Romance'},
        {'id': 9, 'title': 'Resident Evil', 'image': 'images/movies/resident-evil.jpg', 'rating': 4.4, 'genre': 'Horror'},
        {'id': 10, 'title': 'Transformer', 'image': 'images/movies/transformer.jpg', 'rating': 4.7, 'genre': 'Sci-fi'}
    ]
    return render_template('home.html', movies=movies)

@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    movie = get_movie_by_id(movie_id)  # Remove the second argument
    if not movie:
        return "Movie not found", 404
    return render_template('movie_details.html', movie=movie)


@app.route('/genre')
def genre():
    # Group movies by genre using the first genre in the genres list
    action_movies = [m for m in movies if 'Action' in m['genres']]
    scifi_movies = [m for m in movies if 'Sci-Fi' in m['genres']]
    horror_movies = [m for m in movies if 'Horror' in m['genres']]
    thriller_movies = [m for m in movies if 'Thriller' in m['genres']]
    romance_movies = [m for m in movies if 'Romance' in m['genres']]
    
    return render_template('genre.html', 
                         action_movies=action_movies,
                         scifi_movies=scifi_movies,
                         horror_movies=horror_movies,
                         thriller_movies=thriller_movies,
                         romance_movies=romance_movies)

@app.route('/movies')
def movies_page():
    movies = [
        {'id': 1, 'title': 'Bat-man', 'image': 'images/movies/bat-man.jpg', 'rating': 4.5, 'genre': 'Action'},
        {'id': 2, 'title': 'Blood-shot', 'image': 'images/movies/blood-shot.jpg', 'rating': 4.2, 'genre': 'Sci-fi'},
        {'id': 3, 'title': 'Call', 'image': 'images/movies/call.jpg', 'rating': 4.0, 'genre': 'Thriller'},
        {'id': 4, 'title': 'Captain Marvel', 'image': 'images/movies/captain-marvel.png', 'rating': 4.7, 'genre': 'Action'},
        {'id': 5, 'title': 'End Game', 'image': 'images/movies/end-game.jpg', 'rating': 4.8, 'genre': 'Action'},
        {'id': 6, 'title': 'Hunter Killer', 'image': 'images/movies/hunter-killer.jpg', 'rating': 4.3, 'genre': 'Action'},
        {'id': 7, 'title': 'Insidious', 'image': 'images/movies/insidious.jpg', 'rating': 4.1, 'genre': 'Horror'},
        {'id': 8, 'title': 'Love-roise', 'image': 'images/movies/love-roise.jpg', 'rating': 4.6, 'genre': 'Romance'},
        {'id': 9, 'title': 'Resident Evil', 'image': 'images/movies/resident-evil.jpg', 'rating': 4.4, 'genre': 'Horror'},
        {'id': 10, 'title': 'Transformer', 'image': 'images/movies/transformer.jpg', 'rating': 4.7, 'genre': 'Sci-fi'}
    ]
    return render_template('movies.html', movies=movies)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
