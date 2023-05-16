from Item import Item


class Storage:
    def __init__(self) -> None:
        self.storage: list[Item] = list()

        self.weight: int = int(0)
        """무게\n
        아이템마다 무게가 다르며, 플레이어가 한 번에 소지할 수 있는 아이템 수량에 제한을 두는 기능이다.
        """

        self.weight_max: int = int(20)
        """최대 무게 제한\n
        플레이어는 시작 시 최대무게(weight_max)가 설정된다.
        특정 이벤트를 통하여 최대 무게를 늘릴 수 있다.
        """

    def addItem(self, item):
        print(f"{item}을 획득했습니다.")
        self.storage.append(item)

    def removeItem(self, item):
        print(f"{item}을 버렸습니다.")
        self.storage.remove(item)

    def printStorage(self) -> None:
        """인벤토리 출력"""
        print("인벤토리")
        for item in self.storage:
            print(f"- {item.getName()}(무게:{item.getWeight()})")
        return None

    def getWeight(self) -> int:
        """무게 값 반환"""
        return self.weight

    def setWeight(self, weight: int) -> "Storage":
        """무게 값 설정"""
        if weight >= 0 and weight <= self.weight_max:
            self.weight = weight
            return self
        else:
            return "Out of Range"

    def getWeightMax(self) -> int:
        """최대 무게 값 반환"""
        return self.weight_max

    def setWeightMax(self, max: int) -> "Storage":
        """최대 무게 값 설정"""
        self.weight_max = max
        return self
