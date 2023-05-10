from Events.Event import Event
from Player import Player
from item_dict import *

class Fall_by_rock(Event):
    """
    지속성 이벤트
    허기짐에 따라 해결하지 못할시 지속적으로 체력 감소
    """
    def __init__(self, player: Player, name: str = "", level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None: