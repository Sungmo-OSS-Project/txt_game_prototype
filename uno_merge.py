def injureEvent():
    """이벤트\n
    물자 획득 이벤트, 물자 손실 이벤트, 체력 증감 이벤트, 상태 추가 및 제거 이벤트, 
    물자 교환 이벤트, 전투 이벤트 등의 각종 이벤트가 발생한다.
    """
    decoName("타박상 이벤트")

    print("돌뿌리에 걸려 넘어졌습니다.")  # EVENT

    player.health -= 3
    player.printHealth()