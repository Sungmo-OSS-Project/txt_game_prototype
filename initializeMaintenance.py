from decoName import decoName
from Player import Player
from Item import Item

def initializeMaintenance(player: Player):
    """기초 정비\n
    쉘터 출발 이전에 아이템을 소지할 수 있다.
    """
    decoName("기초 정비")

    player.printHealth()

    # 쉘터 출발 이전에 아이템을 소지할 수 있다는 것을 알리는 메시지 출력
    print("쉘터 출발 이전에 아이템을 소지할 수 있습니다.")

    # 가져갈 수 있는 아이템 목록 리스트
    takableItemsList: list[Item] = list()  # 빈 리스트 생성
    takableItemsList.append(Item(name="나이프", weight=1))
    takableItemsList.append(Item(name="식량", weight=2))
    takableItemsList.append(Item(name="물병 500ml", weight=2))
    takableItemsList.append(Item(name="손전등", weight=1))
    takableItemsList.append(Item(name="의약품", weight=2))
    takableItemsList.append(Item(name="등산화", weight=3))
    takableItemsList.append(Item(name="라이터", weight=1))
    takableItemsList.append(Item(name="지도", weight=1))
    takableItemsList.append(Item(name="전지", weight=2))
    takableItemsList.append(Item(name="카메라", weight=2))
    takableItemsList.append(Item(name="충전기", weight=1))

    # 아이템 목록 출력
    print("소지 가능한 아이템 목록:")
    for i, item in enumerate(takableItemsList):
        print(f"{i+1}. {item.getName()}(무게:{item.getWeight()})")

    # 인벤토리 리스트 생성
    inventory: list[Item] = list()

    # 여러개 번호를 선택해서 인벤토리 list에 넣기
    try:
        selected_items = input("인벤토리에 추가할 아이템 번호를 선택하세요 (숫자를 띄어쓰기로 구분): ")
        selected_items = selected_items.split()  # 입력받은 문자열을 공백을 기준으로 분리하여 리스트로 변환

        for i in selected_items:
            inventory.append(takableItemsList[int(i)-1])  # 선택한 번호에 해당하는 아이템을 인벤토리 리스트에 추가
    except IndexError:
        pass

    player.setInventory(inventory)

    # 인벤토리 목록 출력
    player.printInventory()
    
    print("을 가지고 쉘터로 이동합니다.")