from Item import Item
from Buff import Buff
from decoName import decoName

class Player:
    """Player Class"""
    def __init__(self: "Player") -> "Player":
        """Player 생성"""

        self.health: int = int(20)
        """체력\n
        기본(시작) 값은 20으로 고정.\n
        체력이 0이 되는 경우 플레이어는 사망하며, 게임 오버.\n
        체력은 최대 체력 이상으로 상승할 수 없음\n
        특정 이벤트를 통하여 체력에 증감이 있을 수 있음.
        """

        self.health_max: int = int(20)
        """최대 체력\n
        특정 이벤트를 통하여 최대 체력에 증감이 있을 수 있음."""

        self.buffs: list[Buff] = list()
        """각종 긍정적/부정적 상태\n
        긍정적 상태(+) :
        각종 이벤트의 선택지(분기)에서 특정 상태가 존재할 경우 선택할 수 있는 분기가 활성화 또는 추가됨.\n
        부정적 상태(-) :
        지속적인 체력 감소, 특정 행동의 제약 등을 유발하는 기능.
        """

        self.inventory: list[Item] = list()
        """인벤토리\n
        긍정적 상태처럼 특정 선택지를 선택할 수 있다.
        하지만 아이템 중 일회성 아이템의 경우, 해당 아이템 사용 시 소멸한다.
        """

        self.weight: int = int(0)
        """무게\n
        아이템마다 무게가 다르며, 플레이어가 한 번에 소지할 수 있는 아이템 수량에 제한을 두는 기능이다.
        """

        self.weight_max: int = int(20)
        """최대 무게 제한\n
        플레이어는 시작 시 최대무게(weight_max)가 설정된다.
        특정 이벤트를 통하여 최대 무게를 늘릴 수 있다.
        """


    def getHealth(self: "Player") -> int:
        """
        체력 값을 반환
        """
        return self.health

    def setHealth(self: "Player", health: int) -> "Player":
        """
        체력 값을 설정
        """
        if health <= 0:
            self.health = 0
        elif health >= self.health_max:
            self.health = self.health_max
        return self

    def printHealth(self: "Player") -> None:
        """체력 값을 출력"""
        print(f"체력: {self.health}/{self.health_max}")
        for i in range(self.health_max):
            if i < self.health:
                print("■", end="")
            else:
                print("□", end="")
        print()
        return None
        
    def getIsDied(self: "Player") -> bool:
        """죽었는가 반환"""
        if self.health <= 0: # 체력이 0보다 작거나 같아지면 True
            return True
        else:
            return False


    def getHealthMax(self: "Player") -> int:
        """최대 체력 값을 반환"""
        return self.health_max

    def setHealthMax(self: "Player", max: int) -> "Player":
        """최대 체력 값을 설정"""
        self.health_max = max
        return self


    def getBuffs(self: "Player") -> dict:
        """버프 반환"""
        return self.buffs

    def setBuffs(self: "Player", buffs: dict) -> "Player":
        """버프 설정"""
        self.buffs = buffs
        return self


    def getInventory(self: "Player") -> list[Item]:
        """인벤토리 값 반환"""
        return self.inventory

    def setInventory(self: "Player", inventory: list) -> "Player":
        """인벤토리 값 설정"""
        self.inventory = inventory
        return self

    def printInventory(self: "Player") -> None:
        """인벤토리 출력"""
        decoName("인벤토리")
        for item in self.inventory:
            print(f"- {item.getName()}(무게:{item.getWeight()})")
        return None


    def getWeight(self: "Player") -> int:
        """무게 값 반환"""
        return self.weight

    def setWeight(self: "Player", weight: int) -> "Player":
        """무게 값 설정"""
        if weight >= 0 and weight <= self.weight_max:
            self.weight = weight
            return self
        else:
            return "Out of Range"


    def getWeightMax(self: "Player") -> int:
        """최대 무게 값 반환"""
        return self.weight_max

    def setWeightMax(self: "Player", max: int) -> "Player":
        """최대 무게 값 설정"""
        self.weight_max = max
        return self


if __name__ == "__main__":
    p1 = Player()
    p1.setHealth(100)
    p1.printHealth()