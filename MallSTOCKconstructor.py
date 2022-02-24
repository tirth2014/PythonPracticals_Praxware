Total_Stock = int(input("enter no. of items: "))

class Mall:
    def __init__(self):

        self.item_list = []
        for x in range(0, Total_Stock):
            item = input(F"Enter item{x} : ")
            self.item_list.append(item)
            print(self.item_list)

        # Stock
        self.stock = []
        print("\nEnter the stock of items \n")
        for x in range(0, Total_Stock):
            list_stock = int(input(F"Enter the stock of {self.item_list[x]} : "))
            self.stock.append(list_stock)
            print(self.stock)

        # Arriving Price of Stock
        self.Arriving_Price = []
        for i in range(0, Total_Stock):
            arriving_price = int(input(F"Enter the arriving price of {self.item_list[i]} : "))
            self.Arriving_Price.append(arriving_price)
            print(self.Arriving_Price)

        # Selling Price of Stock
        self.Selling_price = []
        for x in range(0, Total_Stock):
            selling_item = int(input(F"Enter the selling price of {self.item_list[x]} : "))
            self.Selling_price.append(selling_item)
            print(self.Selling_price)

        # Sold items
        self.Sold_items = []
        print('\nEnter your sold item \n')
        for x in range(0, Total_Stock):
            sold_count = int(input(F"Enter the number of {self.item_list[x]} sold : "))
            self.Sold_items.append(sold_count)
            print(self.Sold_items)

        # Available Stock
        self.Available = []
        for x in range(0, Total_Stock):
            available_stock = self.stock[x] - self.Sold_items[x]
            self.Available.append(available_stock)
            print(self.Available)

        self.Commission = []
        for x in range(0, Total_Stock):
            commissions = (self.Sold_items[x] * self.Selling_price[x]) * 0.1
            self.Commission.append(commissions)

        # salesman information
        Salesman = input("\nEnter salesman Name : ")

    def show(self):
        for x in range(0, Total_Stock):
            print("stock available: {} : {}".format(self.item_list[x], self.Available[x]))
        for x in range(0, Total_Stock):
            print("arrival price & selling price are: {} : {}".format(self.Arriving_Price[x], self.Selling_price[x]))
        for x in range(0, Total_Stock):
            print("commision on {} is {} ".format(self.item_list[x], self.Commission[x]))


obj = Mall()
obj.show()
