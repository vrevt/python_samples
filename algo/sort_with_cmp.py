from functools import cmp_to_key

class Elem:
    def __init__(self, amount):
        self.amount = amount
    def __lt__(self, other):
        return str(self.amount) + str(other.amount) < str(other.amount) + str(self.amount)

    def __repr__(self):
        return str(self.amount)

values = [Elem(91), Elem(1), Elem(434), Elem(23), Elem(993), Elem(92)]

res = sorted(values, reverse=True)
print(res)
