from dataclasses import dataclass


# class Payment:
#     def __init__(self, id, sum):
#         self.__id = id
#         self.__sum = sum
@dataclass
class Payment:
    id: int
    sum: int

    def __str__(self):
        print(f"{self.id}; {self.sum}")

obj = Payment(1, 255)
print(obj)