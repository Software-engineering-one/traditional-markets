import tkinter as tk
from tkinter import messagebox
from inventory2 import InventoryApp  # Importing InventoryApp from inventory2.py

class FoodItem:
    def __init__(self, name, inventory, explanation):
        self.name = name
        self.inventory = inventory
        self.explanation = explanation

class FoodManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("음식 관리")

        self.inventory = []

        # Labels
        self.label_name = tk.Label(root, text="음식명")
        self.label_name.grid(row=0, column=0)
        self.label_inventory = tk.Label(root, text="재료")
        self.label_inventory.grid(row=1, column=0)
        self.label_explanation = tk.Label(root, text="설명")
        self.label_explanation.grid(row=2, column=0)

        # Entry fields
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1)
        self.entry_inventory = tk.Entry(root)
        self.entry_inventory.grid(row=1, column=1)
        self.entry_explanation = tk.Entry(root)
        self.entry_explanation.grid(row=2, column=1)

        # Buttons
        self.button_add = tk.Button(root, text="음식 추가", command=self.add_item)
        self.button_add.grid(row=4, column=0, columnspan=1)
        self.button_delete = tk.Button(root, text="음식 삭제", command=self.remove_item)
        self.button_delete.grid(row=4, column=1, columnspan=2)
        self.button_show_all = tk.Button(root, text="음식 목록", command=self.show_all_items)
        self.button_show_all.grid(row=4, column=3, columnspan=4)

        # Store original widgets to restore later
        self.original_widgets = [
            self.label_name, self.label_inventory, self.label_explanation,
            self.entry_name, self.entry_inventory, self.entry_explanation,
            self.button_add, self.button_delete, self.button_show_all
        ]

    def add_item(self):
        name = self.entry_name.get()
        inventory = self.entry_inventory.get()
        explanation = self.entry_explanation.get()

        item = FoodItem(name, inventory, explanation)
        self.inventory.append(item)

        # Optionally, you can display a message box or update a status label here
        print(f"{name} added to food.")

    def remove_item(self):
        name = self.entry_name.get()

        for item in self.inventory:
            if item.name == name:
                self.inventory.remove(item)
                break

        # Optionally, you can display a message box or update a status label here
        print(f"{name} deleted from food.")

    def show_all_items(self):
        # Hide all original widgets
        self.hide_original_widgets()

        # Display all items
        for idx, item in enumerate(self.inventory):
            tk.Label(self.root, text=f"음식명 {idx + 1}: {item.name}, 재료: {item.inventory}, 설명: {item.explanation}").grid(row=idx + 6, column=0, columnspan=2)

        # Add a back button to return to the main menu
        tk.Button(self.root, text="돌아가기", command=self.show_main_menu).grid(row=len(self.inventory) + 6, column=0, columnspan=2)

    def hide_original_widgets(self):
        # Hide the original widgets
        for widget in self.original_widgets:
            widget.grid_remove()

    def show_main_menu(self):
        # Clear the display area
        self.clear_display()

        # Show the original widgets
        for widget in self.original_widgets:
            widget.grid()

    def clear_display(self):
        # Clear only the widgets added by show_all_items
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) >= 6:
                widget.grid_forget()

def show_main_screen():
    # Remove existing widgets
    for widget in tkin.winfo_children():
        widget.destroy()

    mainlabel = tk.Label(tkin, text="소비자 또는 소상공인 유무를 확인하세요")
    mainlabel.pack()

    button1 = tk.Button(tkin, text="1. 소비자", command=click_button1)
    button1.pack()

    button2 = tk.Button(tkin, text="2. 소상공인", command=click_button2)
    button2.pack()

def click_button1():
    # Remove existing widgets
    for widget in tkin.winfo_children():
        widget.destroy()

    sublabel = tk.Label(tkin, text="1. 별점 및 평가 입력 2. 별점 및 평가 조회")
    sublabel.pack()

    button3 = tk.Button(tkin, text="1. 별점 및 평가 입력", command=click_button3)
    button3.pack()

    button4 = tk.Button(tkin, text="2. 별점 및 평가 조회", command=click_button4)
    button4.pack()

    back_button = tk.Button(tkin, text="뒤로가기", command=show_main_screen)
    back_button.pack()

def click_button2():
    # Remove existing widgets
    for widget in tkin.winfo_children():
        widget.destroy()

    sublabel2 = tk.Label(tkin, text="작업을 선택하세요")
    sublabel2.pack()

    inventory_button = tk.Button(tkin, text="재고관리", command=execute_inventory)
    inventory_button.pack()

    food_button = tk.Button(tkin, text="음식관리", command=execute_food)
    food_button.pack()

    eval_button = tk.Button(tkin, text="평가관리", command=notice)
    eval_button.pack()

    back_button = tk.Button(tkin, text="뒤로가기", command=show_main_screen)
    back_button.pack()

def execute_inventory():
    global inventory_window
    inventory_window = tk.Toplevel(tkin)
    inventory_window.protocol("WM_DELETE_WINDOW", on_inventory_window_close)  # Define close behavior
    app1 = InventoryApp(inventory_window)

def execute_food():
    global food_window
    food_window = tk.Toplevel(tkin)
    food_window.protocol("WM_DELETE_WINDOW", on_food_window_close)  # Define close behavior
    app2 = FoodManagerApp(food_window)

def notice():
    for widget in tkin.winfo_children():
        widget.destroy()
    for star, eval in rate.items():
        total_Label = tk.Label(tkin, text=f"{star}: {eval}")
        total_Label.pack()

    back_button = tk.Button(tkin, text="뒤로가기", command=click_button2)
    back_button.pack()


def click_button3():
    # Remove existing widgets
    for widget in tkin.winfo_children():
        widget.destroy()

    consumer_Label = tk.Label(tkin, text="별점 및 평가를 입력하세요")
    consumer_Label.pack()
    consumer_label2 = tk.Label(tkin, text="별점(1.0 ~ 5.0):")
    consumer_label2.pack()
    consumer_entry = tk.Entry(tkin)
    consumer_entry.pack()
    consumer_label3 = tk.Label(tkin, text="평가:")
    consumer_label3.pack()
    consumer_entry2 = tk.Entry(tkin)
    consumer_entry2.pack()
    starandevalcheck = tk.Button(tkin, text="별점 및 평가 입력 완료", command=lambda: starandeval(consumer_entry.get(), consumer_entry2.get()))
    starandevalcheck.pack()

    back_button = tk.Button(tkin, text="뒤로가기", command=click_button1)
    back_button.pack()

def starandeval(star, eval):
    global rate
    rate[star] = eval
    click_button1()

def click_button4():
    # Remove existing widgets
    for widget in tkin.winfo_children():
        widget.destroy()

    for star, eval in rate.items():
        total_Label = tk.Label(tkin, text=f"{star}: {eval}")
        total_Label.pack()

    back_button = tk.Button(tkin, text="뒤로가기", command=click_button1)
    back_button.pack()

def on_inventory_window_close():
    inventory_window.destroy()
    show_main_screen()

def on_food_window_close():
    food_window.destroy()
    show_main_screen()

tkin = tk.Tk()
tkin.title("운영관리")
rate = {}
inventory_window = None
food_window = None

show_main_screen()

tkin.mainloop()
