class InventoryItem:
    def __init__(self, name, expiry_date, purchase_date, quantity):
        self.name = name
        self.expiry_date = expiry_date
        self.purchase_date = purchase_date
        self.quantity = quantity

class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_item(self, name, expiry_date, purchase_date, quantity):
        item = InventoryItem(name, expiry_date, purchase_date, quantity)
        self.inventory.append(item)
        print(f"{name}이(가) 재고에 등록되었습니다.")

    def search_item(self, name):
        for item in self.inventory:
            if item.name == name:
                print(f"재고 이름: {item.name}")
                print(f"유통기한: {item.expiry_date}")
                print(f"구입 날짜: {item.purchase_date}")
                print(f"수량: {item.quantity}")
                return
        print("해당하는 재고를 찾을 수 없습니다.")

    def delete_item(self, name):
        for item in self.inventory:
            if item.name == name:
                self.inventory.remove(item)
                print(f"{name}이(가) 재고에서 삭제되었습니다.")
                return
        print("해당하는 재고를 찾을 수 없습니다.")

    def update_item(self, name, expiry_date=None, purchase_date=None, quantity=None):
        for item in self.inventory:
            if item.name == name:
                if expiry_date:
                    item.expiry_date = expiry_date
                if purchase_date:
                    item.purchase_date = purchase_date
                if quantity:
                    item.quantity = quantity
                print(f"{name}의 정보가 업데이트 되었습니다.")
                return
        print("해당하는 재고를 찾을 수 없습니다.")

    def show_all_items(self):
        print("===== 전체 재고 목록 =====")
        for item in self.inventory:
            print(f"재고 이름: {item.name}")
            print(f"유통기한: {item.expiry_date}")
            print(f"구입 날짜: {item.purchase_date}")
            print(f"수량: {item.quantity}")
            print("=========================")

# 테스트
inventory_manager = InventoryManager()
inventory_manager.show_all_items()

inventory_manager.add_item("사과", "2024-06-30", "2024-05-01", 50)
inventory_manager.add_item("바나나", "2024-05-10", "2024-04-25", 30)

inventory_manager.show_all_items()
