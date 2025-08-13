meatShelves = {}
fruitShelves = {}
vegetableShelves = {}
drinksShelves = {}

shelvesList = [meatShelves, fruitShelves, vegetableShelves, drinksShelves]


def itemFinder(itemName):
    for shelf in shelvesList:  
        for itemList in shelf.values():  
            for item in itemList: 
                if itemName == item[0]: 
                    print("Item Found!")
                    employeeMenu()
                    return
    print(f"Item not Found. Please stock {itemName} first!")
    employeeMenu()

def itemQuantity(itemName, qty):
    for shelf in shelvesList:       
        for itemList in shelf.values():  
            for item in itemList: 
                if itemName == item[0]:  
                    item[1] = min(item[1] + qty, 50)  
                    print(f"Updated quantity: {item[1]}")

                    employeeMenu()
                    return  
    
    print(f"Item not Found. Please stock {itemName} first!")
    employeeMenu()

def displayStockedItems():
    print("\n=== Stocked Items ===")
    for shelf in shelvesList:
        for category, items in shelf.items():
            for item in items:
                print(f"{category} - Name: {item[0]}, Qty: {item[1]}, Price: {item[2]}")

def findItem(itemType):

    match itemType:
        case "Vegetable":
            print("Vegetable")
            vegetableName = input("Enter the name of the vegetable: ")
            itemFinder(vegetableName)
        case "Fruit":
            print("Fruit")
            fruitName = input("Enter the name of the fruit: ")
            itemFinder(fruitName)
        case "Meat":
            print("Meat")
            meatName = input("Enter the name of the meat: ")
            itemFinder(meatName)
        case "Drinks":
            print("Drinks")
            drinkName = input("Enter the name of the drink: ")
            itemFinder(drinkName)


class Items:
    def __init__(self, type, name, quantity, price):
        self.type = type
        self.name = name
        self.quantity = quantity
        self.price = price
        self.item = name, quantity, price

    def isFull(self):

        if self.quantity > 50:
            print(f"The {self.type} {self.name} is filled")
        else:
            print(f"The {self.type} {self.name} quantity is {self.quantity}")


class Shelf(Items):
    def __init__(self, type, name, quantity, price):
        super().__init__(type, name, quantity, price)
        self.type = type
        self.name = name
        self.quantity = quantity
        self.price = price
        self.item = name, quantity, price

    def fruitShelves(self):
        if self.type == "Fruit":
            fruitShelves.update({"fruitShelves": self.item})
            displayStockedItems()

    def vegetableShelves(self):
        if self.type == "Vegetable":
            vegetableShelves.update({"vegetableShelves": self.item})
            displayStockedItems()

    def drinksShelves(self):
        if self.type == "Drinks":
            drinksShelves.update({"drinksShelves": self.item})
            displayStockedItems()

    def meatShelves(self):
        if self.type == "Meat":
            meatShelves.update({"meatShelves": self.item})
            displayStockedItems()


def enterMarket():
    try:
        choice = int(input("""
What are you?
[1] Customer
[2] Employee 
>> """))
        if choice == 1:
            print("Smtg")
        elif choice == 2:
            employeeMenu()
    except:
        enterMarket()

def customerMenu():
    choice = int(input("""
What do you want to do?
[1] Buy Items
[2] Inspect Items
>> """))

def employeeMenu():

    try:
        print(fruitShelves)
        choice = int(input("""
What do you want to do?    
[1] Stock Items
[2] Inspect Items
[3] Add Stock to Item   
>> """))

        if choice == 1:
            stockItems()
        elif choice == 2:
            inspectItem()
        elif choice == 3:
            addQuantity()

    except:
        employeeMenu()


def stockItems():

    try:
        itemType = input("What type of item is this? (Fruit, Vegetable, Drink, Meat)"
                    "\n>> ")
        itemName = input("What is this item?"
                    "\n>> ")
        qty = int(input("How many would you like to restock? (Max. 50)"
                    "\n>> "))
        while int(qty) > 50:
            qty = input("How many would you like to restock? (Max. 50)"
                        "\n>> ")

        price = float(input("How much would the cost be?"
                    "\n>> "))
        item = [itemName, qty, price]
        
        if itemType == "Meat":
            meatShelves.setdefault(itemType, []).append(item)
        elif itemType == "Vegetable":
            vegetableShelves.setdefault("vegetableShelves", []).append(item)
        elif itemType == "Fruit":
            fruitShelves.setdefault(itemType, []).append(item)
        elif itemType == "Drink":
            drinksShelves.setdefault("drinksShelves", []).append(item)
        displayStockedItems()
        employeeMenu()

    except: 
        employeeMenu()


def inspectItem():
    itemType = input("Input the type of the item: ")
    findItem(itemType)

def addQuantity():
    itemName = input("Input item name: ")
    qty = int(input("How many would you like to stock?"))
    
    itemQuantity(itemName, qty)


open = input("Type OPEN to go to supermarket: ")
x = open.upper()
if x == "OPEN":
    enterMarket()



