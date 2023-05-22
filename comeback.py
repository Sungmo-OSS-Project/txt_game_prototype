from Player import Player


def comeback(player: Player):
    """쉘터 복귀\n
    플레이어는 특정 시점마다 '쉘터 복귀' 선택지를 선택하여 쉘터로 복귀할 수 있다.
    """
    print("쉘터 복귀")

    while (True):
        inputs = input("쉘터 복귀하시겠습니까? (Y/N) >>").upper()
        if inputs == "Y":
            return True
        elif inputs == "N":
            return False
        elif inputs == "A":  # death scenario for the test
            player.setHealth(0)
            return True
