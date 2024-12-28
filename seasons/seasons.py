from datetime import date, datetime, timedelta
import sys
import inflect


def main():
    dob = validate(input("Date of Birth: "))
    print(calculate_delta(dob))


def validate(dob):
    format = "%Y-%m-%d"
    result = True
    try:
        result = bool(datetime.strptime(dob, format))
        dob = datetime.strptime(dob, format)
    except ValueError:
        sys.exit("Invalid date")
    # update50print(dob)
    return dob


def calculate_delta(dob):
    today = date.today()
    time = datetime.min.time()

    today_time = datetime.combine(today, time)
    timedelta = today_time - dob
    minutes = int(timedelta.total_seconds() / 60)

    p = inflect.engine()
    words = p.number_to_words(minutes, andword = "").capitalize()
    return words + " minutes"


if __name__ == "__main__":
    main()

