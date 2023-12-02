with open("inputDay1.txt", "r") as file:
    total = 0
    for line in file.read().strip().split("\n"):
        digits = [char for char in line if char.isdigit()]

        if digits:
            calibration = int(digits[0] + digits[-1])
            total += calibration

    print(total)
