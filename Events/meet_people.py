from Events.Event import Event
from Player import Player
from item_dict import *

class Meet_zombie(Event):
    """
    선택지형 이벤트
    다른 생존자와 조우하여 약탈, 거래,  중 하나 결정
    
    임시 이벤트이므로 확장 예정
    """
    def __init__(self, player: Player, name: str = "", level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("당신은 길을 가다가 다른 생존자와 조우했습니다.")
        print("상대가 약해보인다면 약탈 할 수도 있으며 우회하거나 물물거래를 할 수도 있습니다.")
        
        print("1. 약탈한다.")
        print("2. 우회한다.")
        print("2. 거래를 요청한다.")
        selection = input("1, 2, 3 : ")
        if selection == "1":
            print("당신은 승리했습니다. 상대방의 가방에서 가져갈 물건을 선택하세요.") #확률적 승리는 미구현 상태이므로 임시적으로 확정 승리로 고정,
            #혹은 meet_people_win, meet_people_lose같이 두가지를 만들어서 하는 방법도 고려
            print("미구현") # 아이템창의 아이템들을 랜덤하게 2~3개 가져와서 선택할 수 있는 기능을 추가하고 싶습니다.
            
            self.player.inventory.addItem(선택한 아이템) #아이템 추가
            
        elif selection == "2":
            print("당신은 조용히 우회하여 지나갑니다.")
            print("상대 생존자도 딱히 관심이 없는듯 아무 일도 없이 지나갔습니다.")
        
        elif selection == "3":
            print("의문의 생존자 : 거래를 하자고? 내가 가지고 있는 물품을 보여주지.")
            print("미구현")# 역시 아이템창에서 랜덤하게 2~3개 가져와서 보여줄수 있는 기능이 가능한가?
            selection_Item = input("1, 2, 3 : ")
            if selection_Item == "1":