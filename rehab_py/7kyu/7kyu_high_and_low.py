def high_and_low(numbers):
    numbers = [int(n) for n in numbers.split(" ")]

    return f"{max(numbers)} a{min(numbers)}"


aa = "1 2 3 4 5"
bb = [int(n) for n in aa.split(" ")]
print(bb)