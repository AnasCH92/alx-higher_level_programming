#!/usr/bin/python3
    import random
    number = random.randint(-10000, 10000)
    a = number % 10 if number > 0
    else number % -10
    t = "greater than 5" if a > 5
    else a if a == 0 
    else "less than 6 and not 0"
    printf(f"last digit of (number) is (a) and is {t}")
