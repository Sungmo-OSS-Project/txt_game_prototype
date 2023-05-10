from Events.Event import Event
from Player import Player
from item_dict import *


class gihoSampleEevent(Event):
    """
    단발성 이벤트
    휴식을 취합니다. 체력을 2 회복합니다
    """
    def __init__(self, player: Player, name: str = "", level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("휴식을 취합니다. 체력을 2 회복합니다")
        self.player.setHealth(self.player.getHealth() + 2)
        self.player.printHealth()