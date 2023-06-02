from Events.Event import Event
from Player import Player
import item_dict


class Meet_zombie(Event):
    """
    선택지형 이벤트
    좀비와 조우하여 전투, 우회 중 하나 결정

    임시 이벤트이므로 확장 예정
    """

    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("당신은 당신이 가고자 하는 길을 가로막고 있는 좀비 한 마리를 발견했습니다")
        print("좀비와 싸우거나 길을 조금 우회할 수 있습니다.")

        print("1. 좀비와 싸운다")
        print("2. 우회한다.")
        while True:
            selection = input("1, 2 : ")
            if selection == "1":
                print("당신은 좀비와 싸워 이겼습니다.")  # 확률적 승리는 미구현 상태이므로 임시적으로 확정 승리로 고정
                print("좀비의 바지 주머니에서 나이프 한 자루를 발견했습니다.")
                self.player.inventory.addItem(item_dict.knife)  # 아이템 추가
                break

            elif selection == "2":
                print("당신은 조용히 우회하여 지나갑니다.")
                print("다행히 좀비는 당신을 눈치채지 못했습니다.")
                break
            else:
                print("잘못입력하셨습니다.")
                continue
