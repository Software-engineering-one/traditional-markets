import tkinter as tk

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
        self.button_delete = tk.Button(root, text = "음식 삭제", command = self.remove_item)
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

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodManagerApp(root)
    root.mainloop()
