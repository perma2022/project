import random

def play_up_down_game(best_score=None):
    random_number = random.randint(1, 100)
    attempts = 0
    print(f"이전 게임 플레이어 최고 시도 횟수: {best_score}" if best_score is not None else "")

    while True:
        guess = input("숫자를 입력하세요: ")
        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("유효한 범위 내의 숫자를 입력하세요")
            else:
                attempts += 1
                if guess < random_number:
                    print("업")
                elif guess > random_number:
                    print("다운")
                else:
                    print("맞았습니다")
                    print(f"시도한 횟수: {attempts}")
                    return attempts  # 현재 게임의 시도 횟수를 반환
        except ValueError:
            print("유효한 숫자를 입력하세요")

def main():
    best_score = None
    while True:
        current_score = play_up_down_game(best_score)
        best_score = current_score if best_score is None or current_score < best_score else best_score
        
        play_again = input("다시 하시겠습니까? (y/n): ")
        if play_again.lower() != 'y':
            print("게임을 종료합니다")
            break

if __name__ == "__main__":
    main()
