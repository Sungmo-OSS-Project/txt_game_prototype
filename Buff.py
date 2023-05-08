class Buff():
    """Buff Class"""
    def __init__(self: "Buff", name: str = str(), level: int = int()):
        """Buff 생성"""

        self.name: str = name
        """Buff의 이름"""

        self.level: int = level
        """Buff의 레벨"""


    def getName(self: "Buff") -> str:
        """Buff의 이름을 반환"""
        return self.name

    def setName(self: "Buff", name: str) -> "Buff":
        """Buff의 이름을 설정"""
        self.name = name
        return self


    def getLevel(self: "Buff") -> int:
        """Buff의 레벨을 반환"""
        return self.level

    def setLevel(self: "Buff", level: int) -> "Buff":
        """Buff의 레벨을 설정"""
        self.level = level
        return self