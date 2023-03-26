from dataclasses import dataclass

'''Datatransfer object'''
@dataclass
class OrderDto:
    product_name : str
    quantity : int
    cost : int

class OrderDtoCreator:

    @staticmethod #no self. needed -> staticmethod
    def create_dto(product, order):
        return OrderDto(product.name, order.quantity, order.quantity * product.price)