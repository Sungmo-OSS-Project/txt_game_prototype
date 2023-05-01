def initializeMaintainance():
    """기초 정비\n
    쉘터 출발 이전에 아이템을 소지할 수 있다.
    """
    for _ in range(5): print("-", end="")
    print("기초 정비", end="")
    for _ in range(5): print("-", end="")
    print()

def explore():
    """탐사 출발\n
    쉘터에서 출발하며 각종 이벤트에 노출된다.
    """
    for _ in range(5): print("-", end="")
    print("탐사 출발", end="")
    for _ in range(5): print("-", end="")
    print()


def event():
    """이벤트\n
    물자 획득 이벤트, 물자 손실 이벤트, 체력 증감 이벤트, 상태 추가 및 제거 이벤트, 
    물자 교환 이벤트, 전투 이벤트 등의 각종 이벤트가 발생한다.
    """
    for _ in range(5): print("-", end="")
    print("이벤트", end="")
    for _ in range(5): print("-", end="")
    print()

def comeback():
    """쉘터 복귀\n
    플레이어는 특정 시점마다 '쉘터 복귀' 선택지를 선택하여 쉘터로 복귀할 수 있다.
    """
    for _ in range(5): print("-", end="")
    print("쉘터 복귀", end="")
    for _ in range(5): print("-", end="")
    print()

def maintainance():
    """정비\n
    체력이 최대치까지 회복되며, 자신이 소지한 아이템을 저장, 판매, 폐기할 수 있다.\n
    플레이어가 모든 정비를 마친 경우 다시 '탐사 출발'을 선택하여 2 ~ 5의 과정을 반복한다.
    """
    for _ in range(5): print("-", end="")
    print("정비", end="")
    for _ in range(5): print("-", end="")
    print()

def main():
    """
    프로그램 시작
    """
    print("프로그램 시작")
    
    initializeMaintainance()

    explore()

    event()

    comeback()

    maintainance()

    print("프로그램 종료")
    ## 프로그램 종료

if __name__ == "__main__":
    main()