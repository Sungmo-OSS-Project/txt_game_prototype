class Item():
    """Item Class"""
    def __init__(self, category: str = str(), name: str = str(),
                 weight: int = int()) -> None:
        """Item 생성"""

        self.__category: str = category
        """Item의 종류"""

        self.__name: str = name
        """Item의 이름"""

        self.__weight: int = weight
        """Item의 무게"""

    def getName(self) -> str:
        """Item의 이름을 반환"""
        return self.__name

    def setName(self, name: str) -> "Item":
        """Item의 이름을 설정"""
        self.__name = name
        return self

    def getWeight(self) -> int:
        """Item의 무게를 반환"""
        return self.__weight

    def setWeight(self, weight: int) -> "Item":
        """Item의 무게를 설정"""
        self.__weight = weight
        return self
