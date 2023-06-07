from Events.Event import Event
from Player import Player


class Legend_of_the_protein(Event):
    """
    단발성 이벤트
    당신은 최강이 될수 있다는 전설의 프로틴에 대한 소문을 듣고 그것을 찾아나섭니다.
    참고로 최강 프로틴은 실재하지 않는 제품입니다
    """
    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("당신은 길을 가다 전설의 프로틴에 대한 소문을 듣고 찾아 나섭니다.")
        print("당신은 전설의 프로틴이 잠들어 있다는 동굴로 왔지만 그곳은 전설의 프로틴좀비가 지키는 위험한 장소였습니다.")
        print("좀비는 생전의 본능으로 노래를 흥얼거리고 있었습니다.")
        print("최강! 최강! 최강 프로틴이 최강인점 3가지!")
        print("1! 최강의 가성비! 2! 최강의 단백질량! 3. 최강의 다이어트 효율! ")
        print("최강 프로틴 지금 대박 할인중! 지금 당장 구매하세요!")
        print("(해당 제품은 존재하지 않는 제품입니다.)")
        print("당신은 스쿼트를 하며 지폐를 들고 다가갑니다.")
        print("구매 감사합니다.")
        print("당신은 아이템 '프로틴'을 얻었다")
        # 프로틴 - 아이템 : 전투 스킵용
