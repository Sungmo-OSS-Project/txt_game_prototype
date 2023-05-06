from Player import Player
from Item import Item
from Death import Death

# 버프에 관해서는 아직 구현되지 않음. 이벤트 처리 후 구현 예정.
# from Buff import Buff
# heal = Buff(name="치유", level=1)
# poison = Buff(name="독", level=-1)

from initializeMaintenance import initializeMaintenance
from explore import explore
from event import event
from comeback import comeback
from maintenance import maintenance

def main():
    """
    프로그램 시작
    """
    print("프로그램 시작")

    player = Player()

    initializeMaintenance(player)
    days = int(0) # 지난 날짜 수
    try:
        while(True):
            days += 1
            if explore(days): # 탐험하면
                event(player) # 이벤트가 발생하고

                if comeback(player): # 쉘터에 복귀하면
                    maintenance(player) # 정비할 수 있음
    except Death as e:
        print(e)
    except Exception as e:
        print("예외 발생:", e)

    print("프로그램 종료")

if __name__ == "__main__":
    main()