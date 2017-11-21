import datetime

def main():
    for i in range(100):
        s = "1"
        if i < 10:
            s += "0"
        s += str(i)
        s += "6"
        year = int(s)
        if leap(year):
            d = datetime.datetime(year, 1, 27).strftime("%w")
            if d == "2":
                print(year)

def leap(year):
    result = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
            else:
                result = False
        else :
            result = True
    else:
        result = False
    return result

if __name__ == "__main__":
    main()