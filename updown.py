import random

def play_up_down_game():
    random_number = random.randint(1, 100)
    attempts = 0

    print("1부터 100 사이의 숫자를 맞추는 게임입니다. 시작합니다!")

    while True:
        guess = int(input("숫자를 추측해 보세요: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("1부터 100 사이의 숫자를 입력해 주세요.")
        elif guess < random_number:
            print("업!")
        elif guess > random_number:
            print("다운!")
        else:
            print(f"정답입니다! {attempts}번 만에 숫자를 맞췄습니다.")
            break

if __name__ == "__main__":
    play_up_down_game()

