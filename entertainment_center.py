import fav_movies
import media

#storing movie details: movie title, storyline, poster URL and movie trailer URL
avatar = media.Movie("Avatar","A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

bahubali = media.Movie("Bahubali","Story of a kingdom and a young legend",
                       "https://s-media-cache-ak0.pinimg.com/originals/67/fd/63/67fd631e9d9dd46eca00db23012c5908.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")

sing = media.Movie("Sing",
                   "The journey of a Koala Buster Moon to produce the world's greatest singing competition.",
                   "http://t2.gstatic.com/images?q=tbn:ANd9GcQeTMzh3aGw46IVUdS6N2tToanuLOc9dO7f6CgWVQlq1laJjuXa",
                   "https://www.youtube.com/watch?v=YDQizlFzVdA")

idiots = media.Movie("3 idiots","Two friends looking for a lost buddy deal with a forgotten bet,"
                     " a wedding they are forced to crash and an out of control funeral.",
                     "http://sites.psu.edu/pragnyaprabakaran/wp-content/uploads/sites/38771/2016/04/3i-poster-3.jpg",
                     "https://www.youtube.com/watch?v=xvszmNXdM4w")

notebook = media.Movie("Notebook",
                       "In 1940s South Carolina, mill worker Noah Calhoun and rich girl Allie are desperately in love.",
                       "http://cdn3.movieroomreviews.com/sites/movieroomreviews.com/files/imagecache/full_size_image/photos/the-notebook-movie-picture-59.jpg",
                       "https://www.youtube.com/watch?v=FC6biTjEyZw")

despicable = media.Movie("Despicable me","A man who delights in all things wicked,"
                         "supervillain Gru (Steve Carell) hatches a plan to steal the moon.",
                         "https://images-na.ssl-images-amazon.com/images/I/51p%2BZw474tL.jpg",
                         "https://www.youtube.com/watch?v=nVwae09eSpo")

#grouping all instances together in a list
movies = [avatar,bahubali,sing,idiots,notebook,despicable]

#calling function open_movies_page to open in a web browser
fav_movies.open_movies_page(movies)

