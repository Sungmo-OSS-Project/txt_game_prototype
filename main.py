from Player import Player, Death
from Storage import Storage

from initializeMaintenance import initializeMaintenance  # 기초 정비　/　基礎メンテナンス
from explore import explore  # 탐사 출발　/　探索出発
from event import event  # 이벤트　/　イベント
from comeback import comeback  # 쉘터 복귀　/　シェルター帰還
from maintenance import maintenance  # 정비　/　メンテナンス


def main():
    """프로그램 시작"""
    print("프로그램 시작")

    player = Player()
    days = int(0)  # 지난 날짜 수　/　経過した日数
    shelterInventory = Storage()

    try:
        initializeMaintenance(player)
        while (True):
            days += 1
            if explore(days):  # 탐험하면　/　探検したら
                while (True):
                    for _ in range(3):
                        event(player)  # 이벤트가 발생하고　/　イベントが発生して

                    if comeback(player):  # 쉘터에 복귀하면　/　シェルターに帰還したら
                        break
                maintenance(player, shelterInventory)  # 정비할 수 있음　/　メンテナンスが可能
    except Death as e:
        print(e)
    except Exception as e:
        raise e

    """프로그램 종료"""


if __name__ == "__main__":
    main()
