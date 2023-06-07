from Events.Event import Event
from Player import Player
import item_dict
import random as rd


class Get_medikit(Event):
    """
    선택지형 이벤트(이벤트 종류 입력)
    약국에서 구급상자를 얻을 수 있는 이벤트
    """
    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("당신은 길을 걸어가던 중 허름한 건물 앞에 멈춰 섰습니다.")
        print("건물 입구에는 '선문약국' 이라고 쓰여있습니다.")
        print("당신은 약국 안으로 들어갑니다.")
        print("약국 안에는 좀비 한마리가 있습니다. \n 복장을 보니 이곳의 약사였던 모양입니다.")
        print("1. 싸운다.")
        print("2. 약국을 나간다.")
        selection = int(input("1, 2 >> "))
        if selection == 1:  # 90%확률로 아무 피해 없이 좀비를 쓰러뜨림
            if rd.random() < 0.9:
                print("당신은 좀비를 손쉽게 제압했습니다.")
            else:
                print("당신은 좀비를 힘겹게 쓰러뜨렸습니다.")
                print("약간의 부상을 당했습니다.")
                print("체력이 3 감소했습니다.")
                self.player.set_health(self.player.get_health() - 3)

            print("당신은 쓰러뜨린 좀비를 뒤로하고 약국 안으로 더욱 들어갑니다.")
            print("닫혀있는 케비넷을 발견했습니다.")
            print("케비넷을 조심스럽게 열어봅니다")

            if rd.random() < 0.7:  # 70%확률로 구급상자 획득
                print("케비넷 안에는 구급상자가 들어있습니다.")
                print("구급상자의 상태를 보아하니 충분히 쓸만해 보입니다.")
                print("구급상자를 1개 얻었습니다.")
                self.player.inventory.add_item(item_dict.medikit)  # 아이템 추가
                print("당신은 만족스럽게 약국을 나갑니다.")
            else:
                print("케비넷 안에는 아무것도 없었습니다.")
                print("당신은 아쉬워하며 약국을 나갑니다")

        else:
            print("당신은 좀비에게 들키지 않도록 조심스럽게 약국을 나왔습니다.")
