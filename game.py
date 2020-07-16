player_name = input("Введите имя первого игрока: ")
enemy_name = input("Введите имя второго игрока: ")

import random

player = {
    'name' : player_name,
    'health' : 150,
    'damage' : random.randrange(75),
    'armor' : random.randrange(10,20) / 10
}
enemy = {
    'name' : enemy_name,
    'health': 150,
    'damage': random.randrange(75),
    'armor' : random.randrange(10,20) / 10
}

def attack(user):
    def armor(user):
        if user == who_first_name:
            result = who_first_name['damage'] / who_second['armor']
            result = round(result, 2)
            print(f'{who_second["name"]}, вы заблокировали {who_first_name["armor"]} целых от удара\nУрон составил {result}')
            return result
        elif user == who_second:
            result = who_second['damage'] / who_first_name['armor']
            result = round(result, 2)
            print(f'{who_first_name["name"]}, вы заблокировали {who_first_name["armor"]} целых от удара\nУрон составил {result}')
            return result
    if user == who_first_name:
        health_result = who_second['health'] - armor(who_first_name)
        health_result = round(health_result, 2)
        who_second['health'] = health_result
    elif user == who_second:
        health_result = who_first_name['health'] - armor(who_second)
        health_result = round(health_result, 2)
        who_first_name['health'] = health_result

print(f'{player["name"]}, {enemy["name"]}, добро пожаловать в FIGHT CLUB!')
print("Чтобы узнать кто ходит первым, вы должны угадать число...")
who_first = random.randrange(5)
# print(who_first)
i = 0
who_first_name = str()
who_second = str()
while i != 5:
    player_one = int(input(player['name'] + " угадайте число от 0 до 5: "))
    if who_first == player_one:
        print(f"{player['name']} вы будите ходить первым!")
        who_first_name = player
        break

    elif who_first != player_one:
        player_two = int(input(enemy['name'] + " угадайте число от 0 до 5: "))
        if who_first == player_two:
            print(f"{enemy['name']}, вы будите ходить первым!")
            who_first_name = enemy
            break
        else:
            i +=1
            continue
if who_first_name == player:
    who_second = enemy
elif who_first_name == enemy:
    who_second = player
print("Запомните, чтобы аттаковать напишите '1'")
while who_first_name['health'] > 0 and who_second['health'] > 0:
    print(f'Ваша жизнь = {who_first_name["health"]}\nВаша сила аттаки = {who_first_name["damage"]}')
    player_choice = int(input(""))
    if player_choice == 1:
        attack(who_first_name)
        who_first_name["damage"] = random.randrange(75)
        who_first_name["armor"] = random.randrange(10,20) / 10
    else:
        print("ERROR 404")
    print(f'Ваша жизнь = {who_second["health"]}\nВаша сила аттаки = {who_second["damage"]}')
    player_choice = int(input(""))
    if player_choice == 1:
        attack(who_second)
        who_second["damage"] = random.randrange(75)
        who_second["armor"] = random.randrange(10,20) / 10
else:
    if who_first_name['health'] < 0:
        print(f"{who_second['name']}, вы выйграли!!")
    elif who_second['health'] < 0:
        print(f"{who_first_name['name']}, вы выйграли!!")
print("Спасибо за игру!")
