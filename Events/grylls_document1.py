from Events.Event import Event
from Player import Player


class Rainy_day(Event):
    """
    단발성 이벤트
    문서를 발견하는 이스터에그성 이벤트
    """

    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("문서를 발견했습니다.")
        print("하지만 맛이 중요한가요, 무조건 열량만 있으면 돼요.")
