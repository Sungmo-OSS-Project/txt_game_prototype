from xmlrpc.client import boolean
from Events.Event import Event
from Player import Player


class Smart_zombie(Event):
    """
    �ܹ߼� �̺�Ʈ
    ����� �ȶ��Ͽ� ��ȭ�� ������ ���� �������ϴ�.
    """
    def __init__(self, player: Player, name: str = "",
                 level: int = 0, description: str = "") -> None:
        super().__init__(name, level, description)
        self.player: Player = player
        """self.player�� �޽����� ������ ��ü�� �־���ϴ� �ݵ�� �Ķ���ͷ� �޾ƾ���."""

    def trigger(self) -> None:
        print("����� ����濡 ���� ������ �׸� �����մϴ�. �׷��� ����� ��Ȳ�ϸ� ��ȭ�� �õ��մϴ�.")
        print("���!? �������� ������! �� ���� ���� �ƴϿ���! �̷��� ���� ���ݾƿ�!")
        while True:
            selection = input("���� �����Ͻðڽ��ϱ�? Y/N")
            if(selection == "Y"):
                print("����� ������ ���߽��ϴ�")
                print("�� ���׳�. ��¿�� ���� �ο� �� �ۿ�")
                print("����� �����غ� �մϴ�.")
                print("36�� ������̴�!!! ����� ����Ĩ�ϴ�.")
                inside_while_bool = True
                while inside_while_bool:
                    selection = input("���� �߰��մϱ�? Y/N")
                    if(selection == "Y"):
                        print("����� ����ġ�� �� ���ڱ� ���߰� ����� �ٶ󺾴ϴ�.")
                        print("ũũũ �Ӿұ��� �ΰ�! ö���� ö���� ������ ö����!!!")
                        print("������ �ڿ��� �뷮�� �������� �鸳�ϴ�.")
                        print("����� �ѻ��� �뷮���� �Ծ����ϴ�. �׷��� ������� �ڴʰ� �����Ͽ� ����� ���մϴ�.")
                        # days 1��ŭ ����
                        inside_while_bool = False
                    elif(selection == "N"):
                        print("������ ���ɼ��� �ֽ��ϴ� ���� ö���ϴ°� �°���.")
                        print("�ڸ� �ٶ� �׶�!!! ����� �Ӹ��� ���� ö���� �ֵθ��� ���� ���Դϴ�.")
                        print("����� ���� �����߸����� 1��ŭ �������� �Խ��ϴ�.")
                        self.player.set_health(self.player.getHealth() - 1)
                        self.player.print_health()
                        inside_while_bool = False
                    else:
                        print("�ٽ� �������ּ���")
                break
            elif(selection == "N"):
                print("����� ��ȭ�� �õ��մϴ�.")
                print("���񿡰� �ٰ����� ���ڱ� ����� �ڿ��� �Ǵٸ� ���� ����� ��Ĩ�ϴ�.")
                print("����߱��� �ΰ� �׷� �׾���� ũ����!")
                print("����� ū ��ó�� ������ ������� �ڴʰ� �����Ͽ� ����� ���մϴ�.")
                # days 1��ŭ ����
                break
            else:
                print("�ٽ� �������ּ���")
