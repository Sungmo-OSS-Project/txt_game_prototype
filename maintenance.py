from decoName import decoName
from Player import Player
from Death import Death

def maintenance(player: Player):
    """정비\n
    체력이 최대치까지 회복되며, 자신이 소지한 아이템을 저장, 판매, 폐기할 수 있다.\n
    플레이어가 모든 정비를 마친 경우 다시 '탐사 출발'을 선택하여 2 ~ 5의 과정을 반복한다.
    """
    decoName("정비")

    player.printHealth()
    
    if player.getIsDied(): # 사망할 시 예외 던짐
        raise Death()
        
    player.setHealth(player.getHealthMax()) # 체력을 최대치까지 회복
    print("체력 회복!")
    player.printHealth()
    player.printInventory()