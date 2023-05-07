from Player import Player, Death

from initializeMaintenance import initializeMaintenance
from explore import explore
from event import event
from comeback import comeback
from maintenance import maintenance

def main():
    """프로그램 시작"""
    print("프로그램 시작")

    player = Player()
    days = int(0) # 지난 날짜 수

    try:
        initializeMaintenance(player)
        while(True):
            days += 1
            if explore(days): # 탐험하면
                event(player) # 이벤트가 발생하고

                if comeback(player): # 쉘터에 복귀하면
                    maintenance(player) # 정비할 수 있음
    except Death as e:
        print(e)
    except:
        raise

    print("프로그램 종료")

if __name__ == "__main__":
    main()