from Player import Player
from Events.Event import *

def maintenance(player: Player):
    """정비\n
    체력이 최대치까지 회복되며, 자신이 소지한 아이템을 저장, 판매, 폐기할 수 있다.\n
    플레이어가 모든 정비를 마친 경우 다시 '탐사 출발'을 선택하여 2 ~ 5의 과정을 반복한다.
    """
    print("정비")
    player.setHealth(player.getHealthMax()) #최대체력까지 체력 회복
    player.printHealth() #체력 표시
    player.printInventory() #인벤토리 표시
    #인벤토리 관리 추가 예정