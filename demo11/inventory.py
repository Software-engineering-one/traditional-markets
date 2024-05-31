# inventory.py
import tkinter as tk

class InventoryItem:
    def __init__(self, name, quantity, expiry_date):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date

class InventoryApp:
    def __init__(self, master):
        self.master = master
        master.title("재고 관리")
        master.geometry("300x200")

        self.inventory = []

        self.label = tk.Label(master, text="재고 관리 시스템")
        self.label.pack()

        self.add_button = tk.Button(master, text="재고 추가", command=self.add_item)
        self.add_button.pack()

        self.remove_button = tk.Button(master, text="재고 삭제", command=self.remove_item)
        self.remove_button.pack()

        self.display_button = tk.Button(master, text="재고 목록", command=self.display_inventory)
        self.display_button.pack()

    def add_item(self):
        top = tk.Toplevel(self.master)

        tk.Label(top, text="재료 이름:").pack()
        name_entry = tk.Entry(top)
        name_entry.pack()

        tk.Label(top, text="수량:").pack()
        quantity_entry = tk.Entry(top)
        quantity_entry.pack()

        tk.Label(top, text="유통기한:").pack()
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

        tk.Button(top, text="추가", command=add).pack()

    def remove_item(self):
        top = tk.Toplevel(self.master)

        tk.Label(top, text="재료 이름:").pack()
        name_entry = tk.Entry(top)
        name_entry.pack()

        tk.Label(top, text="수량:").pack()
        quantity_entry = tk.Entry(top)
        quantity_entry.pack()

        def remove():
            name = name_entry.get()
            quantity = int(quantity_entry.get())
            for item in self.inventory:
                if item.name == name:
                    if item.quantity >= quantity:
                        item.quantity -= quantity
                        tk.Label(top, text=f"{quantity} {name}가 삭제되었습니다.").pack()
                    else:
                        tk.Label(top, text="인벤토리에 충분한 수량이 없습니다.").pack()
                    break
            else:
                tk.Label(top, text="인벤토리에서 재료를 찾을수 없습니다.").pack()

        tk.Button(top, text="삭제", command=remove).pack()

    def display_inventory(self):
        top = tk.Toplevel(self.master)

        tk.Label(top, text="현재 품목:").pack()
        for item in self.inventory:
            tk.Label(top, text=f"재료명: {item.name}, 수량: {item.quantity}, 유통기한: {item.expiry_date}").pack()
