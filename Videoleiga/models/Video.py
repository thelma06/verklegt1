class Video:

    def __init__(self, title = "", genre = "", length = ""):
        self.title = title
        self.genre = genre
        self.length = length

    def get_title(self):
        return self.title
    
    def get_genre(self):
        return self.genre
    
    def get_length(self):
        return self.length
