from Events.Event import Event
from Player import Player
import item_dict
from Item import Item


class Rainy_day(Event):
    """
    단발성 이벤트
    비가 내려서 가방의 무게가 증가
    """

    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("비가 오기 시작했습니다.")
        all_items = self.player.inventory.get_item()
        items_weight = 0
        rain_amount = 0.2
        for item in all_items:
            items_weight += item.get_weight()
        self.player.inventory.add_item(
            Item(category="상태이상", name="젖은무게", weight=int(items_weight*rain_amount)))
