
def word_count(text: str) -> int:
    result = []
    words = text.split(' ')

    for word in words:
        if ',' in word:
            result.extend(word.split(','))
        elif '.' in word:
            result.extend(word.split('.'))
        else:
            result.append(word)

    return sum(1 for x in result if x)

txt = input('Enter a text: ')
print(word_count(txt))
