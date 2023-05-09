def explore(days: int):
    """탐사 출발\n
    쉘터에서 출발하며 각종 이벤트에 노출된다.
    """
    print("탐사 출발")
    
    print(f"Days : {days}")

    while(True):
        inputs = input("탐사 출발하시겠습니까? (Y/N) >>").upper()
        if inputs == "Y":
            return True
        elif inputs == "N":
            return False