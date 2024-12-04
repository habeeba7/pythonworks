
movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},

]

# total number of movies
print(len(movies))

# print movies titles
movie_titles=[m.get("title") for m in movies]
print(movie_titles)

# print malayalam movies
malayalam_movie=[m.get("title") for m in movies if m.get("language")=="malayalam"]
print(malayalam_movie)


all_language=[m.get("language") for m in movies ]
print(all_language)
language_count={l:all_language.count(l) for l in all_language}
print(language_count)

# movies in 2024
movies_year=[m.get("title") for m in movies if m.get("year")==2024]
print(movies_year)