import random

def play_game():
    choices = ["가위", "바위", "보"]
    stats = {"승": 0, "패": 0, "무승부": 0}

    while True:
        player_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
        if player_choice not in choices:
            print("유효한 입력이 아닙니다")
            continue

        computer_choice = random.choice(choices)
        print(f"사용자: {player_choice}, 컴퓨터: {computer_choice}")

        if player_choice == computer_choice:
            print("무승부!")
            stats["무승부"] += 1
        elif (player_choice == "가위" and computer_choice == "보") or \
            (player_choice == "바위" and computer_choice == "가위") or \
            (player_choice == "보" and computer_choice == "바위"):
            print("사용자 승리!")
            stats["승"] += 1
        else:
            print("컴퓨터 승리!")
            stats["패"] += 1

        if input("다시 하시겠습니까? (y/n): ").lower() != 'y':
            print("게임을 종료합니다")
            break

    print(f"승: {stats['승']} 패: {stats['패']} 무승부: {stats['무승부']}")

if __name__ == "__main__":
    play_game()
