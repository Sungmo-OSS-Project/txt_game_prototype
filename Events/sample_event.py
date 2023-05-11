from Events.Event import Event
from Player import Player
from item_dict import *


class event_name_here(Event):
    """
    00형 이벤트(이벤트 종류 입력)
    이벤트에 대한 설명
    """
    def __init__(self, player: Player, name: str = "", level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("이벤트의 텍스트와 선택지를 제시.")
        # 필요에 따라서 조건문, 반복문을 추가

        # 이벤트의 진행에 따라서 구현된 기능을 사용.
        self.player.setHealth(self.player.getHealth() - 1)  # 본 구문은 체력이 1 감소하는 코드
