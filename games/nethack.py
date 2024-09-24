import random
import curses

# 游戏地图大小
MAP_WIDTH = 80
MAP_HEIGHT = 20


# 玩家类
class Player:
    def __init__(self):
        self.x = MAP_WIDTH // 2
        self.y = MAP_HEIGHT // 2
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.defense = 5
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.equipped_weapon = None
        self.equipped_armor = None

    def equip_item(self, item):
        if isinstance(item, Weapon):
            self.equipped_weapon = item
            self.attack += item.damage
        elif isinstance(item, Armor):
            self.equipped_armor = item
            self.defense += item.defense_bonus


# 怪物类
class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = random.randint(30, 60)
        self.max_health = self.health
        self.attack = random.randint(5, 15)
        self.defense = random.randint(2, 8)
        self.type = random.choice(["Goblin", "Orc", "Skeleton"])


# 物品类
class Item:
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, defense_bonus):
        super().__init__(name)
        self.defense_bonus = defense_bonus


# 生成游戏地图
def generate_map():
    return [['.' for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]


# 绘制游戏画面
def draw_map(stdscr, game_map, player, monsters):
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if (x, y) == (player.x, player.y):
                stdscr.addstr(y, x, '@')
            else:
                for monster in monsters:
                    if (x, y) == (monster.x, monster.y):
                        stdscr.addstr(y, x, monster.type[0])
                        break
                else:
                    stdscr.addstr(y, x, cell)
    stdscr.addstr(MAP_HEIGHT, 0,
                  f"Health: {player.health}/{player.max_health}  Level: {player.level}  Experience: {player.experience}")
    if player.equipped_weapon:
        stdscr.addstr(MAP_HEIGHT + 1, 0,
                      f"Equipped Weapon: {player.equipped_weapon.name} (+{player.equipped_weapon.damage} damage)")
    if player.equipped_armor:
        stdscr.addstr(MAP_HEIGHT + 2, 0,
                      f"Equipped Armor: {player.equipped_armor.name} (+{player.equipped_armor.defense_bonus} defense)")
    stdscr.refresh()


# 移动玩家
def move_player(direction, player, game_map, monsters):
    new_x, new_y = player.x, player.y
    if direction == curses.KEY_UP:
        new_y -= 1
    elif direction == curses.KEY_DOWN:
        new_y += 1
    elif direction == curses.KEY_LEFT:
        new_x -= 1
    elif direction == curses.KEY_RIGHT:
        new_x += 1
    if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
        target_cell = game_map[new_y][new_x]
        if target_cell == '.':
            player.x, player.y = new_x, new_y
        elif target_cell == 'M':
            for monster in monsters:
                if (monster.x, monster.y) == (new_x, new_y):
                    combat(player, monster)
                    if monster.health <= 0:
                        monsters.remove(monster)
                        player.experience += random.randint(10, 20)
                        drop_item_chance = random.randint(1, 100)
                        if drop_item_chance <= 30:
                            item = generate_random_item()
                            player.inventory.append(item)
                            stdscr.addstr(MAP_HEIGHT + 3, 0, f"You found a {item.name}!")
                        if player.experience >= player.level * 100:
                            level_up(player)
                    break


# 战斗函数
def combat(player, monster):
    player_damage = max(0, player.attack - monster.defense)
    monster_damage = max(0, monster.attack - player.defense)
    monster.health -= player_damage
    player.health -= monster_damage


# 升级函数
def level_up(player):
    player.level += 1
    player.health += 20
    player.max_health += 20
    player.attack += 5
    player.defense += 3
    player.experience %= player.level * 100


# 生成随机物品
def generate_random_item():
    item_type = random.choice(["weapon", "armor"])
    if item_type == "weapon":
        return Weapon(f"Rusty Sword", random.randint(5, 10))
    else:
        return Armor(f"Leather Armor", random.randint(2, 5))


# 主游戏循环
def main(stdscr):
    stdscr.clear()
    game_map = generate_map()
    player = Player()
    monsters = [Monster(random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)) for _ in range(10)]
    while True:
        draw_map(stdscr, game_map, player, monsters)
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('i'):
            show_inventory(stdscr, player)
        else:
            move_player(key, player, game_map, monsters)
            if player.health <= 0:
                stdscr.addstr(MAP_HEIGHT + 1, 0, "Game Over!")
                stdscr.refresh()
                stdscr.getch()
                break


def show_inventory(stdscr, player):
    stdscr.clear()
    stdscr.addstr(0, 0, "Inventory:")
    for index, item in enumerate(player.inventory):
        stdscr.addstr(index + 1, 0, f"{index + 1}. {item.name}")
    stdscr.addstr(len(player.inventory) + 1, 0, "Enter item number to equip or 'q' to close.")
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key.isdigit():
            item_index = int(chr(key)) - 1
            if 0 <= item_index < len(player.inventory):
                item = player.inventory[item_index]
                player.equip_item(item)
                stdscr.addstr(len(player.inventory) + 2, 0, f"Equipped {item.name}.")
    stdscr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
