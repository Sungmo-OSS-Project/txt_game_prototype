from Item import Item
"""
인게임에서 사용할 아이템 목록
아이템명, 무게를 표기
"""

#아이템 추가할 때 참고하세요
sample = Item(category = "아이템 종류", name = "아이템이름", weight = int())

#변수명 
knife = Item(category = "무기", name = "나이프", weight = 1)
water_bottle = Item(category = "음식", name = "생수", weight = 2)
medikit = Item(category = "의약품", name = "구급상자", weight = 4)
crowbar = Item(category = "도구", name="쇠지렛대", weight=3)
flashLight = Item(category = "도구", name="손전등", weight=2)
milk = Item(category = "음식", name="우유", weight=1)
tomato_can = Item(category = "음식", name="토마토 통조림", weight=2)
fish=Item(category="음식", name="생선",weight=3)
shovel = Item(category = "도구", name="삽", weight=3)
pistol = Item(category = "무기", name="권총", weight=3)
axe = Item(category = "도구", name="도끼", weight=3)
gasmask = Item(category = "도구", name="방독면", weight=2)
serum = Item(category = " 도구", name="혈청", weight = 3 #사람 만나는 이벤트에서 거래 선택시 혈청을 추가했는데 무게로 인해 못가져가는 상황을 만들고 싶어서 우선 높게 책정
