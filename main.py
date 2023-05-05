days = 0 # 지난 날짜 수

from Player import Player
player = Player()

from Buff import Buff
heal = Buff(name="치유", level=1)
poison = Buff(name="독", level=-1)

from Item import Item

class Death(Exception):
    def __init__(self):
        super().__init__("당신은 쉘터에 복귀하지 못하고 사망하였습니다.")

def decoName(name: str):
    """
    함수의 시작을 꾸며주는 데코레이터
    """
    for _ in range(5): print("-", end="")
    print(name, end="")
    for _ in range(5): print("-", end="")
    print()        


def initializeMaintenance():
    """기초 정비\n
    쉘터 출발 이전에 아이템을 소지할 수 있다.
    """
    decoName("기초 정비")

    print("체력: " + str(player.getHealth()) + "/" + str(player.getHealthMax()))

    # 쉘터 출발 이전에 아이템을 소지할 수 있다는 것을 알리는 메시지 출력
    print("쉘터 출발 이전에 아이템을 소지할 수 있습니다.")

    # 가져갈 수 있는 아이템 목록 리스트
    item_list: list[Item] = list()  # 빈 리스트 생성
    item_list.append(Item(name="식수", weight=2))
    item_list.append(Item(name="식량", weight=1))
    item_list.append(Item(name="손전등", weight=2))
    item_list.append(Item(name="전지", weight=2))
    item_list.append(Item(name="카메라", weight=2))
    item_list.append(Item(name="충전기", weight=1))

    # 아이템 목록 출력
    print("소지 가능한 아이템 목록:")
    for i, item in enumerate(item_list):
        print(f"{i+1}. {item.getName()}(무게:{item.getWeight()})")

    # 인벤토리 리스트 생성
    inventory: list[Item] = list()

    # 여러개 번호를 선택해서 인벤토리 list 에 넣어줘
    selected_items = input("인벤토리에 추가할 아이템 번호를 선택하세요 (숫자를 띄어쓰기로 구분): ")
    selected_items = selected_items.split()  # 입력받은 문자열을 공백을 기준으로 분리하여 리스트로 변환

    for i in selected_items:
        inventory.append(item_list[int(i)-1])  # 선택한 번호에 해당하는 아이템을 인벤토리 리스트에 추가

    player.setInventory(inventory)

    # 인벤토리 목록 출력
    player.printInventory()
    
    print("을 가지고 쉘터로 이동합니다.")


def explore():
    """탐사 출발\n
    쉘터에서 출발하며 각종 이벤트에 노출된다.
    """
    decoName("탐사 출발")
    
    print(f"Days : {days}")

    while(True):
        inputs = input("탐사 출발하시겠습니까? (Y/N) >>").upper()
        if inputs == "Y":
            return True
        elif inputs == "N":
            return False
    

def event():
    """이벤트\n
    물자 획득 이벤트, 물자 손실 이벤트, 체력 증감 이벤트, 상태 추가 및 제거 이벤트, 
    물자 교환 이벤트, 전투 이벤트 등의 각종 이벤트가 발생한다.
    """
    decoName("이벤트")

    print("어떤 이벤트가 발생하여 무언가를 선택했습니다!") # EVENT
    
    items: list[Item] = [Item(name="물병 500ml", weight=2)\
                        ,Item(name="물병 500ml", weight=2)\
                        ,Item(name="통조림", weight=1)]
    for i in items:
        print(i.getName() + "아이템을 획득하였습니다.")
        player.inventory.append(i)
    
    player.printInventory()
    # for item in player.getInventory():
    #     print("- " + item.getName() + ". 무게: " + str(item.getWeight()))


def comeback():
    """쉘터 복귀\n
    플레이어는 특정 시점마다 '쉘터 복귀' 선택지를 선택하여 쉘터로 복귀할 수 있다.
    """
    decoName("쉘터 복귀")

    while(True):
        inputs = input("쉘터 복귀하시겠습니까? (Y/N) >>").upper()
        if inputs == "Y":
            return True
        elif inputs == "N":
            return False
        elif inputs == "A": # death scenario for the test
            player.setHealth(0)
            return True


def maintenance():
    """정비\n
    체력이 최대치까지 회복되며, 자신이 소지한 아이템을 저장, 판매, 폐기할 수 있다.\n
    플레이어가 모든 정비를 마친 경우 다시 '탐사 출발'을 선택하여 2 ~ 5의 과정을 반복한다.
    """
    decoName("정비")

    if player.getIsDied(): # 사망할 시 예외 던짐
        raise Death()
        
    print("체력: " + str(player.getHealth()) + "/" + str(player.getHealthMax()))
    player.setHealth(player.getHealthMax()) # 체력을 최대치까지 회복
    print("체력 회복!")
    print("체력: " + str(player.getHealth()) + "/" + str(player.getHealthMax()))

    for item in player.getInventory():
        print("- " + item.getName() + ". 무게: " + str(item.getWeight()))

def main():
    """
    프로그램 시작
    """
    print("프로그램 시작")
    
    initializeMaintenance()

    try:
        while(True):
            global days
            days += 1
            if explore(): # 탐험하면
                event() # 이벤트가 발생하고

                if comeback(): # 쉘터에 복귀하면
                    maintenance() # 정비할 수 있음
    except Death as e:
        print(e)
    except Exception as e:
        print("예외 발생:", e)
            

    print("프로그램 종료")
    ## 프로그램 종료

if __name__ == "__main__":
    main()