from calendar import isleap
from datetime import date


def main():
    Tuesday = 1
    for year in range(1006, 1997, 10):
        d = date(year, 1, 27)
        if isleap(year) and d.weekday() == Tuesday:
            print(d)


if __name__ == "__main__":
    main()