import strawberry

@strawberry.type
class TypeBook:
    book_id: int
    title: str
    author: str
    publisher: str