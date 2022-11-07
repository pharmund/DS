class Research:
    def file_reader():
        with open('data.csv', 'r') as file:
            text = file.read()
            return(text)

if __name__ == '__main__':
    print(Research.file_reader())