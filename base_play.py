health_max = 20 #최대 체력 제한
health = 20


buffs = {} 

weight_max = 20 #최대 무게 제한
weight = 0

inventory = {}


from items.Item import *

def health_checker():
    print("체력: {}/{}".format(health,health_max))

def health_change(value):
    """
    체력 변화 함수
    """
    global health
    health += value


def stater_Maintenance():
    """
    기초정비
    스토리 배경 설명 및 기본 아이템 지급
    """
    print("당신은 쉘터의 탐색가로 선발되었습니다.\n첫 탐사에 앞서 기초 물자를 지급받습니다.")
    inventory["붕대"] = 2
    inventory["육포"] = 2
    inventory["생수"] = 2
    inventory["나이프"] = 1


def fall_by_rock():
    """
    넘어져서 체력이 1 감소\n
    본 함수는 이벤트 함수로 추후에 events 폴더로 이전할 예정.
    """

    print("돌부리에 걸려 넘어졌습니다.\n체력이 1 감소했습니다.")
    health_change(-1)
    

def explore():
    """
    탐사
    각종 이벤트가 해당 함수에서 발생
    """
    for i in range(1):
        fall_by_rock(health) #해당 행은 여러 이벤트를 랜덤으로 불러오도록 설정할 예정
        health_checker()

def maintenance():
    """
    쉘터 복귀 후 정비하는 함수 추가 예정
    """