def decoName(name: str) -> None:
    """
    함수의 시작을 꾸며주는 데코레이터
    """
    for _ in range(5): print("-", end="")
    print(name, end="")
    for _ in range(5): print("-", end="")
    print()