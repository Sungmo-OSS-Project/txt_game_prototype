from typing import List
from Item import Item


class Storage:
    """Storage Class\n
    아이템을 저장하는 공간을 담당하는 클래스입니다.
    """
    def __init__(self, name: str = "저장공간", weight_max: int = 20) -> None:
        """init Storage"""

        self.__name: str = name
        """저장공간의 이름"""

        self.__storage: List[Item] = list()

        self.__weight: int = int(0)
        """무게\n
        아이템마다 무게가 다르며, 플레이어가 한 번에 소지할 수 있는 아이템 수량에 제한을 두는 기능이다.
        """

        self.__weight_max: int = int(20)
        """최대 무게 제한\n
        플레이어는 시작 시 최대무게(weight_max)가 설정된다.
        특정 이벤트를 통하여 최대 무게를 늘릴 수 있다.
        """

    def getName(self) -> str:
        """저장공간의 이름을 반환"""
        return self.__name

    def getItem(self) -> List[Item]:
        """아이템 리스트를 반환"""
        return self.__storage

    def setItem(self, storage: List[Item]) -> "Storage":
        """아이템 목록을 저장"""
        self.__storage = storage
        self.setWeight()
        return self

    def addItem(self, item: Item) -> None:
        print(f"{item.getName()}을 획득했습니다.")
        self.__storage.append(item)
        self.setWeight()

    def removeItem(self, item: Item) -> None:
        print(f"{item.getName()}을 버렸습니다.")
        self.__storage.remove(item)
        self.setWeight()

    def printStorage(self) -> None:
        """인벤토리 출력"""
        print(self.__name)
        for item in self.__storage:
            print(f"- {item.getName()}(무게:{item.getWeight()})")
        print(f"용량: {self.__weight}/{self.__weight_max}")

    def getWeight(self) -> int:
        """무게 값 반환"""
        return self.__weight

    def setWeight(self) -> None:
        """무게 값 설정"""
        totalWeight = int(0)
        for i in self.__storage:
            totalWeight += i.getWeight()
        if totalWeight > self.__weight_max:
            print("용량 초과")
            # 아이템 빼내는 기능 구현 필요
        else:
            self.__weight = totalWeight

    def getWeightMax(self) -> int:
        """최대 무게 값 반환"""
        return self.__weight_max

    def setWeightMax(self, max: int) -> "Storage":
        """최대 무게 값 설정"""
        self.__weight_max = max
        return self
