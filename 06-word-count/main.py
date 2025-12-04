
def word_count(text: str) -> int:
    seprators = [',', '.']
    for sep in seprators:
        text = text.replace(sep, ' ')
    words = text.split(' ')
    return sum(1 for word in words if word)

def main():
    txt = input('Enter a text: ')
    print(word_count(txt))

if __name__ == "__main__":
    main()
