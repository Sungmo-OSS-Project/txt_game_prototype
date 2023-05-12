# 상위 폴더 모듈 접근.
import sys
import os
sys.path.append(os.path.abspath(".."))

from Events.meet_zombie import *
from initializeMaintenance import initializeMaintenance


def test():
    testPlayer = Player()
    Meet_zombie(testPlayer, testMode=True).trigger()
    assert testPlayer.inventory.getItem() == [knife]


def test2():
    testPlayer = Player()
    initializeMaintenance(testPlayer)
    assert testPlayer.inventory.getItem() == [knife]