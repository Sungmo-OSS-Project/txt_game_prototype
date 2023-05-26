from Player import Player
from Events.fall_by_rock import Fall_by_rock
from Events.meet_zombie import Meet_zombie
import random

이벤트목록 = [
    Fall_by_rock,
    Meet_zombie,
]
"""이벤트 클래스들이 list형으로 담겨져 있음"""


def event(player: Player):
    """이벤트\n
    물자 획득 이벤트, 물자 손실 이벤트, 체력 증감 이벤트, 상태 추가 및 제거 이벤트,\n
    물자 교환 이벤트, 전투 이벤트 등의 각종 이벤트가 발생한다.
    """
    print("이벤트")

    # 이벤트목록 중에 랜덤으로 이벤트 하나 뽑아서 실행한다.
    발생할이벤트 = random.choice(이벤트목록)
    발생할이벤트(player=player).trigger()
