import strawberry
from Strawberry.models import Book
from Strawberry.GraphQL.type import TypeBook
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def books(self, author:str = None) -> List[TypeBook]:
        try:
            # logging.info("Querying books")
            if author:
                books = Book.objects.filter(author=author)
                return books
            return Book.objects.all()  
        except Exception as e:
            # logging.error(e, "Error querying movies")
            return None

@strawberry.type
class Mutation:
    @strawberry.field
    def add_book(self, title: str, author: str, publisher: str ) -> TypeBook:
        book = Book(title=title, author=author, publisher=publisher )
        book.save()
        return book
    
    
    @strawberry.field
    def update_book(self, book_id:int, title: str, author: str, publisher: str ) -> TypeBook:
        book = Book.get(book_id=book_id)
        book.title = title
        book.author = author
        book.publisher = publisher
        book.save()
        return book
    @strawberry.field
    def delete_book(self, book_id:str) -> bool:
        book = Book.objects.get(book_id=book_id)
        book.delete()
        return True
    
Schema = strawberry.Schema( query=Query , mutation=Mutation )