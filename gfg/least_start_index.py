# https://www.geeksforgeeks.org/find-least-start-index-of-a-substring-from-given-string-that-contains-all-the-given-words-in-a-contiguous-manner/

from collections import Counter
import copy


def get_min_index(words, s):
    length = len(s)
    words_length = len(words)
    single_word_length = len(words[0])
    words_index = dict(Counter(words))
    # print(words_index)
    string_matching_indeces = []

    for i in range(0, length - (single_word_length * words_length)):
        temp = s[i:i + single_word_length]
        if temp in words_index and i + (words_length * single_word_length) - 1 <= length:
            string_matching_indeces.append(i)
    if len(string_matching_indeces) == 0:
        return -1

    string_matching_indeces.sort()
    # print(string_matching_indeces)
    for matched_index in string_matching_indeces:
        temp = copy.deepcopy(words_index)
        for current_index in range(matched_index, matched_index + (single_word_length * words_length),
                                   single_word_length):
            temp1 = s[current_index:current_index + single_word_length]
            if temp1 not in temp:
                break
            else:
                temp[temp1] -= 1
                if temp[temp1] == 0:
                    temp.pop(temp1)
        if len(temp) == 0:
            return matched_index
    return -1


word = ["bat", "bal", "bal", "cat"]
s1 = "hellocatbyebalbalbatcatyo"

word1 = ["hat", "mat"]
s2 = "aslkfndsuvbsdlvnsk"

print(get_min_index(word, s1))
print(get_min_index(word1, s2))
