class Must_read:
    with open('data.csv', 'r') as file:
        text = file.read()
        print(text)

if __name__ == '__main__':
    Must_read()