from Item import Item
"""
인게임에서 사용할 아이템 목록
아이템명, 무게를 표기
"""

# 아이템 추가할 때 참고하세요　/　アイテムを追加するときに参考にしてください
sample = Item(category="아이템 종류", name="아이템이름", weight=int())

# 변수명　/　変数名
knife = Item(category="무기", name="나이프", weight=1)
water_bottle = Item(category="음식", name="생수", weight=2)
medikit = Item(category="의약품", name="구급상자", weight=4)
crowbar = Item(category="도구", name="쇠지렛대", weight=3)
flashLight = Item(category="도구", name="손전등", weight=2)
milk = Item(category="음식", name="우유", weight=1)
tomato_can = Item(category="음식", name="토마토 통조림", weight=2)
shovel = Item(name="삽", weight=2)
bag = Item(name="가방", weight=0)
fish = Item(category="음식", name="생선", weight=3)
shovel = Item(category="도구", name="삽", weight=3)
pistol = Item(category="무기", name="권총", weight=3)
axe = Item(category="도구", name="도끼", weight=3)
gasmask = Item(category="도구", name="방독면", weight=2)
bread = Item(category="음식", name="빵", weight=1)
serum = Item(category=" 도구", name="혈청", weight=5) #소지 시의 리스크를 위해 무게를 높게 설정