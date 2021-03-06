class News:
    """
    News class to define News Objects
    """

    def __init__(self, description, urlToImage, publishedAt):
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


class Sources:
    def __init__(self, id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country