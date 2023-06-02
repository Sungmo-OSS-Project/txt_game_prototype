from typing import List
from Item import Item
import unicodedata


class Storage:
    """Storage Class\n
    아이템을 저장하는 공간을 담당하는 클래스입니다.
    """
    def __init__(self, name: str = "저장공간", weight_max: int = int(20)) -> None:
        """Storage 초기화"""

        self.__name: str = name
        """저장공간의 이름"""

        self.__storage: List[Item] = list()
        """저장공간. 리스트의 자료구조를 가짐"""

        self.__weight: int = int(0)
        """무게\n
        아이템마다 무게가 다르며, 플레이어가 한 번에 소지할 수 있는 아이템 수량에 제한을 두는 기능이다.
        """

        self.__weight_max: int = weight_max
        """최대 무게 제한\n
        플레이어는 시작 시 최대무게(weight_max)가 설정된다.
        특정 이벤트를 통하여 최대 무게를 늘릴 수 있다.
        """

    def get_name(self) -> str:
        """저장공간의 이름을 반환"""
        return self.__name

    def get_item(self) -> List[Item]:
        """아이템 리스트를 반환"""
        return self.__storage

    def set_item(self, storage: List[Item]) -> "Storage":
        """아이템 리스트를 설정"""
        self.__storage = storage
        self.set_weight()
        return self

    def add_item(self, item: Item) -> None:
        """아이템을 저장공간에 추가합니다."""
        print(f"{item.get_name()}을 획득했습니다.")
        self.__storage.append(item)
        self.set_weight()

    def remove_item(self, item: Item) -> None:
        """아이템을 저장공간에서 제거합니다."""
        print(f"{item.get_name()}을 버렸습니다.")
        self.__storage.remove(item)
        self.set_weight()

    def print_storage(self, do_print: bool = True) -> List[str]:
        """인벤토리 출력"""
        string: List[str] = list()  # print한 텍스트의 리스트
        if do_print:
            print(self.__name)
        string.append(self.__name)

        for item in self.__storage:
            if do_print:
                print(f"- {item.get_name()}(무게:{item.get_weight()})")
            string.append(f"- {item.get_name()}(무게:{item.get_weight()})")

        if do_print:
            print(f"용량: {self.__weight}/{self.__weight_max}")
        string.append(f"용량: {self.__weight}/{self.__weight_max}")

        return string

    def print_two_storage(self, otherStorage: "Storage",
                          reverse: bool = False) -> None:
        """두개의 저장소를 가로로 출력합니다.\n
        reverse는 주체와 객체가 바뀌어 출력하는 옵션입니다.
        """
        if reverse is False:
            text1 = self.print_storage(do_print=False)
            text2 = otherStorage.print_storage(do_print=False)
        elif reverse is True:
            text1 = otherStorage.print_storage(do_print=False)
            text2 = self.print_storage(do_print=False)

        def get_width(text: str):
            width = 0
            for char in text:
                if unicodedata.east_asian_width(char) == 'W':
                    char_width = 2
                else:
                    char_width = 1
                width += char_width
            return width

        # 가장 긴 문자열의 폭
        max_length = max(get_width(text) for text in text1)

        text1_end = False
        text2_end = False
        index = 0
        while not text1_end or not text2_end:
            try:
                print(text1[index], end=" "*(max_length - get_width(text1[index])) + "\t")
            except IndexError:
                print("", end=" "*(max_length) + "\t")
                text1_end = True
            try:
                print(text2[index])
            except IndexError:
                print("")
                text2_end = True

            index += 1

    def get_weight(self) -> int:
        """무게 값 반환"""
        return self.__weight

    def set_weight(self) -> None:
        """무게 값 설정"""
        total_weight = int(0)
        for i in self.__storage:
            total_weight += i.get_weight()
        self.__weight = total_weight
        if total_weight > self.__weight_max:
            print("용량 초과")

            # 아이템을 빼내는 기능
            self.give_item(Storage(name="쓰레기통", weight_max=1000))
            self.set_weight()

    def get_weight_max(self) -> int:
        """최대 무게 값 반환"""
        return self.__weight_max

    def set_weight_max(self, max: int) -> "Storage":
        """최대 무게 값 설정"""
        self.__weight_max = max
        return self

    def give_item(self, other_storage: "Storage") -> None:
        """other_storage에게 아이템을 줍니다."""
        self.print_two_storage(other_storage, reverse=False)

        item_idx = int(input("주고 싶은 아이템의 인덱스를 입력하세요: "))

        try:
            item = self.__storage[item_idx]

            self.remove_item(item)
            other_storage.add_item(item)

            print(f"{item.get_name()}을(를) {other_storage.__name}에게 주었습니다.")
        except IndexError:
            print("유효하지 않은 인덱스입니다.")

    def receive_item(self, other_storage: "Storage") -> None:
        """otherStorage로부터 아이템을 받습니다."""
        self.print_two_storage(other_storage, reverse=True)

        item_idx = int(input("받고 싶은 아이템의 인덱스를 입력하세요: "))

        try:
            item = other_storage.__storage[item_idx]

            other_storage.remove_item(item)
            self.add_item(item)

            print(f"{item.get_name()}을(를) {self.__name}에게 받았습니다.")
        except IndexError:
            print("유효하지 않은 인덱스입니다.")

    def communicate_with(self, other_storage: "Storage") -> None:
        """다른 Storage 객체와 상호작용"""
        print(f"{self.__name}와 {other_storage.__name} 주고받기")
        self.print_two_storage(other_storage, reverse=False)

        while True:
            print("0. 서로의 아이템 출력")
            print("1. 아이템 주기")
            print("2. 아이템 받기")
            print("3. 종료하기")
            choice = input("선택하세요: ")

            if choice == "0":
                self.print_two_storage(other_storage, reverse=False)
            elif choice == "1":
                self.give_item(other_storage)
            elif choice == "2":
                self.receive_item(other_storage)
            elif choice == "3":
                break
            else:
                print("유효하지 않은 선택입니다.")
