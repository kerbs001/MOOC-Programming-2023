# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rating_list = []
        self.movie_list = []
    
    def __str__(self):
        genre_list = ", ".join(self.genres)
        rating_count = len(self.rating_list)
        if rating_count != 0:
            rating_average = sum(self.rating_list) / rating_count
            statement = f"{self.title} ({self.seasons} seasons)\ngenres: {genre_list}\n{rating_count} ratings, average {rating_average:.1f} points"
        else:
            statement = f"{self.title} ({self.seasons} seasons)\ngenres: {genre_list}\nno ratings"
        
        return statement

    def rate(self, rating: int):
        self.rating_list.append(rating)
        
def minimum_grade(rating: int, series_list):
    result = []
    for series in series_list:
        if series.rating_list and sum(series.rating_list) / len(series.rating_list) >= rating:
            result.append(series)
    return result
    
def includes_genre(genre, series_list):
    result = []
    for series in series_list:
        if genre in series.genres:
            result.append(series)
    return result

    

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)