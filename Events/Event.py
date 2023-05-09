class Event():
    """Event Class"""
    def __init__(self, name: str = str(), level: int = int(), description: str = str()) -> None:
        """Event 생성자"""
        
        self.name: str = name
        """이벤트 이름"""

        self.level: int = level
        """이벤트 레벨. 난이도"""

        self.description: str = description
        """이벤트 설명"""

    def trigger(self) -> None:
        """이벤트 실행"""