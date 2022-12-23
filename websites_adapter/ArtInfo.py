import json

class Image:

    thumb: str
    original: str
    width: int
    height: int

    def __init__(self, thumb: str, original: str, width: int, height: int) -> None:
        self.height = height
        self.width = width
        self.thumb = thumb
        self.original = original

    def __repr__(self) -> str:
        # return f'{{"width":{self.width},"height":{self.height},"thumb":"{self.thumb}","original"}}'
        return json.dumps(self.__dict__)


class ArtInfo:

    source: str
    post_url: str
    title: str
    description: str
    illustrator: str
    userId: str
    pageCount: int
    images: list[Image]

    def __init__(self, source: str, post_url: str, title: str, description: str, illustrator: str, userId: str, pageCount: int, images: list[Image]) -> None:
        self.source = source
        self.post_url = post_url
        self.title = title
        self.description = description
        self.illustrator = illustrator
        self.userId = userId
        self.pageCount = pageCount
        self.images = images

    def __repr__(self) -> str:
        # return f'{{"source":"{self.source}","post_url":"{self.post_url}","title":"{self.title}","description":"{self.description}","pageCount":{self.pageCount},"images:{self.images}}}'
        return json.dumps(self.__dict__, default=lambda obj: obj.__dict__, ensure_ascii=False)
