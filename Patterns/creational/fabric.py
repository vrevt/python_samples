from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
	@abstractmethod
	def factory_method(self):
		pass

	def some_operation(self) -> str:
		product = self.factory_method()
		res = f"Creator - {product.operation()}"
		return res


class ConcreteCreator1(Creator):
	def factory_method(self) -> Product:
		return ConcreteProduct1()


class ConcreteCreator2(Creator):
	def factory_method(self) -> Product:
		return ConcreteProduct2()


class Product(ABC):
	def operation(self) -> str:
		pass


class ConcreteProduct1(Product):
	def operation(self) -> str:
		return "result of ConcreteProduct1"


class ConcreteProduct2(Product):
	def operation(self) -> str:
		return "result of ConcreteProduct2"


def client_code(creator: Creator) -> None:
	print(f"Client: {creator.some_operation()}")


if __name__ == "__main__":
	print("work with creator1")
	client_code(ConcreteCreator1())

	print("work with creator2")
	client_code(ConcreteCreator2())
