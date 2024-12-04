




class Movie:

    title:str

    rating:int

    run_time:int

    director:str

    genre:str

    def set_movie(self,title,rating,run_time,director,genre):

        self.title=title

        self.rating=rating

        self.run_time=run_time

        self.director=director

        self.genre=genre

    def display_movie(self):

            print(self.title,self.rating,self.run_time)

movie_instance=Movie()

movie_instance.set_movie("ARM",4.5,"2:30","jithin lal","action")

movie_instance.display_movie()
