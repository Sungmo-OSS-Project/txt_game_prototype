from Events.Event import Event
from Player import Player
import item_dict


class Open_chest(Event):
    """
    선택지형 이벤트(이벤트 종류 입력)
    잠겨있는 상자를 발견함.
    쇠지렛대로 상자를 열 수 있음
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

        #선택지에 따른 이벤트 진행
        if select == "1":
            print("당신은 아쉬움을 뒤로하고 가던 길을 갑니다.")

        elif select == "2":
            print("당신은 쇠지렛대로 금고를 열었습니다.")
            print("금고 안에는 토마토 통조림 두 개가 들어있었습니다.")
            self.player.inventory.add_item(item_dict.tomato_can)
            self.player.inventory.add_item(item_dict.tomato_can)
