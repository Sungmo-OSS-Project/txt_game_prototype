class Buff():
    def __init__(self, name: str = str(), level: int = 0):
        """Buff 생성"""

        self.name: str = name
        """Buff의 이름"""

        self.level: int = level
        """Buff의 레벨"""


    def getName(self) -> str:
        """Buff의 이름을 반환"""
        return self.name

    def setName(self, name: str) -> str:
        """Buff의 이름을 설정"""
        self.name = name
        return self.name


    def getLevel(self) -> int:
        """Buff의 레벨을 반환"""
        return self.level

    def setLevel(self, level: int) -> int:
        """Buff의 레벨을 설정"""
        self.level = level
        return self.level