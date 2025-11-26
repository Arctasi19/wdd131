import random

def main():
    difficulty_num = get_level()
    wins = 0
    for i in range(0,10):
        success_test = run_question(difficulty_num)
        if success_test == True:
            wins = wins + 1
    print(f"Score: {wins}")

def get_level():
    while True:
        user_dif = input("Level: ")
        if user_dif in ["1","2","3"]:
             return int(user_dif)

def generate_integer(level):
    if level == 1:
        floor = 0
        ceiling = 9
    elif level == 2:
        floor = 10
        ceiling = 99
    else:
        floor = 100
        ceiling = 999
    return random.randint(floor,ceiling)

def run_question(d):
    first_number = generate_integer(d)
    second_number = generate_integer(d)

    answer = first_number + second_number
    equation = f"{first_number} + {second_number} = "
    tries = 3

    while tries > 0:
        user_attempt = input(equation)
        if user_attempt != str(answer):
            tries = tries - 1
            print("EEE")
        else:
            return True
    if tries == 0:
        print(f"{first_number} + {second_number} = {answer}")
        return False

if __name__ == "__main__":
    main()