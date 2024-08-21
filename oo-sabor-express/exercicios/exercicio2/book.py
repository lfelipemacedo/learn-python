class Book:
    
    books = []
    
    def __init__(self, title: str, author: str, publication_year: int) -> None:
        self._title: str = title
        self._author: str = author
        self._publication_year: int = publication_year
        self._available: bool = True
        Book.books.append(self)
    
    def __str__(self) -> str:
        return f'{self._title} | {self._author} | {self._publication_year} | {"Available" if self._available else "Unavailable"}'
    
    @classmethod
    def check_availability(cls, year: int) -> list:
        result = []
        
        for book in cls.books:
            if book._publication_year == year:
                result.append(book)
        return result
    
    def lendBook(self) -> None:
        self._available = False