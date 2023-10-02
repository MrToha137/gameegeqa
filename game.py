from random import randint
from random import uniform
from time import sleep
from actions import *
from data import *

# записывает игрока
name = input('Введи своё имя, путник и добро пожаловать в مستحيل: ')
player['name'] = name


while True:
    action = int(input(f'Выберите действие: \n1. Бой \n2. Тренировка\n3. Магазин'))
    print()
    if action == 1:
        fight()
    elif action == 2:
        train()
    elif action == 3:
        shop()    
    


