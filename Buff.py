class Buff():
    """Buff Class"""
    def __init__(self, name: str = str(), level: int = int()) -> None:
        """Buff 생성"""

        self.__name: str = name
        """Buff의 이름"""

        self.__level: int = level
        """Buff의 레벨"""

    def get_name(self) -> str:
        """Buff의 이름을 반환"""
        return self.__name

    def set_name(self, name: str) -> "Buff":
        """Buff의 이름을 설정"""
        self.__name = name
        return self

    def get_level(self) -> int:
        """Buff의 레벨을 반환"""
        return self.__level

    def set_level(self, level: int) -> "Buff":
        """Buff의 레벨을 설정"""
        self.__level = level
        return self
