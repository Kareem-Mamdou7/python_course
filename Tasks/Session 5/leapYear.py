def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    return False


year = int(input("Enter the year: "))
print(isLeap(year))
