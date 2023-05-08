# 상위 폴더 모듈 접근.
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath("."))

from Player import Player
from Item import Item
from Buff import Buff

class Event():
    """Event Class"""
    def __init__(self: "Event", name: str = str(), level: int = int(), description: str = str()) -> "Event":
        """Event 생성자"""
        
        self.name: str = name
        """이벤트 이름"""

        self.level: int = level
        """이벤트 레벨. 난이도"""

        self.description: str = description
        """이벤트 설명"""

class DecreaseHealthEvent(Event):
    def __init__(self: "DecreaseHealthEvent", player: Player, name: str = "체력이 감소하는 이벤트", level: int = 0, description: str = "당신은 길을 가던 중 돌부리에 발이 걸려 넘어졌습니다.") -> "DecreaseHealthEvent":
        super().__init__(name, level, description)
        self.player: Player = player
        """player는 반드시 파라미터로 받아야함."""

    def trigger(self: "DecreaseHealthEvent") -> None:
        print(self.description)
        print("체력이 1 감소합니다.")
        self.player.setHealth(self.player.getHealth() - 1)
        self.player.printHealth()

class GetKnifeEvent(Event):
    def __init__(self: "GetKnifeEvent", player: Player, name: str = "나이프(아이템) 1개 인벤토리에 추가", level: int = 0, description: str = "당신은 길에 떨어져 있는 나이프를 주웠습니다.") -> "GetKnifeEvent":
        super().__init__(name, level, description)
        self.player: Player = player
        """player는 반드시 파라미터로 받아야함."""

    def trigger(self: "GetKnifeEvent") -> None:
        print(self.description)
        
        # 인벤토리 리스트를 받아오고 나이프 아이템 객체 생성 후 인벤토리에 설정.
        inventory: list[Item] = self.player.getInventory()
        inventory.append(Item(name="나이프", weight=1))
        self.player.setInventory(inventory)
        
        self.player.printInventory()

class GetHealthMaxEvent(Event):
    """최대 체력으로 회복하는 이벤트"""
    def __init__(self: "GetHealthMaxEvent", player: Player, name: str = "최대 체력", level: int = 0, description: str = "체력 회복!") -> "GetHealthMaxEvent":
        super().__init__(name, level, description)
        self.player: Player = player
        """player는 반드시 파라미터로 받아야함."""

    def trigger(self: "GetHealthMaxEvent") -> None:
        print(self.description)
        self.player.setHealth(self.player.getHealthMax()) # 최대 체력으로 회복
        self.player.printHealth()


class InfectedByZombiesEvent(Event):
    """좀비에게 감염되는 이벤트. 독의 디버프"""
    def __init__(self: "InfectedByZombiesEvent", player: Player, name: str = "좀비에게 감염되는 이벤트", level: int = 0, description: str = "좀비에게 감염되었습니다. 독의 디버프가 생겼습니다.") -> "InfectedByZombiesEvent":
        super().__init__(name, level, description)
        self.player: Player = player
        """player는 반드시 파라미터로 받아야함."""

    def trigger(self: "InfectedByZombiesEvent") -> None:
        print(self.description)
        buffs: list[Buff] = self.player.getBuffs()
        buffs.append(Buff(name="독", level=-1))
        self.player.setBuffs(buffs)
        
        self.player.printBuffs()


if __name__ == "__main__":
    # example code
    p1 = Player()

    DecreaseHealthEvent(player=p1).trigger()
    GetKnifeEvent(player=p1).trigger()
    GetHealthMaxEvent(player=p1).trigger()
    InfectedByZombiesEvent(player=p1).trigger()