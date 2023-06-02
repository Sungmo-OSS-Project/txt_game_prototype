from Events.Event import Event
from Player import Player


class Rainy_day(Event):

    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("문서를 발견했습니다.")
        print("내가 섬에서 유일하게 할 수 있었던 선택은 언제, 어떻게, 어디서 죽을 것인가 밖엔 없었지.")
        print("그래서... 나는 목을 매달기 위해 밧줄을 만들고 정상에 올랐어.")
        print("그리고 성공할 수 있는지 시험해봐야 했어. 알잖아? 내 성격.")
        print("대신 매달은 통나무가 무거워서 나뭇가지가 부러져버렸어.")
        print("결국 나는 내가 원하는 방법으로 자살조차 할 수 없었고... 아무것도 할 수가 없었어.")
        print("")
        print("그때, 따뜻한 담요 같은 느낌이 나를 덮쳐왔어.")
        print("그리고 나는 어떻게든 살아있어야 한다는 것을 알았지.")
        print("어떻게든 나는 계속 숨을 쉬어야 했어. 희망이 없었음에도 말이야.")
        print("내 논리로는 이곳을 다시는 보지 못할 거란걸 알고 있었지만, 그냥 그렇게 했고, 계속 숨을 쉬었지.")
        print("그리고 내 예상이 완전히 틀렸다는 게 증명됐어. 파도가 가져온 돛 덕분에.")
        print("결국 나는 이 곳 멤피스에 있고, 돌아와서 너와 이야기하고 있지. 얼음이 든 잔을 들고 말이야.")
        print("")
        print("그리고... 나는 켈리를 다시 잃어버렸어.")
        print("그녀가 내 곁에 없다는 게 너무 슬퍼.")
        print("")
        print("하지만 그녀가 그 섬에서 나와 함께 있어줘서 정말 고마웠어.")
        print("난 내가 이제 뭘 해야 할지 알지.")
        print("계속 숨을 쉬어야 한다는 거.")
        print("내일은 내일의 해가 뜨니까.")
        print("파도가 뭘 가져다 줄지 누가 알겠어?")
