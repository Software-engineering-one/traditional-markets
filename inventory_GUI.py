import tkinter as tk

class InventoryItem:
    def __init__(self, name, expiry_date, purchase_date, quantity):
        self.name = name
        self.expiry_date = expiry_date
        self.purchase_date = purchase_date
        self.quantity = quantity

class InventoryManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("재고 관리")

        self.inventory = []

        # Labels
        self.label_name = tk.Label(root, text="이름:")
        self.label_name.grid(row=0, column=0)
        self.label_expiry_date = tk.Label(root, text="유통 기한:")
        self.label_expiry_date.grid(row=1, column=0)
        self.label_purchase_date = tk.Label(root, text="구입 기한:")
        self.label_purchase_date.grid(row=2, column=0)
        self.label_quantity = tk.Label(root, text="수량:")
        self.label_quantity.grid(row=3, column=0)

        # Entry fields
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1)
        self.entry_expiry_date = tk.Entry(root)
        self.entry_expiry_date.grid(row=1, column=1)
        self.entry_purchase_date = tk.Entry(root)
        self.entry_purchase_date.grid(row=2, column=1)
        self.entry_quantity = tk.Entry(root)
        self.entry_quantity.grid(row=3, column=1)

        # Buttons
        self.button_add = tk.Button(root, text="재고 추가", command=self.add_item)
        self.button_add.grid(row=4, column=0, columnspan=2)
        self.button_show_all = tk.Button(root, text="재고 목록", command=self.show_all_items)
        self.button_show_all.grid(row=5, column=0, columnspan=2)

    def add_item(self):
        name = self.entry_name.get()
        expiry_date = self.entry_expiry_date.get()
        purchase_date = self.entry_purchase_date.get()
        quantity = self.entry_quantity.get()

        item = InventoryItem(name, expiry_date, purchase_date, quantity)
        self.inventory.append(item)

        # Optionally, you can display a message box or update a status label here
        print(f"{name} added to inventory.")

    def show_all_items(self):
        # Clear the previous content
        self.clear_display()

        # Display all items
        for idx, item in enumerate(self.inventory):
            tk.Label(self.root, text=f"품목 {idx + 1}: {item.name}, 유통 기한: {item.expiry_date}, 구입 기한: {item.purchase_date}, 수량: {item.quantity}").grid(row=idx + 6, column=0, columnspan=2)

    def clear_display(self):
        # Clear the display area
        for widget in self.root.winfo_children():
            widget.grid_forget()


if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagerApp(root)
    root.mainloop()
