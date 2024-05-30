import tkinter as tk
from tkinter import messagebox
import foodGUI2  # Importing foodGUI2.py module

class InventoryItem:
    def __init__(self, name, quantity, expiry_date):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date

class InventoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("재고 관리")

        self.inventory = []

        self.label = tk.Label(master, text="재고 관리")
        self.label.pack()

        self.add_button = tk.Button(master, text="아이템 추가", command=self.add_item)
        self.add_button.pack()

        self.remove_button = tk.Button(master, text="아이템 제거", command=self.remove_item)
        self.remove_button.pack()

        self.display_button = tk.Button(master, text="재고 보기", command=self.display_inventory)
        self.display_button.pack()

        self.quit_button = tk.Button(master, text="종료", command=self.master.quit)
        self.quit_button.pack()

    def add_item(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("아이템 추가")

        tk.Label(self.add_window, text="이름:").grid(row=0, column=0)
        tk.Label(self.add_window, text="수량:").grid(row=1, column=0)
        tk.Label(self.add_window, text="유효기간:").grid(row=2, column=0)

        self.name_entry = tk.Entry(self.add_window)
        self.name_entry.grid(row=0, column=1)

        self.quantity_entry = tk.Entry(self.add_window)
        self.quantity_entry.grid(row=1, column=1)

        self.expiry_entry = tk.Entry(self.add_window)
        self.expiry_entry.grid(row=2, column=1)

        add_button = tk.Button(self.add_window, text="추가", command=self.add_to_inventory)
        add_button.grid(row=3, columnspan=2)

    def add_to_inventory(self):
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        expiry_date = self.expiry_entry.get()

        item = InventoryItem(name, quantity, expiry_date)
        self.inventory.append(item)
        messagebox.showinfo("성공", f"{name} 이/가 재고에 추가되었습니다.")

        self.add_window.destroy()

    def remove_item(self):
        self.remove_window = tk.Toplevel(self.master)
        self.remove_window.title("아이템 제거")

        tk.Label(self.remove_window, text="이름:").grid(row=0, column=0)
        tk.Label(self.remove_window, text="수량:").grid(row=1, column=0)

        self.name_entry = tk.Entry(self.remove_window)
        self.name_entry.grid(row=0, column=1)

        self.quantity_entry = tk.Entry(self.remove_window)
        self.quantity_entry.grid(row=1, column=1)

        remove_button = tk.Button(self.remove_window, text="제거", command=self.remove_from_inventory)
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
                        messagebox.showinfo("성공", f"{name} 의 재고가 비어 제거되었습니다.")
                    else:
                        messagebox.showinfo("성공", f"{quantity} 개의 {name} 이/가 재고에서 제거되었습니다.")
                    break
                else:
                    messagebox.showerror("오류", "재고가 부족합니다.")
                    break
        else:
            messagebox.showerror("오류", "재고에서 아이템을 찾을 수 없습니다.")

        self.remove_window.destroy()

    def display_inventory(self):
        self.display_window = tk.Toplevel(self.master)
        self.display_window.title("재고")

        tk.Label(self.display_window, text="재고:").pack()

        for item in self.inventory:
            tk.Label(self.display_window, text=f"이름: {item.name}, 수량: {item.quantity}, 유효기간: {item.expiry_date}").pack()

def click_button1():
    tkin.destroy()
    global tkin2
    tkin2 = tk.Tk()
    tkin2.title("별점 및 평가")
    sublabel = tk.Label(tkin2, text="1. 별점 및 평가 입력 2. 별점 및 평가 조회")
    sublabel.pack()
    button3 = tk.Button(tkin2, text="1. 별점 및 평가 입력", command=click_button3)
    button3.pack()
    button4 = tk.Button(tkin2, text="2. 별점 및 평가 조회", command=click_button4)
    button4.pack()

def click_button2():
    tkin.destroy()
    global tkin2
    tkin2 = tk.Tk()
    tkin2.title("작업 선택")
    sublabel2 = tk.Label(tkin2, text="작업을 선택하세요")
    sublabel2.pack()

    def execute_inventory():
        tkin2.destroy()
        root = tk.Tk()
        app1 = InventoryApp(root)
        root.mainloop()
        
    def execute_food():
        tkin2.destroy()
        root = tk.Tk()  # Create a new Tkinter window
        app = foodGUI2.InventoryApp(root)  # Create an instance of food.InventoryApp
        root.mainloop()  # Run the Tkinter event loop for the food inventory app

    def starandevalmanagement():
        tkin2.destroy()
        notice()

    inventory_button = tk.Button(tkin2, text="재고관리", command=execute_inventory)
    inventory_button.pack()

    food_button = tk.Button(tkin2, text="음식관리", command=execute_food)
    food_button.pack()

    board_button = tk.Button(tkin2, text="별점 및 평가관리", command=starandevalmanagement)
    board_button.pack()

def click_button3():
    tkin2.destroy()
    global tkin3
    tkin3 = tk.Tk()
    tkin3.title("별점 및 평가 입력")
    consumer_Label = tk.Label(tkin3, text="별점 및 평가를 입력하세요")
    consumer_Label.pack()
    consumer_label2 = tk.Label(tkin3, text="별점:")
    consumer_label2.pack()
    consumer_entry = tk.Entry(tkin3)
    consumer_entry.pack()
    consumer_label3 = tk.Label(tkin3, text="평가:")
    consumer_label3.pack()
    consumer_entry2 = tk.Entry(tkin3)
    consumer_entry2.pack()
    starandevalcheck = tk.Button(tkin3, text="별점 및 평가 입력 완료", command=lambda: starandeval(consumer_entry.get(), consumer_entry2.get()))
    starandevalcheck.pack()

def starandeval(star, eval):
    rate[star] = eval
    tkin3.destroy()
    click_button1()

def notice():
    global tkin4
    tkin4 = tk.Tk()
    tkin4.title("별점 및 평가 조회")
    for star, eval in rate.items():
        total_Label = tk.Label(tkin4, text=star)
        total_Label.pack()
        total_Label2 = tk.Label(tkin4, text=eval)
        total_Label2.pack()

def click_button4():
    tkin2.destroy()
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