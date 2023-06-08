from Events.Event import Event
from Player import Player
# import item_dict 아이템 사전이 필요시 주석 해제


class chainLetter(Event):
    """
    텍스트형 이벤트
    행운의 편지이다.
    """
    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player

    def trigger(self) -> None:
        print("이 편지는 영국에서 최초로 시작되어 일년에 한바퀴를 돌면서 받는 사람에게 행운을 주었고 지금은 당신에게로 옮겨진 이 편지는 4일 안에 당신 곁을 떠나야 합니다.")
        print("이 편지를 포함해서 7통을 행운이 필요한 사람에게 보내 주셔야 합니다. 복사를 해도 좋습니다.")
        print("혹 미신이라 하실지 모르지만 사실입니다.")
        print("영국에서 HGXWCH이라는 사람은 1930년에 이 편지를 받았습니다.")
        print("그는 비서에게 복사해서 보내라고 했습니다.")
        print("며칠 뒤에 복권이 당첨되어 20억을 받았습니다.")
        print("어떤 이는 이 편지를 받았으나 96시간 이내 자신의 손에서 떠나야 한다는 사실을 잊었습니다.")
        print("그는 곧 사직되었습니다.")
        print("나중에야 이 사실을 알고 7통의 편지를 보냈는데 다시 좋은 직장을 얻었습니다.")
        print("미국의 케네디 대통령은 이 편지를 받았지만 그냥 버렸습니다.")
        print("결국 9일 후 그는 암살당했습니다.")
        print("기억해 주세요.")
        print("이 편지를 보내면 7년의 행운이 있을 것이고 그렇지 않으면 3년의 불행이 있을 것입니다.")
        print("그리고 이 편지를 버리거나 낙서를 해서는 절대로 안됩니다.")
        print("7통입니다.")
        print("이 편지를 받은 사람은 행운이 깃들것입니다.")
        print("힘들겠지만 좋은게 좋다고 생각하세요.")
        print("7년의 행운을 빌면서...")
