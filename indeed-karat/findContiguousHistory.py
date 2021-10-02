# We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of
# users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL
# was visited more than once per person. Write a function that takes two users' browsing histories as input and
# returns the longest contiguous sequence of URLs that appears in both.
#
# Sample input:
#
# user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"] user1 = ["/start", "/pink",
# "/register", "/orange", "/red", "a"] user2 = ["a", "/one", "/two"] user3 = ["/pink", "/orange", "/yellow", "/plum",
# "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow",
# "/BritishRacingGreen"] user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan",
# "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"] user5 = ["a"] user6 = ["/pink",
# "/orange","/six","/plum","/seven","/tan","/red", "/amber"]
#
# Sample output:
#
# findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
# findContiguousHistory(user0, user2) => [] (empty)
# findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
# findContiguousHistory(user2, user1) => ["a"]
# findContiguousHistory(user5, user2) => ["a"]
# findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
# findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
# findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]
#
# n: length of the first user's browsing history
# m: length of the second user's browsing history

def get_longest_contiguous_sequence(user1, user2):
    max_length = 0
    length1 = len(user1)
    length2 = len(user2)
    final_index = 0

    for index, user1_history in enumerate(user1):
        user2_history_index = getIndex(user2, user1_history)
        # print("index", user2_history_index, user1_history)
        if user2_history_index >= 0:

            index1 = index
            index2 = user2_history_index
            count = 0

            while index1 < length1 and index2 < length2 and user1[index1] == user2[index2]:
                count += 1
                index1 += 1
                index2 += 1

            if max_length < count:
                # print("maxlength-", max_length, count, index1)
                max_length = count
                final_index = index1

    print(user1[final_index - max_length:final_index])
    # print(max_length, final_index)


def getIndex(user2, search_item):
    for index, history in enumerate(user2):
        if history == search_item:
            return index
    return -1


input1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
input2 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
input3 = ["a", "/one", "/two"]
input4 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue",
          "/LightGoldenRodYellow", "/BritishRacingGreen"]
input5 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender",
          "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
input6 = ["a"]
input7 = ["/pink", "/orange", "/six", "/plum", "/seven", "/tan", "/red", "/amber"]

# get_longest_contiguous_sequence(input1, input2)
# get_longest_contiguous_sequence(input1, input3)
get_longest_contiguous_sequence(input1, input1)
get_longest_contiguous_sequence(input3, input2)
get_longest_contiguous_sequence(input6, input3)
get_longest_contiguous_sequence(input4, input5)
get_longest_contiguous_sequence(input5, input4)
get_longest_contiguous_sequence(input4, input7)
