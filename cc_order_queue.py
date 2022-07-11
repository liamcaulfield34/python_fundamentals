
class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        order = {"customer": customer, "flavor": flavor, "scoops": scoops}

        if order.get("flavor") in self.flavors and scoops <= 3 and scoops >= 1:
            print("Order created!")
        elif scoops < 1 or scoops > 3:
            print("Choose between 1-3 scoops.")
            return None
        elif order.get("flavor") not in self.flavors:
            print("Sorry, we don't have that flavor.")
            return None

        self.orders.enqueue(order)

    def show_all_orders(self):
        orders = self.orders
        print('\nAll Pending Ice Cream Orders:')
        for key in orders.items:
            print(
                "Customer: {customer} -- Flavor: {flavor} -- Scoops: {scoops}".format(**key))

    def next_order(self):
        orders = self.orders.dequeue()
        print('\nNext Order Up!')
        print(
            "Customer: {customer} -- Flavor: {flavor} -- Scoops: {scoops}".format(**orders))


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
