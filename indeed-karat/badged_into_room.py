# https://leetcode.com/discuss/interview-question/1501107/Indeed-or-Karat-or-security-system-for-a-badged-access

# We want to find employees who badged into our secured room unusually often. We have an unordered list of names and
# entry times over a single day. Access times are given as numbers up to four digits in length using 24-hour time,
# such as "800" or "2250".
#
# Write a function that finds anyone who badged into the room three or more times in a one-hour period. Your function
# should return each of the employees who fit that criteria, plus the times that they badged in during the one-hour
# period. If there are multiple one-hour periods where this was true for an employee, just return the earliest one
# for that employee.
#
badge_times = [
    ["Paul", "1355"],
    ["Jennifer", "1910"],
    ["John", "835"],
    ["John", "830"],
    ["Paul", "1315"],
    ["John", "1615"],
    ["John", "1640"],
    ["Paul", "1405"],
    ["John", "855"],
    ["John", "930"],
    ["John", "915"],
    ["John", "730"],
    ["John", "940"],
    ["Jennifer", "1335"],
    ["Jennifer", "730"],
    ["John", "1630"],
    ["Jennifer", "5"]
]


#
# Expected output (in any order)
# John: 830 835 855 915 930
# Paul: 1315 1355 1405
#
# n: length of the badge records array


def badged_times():
    times = {}
    for person, time in badge_times:
        if person not in times:
            times[person] = []
            times[person].append(int(time))
        else:
            times[person].append(int(time))
    # print(times)
    result = {}
    for person in times:
        is_valid, person, periods = is_valid_person(person, times[person])
        print(is_valid, person, periods)
        if is_valid:
            result[person] = periods
    print("Result - \n")
    print(result)


def is_valid_person(person, periods):
    periods.sort()
    if len(periods) <= 2:
        return False, None, None
    result = []
    length = len(periods)
    first = periods[0]

    for i in range(0, length - 2):
        print(person, periods[i:i + 3], periods[i], periods[i + 2], abs(periods[i] - periods[i + 2]))
        if abs(periods[i] - periods[i + 2]) <= 100:
            result += periods[i:i + 3]

    if len(result) > 3:
        print(set(result))
        result = first_one_hour(list(set(result)))

    return True, person, result


def first_one_hour(periods):
    periods.sort()
    length = len(periods)
    first = periods[0]
    result = [first]

    for index in range(1, length):
        if abs(first - periods[index]) <= 100:
            result.append(periods[index])
        else:
            break
    return result


badged_times()
