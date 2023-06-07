from Events.Event import Event
from Player import Player


class Zumba_dance_with_zombie(Event):
    """
    단발성 이벤트
    좀비와 함께 줌바 춤을 (늑대와 함께 춤을 패러디)
    """
    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("당신은 원시부족들을 만나 생존의 비결을 듣기로 합니다.")
        print("부족장의 이름은 '좀비와 줌바춤을'입니다. 특이한 이름이네요.")
        print("그들에게 생존 비결을 듣고 나니 시간이 늦은것 같습니다.")
        print("오늘은 늦었으니까 자고 가게. 덤으로 축제도 보고 가게")
        print("원시부족들은 갑자기 힙한 옷을 입으며 줌바댄스를 추기 시작합니다.")
        print("분위기에 휩쓸린 당신은 같이 줌바댄스를 춥니다.")
        print("소리에 이끌려온 좀비들도 분위기에 휩쓸려 줌바댄스를 춥니다.")
        print("당신은 생존에 관련한 지식을 얻었고, 마음이 가벼워졌습니다")
