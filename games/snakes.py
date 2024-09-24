import time
import os
import random

# 游戏区域大小
WIDTH = 80
HEIGHT = 20


# 定义蛇的节点类
class SnakeNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None


# 绘制游戏场景
def draw_game(snake_head, food):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i == 0 or i == HEIGHT - 1 or j == 0 or j == WIDTH - 1:
                print('#', end='')
            else:
                is_snake = False
                node = snake_head
                while node:
                    if node.x == j and node.y == i:
                        print('O', end='')
                        is_snake = True
                        break
                    node = node.next
                if not is_snake:
                    if j == food.x and i == food.y:
                        print('X', end='')
                    else:
                        print(' ', end='')
        print()


# 移动蛇
def move_snake(snake_head, direction):
    new_head = SnakeNode(snake_head.x, snake_head.y)
    if direction == 'up':
        new_head.y -= 1
    elif direction == 'down':
        new_head.y += 1
    elif direction == 'left':
        new_head.x -= 1
    elif direction == 'right':
        new_head.x += 1

    new_head.next = snake_head
    return new_head


# 检查游戏是否结束
def is_game_over(snake_head):
    if snake_head.x == 0 or snake_head.x == WIDTH - 1 or snake_head.y == 0 or snake_head.y == HEIGHT - 1:
        return True

    node = snake_head.next
    while node:
        if snake_head.x == node.x and snake_head.y == node.y:
            return True
        node = node.next

    return False


# 生成食物
def generate_food(snake_head):
    while True:
        food = SnakeNode(random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2))
        node = snake_head
        is_food_on_snake = False
        while node:
            if node.x == food.x and node.y == food.y:
                is_food_on_snake = True
                break
            node = node.next

        if not is_food_on_snake:
            break

    return food


# 游戏主循环
def game_loop():
    # 初始化蛇
    snake_head = SnakeNode(WIDTH // 2, HEIGHT // 2)
    snake_head.next = SnakeNode(snake_head.x - 1, snake_head.y)

    food = generate_food(snake_head)
    direction = 'right'

    while not is_game_over(snake_head):
        draw_game(snake_head, food)
        # 获取用户输入
        key = input()
        if key in ['w', 'W'] and direction != 'down':
            direction = 'up'
        elif key in ['s', 'S'] and direction != 'up':
            direction = 'down'
        elif key in ['a', 'A'] and direction != 'right':
            direction = 'left'
        elif key in ['d', 'D'] and direction != 'left':
            direction = 'right'

        new_head = move_snake(snake_head, direction)
        if new_head.x == food.x and new_head.y == food.y:
            food = generate_food(new_head)
        else:
            # 移除蛇尾
            node = new_head
            while node.next.next:
                node = node.next
            node.next = None

        snake_head = new_head
        time.sleep(0.1)

    print("游戏结束！")


if __name__ == "__main__":
    game_loop()
