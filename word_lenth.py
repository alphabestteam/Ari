def word_length(*words):
    sum = 0
    for name in words:
        sum += len(name)
    print(sum)


word_length("yael", "ari", "hen", "daniel")
