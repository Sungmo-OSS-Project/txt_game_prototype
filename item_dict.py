from typing import Dict
from Item import Item


item_dict: Dict[str, Item] = {
    item.getName(): item
    for item in [
        Item(name="나이프", weight=1),
        Item(name="생수", weight=2),
        Item(name="구급상자", weight=4),
        Item(name="쇠지렛대", weight=3),
        Item(name="손전등", weight=2),
        Item(name="우유", weight=1),
        Item(name="토마토 통조림", weight=2),
        Item(name="삽", weight=2)
    ]
}
"""
인게임에서 사용할 아이템 목록\n
item_dict["아이템 이름"]: Item 객체\n
아이템 이름과 Item 객체가 1대1 대응
"""
