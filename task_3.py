from calendar import month


def season():
    month = int(input("Type 1 month: "))
    if month >= 1 and month <= 2:
        print('This is Winter')
    if month >= 3 and month <= 5:
        print('This is Spring')
    if month >= 6 and month <= 8:
        print('This is Summer')
    if month >= 9 and month <= 11:
        print('This is Winter')
    if month == 12:
        print('This is Winter')

print(season())