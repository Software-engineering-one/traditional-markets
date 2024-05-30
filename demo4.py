import tkinter as tk
from tkinter import messagebox
import food  # Importing food.py module

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

        self.quit_button = tk.Button(master, text="Quit", command=self.master.quit)
        self.quit_button.pack()

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

        # Save inventory to a file
        self.save_inventory()

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

        # Save inventory to a file
        self.save_inventory()

    def display_inventory(self):
        self.display_window = tk.Toplevel(self.master)
        self.display_window.title("Inventory")

        tk.Label(self.display_window, text="Inventory:").pack()

        for item in self.inventory:
            tk.Label(self.display_window, text=f"Name: {item.name}, Quantity: {item.quantity}, Expiry Date: {item.expiry_date}").pack()

    def save_inventory(self):
        with open("inventory.txt", "w") as f:
            for item in self.inventory:
                f.write(f"{item.name},{item.quantity},{item.expiry_date}\n")

def click_button1():
   sublabel = tk.Label(tkin, text="1. 별점 및 평가 입력 2. 별점 및 평가 조회")
   sublabel.pack()
   button3 = tk.Button(tkin, text="1. 별점 및 평가 입력", command=click_button3)
   button3.pack()
   button4 = tk.Button(tkin, text="2. 별점 및 평가 조회", command=click_button4)
   button4.pack()

def click_button2():
    sublabel2 = tk.Label(tkin, text="작업을 선택하세요")
    sublabel2.pack()

    def execute_inventory():
        import inventory
        root = tk.Tk()
        app1 = inventory.InventoryApp(root) 
        root.mainloop()
        
    def execute_food():
        root = tk.Tk()  # Create a new Tkinter window
        app = food.InventoryApp(root)  # Create an instance of food.InventoryApp
        root.mainloop()  # Run the Tkinter event loop for the food inventory app

    def starandevalmanagement():
        notice()


    inventory_button = tk.Button(tkin, text="재고관리", command=execute_inventory)
    inventory_button.pack()

    food_button = tk.Button(tkin, text="음식관리", command=execute_food)
    food_button.pack()

    board_button = tk.Button(tkin, text = "별점 및 평가관리", command = starandevalmanagement)
    board_button.pack()

def click_button3():
    consumer_Label = tk.Label(tkin, text="별점 및 평가를 입력하세요")
    consumer_Label.pack()
    consumer_label2 = tk.Label(tkin, text="별점:")
    consumer_label2.pack()
    consumer_entry = tk.Entry(tkin)
    consumer_entry.pack()
    consumer_label3 = tk.Label(tkin, text="평가:")
    consumer_label3.pack()
    consumer_entry2 = tk.Entry(tkin)
    consumer_entry2.pack()
    consumer_entry.get()
    consumer_entry2.get()
    starandevalcheck = tk.Button(tkin, text="별점 및 평가 입력 완료", command=lambda: starandeval(consumer_entry.get(), consumer_entry2.get()))
    starandevalcheck.pack()

def starandeval(star, eval):
    rate[star] = eval
    click_button1()

def notice():
    for star, eval in rate.items():
        total_Label = tk.Label(tkin, text=star)
        total_Label.pack()
        total_Label2 = tk.Label(tkin, text=eval)
        total_Label2.pack()


def click_button4():
    notice()

star = 0
eval = 0
tkin = tk.Tk()
tkin.title("운영관리")
rate = dict()

mainlabel = tk.Label(tkin, text="소비자 또는 소상공인 유무를 확인하세요")
mainlabel.pack()
button1 = tk.Button(tkin, text="1. 소비자", command=click_button1)
button1.pack()
button2 = tk.Button(tkin, text="2. 소상공인", command=click_button2)
button2.pack()

tkin.mainloop()