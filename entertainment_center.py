import fresh_tomatoes
import media

"""Create movies"""
toy_story = media.Movie("Toy Story",
                        "Toys come to life",
                        "http://ia.media-imdb.com/images/M/MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@._V1_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://emilydavison16.files.wordpress.com/2014/03/avatar-1st-movie-poster-experimentation.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
fight_club = media.Movie("Fight Club",
                         "People fight in the fight club",
                         "http://ia.media-imdb.com/images/M/MV5BMjIwNTYzMzE1M15BMl5BanBnXkFtZTcwOTE5Mzg3OA@@._V1_.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")
life_is_beautiful = media.Movie("Life is Beautiful",
                                "An unforgettable fable that proves love, family, and imagination conquer all.",
                                "https://upload.wikimedia.org/wikipedia/zh/4/44/Life_is_beautiful_ver1.jpg",
                                "https://www.youtube.com/watch?v=3Y_p7KmAiLM")
the_intouchables = media.Movie("The Intouchables",
                               "Sometimes you have to reach into someone else's world to find what's missing in your own",
                               "http://ia.media-imdb.com/images/M/MV5BMTYxNDA3MDQwNl5BMl5BanBnXkFtZTcwNTU4Mzc1Nw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                               "https://www.youtube.com/watch?v=34WIbmXkewU")
snatch = media.Movie("Snatch.",
                     "A rock-'em sock-'em caper with energy to share.",
                     "http://ia.media-imdb.com/images/M/MV5BMTk5NzE0MDQyNl5BMl5BanBnXkFtZTcwNzk4Mjk3OA@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=nd7df-Yv_Z4")

#add all movies into an array
movies = [toy_story, avatar, fight_club, life_is_beautiful, the_intouchables, snatch]

#display the movies on the web via fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies) 

