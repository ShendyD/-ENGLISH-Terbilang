import os

belas = ['',' Eleven ',' Twelve ',' Thirteen ',' Fourteen ',' Fifthteen ',' Sixteen ',' Seventeen ',' Eighteen ',' Nineteen ']
puluh = ['',' Ten ',' Twenty ',' Thirty ', ' Forty ',' Fifty ',' Sixty ',' Seventy ',' Eighty ',' Ninety ']
kata  = ['',' One ',' Two ',' Three ',' Four ',' Five ',' Six ',' Seven ',' Eight ',' Nine ']

def number(x):
    if 10 < x <= 19 :
        return belas[x-10]
    elif x < 10 :
        return kata[x]
    elif x >= 1_000_000_000:
        return number(x // 1_000_000_000) + ' Billion ' + (number(x % 1_000_000_000) if x % 1_000_000 != 0 else '')
    elif x >= 1_000_000:
        return number(x // 1_000_000) + ' Million ' + (number(x % 1_000_000) if x % 1_000_000 != 0 else '')
    elif x >= 1_000:
        return number(x// 1_000) + ' Thousand ' + (number(x % 1_000) if x % 1_000 != 0 else '')
    elif x >= 100:
        return number(x// 100) + ' Hundred ' + (number(x % 100) if x % 100 != 0 else '')
    elif x >= 20 :
        return puluh[x//10] + ' ' + (number(x % 10) if x % 10 != 0 else '')

    else:
        if x == 11:
            return ' Eleven '
        elif x == 10:
            return' Ten '
        else:
            return

while True:
    os.system('cls')
    try:
        x = int(input(' HEYYY YOO INPUT NUMBER = '))
        print(f'{x:,} iiiiisssssssss {number(x)}')
    except:
        print('YOOO SERIOUSLY LA ! NUMBER LOH !! NO PLAYING PLAYING ')
    
    while True:
        lanjut = input('Continue [y/n] ? ')
        if lanjut in ('y', 'n'):
            break
    
    if lanjut == 'n':
        break
    
    os.system('pause')