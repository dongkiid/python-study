P = int(input())
B = int(input())
D = int(input())
total = 0
all_badge = P // B
total += all_badge * D
left = P % B
total += left
print(total)