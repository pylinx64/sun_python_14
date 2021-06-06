import random
import time
import os
import sys


# размер поля, не менять (!); 
# глобальная зажержка (по умолчанию = 0.3); 
# всегда ходить первым (по умолчанию = False);
# цвет игры (по умолчанию желтый);
# глубина просчетов;
# символ пустого поля (менять только на поддерживаемые);
# описание переменных смотри в настройках;
N = 3
RATE = .3
FIRST = False
COLOUR = 'E'
MAX_DEPTH = 5
EMPTY_CHAR = '□'


#-----------------------design game-------------------------------------
def pb_start():
    '''
    Прогресс-бар для начала игры
    '''
    # 20 - длина полосы загрузки (~ скорость)
    targetArray = ["#" for x in range(20)]
    stringArray = ["" for x in range(20)]
    
    
    print('LOADING GAME...')
    i = 0
    while i < len(targetArray):
        if stringArray[i] != targetArray[i]:
            stringArray[i] = chr(random.randint(32, 68))
        
        if stringArray[i] == targetArray[i]:
            i += 1
            
        x = 0
        print('\r', end='')
        while x < len(stringArray):
            print(stringArray[x], end='')
            x += 1
        # скрость загрузки
        time.sleep(RATE / 125)
        print(' '+ str(i*5) + ' %', end='')
    print()
    
def pb_loading():
    '''
    Прогресс-бар для загрузки игры
    '''
    stringArray = ["." for x in range(3)]
    
    for i in range(0, 2):
        i = 0
        while i < 2:
            stringArray[i] = "0"
            #print(stringArray[i], end='')
            
            x = 0
            print('\r', end='')
            while x < len(stringArray):
                print(stringArray[x], end='')
                x += 1
            stringArray[i] = "."
            # скрость загрузки
            time.sleep(RATE / 4)
            i += 1
        
    print()
    
def infoHelp():
    '''
    Показывает всю информацию для настроек
    '''
    print('Настройка и параметр настройки указываются через пробел.')  
    print('Сброс настроек по умолчанию (reset)') 
    print('Настройки цвета (colour [параметр] или colour [параметр1][параметр2], напр. colour 0A или colour B): ') 
    print('\t- ', end='')
    #список возможных цветов (консоль Windows)
    colours = [str(d) for d in range(0, 10)] + [chr(d) for d in range(65, 71)]
    [print(d, end=';') for d in colours]
    print('\r\n', end='')
    print('Настройки скорости игры (rate [параметр], напр. rate 0.3): ') 
    print('\t- 0; от 0.01 до 4')
    print('Настройки игрок ходит всегда первым (first [параметр], напр. first false): ') 
    print('\t- true; false') 
    print('Для выхода из настроек напишите: ')
    print('\t- quit; q; exit; close') 
    
def infoGame():
    '''
    показывает подсказки игроку в меню 
    '''
    print('Для продолжение игры введите: ') 
    print('\t- lf; да; д; yes; y; пробел')
    print('Для выхода из игры введите: ') 
    print('\t- нет; н; ytn; no; n; q; quit; close; exit')
    print('Для настроек введите: ') 
    print('\t- настройки; setting')

def infoEndGame():
    '''
    Печатает сообщения для игрока в конце игры
    '''
    os.system('cls||clear')
    print('Close...         See you again my computer friend! Create by Pypylex64™')
    time.sleep(RATE*2)
    print()
    print('#######################################################################')
    print('#github.com: https://github.com/Pypylex64                             #')
    print('#soundcloud.com: https://soundcloud.com/dinopi_music                  #')
    print('#youtube.com: https://www.youtube.com/channel/UCMcUGaWm-2x0ElT0F3w_FCg#')
    print('#######################################################################')
#-----------------------design game-------------------------------------
#-----------------------setting game------------------------------------
def settingGame():
    '''
    Найстройки для игрока: 
    помощь, цвет, ход первым, fast режим, сбросить
    ''' 
    # настройки - изменение глобальных переменных
    global RATE, COLOUR, FIRST
    # просто удобно
    exit_str = ['quit', 'q', 'exit','close']
    flLoopInput = True
    while flLoopInput:
        try:
            print('-> Настройка (help - для справки): ', end='')
            setting = input()
            if 'help' in setting[:4].lower():
                infoHelp()
                input('-> Для продолжения нажмите Enter...')
                continue
            elif 'colour' in setting[:6].lower():
                if setting[7:] in colours:
                    COLOUR = setting[7:8]
                    continue
                else:
                    continue
            elif 'rate' in setting[:4].lower():
                RATE = float(setting[5:10])
                continue
            elif 'first' in setting[:5].lower():
                FIRST = True if setting[6:10].lower() in 'true' else False
                continue
            elif 'reset' in setting[:5].lower():
                RATE = 0
                FIRST = False
                COLOUR = 'A' 
                continue
            # через else странно работает ( когда были elif)
            elif setting[:4].lower() in exit_str:
                break
            pb_loading()
            os.system('cls||clear')
        except:
            print('Ошибка ввода. Попроблуйте снова!')
#-----------------------setting game------------------------------------
#-----------------------function game-----------------------------------
def checkLetter(x, y, FIELD):
    '''
    Проверяет, не стоит ли на клетке уже символ X или 0
    '''
    if FIELD[x*N+y] == 'X' or FIELD[x*N+y] == '0': return True

def isFirst():
    '''
    Рандомно определяет кто будет ходить первым
    True - игрок
    ''' 
    return random.choice([True, False])

def inputPlayer(FIELD):
    '''
    Вводит пользовательские данные (ход игрока)
    '''
    # вводит координаты, пока не введет правильно
    flLoopInput = True
    
    while flLoopInput:
        try:
            print('-> Введите номер клетки через пробел (напр. 2 3 - 2 рядок, 3 - столбец): ', end='')
            x, y = input().split()
            
            # игра перезапускается
            if 'game' in x and 'reset' in y:
                return ('game', 'reset')

            # предпологаем что пользоватедб вводит координаты от 1 до N
            x = int(x) - 1
            y = int(y) - 1
            
            if x < 0  or x >= N or y < 0  or y >= N :
                print('Координаты выходят за пределы поля')
                continue
                  
            if checkLetter(x, y, FIELD):
                print('Эта клетка уже занята!')
                continue
           
            flLoopInput = False
            return (x, y)
        
        except:
            print('Ошибка ввода. Попробуйте заново. ')
            print('(если хотите выйти/перезапустить игру, то напишите game reset через пробел)')
    
def inputComputerSimple(FIELD):
    '''
    Вводит данные компьютера рандомно (ход ПК) или симуляция ходов
    '''
    flLoopInput = True
    while flLoopInput:
        x, y = (random.randint(0, 2), random.randint(0, 2))
        
        # TODO: не забыть про проверку символов 
        if checkLetter(x, y, FIELD):
            continue
            
        return (x, y)
        
def search(letter, FIELD_ORIGINAL, alpha, beta, depth):
    '''
    Алгоритм ищет лучший ход (альфа-бета),
    depth - cложность (глубина рассчетов)
    '''

    # определим фигуру противника
    ops = 'X' if '0' in letter else '0'

    # проверка статуса для симуляции игры
    status = isFinish(FIELD_ORIGINAL)

    # если замкнутая линия или ничья вернем оценку
    # -1 - поражение AI, 1 - победа AI, 0 - ничья
    if (status == -1 and ops == 'X') or (status == -2 and ops == '0'):
        alpha = -1
        return alpha
    
    elif status == 0:
        alpha = 0
        return alpha
   
    elif (status == -1 and ops == '0') or (status == -2 and ops == 'X'):
        alpha = 1
        return alpha
    
    # перебераем все клетки в симуляции
    for i in range(0, N):
        for j in range(0, N):
            if FIELD_ORIGINAL[i*N+j] == EMPTY_CHAR:
                # делаем ход
                FIELD_ORIGINAL[i*N+j] = letter
                # подсчет
                tmp = -search(ops, FIELD_ORIGINAL, -beta, -alpha, depth+1)
                if tmp > alpha:
                    alpha = tmp 
                    if depth == 0:
                        # выдаем лучшие координаты
                        return i, j
                        
                # восстанавливаем позицию
                FIELD_ORIGINAL[i*N+j] = EMPTY_CHAR
                # отсечение, чтобы не перебирать все ходы
                if alpha >= beta:
                    break
                    
    return alpha
     
def moveComputer(letter, FIELD):
    '''
    Выполняет ход компьютера (ход ПК)
    '''
    print('ход компьютера...')
    pb_loading()
    x ,y = search(letter, FIELD, -1, 1, 0)
    #x, y = inputComputerSimple(FIELD)
    FIELD[x*N+y] = letter

    return FIELD
    
def movePlayer(letter, FIELD):
    '''
    Выполняет ход игрока 
    '''
    print('ход игрока:')
    x, y = inputPlayer(FIELD)
    FIELD[x*N+y] = letter
    pb_loading()
    return FIELD

def show_gamemode(FIELD):
    '''
    Показывает поле для игры
    '''
    print('------------')
    for i in range(0, N):
        for j in range(0, N):
            if FIELD[i*N+j] == 'X':
                print(str(FIELD[i*N+j]).rjust(3), end='' )
            elif FIELD[i*N+j] == '0':
                print(str(FIELD[i*N+j]).rjust(3), end='' ) 
            else: 
                print(str(FIELD[i*N+j]).rjust(3), end='' )
        print()
    print('------------')
    
def isFinish(FIELD):
    '''
    Проверяет текущее состояние игры
    Есть ли замкнутая линия крестиков то победа
    Есть ли замкнутая линия ноликов то победа
    Если нету клеток для ввода то ничья
    в противном случае игра продолжается
    '''
    if FIELD[0] == 'X' and FIELD[1] == 'X' and FIELD[2] == 'X': return -1
    elif FIELD[3] == 'X' and FIELD[4] == 'X' and FIELD[5] == 'X': return -1
    elif FIELD[6] == 'X' and FIELD[7] == 'X' and FIELD[8] == 'X': return -1
    elif FIELD[0] == 'X' and FIELD[3] == 'X' and FIELD[6] == 'X': return -1
    elif FIELD[1] == 'X' and FIELD[4] == 'X' and FIELD[7] == 'X': return -1
    elif FIELD[2] == 'X' and FIELD[5] == 'X' and FIELD[8] == 'X': return -1
    elif FIELD[0] == 'X' and FIELD[4] == 'X' and FIELD[8] == 'X': return -1
    elif FIELD[6] == 'X' and FIELD[4] == 'X' and FIELD[2] == 'X': return -1

    elif FIELD[0] == '0' and FIELD[1] == '0' and FIELD[2] == '0': return -2
    elif FIELD[3] == '0' and FIELD[4] == '0' and FIELD[5] == '0': return -2
    elif FIELD[6] == '0' and FIELD[7] == '0' and FIELD[8] == '0': return -2
    elif FIELD[0] == '0' and FIELD[3] == '0' and FIELD[6] == '0': return -2
    elif FIELD[1] == '0' and FIELD[4] == '0' and FIELD[7] == '0': return -2
    elif FIELD[2] == '0' and FIELD[5] == '0' and FIELD[8] == '0': return -2
    elif FIELD[0] == '0' and FIELD[4] == '0' and FIELD[8] == '0': return -2
    elif FIELD[6] == '0' and FIELD[4] == '0' and FIELD[2] == '0': return -2

    elif EMPTY_CHAR not in FIELD: return 0
    
    else: return 1
    
def checkWin(game_status, who_first):
    '''
    Проверяет кто выиграл
    '''
    if who_first:
        if game_status == -1:
            print('-> ПОБЕДИЛ ИГРОК!')
        elif game_status == -2:
            print('-> ПОБЕДИЛ КОМПЬЮТЕР!')
        else:
            print('-> НИЧЬЯ!')
    else:
        time.sleep(RATE)
        if game_status == -2:
            print('-> ПОБЕДИЛ ИГРОК!')
        elif game_status == -1:
            print('-> ПОБЕДИЛ КОМПЬЮТЕР!')
        else:
            print('-> НИЧЬЯ!')
    
def startGame(FIELD):
    '''
    Основной цикл игры
    '''
    if FIRST:
        # настройка всегда игрок первый
        who_first = True
    else:
        who_first = isFirst()
    game_status = isFinish(FIELD)         # состояние игры
    
    os.system('cls||clear')
    time.sleep(RATE * 2)
    show_gamemode(FIELD)
    time.sleep(RATE)
    
    if who_first:
        print('Игрок ходит первым!')
        pb_loading()
    else:
        print('Компьютер ходит первым!')
        
    time.sleep(RATE)
    
    # основной цикл
    # игра меняется, в зависимости кто будет играть первым (gamemod_1 = Игрок первый)
    if who_first:
        turn = 'move_player'     # меняет очередь игрок/ПК
        while game_status > 0:
            time.sleep(RATE)
            os.system('cls||clear')
            show_gamemode(FIELD)
            if turn == 'move_player':
                # поможет человеку выйти в настройки
                try:
                    movePlayer('X', FIELD)
                    turn = 'move_pc'
                except:
                    pb_loading()
                    os.system('cls||clear')
                    return None 
            else:
                moveComputer('0', FIELD)
                turn = 'move_player'
            game_status = isFinish(FIELD)
            
    else:
        turn = 'move_pc'     # Первый ход ПК
        while game_status > 0:
            time.sleep(RATE)
            os.system('cls||clear')
            show_gamemode(FIELD)
            if turn == 'move_pc':
                moveComputer('X', FIELD)
                turn = 'move_player'
            else:
                try:
                    movePlayer('0', FIELD)
                    turn = 'move_pc'
                except:
                    pb_loading()
                    os.system('cls||clear')
                    return None
            game_status = isFinish(FIELD)
            
    pb_loading()
    os.system('cls||clear')
    show_gamemode(FIELD)
    checkWin(game_status, who_first) 
    time.sleep(RATE*3)
#-----------------------function game-----------------------------------


#-----------------------start game--------------------------------------
# для удобства (можно запихать много ключевых слов, хотя хз зачем)
message_again = ['lf', 'да', 'д', 'yes', 'y', ' ']
message_end = ['нет', 'н', 'ytn', 'no', 'n', 'q', 'quit', 'close', 'exit']
message_setting = ['настройки', 'setting']
message_help = ['help', 'h', 'помощь']

# Проверяет статус игры: 1 - новая, 2 - заново, 3 - настройки/помощь/выход
againe = 1
while againe > 0:
    if againe == 1:
        os.system("color "+COLOUR)
        pb_loading()
        # очищает поле для удобной игры
        os.system('cls||clear')
        time.sleep(RATE)
        pb_start() 
        FIELD = [EMPTY_CHAR]*N*N 
        startGame(FIELD)
        againe = 3
    elif againe == 2:
        FIELD = [EMPTY_CHAR]*N*N 
        startGame(FIELD)
        againe = 3
    else:
        input('-> Для продолжения нажмите Enter...')
        pb_loading()
        os.system('cls||clear')
        print('-> Желаете сыграть снова (да(пробел)/нет/help)?: ', end='')
        answer = input()         
        pb_loading()
        os.system('cls||clear')
        time.sleep(RATE)
        if answer.lower() in message_again:
            againe = 2
        elif answer.lower() in message_help:
            infoGame()
        elif answer.lower() in message_setting:
            settingGame()
            # при изменении настроек игра перезагружается
            againe = 1
        elif answer.lower() in message_end:
            againe = 0

infoEndGame()
#os.system('exit')
#-----------------------end game---------------------------------------- 
