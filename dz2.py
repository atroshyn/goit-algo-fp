import matplotlib.pyplot as plt
import numpy as np

def draw_pifagoras_tree(ax, x, y, length, angle, level):
    if level == 0:
        return
    x_end = x + length * np.cos(np.radians(angle))
    y_end = y + length * np.sin(np.radians(angle))
    ax.plot([x, x_end], [y, y_end], color='green')
    draw_pifagoras_tree(ax, x_end, y_end, length * 0.7, angle - 45, level - 1)
    draw_pifagoras_tree(ax, x_end, y_end, length * 0.7, angle + 45, level - 1)

def main():
    length = 100  # довжина початкової гілки
    level = int(input("Введіть рівень рекурсії: "))

    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.axis('off')

    draw_pifagoras_tree(ax, 0, 0, length, 90, level)

    plt.show()

if __name__ == "__main__":
    main()
