![](http://www.underconsideration.com/brandnew/archives/udacity_logo.png)
# Movie Trailer Website
Movie trailer website is an Object oriented python project that stores list of favorite movies, including box art imagery and a movie trailer URL which gets displayed on a website.

The information of the movie stored are:
  - Movie Title
  - Movie Storyline
  - Movie Poster
  - Movie Trailer URL

# Project files
A constructor for the movie class is written to create instances of movie in `media.py`. Created a list of  movie objects in `entertainment_center.py` by calling the constructor **media.Movie()** to instantiate movie objects. These objects can be stored in a list data structure. This list of movies is what the **open_movies_page()** function needs as input in order to build the HTML file, in order to display movie trailer website.

`entertainment_center.py`: 
- Python Class to store favorite movies, including movie title, poster URL and a YouTube link to the movie trailer.
- Creates multiple instances of that Python Class to represent favorite movies; grouping all the instances together in a list.
```
# storing movie details: movie title, storyline, poster URL and movie trailer URL
avatar = media.Movie("Avatar","A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", # NOQA
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
```

```
# grouping all instances together in a list
movies = [avatar, bahubali, sing, idiots, notebook, despicable]
```
```
# calling function open_movies_page to open in a web browser
fav_movies.open_movies_page(movies)
```

`fav_movies.py`:
- It helps in generating a website that displays all favorite movies. 
- The fav_movies.py module has a function called open_movies_page() that takes in one argument, which is a list of movies, and creates an HTML file which will display all favorite movies.
```
 <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Favorite Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
```
```
# function defined in fav_movies.py
def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fav_movies.html', 'w')
```

```
 # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
```

`media.py`:
- Movie class is created in this file to encapsulate the properties of a movie in a movie object.
```
class Movie():
# function that stores all the information related to movie
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
```
### How to run the project?

- Download the Movie Trailer project 
- Install [python](https://www.python.org/) to run the project.
- Open python GUI (IDLE) > File > Open... > Select `entertainment_center.py` from the downloaded Movie Trailer project.
- Click Run > **Run Module**

Resources:
----
Udacity instructor notes.

License
----

Rudra Narayan Banjara, Udacian
