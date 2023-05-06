# 상위 폴더 모듈 접근.
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath("."))

from Player import Player
from Item import Item

class Event():
    def __init__(self: "Event", name: str = "이벤트 이름", level: int = 0, description: str = "") -> "Event":
        """Event 생성자"""
        
        self.name: str = name
        """이벤트 이름"""

        self.level: int = level
        """이벤트 레벨. 난이도"""

        self.description: str = description
        """이벤트 설명"""

class DecreaseHealthEvent(Event):
    def __init__(self: "Event", name: str = "체력이 감소하는 이벤트", level: int = 0, description: str = "당신은 길을 가던 중 돌부리에 발이 걸려 넘어졌습니다.", player: Player = Player()) -> "Event":
        super().__init__(name, level, description)
        self.player: Player = player

    def trigger(self):
        print(self.description)
        print("체력이 1 감소합니다.")
        self.player.setHealth(self.player.getHealth() - 1)
        self.player.printHealth()

class GetKnifeEvent(Event):
    def __init__(self: "Event", name: str = "나이프(아이템) 1개 인벤토리에 추가", level: int = 0, description: str = "당신은 길에 떨어져 있는 나이프를 주웠습니다.", player: Player = Player()) -> "Event":
        super().__init__(name, level, description)
        self.player: Player = player

    def trigger(self):
        print(self.description)
        
        # 인벤토리 리스트를 받아오고 나이프 아이템 객체 생성 후 인벤토리에 설정.
        inventory: list[Item] = self.player.getInventory()
        inventory.append(Item(name="나이프", weight=1))
        self.player.setInventory(inventory)
        
        self.player.printInventory()

if __name__ == "__main__":
    DecreaseHealthEvent().trigger()
    GetKnifeEvent().trigger()