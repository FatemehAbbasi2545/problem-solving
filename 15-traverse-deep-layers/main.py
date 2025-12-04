def collect(items: list | tuple):
    final_list = []
    stack = list(items)
    while len(stack):
        last_item = stack.pop()
        if isinstance(last_item, (tuple, list)):
            final_list += collect(last_item)
        else:
            final_list.append(last_item)
    return final_list

def main():
    items = (1, 2, 3, 4, 5, ('Apple', 'Google', 'Microsoft', [[3.14, 17.25, 19.75], 'Nike', 'Adidas', (
        'Puma', (100, 200, 300, (True, 'orange', 'banana', 'cherry'))
    )]))
    result = collect(items)
    print(result[::-1])

if __name__ == '__main__':
    main()