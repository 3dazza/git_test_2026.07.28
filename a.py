s = 0
control_sum = 0

while True:
    s += 1
    control_sum = 0
    str_s = str(s)
    for ch in str_s:
        control_sum += int(ch)
    if control_sum == 101:
        break
    if s % 10000 == 0:
        print(s)
print(f"The desired number is: {s}")
