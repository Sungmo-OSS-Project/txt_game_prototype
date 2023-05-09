from Player import Player, Death

from initializeMaintenance import initializeMaintenance # 기초 정비
from explore import explore # 탐사 출발
from event import event # 이벤트
from comeback import comeback # 쉘터 복귀
from maintenance import maintenance # 정비

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
                while (True):
                    for i in range(3):
                        event(player) # 이벤트가 발생하고

                    if comeback(player): # 쉘터에 복귀하면
                        break
                maintenance(player) # 정비할 수 있음
    except Death as e:
        print(e)
    except:
        raise

    """프로그램 종료"""

if __name__ == "__main__":
    main()