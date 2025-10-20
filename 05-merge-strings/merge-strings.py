
def get_input_data():
    collection1 = []
    collection2 = []
    for i in range(10):
        item = input('Enter an item: ')
        collection1.append(item) if i < 5 else collection2.append(item)
    return collection1, collection2

def extract_word(text: str):
    words = []
    result = text.split(' ')
    for x in result:
        if '.' in x:
            words.extend(x.split('.'))
        elif ',' in x:
            words.extend(x.split(','))
        else: 
            words.append(x)
    
    return words

def merge_strings(collection1, collection2):
    result = []
    for i in range(5):
        words1 = extract_word(collection1[i])
        words2 = extract_word(collection2[i])

        len_words1 = len(words1)
        len_words2 = len(words2)

        min = len_words1
        if len_words2 < min:
            min = len_words2

        for j in range(min):
            if j == min - 1:
                if min == len_words1:
                    result.append(words1[j] + ' ' + (" ".join(words2[j:])))
                if min == len_words2:
                    result.append((" ".join(words1[j:])) + ' ' + words2[j])
            else:
                result.append(words1[j] + ' ' + words2[j])

    for x in result:
        print(x)

def main():  
    collection1, collection2 = get_input_data()
    merge_strings(collection1, collection2)
    
if __name__ == "__main__":
    main()

