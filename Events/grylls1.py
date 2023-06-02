from Events.Event import Event
from Player import Player


class Rainy_day(Event):
    """
    선택지형 이벤트
    좀비와 조우하여 전투, 우회 중 하나 결정
    임시 이벤트이므로 확장 예정
    """

    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("문서를 발견했습니다.")
        print("하지만 맛이 중요한가요, 무조건 열량만 있으면 돼요.")
