import tkinter as tk
from tkinter import messagebox

class InventoryItem:
    def __init__(self, name, quantity, expiry_date):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date

class InventoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management")

        self.inventory = []

        self.label = tk.Label(master, text="Inventory Management")
        self.label.pack()

        self.add_button = tk.Button(master, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.remove_button = tk.Button(master, text="Remove Item", command=self.remove_item)
        self.remove_button.pack()

        self.display_button = tk.Button(master, text="Display Inventory", command=self.display_inventory)
        self.display_button.pack()



    def add_item(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Add Item")

        tk.Label(self.add_window, text="Name:").grid(row=0, column=0)
        tk.Label(self.add_window, text="Quantity:").grid(row=1, column=0)
        tk.Label(self.add_window, text="Expiry Date:").grid(row=2, column=0)

        self.name_entry = tk.Entry(self.add_window)
        self.name_entry.grid(row=0, column=1)

        self.quantity_entry = tk.Entry(self.add_window)
        self.quantity_entry.grid(row=1, column=1)

        self.expiry_entry = tk.Entry(self.add_window)
        self.expiry_entry.grid(row=2, column=1)

        add_button = tk.Button(self.add_window, text="Add", command=self.add_to_inventory)
        add_button.grid(row=3, columnspan=2)

    def add_to_inventory(self):
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        expiry_date = self.expiry_entry.get()

        item = InventoryItem(name, quantity, expiry_date)
        self.inventory.append(item)
        messagebox.showinfo("Success", f"{name} has been added to the inventory.")

        self.add_window.destroy()

    def remove_item(self):
        self.remove_window = tk.Toplevel(self.master)
        self.remove_window.title("Remove Item")

        tk.Label(self.remove_window, text="Name:").grid(row=0, column=0)
        tk.Label(self.remove_window, text="Quantity:").grid(row=1, column=0)

        self.name_entry = tk.Entry(self.remove_window)
        self.name_entry.grid(row=0, column=1)

        self.quantity_entry = tk.Entry(self.remove_window)
        self.quantity_entry.grid(row=1, column=1)

        remove_button = tk.Button(self.remove_window, text="Remove", command=self.remove_from_inventory)
        remove_button.grid(row=2, columnspan=2)

    def remove_from_inventory(self):
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())

        for item in self.inventory:
            if item.name == name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    if item.quantity == 0:
                        self.inventory.remove(item)
                        messagebox.showinfo("Success", f"{name}'s inventory is empty and removed.")
                    else:
                        messagebox.showinfo("Success", f"{quantity} {name}(s) removed from inventory.")
                    break
                else:
                    messagebox.showerror("Error", "Insufficient stock.")
                    break
        else:
            messagebox.showerror("Error", "Item not found in inventory.")

        self.remove_window.destroy()

    def display_inventory(self):
        self.display_window = tk.Toplevel(self.master)
        self.display_window.title("Inventory")

        tk.Label(self.display_window, text="Inventory:").pack()

        for item in self.inventory:
            tk.Label(self.display_window, text=f"Name: {item.name}, Quantity: {item.quantity}, Expiry Date: {item.expiry_date}").pack()

def main():
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
