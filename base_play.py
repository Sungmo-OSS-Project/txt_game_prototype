health_max = 20 #최대 체력 제한
health = 20


buffs = {} 

weight_max = 20 #최대 무게 제한
weight = 0

inventory = {}

event_count = 0 #한 번의 탐사에서 진행한 이벤트 수를 표시. 
event_cycle = 10 #탐사 한 번당 최대 이벤트 횟수(개발에 따라 조정)

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
    이벤트를 특정 횟수 이상 진행하면 '쉘터 복귀' 활성화
    """
    global event_count
    for i in range(event_cycle):
        
        fall_by_rock(health) #해당 부분은 임시적으로 생성한 이벤트를 불러왔음. 추후에는 여러 이벤트 중 랜덤하게 불러오도록 할 예정
        
        health_checker() #매 이벤트 종료 시 체력 상황 출력
        event_count += 1
        
        if health <= 0: #체력이 0 이하가 되면 사망
            break
    return "GameOver"
    
def maintenance():
    """
    쉘터 복귀 후 정비
    체력이 최대치로 회복
    """
    global health
    global health_max
    print("당신은 쉘터로 복귀했습니다.\n체력이 최대치로 회복되었습니다.\n당신은 아이템을 보관하거나, 다음 탐사를 위한 아이템을 소지할 수 있습니다.")
    health = health_max
    health_checker()
    #아이템 관리에 관한 코드 구현 

#게임 플레이
stater_Maintenance()
print("당신의 이야기를 시작합니다")

while True:
    while True:
        explore()
        if explore() == "GameOver":
            break
        yes_no = input("쉘터로 복귀하시겠습니까? (Y/N)")
        if yes_no == "N":   #event_cycle 만큼의 이벤트 진행 후 추가 탐사 진행 여부 결정, 추가 탐사 진행 시 다시 event_cycle 만큼의 탐사 진행 
            print("당신은 탐사를 더 진행하기로 합니다.")
            event_count = 0 
            continue
        else:
            print("당신은 쉘터로 복귀합니다.")
            event_count = 0
            break
    maintenance()
