import random,os
def cprint(color,content):
    if color == 'red':
        print('\033[31m'+content+'\033[0m')
    elif color == 'green':
        print('\033[32m'+content+'\033[0m')
    elif color == 'yellow':
        print('\033[33m'+content+'\033[0m')
    elif color == 'blue':
        print('\033[34m'+content+'\033[0m')
    elif color == 'purple':
        print('\033[35m'+content+'\033[0m')
    elif color == 'cyan':
        print('\033[36m'+content+'\033[0m')
    elif color == 'white':
        print('\033[37m'+content+'\033[0m')
    elif color == 'black':
        print('\033[30m'+content+'\033[0m')
    elif color == 'gray':
        print('\033[90m'+content+'\033[0m')
    elif color == 'pink':
        print('\033[91m'+content+'\033[0m')
    elif color == 'light_blue':
        print('\033[94m'+content+'\033[0m')
    elif color == 'light_green':
        print('\033[92m'+content+'\033[0m')
    elif color == 'light_yellow':
        print('\033[93m'+content+'\033[0m')
    elif color == 'light_purple':
        print('\033[95m'+content+'\033[0m')
def pin_gen():
    ex='1212-2323-3434-454545'
    pin=[]
    for i in range(3):
        pin.append(random.randint(1000,9999))
    pin.append(random.randint(100000,999999))
    pin='-'.join(map(str,pin))
    return pin
def main():
    os.system('cls')
    os.system(f'title wasreal money gen')
    cprint('blue','''
░██╗░░░░░░░██╗░█████╗░░██████╗██████╗░███████╗░█████╗░██╗░░░░░░░░██╗░░██╗██╗░░░██╗███████╗
░██║░░██╗░░██║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██║░░░░░░░░╚██╗██╔╝╚██╗░██╔╝╚════██║
░╚██╗████╗██╔╝███████║╚█████╗░██████╔╝█████╗░░███████║██║░░░░░░░░░╚███╔╝░░╚████╔╝░░░███╔═╝
░░████╔═████║░██╔══██║░╚═══██╗██╔══██╗██╔══╝░░██╔══██║██║░░░░░░░░░██╔██╗░░░╚██╔╝░░██╔══╝░░
░░╚██╔╝░╚██╔╝░██║░░██║██████╔╝██║░░██║███████╗██║░░██║███████╗██╗██╔╝╚██╗░░░██║░░░███████╗
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝''')
    cprint('purple','='*100)
    cprint('yellow','몇개의 문상을 생성하시겠습니까 : ')
    amount=input()
    if not amount.isdigit() or amount=='':
        cprint('red','잘못된 입력입니다.')
        main()
    for i in range(int(amount)):
        pin=pin_gen()
        cprint('green',f'{pin}')
        with open('pin.txt','a') as f:
            f.write(f'{pin}\n')
    os.system('pause')
    return
if __name__ == '__main__':
    while 1:
        main()
