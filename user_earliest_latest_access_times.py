# Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time,
# the ID of the user making the access, and the resource ID. The access time is represented as seconds since
# 00:00:00, and all times are assumed to be in the same day.
#
# For example:
logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]


#
# We would like to compute user sessions, specifically: write a function that takes the logs and returns a data
# structure that associates to each user their earliest and latest access times.
#
# Example:
# {'user_1': [54001, 58523],
# 'user_2': [54060, 62314],
# 'user_3': [53760, 53760],
# 'user_5': [53651, 53651],
# 'user_6': [2, 215],
# 'user_7': [400, 400],
# 'user_8': [100, 100],
# 'user_22': [58522, 58522],
# }

def get_user_earliest_latest_access_times():
    user_access_times = {}
    for access_time, user, resource in logs1:
        if user not in user_access_times:
            user_access_times[user] = []
            user_access_times[user].append(access_time)
            user_access_times[user].append(access_time)
        else:
            if int(user_access_times[user][0]) > int(access_time):
                temp = user_access_times[user][0]
                user_access_times[user][0] = access_time
                user_access_times[user][1] = max(int(user_access_times[user][1]), int(temp))
            elif int(user_access_times[user][1]) < int(access_time):
                user_access_times[user][1] = int(access_time)
    print(user_access_times)


get_user_earliest_latest_access_times()
