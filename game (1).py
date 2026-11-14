import random

title = "ЛЕДЯНАЯ ПЕЩЕРА"
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
max_health = health
max_stamina = stamina

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

def hero_hit(strike_n):
    """
    Урон героя в удар номер strike_n.
    Возвращает пару (hit, crit): урон и признак критического удара.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False

def fight(enemy, hero_health, bonus=0):
    """
    Бой с enemy до гибели одного из двоих.
    bonus — надбавка к урону героя, по умолчанию 0.
    Надбавка прибавляется к базовому урону до удвоения критическим ударом.
    Печатает строки раундов.
    Возвращает кортеж (rounds, won, hero_health, loot).
    """
    enemy_hp = enemies[enemy]
    rounds = []
    round_n = 0
    print(f"Ты спускаешься по ступеням. Из темноты появляется {enemy}!")
    
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
        hit = hit + bonus
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
        
    won = enemy_hp <= 0
    if won:
        loot = 10 + 5 * round_n
    else:
        loot = 0
        
    return rounds, won, hero_health, loot

def buy(price, gold, quantity=1):
    """
    Покупает quantity штук товара ценой price за золото gold.
    quantity по умолчанию 1. Возвращает (gold_left, ok): остаток
    золота и признак успешной покупки. Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False

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

running = True
actions = 0
menu_last = 9
outcome = "прерывание"

enemies = {
    "ледяной скелет": 60,
    "пещерный паук": 30,
    "замерзший зомби": 85,
    "снежный йети": 200
}
log = []
gold_total = 0
ability_bonus = 0

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
        print("9 - магазин")
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
                stamina = min(stamina + 3, max_stamina)
                print("Ты присел отдохнуть и немного согрелся у стены.")
            case "4":
                stamina = stamina - 1
                health = min(health + 5, max_health)
                print("Ты достал грелку. Стало теплее, здоровье немного восстановилось.")
            case "5":
                print("Ты смотришь на ледяные колонны. Они переливаются в свете факела.")
            case "6":
                strikes = 6
                total_damage = 0.0
                crit_count = 0
                stamina = stamina - 3 
                
                print("Ты подходишь к ледяной глыбе, которая пока является твоим главным противником.")
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
                    rounds, won, health, loot = fight(enemy, health, bonus=ability_bonus)
                    
                    for r in rounds:
                        log.append(r)
                        
                    if won:
                        gold_total += loot
                        del enemies[enemy]
                        print(f"{enemy.capitalize()} побежден! В подземелье осталось врагов: {len(enemies)}. Добыча: {loot} золота.")
                        print(f"Бой: {len(rounds)} раундов.")
                    elif health <= 0:
                        print(f"В этом бою {enemy} одолел тебя.")
            case "8":
                print_leaderboard(log)
            case "9":
                print("Магазин:")
                print("1 - зелье (+10 здоровья): 10 золота")
                print("2 - масло для факела (+5 запаса сил): 15 золота")
                print("3 - боевой эликсир (+2 к урону до конца забега): 40 золота")
                print("Номер предмета (0 — ничего не покупать):")
                item = input()
                prices = (10, 15, 40)
                names = ("зелье", "масло для факела", "боевой эликсир")
                
                if item in ("1", "2", "3"):
                    price = prices[int(item) - 1]
                    name = names[int(item) - 1]
                    print("Количество:")
                    qty_line = input()
                    
                    if qty_line == "":
                        qty = 1
                        gold_total, ok = buy(price, gold_total)
                    else:
                        qty = int(qty_line)
                        gold_total, ok = buy(price, gold_total, quantity=qty)
                        
                    if ok:
                        if item == "1":
                            health = min(health + 10 * qty, max_health)
                        elif item == "2":
                            stamina = min(stamina + 5 * qty, max_stamina)
                        else:
                            ability_bonus += 2 * qty
                            
                        print(f"Куплено {qty} {name} за {price * qty} золота. Осталось золота: {gold_total}.")
                    else:
                        print(f"Недостаточно золота: нужно {price * qty}, есть {gold_total}.")
                elif item != "0":
                    print("Такого предмета нет в магазине.")

        if health <= 0:
            print(f"{hero_name} падает без сил. Пещера забирает ещё одного искателя приключений.")
            outcome = "гибель"
            running = False
            
        if running:
            actions += 1
            
        print()
        print(f"Здоровье: {health} Запас сил: {stamina} Врагов осталось: {len(enemies)} Золото: {gold_total}")
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