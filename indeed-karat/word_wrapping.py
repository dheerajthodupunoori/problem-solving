def word_wrap(words, limit):
    result = []
    temp = ""
    total_length = 0

    for word in words:

        word_length = len(word)
        if total_length + word_length < limit:
            total_length += word_length + 1
            temp += word + "-"
        else:
            result.append(temp[0:total_length-1])
            total_length = word_length + 1
            temp = word + "-"

    result.append(temp[0:total_length-1])
    print(result)
    return result


# words1 = ['It', 'is', 'a', 'calm', 'and', 'quiet', 'day']
# word_wrap(words1, 10)

words2 = ['It', 'is', 'an', 'easy', 'and', 'cool', 'question']
words3 = ['It', 'is', 'an', 'easy', 'and', 'cool', 'question']
word_wrap(words3, 32)
