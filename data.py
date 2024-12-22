from datetime import date
movies = [
    {
        'id': 1,
        'title': 'The Dark Knight',
        'image': 'images/movies/bat-man.jpg',
        'trailer_url': 'https://www.youtube.com/embed/EXeTwQWrcwY',  # Changed from watch?v= to embed/
        'synopsis': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
        'director': 'Christopher Nolan',
        'cast': ['Christian Bale', 'Heath Ledger', 'Aaron Eckhart'],
        'runtime': '2h 32min',
        'genres': ['Action', 'Crime', 'Drama'],
        'rating': 9.0,
        'reviews': [
            {
                'title': 'A Masterpiece of Superhero Cinema',
                'body': 'The Dark Knight is a dark, complex, and thrilling masterpiece that redefined superhero movies.',
                'rating': 10,
                'author': 'John Doe',
                'date': '2024-12-20',
                'helpful_count': 150,
                'not_helpful_count': 5
            },
            {
                'title': 'Heath Ledger\'s Joker is Iconic',
                'body': 'Heath Ledger\'s performance as the Joker is legendary, and the film is a must-watch for any fan of superhero movies.',
                'rating': 9,
                'author': 'Jane Smith',
                'date': '2024-12-18',
                'helpful_count': 120,
                'not_helpful_count': 3
            }
        ]
    },
    {
        'id': 2,
        'title': 'Bloodshot',
        'image': 'images/movies/blood-shot.jpg',
        'trailer_url': 'https://www.youtube.com/embed/vOUVVDWdXbo',  # Changed from watch?v= to embed/
        'synopsis': 'Ray Garrison, a slain soldier, is re-animated with superpowers.',
        'director': 'Dave Wilson',
        'cast': ['Vin Diesel', 'Eiza González', 'Sam Heughan'],
        'runtime': '109 min',
        'genres': ['Action', 'Sci-Fi', 'Thriller'],
        'rating': 6.7,
        'reviews': [
            {
                'title': 'Action-Packed Sci-Fi Thriller',
                'body': 'Bloodshot is a decent action sci-fi thriller with some impressive visual effects and a compelling performance by Vin Diesel.',
                'rating': 7,
                'author': 'Alice Johnson',
                'date': '2024-12-15',
                'helpful_count': 90,
                'not_helpful_count': 10
            },
            {
                'title': 'A Fun, Mindless Action Flick',
                'body': 'If you\'re looking for a fun, mindless action movie with cool superpowers, Bloodshot is worth checking out.',
                'rating': 6,
                'author': 'Bob Williams',
                'date': '2024-12-12',
                'helpful_count': 70,
                'not_helpful_count': 8
            }
        ]
    },
    {
        'id': 3,
        'title': 'Call',
        'image': 'images/movies/call.jpg',
        'trailer_url': 'https://www.youtube.com/embed/39gmdzMmf7Q',  # Changed from watch?v= to embed/
        'synopsis': 'Two young women from different times become connected through a phone call, but their actions have dangerous consequences.',
        'director': 'Lee Chung-hyun',
        'cast': ['Park Shin-hye', 'Jeon Jong-seo', 'Kim Sung-ryung'],
        'runtime': '112 min',
        'genres': ['Mystery', 'Thriller'],
        'rating': 7.1,
        'reviews': [
            {
                'title': 'A Gripping and Twisty Thriller',
                'body': 'Call is a suspenseful and well-crafted thriller with strong performances and a unique premise.',
                'rating': 8,
                'author': 'Emily Davis',
                'date': '2024-12-10',
                'helpful_count': 100,
                'not_helpful_count': 5
            },
            {
                'title': 'Intense and Unpredictable',
                'body': 'The movie keeps you on the edge of your seat with its twists and turns. Highly recommended!',
                'rating': 9,
                'author': 'Michael Brown',
                'date': '2024-12-08',
                'helpful_count': 85,
                'not_helpful_count': 2
            }
        ]
    },
    {
        'id': 4,
        'title': 'Captain Marvel',
        'image': 'images/movies/captain-marvel.png',
        'trailer_url': 'https://www.youtube.com/embed/Z1BCujX3pw8',  # Changed from watch?v= to embed/
        'synopsis': 'Carol Danvers becomes one of the universe\'s most powerful heroes when Earth is caught in the middle of a galactic war between two alien races.',
        'director': 'Anna Boden and Ryan Fleck',
        'cast': ['Brie Larson', 'Samuel L. Jackson', 'Ben Mendelsohn'],
        'runtime': '123 min',
        'genres': ['Action', 'Adventure', 'Sci-Fi'],
        'rating': 6.8,
        'reviews': [
            {
                'title': 'A Solid Entry in the MCU',
                'body': 'Captain Marvel is a fun and action-packed addition to the Marvel Cinematic Universe with a great performance by Brie Larson.',
                'rating': 7,
                'author': 'Sarah Wilson',
                'date': '2024-12-05',
                'helpful_count': 110,
                'not_helpful_count': 15
            },
            {
                'title': 'Empowering and Entertaining',
                'body': 'Captain Marvel is a great superhero movie with a strong female lead and a positive message.',
                'rating': 8,
                'author': 'David Garcia',
                'date': '2024-12-03',
                'helpful_count': 95,
                'not_helpful_count': 8
            }
        ]
    },
    {
        'id': 5,
        'title': 'Avengers: Endgame',
        'image': 'images/movies/end-game.jpg',
        'trailer_url': 'https://www.youtube.com/embed/TcMBFSGVi1c',  # Changed from watch?v= to embed/
        'synopsis': 'After the devastating events of Avengers: Infinity War, the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to undo Thanos\' actions and restore order to the universe.',
        'director': 'Anthony Russo and Joe Russo',
        'cast': ['Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo'],
        'runtime': '181 min',
        'genres': ['Action', 'Adventure', 'Drama'],
        'rating': 8.4,
        'reviews': [
            {
                'title': 'An Epic Conclusion to the Infinity Saga',
                'body': 'Avengers: Endgame is a satisfying and emotional conclusion to the Infinity Saga, with plenty of action, humor, and heart.',
                'rating': 9,
                'author': 'Kevin Rodriguez',
                'date': '2024-12-01',
                'helpful_count': 200,
                'not_helpful_count': 10
            },
            {
                'title': 'A Must-See for Marvel Fans',
                'body': 'Endgame is a cinematic triumph that delivers on its promises and provides a fitting end to an era of superhero movies.',
                'rating': 10,
                'author': 'Jessica Martinez',
                'date': '2024-11-29',
                'helpful_count': 180,
                'not_helpful_count': 7
            }
        ]
    },
    {
        'id': 6,
        'title': 'Hunter Killer',
        'image': 'images/movies/hunter-killer.jpg',
        'trailer_url': 'https://www.youtube.com/embed/j9Cx2Kwq95s',  # Changed from watch?v= to embed/
        'synopsis': 'An untested American submarine captain teams with U.S. Navy SEALs to rescue the Russian president, who has been kidnapped by a rogue general.',
        'director': 'Donovan Marsh',
        'cast': ['Gerard Butler', 'Gary Oldman', 'Common'],
        'runtime': '122 min',
        'genres': ['Action', 'Thriller'],
        'rating': 6.6,
        'reviews': [
            {
                'title': 'Intense Submarine Action',
                'body': 'Hunter Killer delivers solid submarine action and suspense, even if the plot is a bit predictable.',
                'rating': 7,
                'author': 'Chris Anderson',
                'date': '2024-11-25',
                'helpful_count': 70,
                'not_helpful_count': 12
            },
            {
                'title': 'Gerard Butler Does It Again',
                'body': 'Another good action movie from Gerard Butler. The underwater sequences are particularly well-done.',
                'rating': 6,
                'author': 'Laura Thomas',
                'date': '2024-11-22',
                'helpful_count': 60,
                'not_helpful_count': 9
            }
        ]
    },
    {
        'id': 7,
        'title': 'Insidious',
        'image': 'images/movies/insidious.jpg',
        'trailer_url': 'https://www.youtube.com/embed/zuZnRUcoWos',  # Changed from watch?v= to embed/
        'synopsis': 'A family looks to prevent evil spirits from trapping their comatose son in a realm called The Further.',
        'director': 'James Wan',
        'cast': ['Patrick Wilson', 'Rose Byrne', 'Ty Simpkins'],
        'runtime': '103 min',
        'genres': ['Horror', 'Mystery', 'Thriller'],
        'rating': 6.8,
        'reviews': [
            {
                'title': 'Effectively Creepy Horror',
                'body': 'Insidious is a genuinely scary movie with a chilling atmosphere and some effective jump scares.',
                'rating': 8,
                'author': 'Daniel Jackson',
                'date': '2024-11-18',
                'helpful_count': 80,
                'not_helpful_count': 5
            },
            {
                'title': 'A Modern Horror Classic',
                'body': 'James Wan delivers another horror gem with Insidious. It\'s a must-see for fans of the genre.',
                'rating': 9,
                'author': 'Lisa White',
                'date': '2024-11-15',
                'helpful_count': 95,
                'not_helpful_count': 3
            }
        ]
    },
    {
        'id': 8,
        'title': 'Love, Rosie',
        'image': 'images/movies/love-roise.jpg',
        'trailer_url': 'https://www.youtube.com/embed/5zL3YJKygd4',  # Changed from watch?v= to embed/
        'synopsis': 'Rosie and Alex have been best friends since they were 5, so they couldn\'t possibly be right for one another...or could they? When it comes to love, life and making the right choices, these two are their own worst enemies.',
        'director': 'Christian Ditter',
        'cast': ['Lily Collins', 'Sam Claflin', 'Christian Cooke'],
        'runtime': '102 min',
        'genres': ['Comedy', 'Drama', 'Romance'],
        'rating': 7.2,
        'reviews': [
            {
                'title': 'Charming and Heartwarming',
                'body': 'Love, Rosie is a sweet and charming romantic comedy with great chemistry between the leads.',
                'rating': 8,
                'author': 'Sophia Harris',
                'date': '2024-11-10',
                'helpful_count': 120,
                'not_helpful_count': 7
            },
            {
                'title': 'A Feel-Good Movie',
                'body': 'If you\'re looking for a feel-good movie about love and friendship, Love, Rosie is a great choice.',
                'rating': 7,
                'author': 'Anthony Martin',
                'date': '2024-11-08',
                'helpful_count': 90,
                'not_helpful_count': 5
            }
        ]
    },
    {
        'id': 9,
        'title': 'Resident Evil',
        'image': 'images/movies/resident-evil.jpg',
        'trailer_url': 'https://www.youtube.com/embed/u6uDnd_vJCo',  # Changed from watch?v= to embed/
        'synopsis': 'A special military unit fights a powerful, out-of-control supercomputer and hundreds of scientists who have mutated into flesh-eating creatures after a laboratory accident.',
        'director': 'Paul W.S. Anderson',
        'cast': ['Milla Jovovich', 'Michelle Rodriguez', 'Eric Mabius'],
        'runtime': '100 min',
        'genres': ['Action', 'Horror', 'Sci-Fi'],
        'rating': 6.7,
        'reviews': [
            {
                'title': 'A Guilty Pleasure Action Horror',
                'body': 'Resident Evil is a fun, action-packed horror movie with some decent scares and cool visuals.',
                'rating': 6,
                'author': 'Matthew Lewis',
                'date': '2024-11-05',
                'helpful_count': 75,
                'not_helpful_count': 15
            },
            {
                'title': 'Entertaining Despite Its Flaws',
                'body': 'It\'s not a perfect movie, but Resident Evil is still an entertaining watch for fans of action horror.',
                'rating': 7,
                'author': 'Ashley Robinson',
                'date': '2024-11-03',
                'helpful_count': 80,
                'not_helpful_count': 10
            }
        ]
    },
    {
        'id': 10,
        'title': 'Transformers',
        'image': 'images/movies/transformer.jpg',
        'trailer_url': 'https://www.youtube.com/embed/dxQWpvohuJg',  # Changed from watch?v= to embed/
        'synopsis': 'An ancient struggle between two Cybertronian races, the heroic Autobots and the evil Decepticons, comes to Earth, with a clue to the ultimate power held by a teenager.',
        'director': 'Michael Bay',
        'cast': ['Shia LaBeouf', 'Megan Fox', 'Josh Duhamel'],
        'runtime': '144 min',
        'genres': ['Action', 'Adventure', 'Sci-Fi'],
        'rating': 7.0,
        'reviews': [
            {
                'title': 'Visually Stunning Action',
                'body': 'Transformers is a visual spectacle with impressive special effects and exciting action sequences.',
                'rating': 8,
                'author': 'Brian Clark',
                'date': '2024-10-30',
                'helpful_count': 130,
                'not_helpful_count': 20
            },
            {
                'title': 'A Fun Popcorn Flick',
                'body': 'While not a masterpiece, Transformers is a fun and entertaining popcorn flick for fans of action and sci-fi.',
                'rating': 7,
                'author': 'Angela Walker',
                'date': '2024-10-28',
                'helpful_count': 100,
                'not_helpful_count': 15
            }
        ]
    }
]

def get_movie_by_id(movie_id):
    # Convert movie_id to int since we're comparing with integer IDs
    movie_id = int(movie_id)
    for movie in movies:  # movies is already defined at module level
        if movie['id'] == movie_id:
            return movie
    return None

def add_review(movie_id, review):
    """Add a review to a specific movie."""
    if movie_id in movies:
        review["helpful_count"] = 0
        review["not_helpful_count"] = 0
        review["date"] = date.today()
        movies[movie_id]["reviews"].append(review)
        return True
    return False
