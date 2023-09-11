from typing import List


class MyList:
    def __init__(self, data: List):
        self.data = data

    def __hash__(self):
        hash_sum = 0
        md = 1000000007
        for ind, elem in enumerate(self.data):
            if elem is int:
                hash_sum = (hash_sum + elem) % md
            else:
                hash_sum = (hash_sum + ind) % md
        return hash_sum

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return str(self.data)
