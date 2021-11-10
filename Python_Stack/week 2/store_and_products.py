class Store:

    def __init__(self, name) -> None:
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        self.products.pop(id)
        return self
        
    def inflation(self, percent_increase):
        is_increased = True
        self.price = Product.update_price(percent_increase, is_increased)
        return self
        
    def set_clearance(self, category, percent_discount):
        is_increased = False
        for product in self.products:
            if product.category == category:
                product.price = Product.update_price(percent_discount, is_increased)
        return self
    
class Product:

    def __init__(self, name, price, category) -> None:
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= (1 + percent_change)
        else:
            self.price *= (1 - percent_change)
        return self


Store_A = Store("Python Master")
Store_A.add_product(Product("Python_package_1", 500, "Python"))
Store_A.products[0].category
Store_A.set_clearance("Python", .05)