from Player import Player
import Events.ad_event
import Events.cast_away
import Events.DropKnife
import Events.fall_by_rock
import Events.get_medikit
import Events.grylls_document1
import Events.grylls_document2
import Events.meet_people
import Events.meet_zombie
import Events.open_chest
import Events.rainy_day
import random

이벤트목록 = [
    Events.ad_event.ad_evet,
    Events.cast_away.Rainy_day,
    Events.DropKnife.DropKnife,
    Events.fall_by_rock.Fall_by_rock,
    Events.get_medikit.event_name_here,
    Events.grylls_document1.Rainy_day,
    Events.grylls_document2.Rainy_day,
    Events.meet_people.Meet_people,
    Events.meet_zombie.Meet_zombie,
    Events.open_chest.Open_chest,
    Events.rainy_day.Rainy_day
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
