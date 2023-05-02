health_max = 20 #최대 체력 제한
health = 20

buffs = {}

weight_max = 20 #최대 무게 제한
weight = 0

items = {}

def health_checker():
    print("체력: {}/{}".format(health,health_max))


def stater_Maintenance():
    """
    기초정비
    스토리 배경 설명 및 기본 아이템 지급
    """
    print("당신은 쉘터의 탐색가로 선발되었습니다.\n첫 탐사에 앞서 기초 물자를 지급받습니다.")
    items["붕대"] = 2
    items["육포"] = 2
    items["생수"] = 2
    items["나이프"] = 1
