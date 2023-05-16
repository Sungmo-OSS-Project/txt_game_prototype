from Events.Event import Event
from Player import Player
from item_dict import *

class Fall_by_rock(Event):
    """
    단발성 이벤트
    다른 생존자가 설치한 덫에 걸려 hp를 감소합니다.
    """
    def __init__(self, player: Player, name: str = "", level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("당신은 길을 가다 다른 생존자가 설치한 덫에 걸렸습니다.\n체력이 2 감소합니다.")
        self.player.setHealth(self.player.getHealth() - 2)
        self.player.printHealth()