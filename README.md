# 쉘터 서바이벌: 좀비 아포칼립스
세상에 좀비 바이러스가 창궐하고, 사람들은 저마다의 방식으로 몸을 숨겼다. 이곳은 지하 쉘터 A-04. 플레이어는 쉘터 밖에서 물자를 탐색 및 조달하는 ‘탐색가’로 선발되었다.
물자를 얻고, 쉘터에 복귀해야한다.

## 플레이 방식
플레이어는 자신의 자원을 관리하며 물자를 얻어야한다. 체력, 무게, 상태 세가지 자원을 관리한다. 물자 획득 후 쉘터에 복귀하며, 플레이어는 쉘터에서 개인 정비를 한다. 
### [쉘터에서 출발] – [물자 탐색 및 획득] – [쉘터 복귀] – [정비] 과정을 반복한다.

## 자원
### 체력
#### 0이되면 사망한다. [체력 회복 이벤트], [쉘터 복귀]를 통해 체력을 회복하고, [부정적 상태], [체력손실 이벤트] 등에서 체력을 잃음.

### 무게
#### 한도가 정해져 있는 수치이다. 플레이어가 아이템을 획득할 때 마다 늘어난다.

### 표시 방식
#### (현재 무게 / 한도 무게) 한도 무게는 [쉘터 복귀] 이후 늘릴 수 있는 이벤트가 발생하기도 한다. 특정 아이템을 버려서 [현재 무게]를 줄일 수 있다.

### 상태
#### 중독, 출혈, 골절 등의 각종 상태이상이 있다. 각 상태에 따라 체력이 감소하거나 행동이 제약됨.


## 쉘터 복귀
쉘터에서는 특정 행동을 선택할 수 있다. 무게 한도를 늘리거나 아이템을 사고 팔 수 있다.

## 엔딩
### 엔딩 1. 사망
어떠한 경우든 체력이 0이 된 경우 발생
“당신은 쉘터에 복귀하지 못하고 사망하였습니다.

### 엔딩 2. 최고의 탐색가
특정 조건 만족 시(제공된 이벤트 전부 소진, 특정 턴 이상 생존 등 조건은 추후에 확정) 발생.
“당신은 A-04쉘터 최고의 탐색가로서 쉘터에 물자를 조달하며 생존을 이어갑니다. 그 끝이 어떻게 될 지는 아무도 모르죠.”

# 클래스 문서
https://sungmo-oss-project.github.io/txt_game_prototype/

# 프로젝트 칸반 보드
https://github.com/orgs/Sungmo-OSS-Project/projects/1

# LICENSE
MIT License
