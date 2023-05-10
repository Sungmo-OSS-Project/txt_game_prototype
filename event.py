from Player import Player
from Events.Event import *
import random

#추후에 이벤트가 여러개가 될 경우 Events 폴더에서 이벤트를 가져오도록 할 예정
from Events.fall_by_rock import Fall_by_rock 
from Events.meet_zombie import Meet_zombie
from Events.first import first
from Events.gihoSampleEvent import gihoSampleEevent

def event(player: Player):
    """이벤트\n
    물자 획득 이벤트, 물자 손실 이벤트, 체력 증감 이벤트, 상태 추가 및 제거 이벤트, 
    물자 교환 이벤트, 전투 이벤트 등의 각종 이벤트가 발생한다.
    """
    print("이벤트")
    # 이벤트 목록을 가져온다. 추후 Events 폴더에서 이벤트를 가져오도록 할 예정
    이벤트목록: list[Event] =   [Fall_by_rock(player),
                                Meet_zombie(player),
                                first(player),
                                gihoSampleEvent(player)]

    # 그 중에 랜덤으로 이벤트 하나 뽑아서 실행한다.
    random.choice(이벤트목록).trigger()