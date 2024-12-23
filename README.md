# Moviz - A Flask Movie Streaming Web App

This is a simple movie streaming web application built with Flask. It allows users to browse movies, view movie details, and add their own reviews. It also includes a watchlist feature to save movies for later viewing.

## Features

* Browse movies with posters, titles, ratings, and genres.
* View detailed information about each movie, including trailers, synopses, directors, cast, runtime, genres, and ratings.
* Add new reviews to movies.
* User authentication (login and signup).
* Watchlist: Save movies to watch later.
* Responsive design.

## Technologies Used

* Flask
* Jinja2
* HTML, CSS, and JavaScript
* (Optional) Database (e.g., SQLite, PostgreSQL)

## Project Structure

* `app.py`: Main Flask application file
* `templates/`: Contains HTML templates
    * `base.html`: Base template
    * `home.html`: Home page template
    * `movie_details.html`: Movie details template
    * `login.html`: Login page template
    * `signup.html`: Signup page template
    * `genre.html`: Genre page template
    * `movies.html`: Movies page template
    * `about.html`: About page template
    * `watchlist.html`: Watchlist template
* `static/`: Contains static files (CSS, JavaScript, images)
    * `css/`: CSS files
    * `js/`: JavaScript files
    * `images/`: Image files
* `data.py`: (Optional) Contains functions for managing movie data (if not using a database)

## Installation

1. Clone the repository: `git clone https://github.com/your-username/your-repository-name.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux)
4. Install the dependencies: `pip install -r requirements.txt`
5. Set up your data source (if applicable):
    * If using a database, create the database schema and populate it with movie data.
    * If using `data.py`, make sure the `movies` list is populated with your movie data.
6. Run the application: `flask run`

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/` (or the address where your Flask app is running).
2. Browse the movies on the home page.
3. Click on a movie poster to view its details.
4. Use the navigation bar to access other pages (login, signup, genre, movies, about).

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.