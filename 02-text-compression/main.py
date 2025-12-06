
def text_compression(txt: str):        
    i = 0
    output = ''

    while i < len(txt):
        count = 1
        while i + count < len(txt) and txt[i] == txt[i + count]:
            count += 1        

        output += f'{txt[i]}{count}' if count > 1 else f'{txt[i]}'
        i = i + count

    return output

def main():
    user_input = input('Enter a text: ')
    output  = text_compression(user_input)
    print(output)

if __name__ == "__main__":
    main()
