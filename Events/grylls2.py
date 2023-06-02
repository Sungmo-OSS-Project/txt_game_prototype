from Events.Event import Event
from Player import Player


class Rainy_day(Event):

    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("문서를 발견했습니다.")
        print("언제나 10%를 애쓰면 100% 더 편해질 수 있죠.")
