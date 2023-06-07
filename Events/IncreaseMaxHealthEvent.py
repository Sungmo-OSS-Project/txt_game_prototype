from Events.Event import Event
from Player import Player
# import item_dict


class IncreaseMaxHealthEvent(Event):
    """
    물약이 있으면 최대체력이 늘어나는 이벤트
    """
    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        if self.player.inventory.has_item_name("물약"):
            print("물약이 있습니다. 마시겠습니까?")
            if self.마실까요_조건검사():
                print("최대 체력이 5만큼 증가했습니다.")
                self.player.set_health_max(self.player.get_health_max() + 5)
            else:
                print("변화가 없습니다.")

    def 마실까요_조건검사(self) -> bool:
        while True:
            inputs = input("물약을 마시겠습니까? (Y/N) >>").upper()
            if inputs == "Y":
                return True
            elif inputs == "N":
                return False
