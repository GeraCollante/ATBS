def list_thing(words):
    if len(words) == 1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])


def sentence(x):
    if len(x) == 1:
        return x[0]
    return ', '.join(x[:-1]) + ' and ' + x[-1]


spam = ['banana', 'apple', 'orange']
print(list_thing(spam))
print(sentence(spam))
