class Death(Exception):  # Death 클래스를 정의합니다. Exception 클래스를 상속받습니다.
    def __init__(self: "Death") -> "Death":  # 생성자 메소드를 정의합니다.
        # 부모 클래스의 생성자 메소드를 호출하며, 메시지를 전달합니다.
        super().__init__("당신은 쉘터에 복귀하지 못하고 사망하였습니다.")