acum = 0
while True:
    try:
        num = input()
    except EOFError:
        break
    acum += float(num)
print(int(acum) if acum % 1 == 0 else acum)
