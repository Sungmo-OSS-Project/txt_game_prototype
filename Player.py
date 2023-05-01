class Player:
    def __init__(self):
        """Player 생성"""

        self.health: int = 20
        """체력\n
        기본(시작) 값은 20으로 고정.\n
        체력이 0이 되는 경우 플레이어는 사망하며, 게임 오버.\n
        체력은 최대 체력 이상으로 상승할 수 없음\n
        특정 이벤트를 통하여 체력에 증감이 있을 수 있음.
        """

        self.health_max: int = 20
        """최대 체력\n
        특정 이벤트를 통하여 최대 체력에 증감이 있을 수 있음."""

        self.buffs: dict = {}
        """각종 긍정적/부정적 상태. ("상태 명": 레벨)의 형태\n
        긍정적 상태(+) :
        각종 이벤트의 선택지(분기)에서 특정 상태가 존재할 경우 선택할 수 있는 분기가 활성화 또는 추가됨.\n
        부정적 상태(-) :
        지속적인 체력 감소, 특정 행동의 제약 등을 유발하는 기능.
        """

        self.items: list = []
        """
        소지 아이템\n
        긍정적 상태처럼 특정 선택지를 선택할 수 있다.
        하지만 아이템 중 일회성 아이템의 경우, 해당 아이템 사용 시 소멸한다.
        """

        self.weight: int = 0
        """무게\n
        아이템마다 무게가 다르며, 플레이어가 한 번에 소지할 수 있는 아이템 수량에 제한을 두는 기능이다.
        """

        self.weight_max: int = 20
        """최대 무게 제한\n
        플레이어는 시작 시 최대무게(weight_max)가 설정된다.
        특정 이벤트를 통하여 최대 무게를 늘릴 수 있다.
        """


    def getHealth(self) -> int:
        """
        체력 값을 반환
        """
        return self.health

    def setHealth(self, health: int) -> int:
        """
        체력 값을 설정
        """
        if health >= 0 and health <= self.health_max:
        self.health = health
        return self.health
        else:
            return "Out of Range"


    def getHealthMax(self) -> int:
        """
        최대 체력 값을 반환
        """
        return self.health_max

    def setHealthMax(self, max: int) -> int:
        """
        최대 체력 값을 설정
        """
        self.health_max = max
        return self.health_max


    def getBuffs(self) -> dict:
        """
        버프 상태를 ("상태 명": 레벨) 형태의 dict로 반환
        """
        return self.buffs

    def setBuffs(self, buffs: dict) -> dict:
        """
        버프 상태를 ("상태 명": 레벨) 형태의 dict로 설정
        """
        self.buffs = buffs
        return self.buffs


    def getItems(self) -> list:
        """
        아이템 반환
        """
        return self.items

    def setItems(self, items: list) -> list:
        """
        아이템 설정
        """
        self.items = items
        return self.items

    
    def getWeight(self) -> int:
        """
        무게 값 반환
        """
        return self.weight

    def setWeight(self, weight: int) -> int:
        """
        무게 값 설정
        """
        if weight >= 0 and weight <= self.weight_max:
        self.weight = weight
        return self.weight
        else:
            return "Out of Range"


    def getWeightMax(self) -> int:
        """
        최대 무게 값 반환
        """
        return self.weight_max

    def setWeightMax(self, max) -> int:
        """
        최대 무게 값 설정
        """
        self.weight_max = max
        return self.weight_max


if __name__ == "__main__":
    p1 = Player()
    p1.setHealth(100)
    print("p1의 체력 값은", p1.getHealth(), "입니다.")