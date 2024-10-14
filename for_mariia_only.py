from time import sleep

def print_big_love():
    print("\n       *****           *****\n    ****   ****     ****   ****\n  ***         *** ***         ***\n **             ***             **\n**               *              **\n**                             **\n ***        LOVE   LOVE       **\n   ***                      ***\n     ***                  ***\n       ****            ****\n          ****       ****\n             ***   ***\n               *****\n                 *\n");


def main():
    print('\n\t=========  ❤  =========')
    
    sleep(1)

    for i in range(3):
        if i == 0:
            print('\t.', end = ' ')
        print('.', end = ' ')

    print('\n\n\t\t❤  Mariia I Love You!!  ❤')

    sleep(1.5)

    while True:
        print('\n\tDo you Love Me ??')
        sleep(1)
        answer = input('\t(type \'yes\' or \'YES\'): ')
        sleep(0.5)
        if (answer == 'yes'):
            break
        if (answer == 'YES'):
            print_big_love()
            break
        sleep(1)
        print('\t****************AGAIN****************')

    sleep(1)
    print('\n\t❤ Hurrah !! ❤ We LOVE each other!! ❤\n\n')
    sleep(2)
    print('********************************************\n********************************************')

if __name__ == "__main__":
    main()
