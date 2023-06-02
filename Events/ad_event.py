from Events.Event import Event
from Player import Player
# import item_dict 아이템 사전이 필요시 주석 해제


class ad_evet(Event):
    """
    광고형 이벤트
    광고가 나오는 이벤트이다
    """
    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player

    def trigger(self) -> None:
        print("광고지를 발견했습니다.")
        print("txt_game하러 바로 가기 바로가기 클릭 ↓")
        print("바로가기")
