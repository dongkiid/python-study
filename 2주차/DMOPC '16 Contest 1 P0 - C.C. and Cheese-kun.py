pizza = int(input())
cheese = int(input())

if pizza == 3 and cheese >= 95:
    print(f"C.C. is absolutely satisfied with her pizza.")
elif pizza == 1 and cheese <= 50:
    print(f"C.C. is fairly satisfied with her pizza.")
else:
    print(f"C.C. is very satisfied with her pizza.")
