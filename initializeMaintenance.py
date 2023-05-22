from Player import Player
from item_dict import knife, tomato_can, water_bottle, flashLight, medikit


def initializeMaintenance(player: Player):
    """기초 정비\n
    쉘터 출발 이전에 아이템을 소지할 수 있다.
    """
    print("기초 정비")

    # 체력 표시
    player.printHealth()

    # 기본 아이템 제공
    player.inventory.addItem(knife)
    player.inventory.addItem(tomato_can)
    player.inventory.addItem(water_bottle)
    player.inventory.addItem(flashLight)
    player.inventory.addItem(medikit)

    # 인벤토리 목록 출력
    player.inventory.printStorage()
    print("을 가지고 쉘터로 이동합니다.")
