def is_valid_input(money, m1, m2, m3):
    if not (money.isdigit() and m1.isdigit() and m2.isdigit() and m3.isdigit()):
        return False
    
    money = int(money)
    if not (0 < money < 1000):
        return False
    
    return True


def slot_machine(money, m1, m2, m3):
    money, m1, m2, m3 = int(money), int(m1), int(m2), int(m3)
    games = 0
    while money > 0:
        # first machine
        if money > 0:
            money -= 1
            games += 1
            m1 += 1
            if m1 == 35:
                money += 30
                m1 = 0
        # second machine
        if money > 0:
            money -= 1
            games += 1
            m2 += 1
            if m2 == 100:
                money += 60
                m2 = 0
        # third machine
        if money > 0:
            money -= 1
            games += 1
            m3 += 1
            if m3 == 10:
                money += 9
                m3 = 0
    
    return games

money = input()
m1 = input()
m2 = input()
m3 = input()

if is_valid_input(money,m1,m2,m3):
    games = slot_machine(money,m1,m2,m3)
    print(f"Martha plays {games} times before going broke."  )