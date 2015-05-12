import media
import fresh_tomatoes

'''
This file contains data about the movies one the website including movie title, storyline, and links to a movie poster and youtube trailer
'''

the_name_of_the_rose = media.Movie("The Name of the Rose",
                        "A young monk solves a mystery",
                        "http://upload.wikimedia.org/wikipedia/en/c/c4/Name_of_rose_movieposter.jpg",
                        "https://www.youtube.com/watch?v=_4YvAeuAMF4")

the_elephant_man = media.Movie("The Elephant Man",
                        "The life story of Joseph Merrick in the Victorian era",
                        "http://upload.wikimedia.org/wikipedia/en/2/27/TheElephantManposter.jpg",
                        "http://www.youtube.com/watch?v=XLvrU4RjoX0")

the_crying_game = media.Movie("The Crying Game",
                        "A transgender love story",
                        "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2-WNiNt6JfrQqCQe3uVerL--OfHc60nG8xH0g4fPvYYBJL02p",
                        "http://www.youtube.com/watch?v=8vs_4-QQACo")

dracula = media.Movie("Dracula",
                        "A vampire attempts to move from Transylvania to England to spread his curse",
                        "http://upload.wikimedia.org/wikipedia/en/d/df/Dracpos.jpg",
                        "http://www.youtube.com/watch?v=fgFPIh5mvNc")

the_mission = media.Movie("The Mission",
                        "The experience of a Jesuit missionary in 18th century South America",
                        "http://upload.wikimedia.org/wikipedia/en/5/5a/The_mission.jpg",
                        "http://www.youtube.com/watch?v=Y-l2-Q7vODc")

tideland = media.Movie("Tideland",
                        "An abandoned child and her adventures in rural Texas",
                        "http://upload.wikimedia.org/wikipedia/en/9/94/Tideland_cover.jpg",
                        "http://www.youtube.com/watch?v=Zi-g_c3RUlA")
                        

movies = [the_name_of_the_rose, the_elephant_man, the_crying_game, dracula, the_mission, tideland]
fresh_tomatoes.open_movies_page(movies)
