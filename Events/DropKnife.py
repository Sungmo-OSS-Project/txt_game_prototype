from Events.Event import Event
from Player import Player
import item_dict


class DropKnife(Event):
    """
    나이프의 내구도가 떨어져서 소지하던 나이프를 버리는 이벤트입니다.
    """
    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        if self.player.inventory.has_item(item_dict.knife):
            print("나이프의 내구도가 떨어져서 버립니다.")
            self.player.inventory.remove_item(item_dict.knife)
