from dataclasses import dataclass

@dataclass
class Book:
    title: str # Важно отметить, что аннотации типов обязательны
    author: str # можете указать Any из модуля typing

