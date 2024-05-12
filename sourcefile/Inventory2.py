class InventoryItem:
    def __init__(self, name, quantity, expiry_date):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date

class Inventory:
    def __init__(self):
        self.inventory = []

    def add_item(self, name, quantity, expiry_date):
        item = InventoryItem(name, quantity, expiry_date)
        self.inventory.append(item)
        print(f"{name}이(가) 재고에 등록되었습니다.")

    def remove_item(self, name, quantity):
        for item in self.inventory:
            if item.name == name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    if item.quantity == 0:
                        self.inventory.remove(item)
                        print(f"{name}의 재고가 모두 소진되어 재고 목록에서 제거되었습니다.")
                    else:
                        print(f"{name}의 재고가 {quantity}개 감소되었습니다.")
                    break
                else:
                    print("재고가 부족합니다.")
                    break
        else:
            print("해당 제품이 재고 목록에 없습니다.")

    def display_inventory(self):
        print("현재 재고:")
        for item in self.inventory:
            print(f"제품명: {item.name}, 수량: {item.quantity}, 유통기한: {item.expiry_date}")

def main():
    inventory = Inventory()

    while True:
        print("\n1. 제품 추가")
        print("2. 제품 제거")
        print("3. 재고 확인")
        print("4. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            name = input("제품 이름을 입력하세요: ")
            quantity = int(input("수량을 입력하세요: "))
            inventory.add_item(name, quantity)
        elif choice == '2':
            name = input("제품 이름을 입력하세요: ")
            quantity = int(input("제거할 수량을 입력하세요: "))
            inventory.remove_item(name, quantity)
        elif choice == '3':
            inventory.display_inventory()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()
