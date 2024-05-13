import tkinter as tk

class InventoryItem:
    def __init__(self, name, quantity, expiry_date):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date

class InventoryApp:
    def __init__(self, master):
        self.master = master
        master.title("Inventory Management")

        self.inventory = []

        self.label = tk.Label(master, text="Inventory Management System")
        self.label.pack()

        self.add_button = tk.Button(master, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.remove_button = tk.Button(master, text="Remove Item", command=self.remove_item)
        self.remove_button.pack()

        self.display_button = tk.Button(master, text="Display Inventory", command=self.display_inventory)
        self.display_button.pack()


    def add_item(self):
        top = tk.Toplevel(self.master)

        tk.Label(top, text="Item Name:").pack()
        name_entry = tk.Entry(top)
        name_entry.pack()

        tk.Label(top, text="Quantity:").pack()
        quantity_entry = tk.Entry(top)
        quantity_entry.pack()

        tk.Label(top, text="Expiry Date:").pack()
        expiry_entry = tk.Entry(top)
        expiry_entry.pack()

        def add():
            name = name_entry.get()
            quantity = int(quantity_entry.get())
            expiry_date = expiry_entry.get()
            item = InventoryItem(name, quantity, expiry_date)
            self.inventory.append(item)
            tk.Label(top, text=f"{name} added to inventory").pack()
            top.destroy()

        tk.Button(top, text="Add", command=add).pack()

    def remove_item(self):
        top = tk.Toplevel(self.master)

        tk.Label(top, text="Item Name:").pack()
        name_entry = tk.Entry(top)
        name_entry.pack()

        tk.Label(top, text="Quantity:").pack()
        quantity_entry = tk.Entry(top)
        quantity_entry.pack()

        def remove():
            name = name_entry.get()
            quantity = int(quantity_entry.get())
            for item in self.inventory:
                if item.name == name:
                    if item.quantity >= quantity:
                        item.quantity -= quantity
                        tk.Label(top, text=f"{quantity} {name}(s) removed from inventory").pack()
                    else:
                        tk.Label(top, text="Not enough quantity in inventory").pack()
                    break
            else:
                tk.Label(top, text="Item not found in inventory").pack()

        tk.Button(top, text="Remove", command=remove).pack()

    def display_inventory(self):
        top = tk.Toplevel(self.master)

        tk.Label(top, text="Current Inventory:").pack()
        for item in self.inventory:
            tk.Label(top, text=f"Item: {item.name}, Quantity: {item.quantity}, Expiry Date: {item.expiry_date}").pack()

def main():
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
