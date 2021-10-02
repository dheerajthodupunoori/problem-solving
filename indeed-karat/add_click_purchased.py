# The people who buy ads on our network don't have enough data about how ads are working for their business. They've
# asked us to find out which ads produce the most purchases on their website.
#
# Our client provided us with a list of user IDs of customers who bought something on a landing page after clicking
# one of their ads:
#
# Each user completed 1 purchase.
# completed_purchase_user_ids = [
# "3123122444","234111110", "8321125440", "99911063"]
#
# And our ops team provided us with some raw log data from our ad server showing every time a user clicked on one of
# our ads:
#
# ad_clicks = [
# #"IP_Address,Time,Ad_Text",
# "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
# "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
# "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
# "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
# "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
# "122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
# "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
# ]
#
# The client also sent over the IP addresses of all their users.
#
# all_user_ips = [
# #"User_ID,IP_Address",
# "2339985511,122.121.0.155",
# "234111110,122.121.0.1",
# "3123122444,92.130.6.145",
# "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
# "8321125440,82.1.106.8",
# "99911063,92.130.6.144"
# ]
#
# Write a function to parse this data, determine how many times each ad was clicked, then return the ad text, that ad's number of clicks, and how many of those ad clicks were from users who made a purchase.
#
# Expected output:
#
# 1 of 2 2017 Pet Mittens
# 0 of 1 The Best Hollywood Coats
# 3 of 4 Buy wool coats for your pets
#
# purchases: number of purchase IDs
# clicks: number of ad clicks
# ips: number of IP addresses
# https://leetcode.com/discuss/interview-question/1152652/Indeed-Karat-Interview-Question

completed_purchase_user_ids = ["3123122444", "234111110", "8321125440", "99911063"]

# "IP_Address,Time,Ad_Text",
ad_clicks = [
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

# "User_ID,IP_Address",
all_user_ips = [
    "2339985511,122.121.0.155",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
    "8321125440,82.1.106.8",
    "99911063,92.130.6.144"
]


def get_add_click_and_purchased_count():
    add_click_data = {}
    completed_purchases = set(completed_purchase_user_ids)

    user_ip_map = {}

    for user_ip in all_user_ips:
        user_ip_data = user_ip.split(",")
        if user_ip_data[1] not in user_ip_map:
            user_ip_map[user_ip_data[1]] = user_ip_data[0]

    for add_click in ad_clicks:
        data = add_click.split(",")
        ip_address = data[0]
        if data[2] not in add_click_data:
            add_click_data[data[2]] = []
            add_click_data[data[2]].append(1)
            add_click_data[data[2]].append(0)
        else:
            add_click_data[data[2]][0] += 1

        if ip_address in user_ip_map:
            user_id = user_ip_map[ip_address]
            if user_id in completed_purchases:
                add_click_data[data[2]][1] += 1

    # print(add_click_data)
    print_add_click_and_purchased_stats(add_click_data)


def print_add_click_and_purchased_stats(data):

    for add in data:
        print(str(data[add][1]) + " of " + str(data[add][0]) + " " + add)


get_add_click_and_purchased_count()
