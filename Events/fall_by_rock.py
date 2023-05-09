from Events.Event import Event
from Player import Player
class Fall_by_rock(Event):
    """
    단발성 이벤트
    돌에 발이 걸려 넘어지며, 체력 감소
    """
    def __init__(self, player: Player, name: str = "", level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("당신은 길을 가다 돌부리에 발이 걸려 넘어졌습니다.\n체력이 1 감소합니다.")
        self.player.setHealth(self.player.getHealth() - 1)
        self.player.printHealth()