"""

@author: radu

 
"""


class ProductValidator:
    def validate(self, product): #one argument! which is the entity
        if product.name == "":
            raise ValueError("name can not be empty")
        # todo: other validations