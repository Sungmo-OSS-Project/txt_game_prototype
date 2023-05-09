from Player import Player
from Events.Event import *
import random

def event(player: Player):
    """이벤트\n
    물자 획득 이벤트, 물자 손실 이벤트, 체력 증감 이벤트, 상태 추가 및 제거 이벤트, 
    물자 교환 이벤트, 전투 이벤트 등의 각종 이벤트가 발생한다.
    """
    print("이벤트")
    # 이벤트 목록을 가져온다.
    이벤트목록: list[Event] =   [DecreaseHealthEvent(player=player),
                                GetKnifeEvent(player=player),
                                GetHealthMaxEvent(player=player),
                                InfectedByZombiesEvent(player=player),
                                InjureEvent(player=player),
                                Get물병2병과통조림Event(player=player)]

    # 그 중에 랜덤으로 이벤트 하나 뽑아서 실행한다.
    random.choice(이벤트목록).trigger()