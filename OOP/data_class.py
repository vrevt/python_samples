from dataclasses import dataclass

@dataclass
class Book:
    title: str # Важно отметить, что аннотации типов обязательны
    author: str # можете указать Any из модуля typing

if __name__ == '__main__':
    book = Book('winni pooh', 'alex miln')
    print(book)
