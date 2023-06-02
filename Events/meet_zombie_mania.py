from turtle import pen
from Events.Event import Event
from Player import Player


class Meet_zombie_mania(Event):
    """
    단발성 이벤트
    자칭 좀비 매니아를 만난다
    """
    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("당신은 길을 가다 자칭 좀비물 매니아를 만났습니다. 그는 지금 상황이 최고라고 말합니다.")
        print("크크큿.. 안녕하신가. 요즘같은 기분좋은 날에 어두운 표정을 한 양반이여..")
        print("뭐? 자네가 이 사태를 멈추겠다고?")
        print("크크크... 이런 영웅나리를 보았나. 자네는 이제 그만 죽도록 하게")
        print("그러나 당신의 나이프에 그는 치명상을 입습니다.")
        print("크하핫 영웅나리, 자네 지금 표정이 가관이군. 크크크.. 어차피 죽는거야 네놈을 길동무로 데려가겠다!")
        print("그는 겉옷 뒤에 숨긴 폭탄을 기동시킵니다.")
        print("당신은 마음과 몸 양쪽에 데미지를 입었습니다.")
        print("체력이 5 줄어듭니다.")

        self.player.set_health(self.player.getHealth() - 5)
        self.player.print_health()
