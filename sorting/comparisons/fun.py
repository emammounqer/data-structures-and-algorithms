
def sort_by_name(movies):
    return sorted(movies, key=lambda movie: format_movie(movie["title"]))


def sort_by_year(movies):
    return sorted(movies, key=lambda movie: movie["year"])


def format_movie(title: str):
    lower_title = title.lower()
    if lower_title.startswith("the "):
        return lower_title[4:]
    if lower_title.startswith("a "):
        return lower_title[2:]
    if lower_title.startswith("an "):
        return lower_title[3:]
    return lower_title
