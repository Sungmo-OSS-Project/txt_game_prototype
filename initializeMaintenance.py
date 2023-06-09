from Player import Player
import item_dict


def initializeMaintenance(player: Player):
    """기초 정비\n
    쉘터 출발 이전에 아이템을 소지할 수 있다.
    """
    print("기초 정비")

    # 체력 표시　/　体力表示
    player.print_health()

    # 기본 아이템 제공　/　基本アイテム提供
    player.inventory.add_item(item_dict.knife)
    player.inventory.add_item(item_dict.water_bottle)
    player.inventory.add_item(item_dict.bread)

    # 인벤토리 목록 출력　/　インベントリ目録出力
    player.inventory.print_storage()
    print("을 가지고 쉘터로 이동합니다.")
