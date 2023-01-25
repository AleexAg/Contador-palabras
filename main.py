def count(string):
    count = 0
    string = string.replace(' ', '')

    for i in range(len(string)):
        count += 1
    
    return count



def main():
    print('-' * 50)
    print('|  Bienvenido al contador de palabras  |')
    string = input('-> ¿En qué estás pensando?: ')
    print('-' * 50)

    res = count(string)
    print('-' * 50)
    print('Tu pensamiento fue expresado en un total de:', res, 'palabras!')
    print('-' * 50)


if __name__ == '__main__':
    main()
