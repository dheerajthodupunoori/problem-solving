# You are running a classroom and suspect that some of your students are passing around the answers to multiple
# choice questions disguised as random strings.
#
# Your task is to write a function that, given a list of words and a string, finds and returns the word in the list
# that is scrambled up inside the string, if any exists. There will be at most one matching word. The letters don't
# need to be contiguous.
#
# Example:
# words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
# string1 = 'tcabnihjs'
# find_embedded_word(words, string1) -> cat
#
# string2 = 'tbcanihjs'
# find_embedded_word(words, string2) -> cat
#
# string3 = 'baykkjl'
# find_embedded_word(words, string3) -> None
#
# string4 = 'bbabylkkj'
# find_embedded_word(words, string4) -> baby
#
# string5 = 'ccc'
# find_embedded_word(words, string5) -> None
#
# string6 = 'nbird'
# find_embedded_word(words, string6) -> bird
#
# n = number of words in words
# m = maximal string length of each word

def find_embedded_word(words_, data):
    for word in words_:
        hashed = get_hash_map_data(data)
        is_found = True
        for char in word:
            if char not in hashed or hashed[char] == 0:
                is_found = False
                break
            elif char in hashed:
                hashed[char] -= 1

        if is_found:
            return word
    return None


def get_hash_map_data(data):
    data_hashed = {}
    for char in data:
        if char not in data_hashed:
            data_hashed[char] = 1
        else:
            data_hashed[char] += 1
    return data_hashed


words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
string1 = 'tcabnihjs'
print(find_embedded_word(words, string1))  # -> cat
string2 = 'tbcanihjs'
print(find_embedded_word(words, string2))  # -> cat
string3 = 'baykkjl'
print(find_embedded_word(words, string3))  # -> None
string4 = 'bbabylkkj'
print(find_embedded_word(words, string4))  # -> baby
string5 = 'ccc'
print(find_embedded_word(words, string5))  # -> None
string6 = 'nbird'
print(find_embedded_word(words, string6))  # -> bird