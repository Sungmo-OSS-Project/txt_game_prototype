from Events.Event import Event
from Player import Player
import item_dict


class Open_chest(f)(Event):
    """
    선택지형 이벤트(이벤트 종류 입력)
    잠겨있는 상자를 발견함. 
    쇠지렛대로 상자를 열 수 있음.
    (꽝 상자를 표현)
    """
    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        
        print("당신은 길에 버려진 금고를 발견했습니다.")
        print("1. 그냥 두고 지나간다")
        select = int()
        if self.player.inventory.has_item(item_dict.crowbar):
            print("2. 금고를 연다.")
            select = input("1, 2 >>")
        else:
            select = input("1 >>")
        
        if select == 1:
            print("당신은 아쉬움을 뒤로하고 가던 길을 갑니다.")
        
        elif select == 2:
            print("당신은 쇠지렛대로 금고를 열었습니다.")
            print("#################################")
            print("         !!!!!!펑!!!!!!!         ")
            print("#################################")
            print("누군가 장난을 쳐놓은 상자가 폭발하는듯한 소리를 내며 검은 연기가 피어오릅니다.")
            print("데미지를 입습니다 : -1)
        
        # 필요에 따라서 조건문, 반복문을 추가

        # 이벤트의 진행에 따라서 구현된 기능을 사용.

        # 본 구문은 체력이 1 감소하는 코드
        self.player.setHealth(self.player.getHealth() - 1)
