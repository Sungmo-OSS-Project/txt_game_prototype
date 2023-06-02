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

    def get_category(self) -> str:
        """Item의 종류를 반환"""
        return self.__category

    def set_category(self, category: str) -> "Item":
        """Item의 종류를 설정"""
        self.__category = category
        return self

    def get_name(self) -> str:
        """Item의 이름을 반환"""
        return self.__name

    def set_name(self, name: str) -> "Item":
        """Item의 이름을 설정"""
        self.__name = name
        return self

    def get_weight(self) -> int:
        """Item의 무게를 반환"""
        return self.__weight

    def set_weight(self, weight: int) -> "Item":
        """Item의 무게를 설정"""
        self.__weight = weight
        return self
