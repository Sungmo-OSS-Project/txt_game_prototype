from typing import List
from Buff import Buff
from Storage import Storage


class Player:
    """Player Class"""
    def __init__(self) -> None:
        """Player 생성"""

        self.__health: int = int(20)
        """체력\n
        기본(시작) 값은 20으로 고정.\n
        체력이 0이 되는 경우 플레이어는 사망하며, 게임 오버.\n
        체력은 최대 체력 이상으로 상승할 수 없음\n
        특정 이벤트를 통하여 체력에 증감이 있을 수 있음.
        """

        self.__health_max: int = int(20)
        """최대 체력\n
        특정 이벤트를 통하여 최대 체력에 증감이 있을 수 있음."""

        self.__buffs: List[Buff] = list()
        """각종 긍정적/부정적 상태\n
        긍정적 상태(+) :
        각종 이벤트의 선택지(분기)에서 특정 상태가 존재할 경우 선택할 수 있는 분기가 활성화 또는 추가됨.\n
        부정적 상태(-) :
        지속적인 체력 감소, 특정 행동의 제약 등을 유발하는 기능.
        """

        self.inventory: Storage = Storage(name="플레이어 인벤토리")
        """인벤토리\n
        긍정적 상태처럼 특정 선택지를 선택할 수 있다.
        하지만 아이템 중 일회성 아이템의 경우, 해당 아이템 사용 시 소멸한다.
        """

    def get_health(self) -> int:
        """체력 값을 반환"""
        return self.__health

    def set_health(self, health: int) -> "Player":
        """체력 값을 설정"""
        if health <= 0:
            self.__health = 0
            Death(player=self).raise_death()  # 체력을 0 이하로 설정할 때, 사망했는지 조회함　/　体力を0以下に設定した時、死亡したのか照会する
        elif health >= self.__health_max:
            self.__health = self.__health_max
        else:
            self.__health = health
        return self

    def print_health(self) -> None:
        """체력 값을 출력"""
        print(f"체력: {self.__health}/{self.__health_max}")
        for i in range(self.__health_max):
            if i < self.__health:
                print("■", end="")
            else:
                print("□", end="")
        print()

    def get_health_max(self) -> int:
        """최대 체력 값을 반환"""
        return self.__health_max

    def set_health_max(self, max: int) -> "Player":
        """최대 체력 값을 설정"""
        self.__health_max = max
        return self

    def get_buffs(self) -> List[Buff]:
        """버프/디버프 반환"""
        return self.__buffs

    def set_buffs(self, buffs: List[Buff]) -> "Player":
        """버프/디버프 설정"""
        self.__buffs = buffs
        return self

    def print_buffs(self) -> None:
        """버프/디버프 출력"""
        print("버프/디버프")
        for i in self.__buffs:
            print(f"- {i.get_name()} : {i.get_level()}")


class Death(Exception):
    """Death Class\n
    Exception Class를 상속받습니다."""
    def __init__(self, player: Player) -> None:
        super().__init__("당신은 쉘터에 복귀하지 못하고 사망하였습니다.")
        self.player = player

    def raise_death(self) -> None:
        """예외를 던집니다."""
        raise self
