from venv import create


class App():
    def __init__(self, inventory = {}):
        self.inventory = inventory
    

    def create_item(self):
        item = input('create item: ')
        self.inventory[item] = 1


    def edit_item(self):
        item, item_amount = input('add or subtract item (Ex: item "shirt 10"): ').split()
        # print(item, item_amount)
        self.inventory[item] += int(item_amount)


    def delete_item(self):
        item = input('Delete item (are you sure): ')
        self.inventory.pop(item, None)


    def view_iventory(self):
        print(self.inventory)


    def start_app(self):
        method = input('\nInventory options: create | edit | delete | view | quit: ')

        if method == 'create':
            self.create_item()
        elif method == 'edit':
            self.edit_item()
        elif method == 'delete':
            self.delete_item()
        elif method == 'view':
            self.view_iventory()
        elif method == 'quit':
            quit()

        self.start_app()


app = App()
app.start_app()