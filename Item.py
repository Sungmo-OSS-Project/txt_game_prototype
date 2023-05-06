class Item():
    def __init__(self, name: str = str(), weight: int = int(), itemsEvents: int = int()) -> None:  # noqa: E501
        """Item 생성"""
        
        self.name = name
        """Item의 이름"""

        self.weight = weight
        """Item의 무게"""

        self.itemsEvents = itemsEvents
        """Item이 리턴하는 이벤트의 종류"""


    def getName(self) -> str:
        """Item의 이름을 반환"""
        return self.name

    def setName(self, name: str) -> str:
        """Item의 이름을 설정"""
        self.name = name
        return self.name


    def getWeight(self) -> int:
        """Item의 무게를 반환"""
        return self.weight

    def setWeight(self, weight: int) -> int:
        """Item의 무게를 설정"""
        self.weight = weight
        return self.weight
        

    def getItemsEvents(self):
        """Item이 리턴하는 이벤트의 종류를 반환"""
        return self.itemsEvents

    def setItemsEvents(self, itemsEvents: int) -> int:
        """Item이 리턴하는 이벤트의 종류를 설정"""
        self.itemsEvents - itemsEvents
        return self.itemsEvents
