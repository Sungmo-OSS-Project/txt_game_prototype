from decoName import decoName
from Item import Item
from Player import Player

def event(player: Player):
    """이벤트\n
    물자 획득 이벤트, 물자 손실 이벤트, 체력 증감 이벤트, 상태 추가 및 제거 이벤트, 
    물자 교환 이벤트, 전투 이벤트 등의 각종 이벤트가 발생한다.
    """
    decoName("이벤트")

    print("어떤 이벤트가 발생하여 무언가를 선택했습니다!") # EVENT
    
    items: list[Item] = [Item(name="물병 500ml", weight=2)\
                        ,Item(name="물병 500ml", weight=2)\
                        ,Item(name="통조림", weight=1)]
    for i in items:
        print(i.getName() + "아이템을 획득하였습니다.")
        player.inventory.append(i)
    
    player.printInventory()