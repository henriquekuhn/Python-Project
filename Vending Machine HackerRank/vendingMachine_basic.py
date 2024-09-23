class VendingMachine:
    def __init__(self, items, price):
        self.items = items
        self.price = price

    def updateStock(self, stock):
        self.stock = stock

    def buy(self, purchase, budget):
        self.purchase = purchase 
        self.budget = budget

        total_price = self.purchase * self.price

        if ((self.items >= self.purchase) and (total_price <= self.budget)):
            self.items -= self.purchase
            return (self.budget - total_price) 
        
        elif self.items < self.purchase:
            return "Not enough items"
        
        else:
            return "Not enough money"
        

if __name__ == "__main__":
    print("You are in maintenance mode.")
    items_feed = input("Please, add the number of items to feed the vender machine: ")
    items_price = input("Please, add price of the items: ")
    client1 = VendingMachine(int(items_feed), int(items_price))

    print("\n\nYou are in purchaser mode.")

    #times to run
    t = 4

    for i in range(t):
        items_purchase = input("Please, add the number of items you want to purchase: ")
        your_budget = input("Please, add yout budget: ")
     
        result = client1.buy(int(items_purchase), int(your_budget))
        print(result)