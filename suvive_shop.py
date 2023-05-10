from Events.Event import Event
from Player import Player
from item_dict import *

class event_name_here(Event):
    """
    00형 이벤트(이벤트 종류 입력)
    이벤트에 대한 설명
    """
    def __init__(self, player: Player, name: str = "", level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("당신은 여행중 자칭 생존 전문가를 만났습니다.")
        print("생존 전문가는 자신이 사용하던 아이템을 몇가지 양도한다고 합니다.")
        selection = input("당신의 선택은? >> 1. 공격한다. 2. 협박한다. 3. 거래한다. 4. 유혹한다 기타. 이벤트 건너뜀")
        
        #필요에 따라서 조건문, 반복문을 추가
        if selection == "1":
            print("자네 지금 생존 챔피언인 나를 공격한 건가? 어리석은 녀석")
            self.player.setHealth(self.player.getHealth() - 2)
        elif selection == "2":
            print("안타깝지만 네놈 따위에게 겁먹을 내가 아닐세. 다음번엔 현명하게 행동하도록")
            self.player.setHealth(self.player.getHealth() - 2)
        elif selection == "3":
            print("아 ㅋㅋ 이걸 속네 개꿀ㅋㅋ")
            print("뭐 ? 사기꾼 새끼라고?")
            print("거짓말은 했던 적이 없네. 생존 전문가란 것도 사실이고 아이템을 양도하겠단것도 사실이네")
            self.player.setHealth(self.player.getHealth() - 1)
            print("자 여기 자네의 신선한 피를 주도록 하지")
            self.player.inventory.addItem(blood)
        elif selection == "4":
            print("당신은 그에 대한 감정이 단순한 감정이 아니라는것을 깨달았습니다.")
            print("당신은 말했디 :실은 오래전부터 당신같은 남자를 기다려왔다우")
            print("사실은 나도 그래.")
            self.player.setHealth(self.player.getHealth() + 5)
            print("당신의 전우애가 충만해졌습니다.")
        else:
            print("당신은 수상한 남자의 제안을 무시하기로 결정했습니다.")

        
   
        