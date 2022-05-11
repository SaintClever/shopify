from venv import create


class App():
    def __init__(self, inventory = {}):
        self.inventory = inventory
    

    def create_item(self):
        item = input('create item: ')
        self.inventory[item] = 0
        print(f'{item} added to inventory: ')


    def edit_item(self):
        item, item_amount = input('add or subtract item (Ex: "shirt 10"): ').split()
        self.inventory[item] += int(item_amount)
        print(f'{item}: {self.inventory[item]} in inventory')


    def delete_item(self):
        item = input('Delete item (Ex: "shirt"): ')
        self.inventory.pop(item, None)
        print(f'Removed {item} from inventory')


    def view_iventory(self):
        print(f'Current inventory: {self.inventory}')


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
        else:
            print('Invalid input')

        self.start_app()


app = App()
print('''\n--- INSTRUCTIONS ---\ncreate: puts item in inventory\nedit: edits the total items\ndelet: removes items\nquit: quits application''')
app.start_app()