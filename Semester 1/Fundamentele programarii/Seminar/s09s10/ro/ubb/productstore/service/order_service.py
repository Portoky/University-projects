
from ro.ubb.productstore.repository.in_memory_repository import GenericRepository
from ro.ubb.productstore.domain.dto import OrderDto, OrderDtoCreator


class OrderService:
    def __init__(self, order_repository, product_repository):
        self.__order_repository = order_repository
        self.__product_repository = product_repository

    def filter_orders(self, cost):
        order_dtos = self.create_order_dtos()
        result_order_dtos = []
        # for dto in order_dtos:
        #     if dto.cost > cost:
        #         result_order_dtos.append(dto)
        # result_order_dtos = [dto for dto in order_dtos if dto.cost > cost]
        result_order_dtos = list(filter(lambda dto: dto.cost > cost, order_dtos))
        return result_order_dtos

    def create_order_dtos(self):
        order_dtos = []
        for order in self.__order_repository.find_all():
            # quantity = order.quantity
            # product = self.__product_repository.find_by_id(order.product_id)
            # cost = product.price * quantity
            # name = product.name
            # order_dto = OrderDto(name, quantity, cost)
            # order_dtos.append(order_dto)
            product = self.__product_repository.find_by_id(order.product_id)
            order_dto = OrderDtoCreator.create_dto(product, order)
            order_dtos.append(order_dto)

        return order_dtos
