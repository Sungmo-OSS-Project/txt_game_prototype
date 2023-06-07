from Events.Event import Event
from Player import Player


class Smart_zombie(Event):
    """
    단발성 이벤트
    당신은 똑똑하여 대화가 가능한 좀비를 만났습니다.
    """
    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player는 메시지를 전달할 객체가 있어야하니 반드시 파라미터로 받아야함."""

    def trigger(self) -> None:
        print("당신은 여행길에 좀비를 만났고 그를 공격합니다. 그러나 좀비는 당황하며 대화를 시도합니다.")
        print("우왓!? 공격하지 마세요! 나 나쁜 좀비 아니에요! 이렇게 말도 하잖아요!")
        while True:
            selection = input("좀비를 공격하시겠습니까? Y/N")
            if (selection == "Y"):
                print("좀비는 공격을 피했습니다")
                print("쳇 들켰나. 어쩔수 없지 싸울 수 밖에")
                print("당신은 전투준비를 합니다.")
                print("36계 줄행랑이닷!!! 좀비는 도망칩니다.")
                inside_while_bool = True
                while inside_while_bool:
                    selection = input("좀비를 추격합니까? Y/N")
                    if (selection == "Y"):
                        print("좀비는 도망치던 중 갑자기 멈추고 당신을 바라봅니다.")
                        print("크크크 속았구나 인간! 철수는 철수라도 전략적 철수닷!!!")
                        print("좀비의 뒤에서 대량의 발포음이 들립니다.")
                        print("당신은 총상을 대량으로 입었습니다. 그러나 동료들이 뒤늦게 도착하여 당신을 구합니다.")

                        print("당신은 10만큼 데미지를 입었습니다.")
                        self.player.set_health(self.player.get_health() - 10)
                        self.player.print_health()
                        
                        # days 1만큼 진행
                        inside_while_bool = False
                    elif (selection == "N"):
                        print("함정의 가능성이 있습니다 여긴 철수하는게 맞겠죠.")
                        print("뒤를 바라본 그때!!! 당신의 머리를 향해 철봉을 휘두르는 좀비가 보입니다.")
                        print("당신은 좀비를 쓰러뜨리지만 1만큼 데미지를 입습니다.")
                        self.player.set_health(self.player.get_health() - 1)
                        self.player.print_health()
                        inside_while_bool = False
                    else:
                        print("다시 선택해주세요")
                break
            elif (selection == "N"):
                print("당신은 대화를 시도합니다.")
                print("좀비에게 다가가자 갑자기 당신의 뒤에서 또다른 좀비가 당신을 덮칩니다.")
                print("방심했구나 인간 그럼 죽어야지 크하핫!")
                print("당신은 큰 상처를 입지만 동료들이 뒤늦게 도착하여 당신을 구합니다.")

                print("당신은 7만큼 데미지를 입었습니다.")
                self.player.set_health(self.player.get_health() - 7)
                self.player.print_health()
                # days 1만큼 진행
                break
            else:
                print("다시 선택해주세요")
