class App():
    def __init__(self, inventory = {}):
        self.inventory = inventory
    
    def create_item(self):
        item = input('Add item: ')
        self.inventory[item] = 1

    def edit_item(self):
        item, item_amount = input('add or subtract item (Ex: item name: amount): ').split()
        self.inventory[item] += int(item_amount)


    def delete_item(self):
        item = input('Delete item (are you sure): ')
        self.inventory(item, None)

    def view_iventory(self):
        print(self.inventory)


app = App()