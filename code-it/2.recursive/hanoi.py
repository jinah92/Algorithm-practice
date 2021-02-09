# 문제
# 하노이의 탑 게임의 해답을 출력해주는 함수 hanoi를 쓰세요. hanoi는 파라미터로 원판 수 num_disks, 게임을 시작하는 기둥 번호 start_peg, 그리고 목표로 하는 기둥 번호 end_peg를 받고, 재귀적으로 문제를 풀어 원판을 옮기는 순서를 모두 출력합니다.
# 가장 작은 원판의 번호는 1번이고 가장 큰 원판의 번호는 num_disks번입니다. 그리고 왼쪽 기둥이 1번, 가운데 기둥이 2번, 오른쪽 기둥이 3번입니다.

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)

    mid_peg = (6 - start_peg - end_peg)
    hanoi(num_disks-1, start_peg, mid_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks-1, mid_peg, end_peg)


# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)
