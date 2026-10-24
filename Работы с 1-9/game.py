# Игра этап 1

# ================================================
# ИГРА «ЛЕДЯНАЯ ПЕЩЕРА: ХОЛОДНЫЙ ГРОТ»
# Автор: Лагутина Надежда
# Дата: сентябрь 2026
#
# Пункт 4 — «согреть дыханием»: герой пытается 
# отогреть замёрзший механизм. Пока пункт только 
# выводится в меню — обрабатывать его будем 
# на третьем занятии.
# ================================================


import random

title = "ЛЕДЯНАЯ ПЕЩЕРА: ХОЛОДНЫЙ ГОРОДОК"
frame = "=" * 35
print(frame)
print(" " + title + " ")
print(frame)
print()
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в пещеру. Стены покрыты льдом, Изо рта идёт густой пар.")
print()

print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")

while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        endurance = int(input())
        
        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
        if strength < 0 or agility < 0 or endurance < 0:
            raise ValueError("Остальные характеристики не могут быть отрицательными")
        if agility > health * 2:
            raise ValueError("Ловкость не может превышать удвоенное здоровье")
            
        break
    except ValueError as e:
        print(f"Ошибка: {e}. Введите все четыре числа снова:")

base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = (health // 5) + endurance

print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Выносливость: {endurance}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил: {stamina}")
print()

# --- ФУНКЦИИ ---

def hero_hit(strike_n):
    """
    Урон героя в удар номер strike_n.
    Возвращает пару (hit, crit): урон и признак критического удара.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False

def fight(enemy, hero_health):
    """
    Бой с enemy до гибели одного из двоих.
    Печатает строки раундов. Возвращает (rounds, won, hero_health).
    """
    enemy_hp = enemies[enemy]
    rounds = []
    round_n = 0
    print(f"Ты спускаешься по ступеням. Из темноты появляется {enemy}!")
    
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
        enemy_hp -= hit
        
        line = f"Раунд {round_n}: герой наносит {hit:.1f}"
        if crit:
            line += " — критический!"
            
        if enemy_hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            blow = random.randint(2, 6)
            hero_health -= blow
            line += f" Здоровье врага: {enemy_hp:.1f}. Враг бьет в ответ на {blow}."
            rounds.append([round_n, hit, blow])
            
        print(line)
        
    return rounds, enemy_hp <= 0, hero_health

def print_leaderboard(log_data):
    """
    Печатает топ-3 раундов по урону героя и рекорд врага.
    Возвращает None.
    """
    if not log_data:
        print("Ты еще не сражался.")
        return
        
    top = sorted(log_data, key=lambda r: r[1], reverse=True)[:3]
    print("Таблица лидеров (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
    worst = max(log_data, key=lambda r: r[2])
    print(f"Самый сильный удар врага: {worst[2]} (раунд {worst[0]}).")

def print_run_summary(log_data):
    """
    Печатает итог забега: суммарный и средний урон героя.
    Возвращает None. Безопасна на пустом журнале.
    """
    total = sum(r[1] for r in log_data)
    rounds = len(log_data)
    if rounds > 0:
        print(f"Урон: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f}.")
    else:
        print("В этом забеге не было боев.")

# --- ГЛАВНЫЙ ЦИКЛ ---

running = True
actions = 0
menu_last = 8
outcome = "прерывание"

enemies = {
    "ледяной скелет": 40,
    "пещерный паук": 20,
    "замерзший зомби": 65,
    "снежный йети": 180
}
log = []

try:
    while running:
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - достать грелку")
        print("5 - посмотреть на ледяные колонны")
        print("6 - тренировка")
        print("7 - спуститься глубже")
        print("8 - таблица лидеров")
        print("0 - выйти из подземелья")
        print()
        
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Такого пункта нет. Введи номер пункта из меню:")
                continue
                
            if 0 <= menu_number <= menu_last:
                break
            print("Такого пункта нет. Введи номер пункта из меню:")
            
        match choice:
            case "0":
                print("Ты поднимаешься обратно к свету. Ледяная пещера остаётся позади.")
                outcome = "выход"
                running = False
            case "1":
                print("Ты осмотрелся. Вокруг только лёд и стены пещеры в далеке виднеется проход.")
            case "2":
                cost = 2
                if stamina >= cost:
                    stamina -= cost
                    print("Ты осторожно идёшь вперёд. Лёд хрустит под ногами.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — ты идёшь на одном упорстве.")
            case "3":
                stamina = stamina + 3
                print("Ты присел отдохнуть и немного согрелся у стены.")
            case "4":
                stamina = stamina - 1
                health = health + 5
                print("Ты достал грелку. Стало теплее, здоровье немного восстановилось.")
            case "5":
                print("Ты смотришь на ледяные колонны. Они переливаются в свете факела и манят тебя.")
            case "6":
                strikes = 6
                total_damage = 0.0
                crit_count = 0
                stamina = stamina - 3 
                
                print("Ты подходишь к ледяной глыбе, которая пока евляется твоим главным противником.")
                print("Она стоит здесь с тех пор, как сюда приходил последний искатель.")
                print()
                print(f"Наносишь {strikes} ударов.")
                
                for i in range(1, strikes + 1):
                    hit_damage, crit = hero_hit(i)
                    if crit:
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} урона — критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f} урона")
                    total_damage += hit_damage
                    
                print()
                print(f"Итог: {strikes} ударов, критических ударов: {crit_count}")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")
            case "7":
                if not enemies:
                    print("Ты спускаешься по ступеням, но подземелье пусто.")
                else:
                    enemy = random.choice(list(enemies.keys()))
                    rounds, won, health = fight(enemy, health)
                    
                    for r in rounds:
                        log.append(r)
                        
                    if won:
                        del enemies[enemy]
                        print(f"{enemy.capitalize()} побежден! В подземелье осталось врагов: {len(enemies)}.")
                        print(f"Бой: {len(rounds)} раундов.")
                    elif health <= 0:
                        print(f"В этом бою {enemy} одолел тебя.")
            case "8":
                print_leaderboard(log)

        if health <= 0:
            print(f"{hero_name} падает без сил. Пещера забирает ещё одного искателя приключений.")
            outcome = "гибель"
            running = False
            
        if running:
            actions += 1
            
        print()
        print(f"Здоровье: {health} Запас сил: {stamina} Врагов осталось: {len(enemies)}")
        print()

except KeyboardInterrupt:
    print()
    print("Ты резко останавливаешься и решаешь покинуть эти места.")

finally:
    print(frame)
    if outcome == "гибель":
        print(f"Твое путешествие окончено, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Ты благополучно выбрался из пещеры, {hero_name}! Действий совершено: {actions}.")
        print(f"Хорошего пути, искатель приключений!")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
        
    print_run_summary(log)
    print(frame)