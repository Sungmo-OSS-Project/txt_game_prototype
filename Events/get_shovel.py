from Events.Event import Event
from Player import Player
import item_dict
import random as rd

class Get_shovel(Event):
    """
    선택지 이벤트
    삽을 얻을 수 있는 이벤트
    """

    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("당신은 좀비 한 마리를 발견했습니다.")
        print("좀비는 등에 삽을 매고 있습니다.")
        print("1. 좀비와 싸운다.")
        print("2. 길을 돌아간다.")
        selection = input("1, 2 >> ")
        if selection == "1":
            if rd.random() < 0.9:
                print("당신은 좀비를 손쉽게 쓰러뜨렸습니다.")
                print("좀비가 매고 있던 삽을 챙깁니다.")
                self.player.inventory.add_item(item_dict.shovel)
            else:
                print("좀비를 쓰러뜨리는데 성공했습니다.")
                print("하지만 싸우던 중에 좀비 등에 있는 삽이 부러졌습니다.")
                print("아쉽게도 별다른 소득은 없었습니다.")
        
        elif selection == "2":
            print("당신은 길을 조금 돌아가기로 합니다.")
        
        else:
            print("잘못된 입력입니다.")
