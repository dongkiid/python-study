# 각 메뉴 옵션에 대한 칼로리 값을 저장한 사전
calories = {
    'burger': {1: 461, 2: 431, 3: 420, 4: 0},
    'side': {1: 100, 2: 57, 3: 70, 4: 0},
    'drink': {1: 130, 2: 160, 3: 118, 4: 0},
    'dessert': {1: 167, 2: 266, 3: 75, 4: 0}
}

# 사용자 입력 받기
burger_choice = int(input())
side_choice = int(input())
drink_choice = int(input())
dessert_choice = int(input())

# 총 칼로리 계산
total_calories = (
        calories['burger'][burger_choice] +
        calories['side'][side_choice] +
        calories['drink'][drink_choice] +
        calories['dessert'][dessert_choice]
)

# 결과 출력
print(f"Your total Calorie count is {total_calories}.")
