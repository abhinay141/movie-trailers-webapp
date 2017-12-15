import fresh_tomatoes
import media
# Creating movies to describe the instances of the Class Movie

justice_league=media.Movie(
            "Justice League",
            "a dc celluloid",
            "http://t0.gstatic.com/images?q=tbn:ANd9GcTbr9aajZtJiuhXc_biRws9jzCi4u1q4MWvyPVe0rGO9Z0RwDqT",
            "https://www.youtube.com/watch?v=Fm3VgcyaPfo")

avengers=media.Movie(
        "Avengers:The infinity war-1",
        "a comic superhero fim",
        "https://upload.wikimedia.org/wikipedia/en/9/90/Avengers_Infinity_War.jpg",
        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

dunkirk=media.Movie(
        "Dunkirk",
        "A real story based on world war-ii",
        "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
        "https://www.youtube.com/watch?v=F-eMt3SrfFU")

Starwars=media.Movie(
        "Starwars:The last jedi",
        "A sci-fi action movie",
        "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
        "https://www.youtube.com/watch?v=Q0CbN8sfihY")

jurassic=media.Movie(
        "Jurassic world: fallen Kingdom",
        "a movie on the dinos",
        "https://upload.wikimedia.org/wikipedia/en/c/c6/Jurassic_World_Fallen_Kingdom.png",
        "https://www.youtube.com/watch?v=vn9mMeWcgoM"  )

#creating the list of all the instances
movies=[
    justice_league,
    avengers,
    dunkirk,
    Starwars,
    jurassic
]

#passing the array of movies to the function
fresh_tomatoes.open_movies_page(movies)
