class Item():
    """Item Class"""
    def __init__(self: "Item", name: str = str(), weight: int = int()) -> "Item":
        """Item 생성"""
        
        self.name: str = name
        """Item의 이름"""

        self.weight: int = weight
        """Item의 무게"""


    def getName(self: "Item") -> str:
        """Item의 이름을 반환"""
        return self.name

    def setName(self: "Item", name: str) -> "Item":
        """Item의 이름을 설정"""
        self.name = name
        return self


    def getWeight(self: "Item") -> int:
        """Item의 무게를 반환"""
        return self.weight

    def setWeight(self: "Item", weight: int) -> "Item":
        """Item의 무게를 설정"""
        self.weight = weight
        return self