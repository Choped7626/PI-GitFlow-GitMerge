from datetime import datetime


class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items  # list of (name, price)
        self.created_at = datetime.now()

    def total_price(self):
        return sum(price for _, price in self.items)

    def summary(self):
        return {
            "order_id": self.order_id,
            "customer": self.customer,
            "total": self.total_price(),
            "items": len(self.items),
        }


class OrderManager:
    def __init__(self):
        self.orders = {}

    def create_order(self, order_id, customer, items):
        order = Order(order_id, customer, items)
        self.orders[order_id] = order
        return order

    def get_order(self, order_id):
        return self.orders.get(order_id)

    def get_total_revenue(self):
        return sum(order.total_price() for order in self.orders.values())


if __name__ == "__main__":
    manager = OrderManager()

    manager.create_order(1, "Alice", [("Keyboard", 50), ("Mouse", 25)])

    print(manager.get_total_revenue())
