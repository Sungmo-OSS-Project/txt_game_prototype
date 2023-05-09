from Player import Player
from Item import Item
from item_dict import *

def initializeMaintenance(player: Player):
    """기초 정비\n
    쉘터 출발 이전에 아이템을 소지할 수 있다.
    """
    print("기초 정비")

    player.printHealth()

    # 쉘터 출발 이전에 아이템을 소지할 수 있다는 것을 알리는 메시지 출력
    print("쉘터 출발 이전에 아이템을 소지할 수 있습니다.")

    # 가져갈 수 있는 아이템 목록 리스트
    takableItemsList: list[Item] = list()  # 빈 리스트 생성
    takableItemsList.append(knife)
    takableItemsList.append(food)
    takableItemsList.append(water_bottle)
    takableItemsList.append(flashLight)
    takableItemsList.append(medikit)
    
    # 아이템 목록 출력
    print("소지 가능한 아이템 목록:")
    for i, item in enumerate(takableItemsList):
        print(f"{i+1}. {item.getName()}(무게:{item.getWeight()})")

    # 여러개 번호를 선택해서 인벤토리 list에 넣기
    try:
        selected_items = input("인벤토리에 추가할 아이템 번호를 선택하세요 (숫자를 띄어쓰기로 구분): ")
        selected_items = selected_items.split()  # 입력받은 문자열을 공백을 기준으로 분리하여 리스트로 변환

        for i in selected_items:
            player.inventory.addItem(takableItemsList[int(i)-1])  # 선택한 번호에 해당하는 아이템을 인벤토리 리스트에 추가
    except IndexError:
        pass

    # 인벤토리 목록 출력
    player.inventory.printStorage()
    print("을 가지고 쉘터로 이동합니다.")