import math
import os
import time


def clear_screen():
    # Clear the screen in a cross-platform way.
    os.system('cls' if os.name == 'nt' else 'clear')


def mul(v, m):
    res = []
    for x, y, z in v:
        x_rot = x * m[0][0] + y * m[0][1] + z * m[0][2]
        y_rot = x * m[1][0] + y * m[1][1] + z * m[1][2]
        z_rot = x * m[2][0] + y * m[2][1] + z * m[2][2]
        res.append((x_rot, y_rot, z_rot))
    return res


def draw_cube(angle):
    # Cube vertices
    r = 15  # Cube size
    vertices = [
        (-r, -r, -r),
        (-r, -r, r),
        (-r, r, -r),
        (-r, r, r),
        (r, -r, -r),
        (r, -r, r),
        (r, r, -r),
        (r, r, r),
    ]

    # Rotation matrices for Y axis
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    rotation_x = [
        [1, 0, 0],
        [0, cos_a, -sin_a],
        [0, sin_a, cos_a]
    ]
    rotation_y = [
        [cos_a, 0, sin_a],
        [0, 1, 0],
        [-sin_a, 0, cos_a],
    ]
    rotation_z = [
        [cos_a, -sin_a, 0],
        [sin_a, cos_a, 0],
        [0, 0, 1]
    ]

    # Apply rotation
    rotated_vertices = mul(mul(mul(vertices, rotation_x), rotation_y), rotation_z)

    # Project 3D vertices to 2D
    projected_points = []
    for x, y, z in rotated_vertices:
        z += 50  # Translate the cube forward
        f = 20 / z  # Focal length
        x_proj = int(x * f + 40)  # Center on screen
        y_proj = int(-y * f + 12)
        projected_points.append((x_proj, y_proj))

    # Create a buffer for the screen
    screen = [[' ' for _ in range(120)] for _ in range(40)]

    # Draw edges
    edges = [
        (0, 1), (1, 3), (3, 2), (2, 0),  # Front face
        (4, 5), (5, 7), (7, 6), (6, 4),  # Back face
        (0, 4), (1, 5), (2, 6), (3, 7),  # Connecting edges
    ]

    faces = [
        [0, 1, 3, 2],
        [4, 5, 7, 6],
        [0, 4, 6, 2],
        [1, 5, 7, 3],
        [0, 1, 5, 4],
        [2, 3, 7, 6]
    ]

    for face in faces:
        v1 = [projected_points[face[1]][0] - projected_points[face[0]][0],
              projected_points[face[1]][1] - projected_points[face[0]][1]]
        v2 = [projected_points[face[2]][0] - projected_points[face[0]][0],
              projected_points[face[2]][1] - projected_points[face[0]][1]]
        normal = [v1[1] * - v2[1], v2[0] - v1[0]]

        if normal[1] > 0:
            for i in range(len(face)):
                start = face[i]
                end = face[(i + 1) % len(face)]
                x1, y1 = projected_points[start]
                x2, y2 = projected_points[end]
                draw_line(screen, x1, y1, x2, y2)

    for line in screen:
        print(''.join(line))


def draw_line(screen, x0, y0, x1, y1):
    # Bresenham's line algorithm
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        if 0 <= x0 < 120 and 0 <= y0 < 40:
            screen[y0][x0] = '*'
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy


def main():
    angle = 0
    while True:
        clear_screen()
        draw_cube(angle)
        angle += 0.1
        time.sleep(0.05)


if __name__ == '__main__':
    main()
