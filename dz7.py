import random
import matplotlib.pyplot as plt

def roll_dice():
       return random.randint(1, 6)

def monte_carlo_simulation(num_simulations):
    """Функція для проведення симуляції методом Монте-Карло"""
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        dice_sum = roll_dice() + roll_dice()
        sums_count[dice_sum] += 1

    # Розрахунок ймовірностей для кожної суми
    probabilities = {k: (v / num_simulations) * 100 for k, v in sums_count.items()}
    return probabilities

# Налаштування симуляції
num_simulations = 100000

# Запуск симуляції Монте-Карло
probabilities = monte_carlo_simulation(num_simulations)

# Виведення результатів
print("Результати симуляції Монте-Карло:")
for sum_val, prob in probabilities.items():
    print(f"Сума: {sum_val}, Імовірність: {prob:.2f}%")

# Аналітичні значення для порівняння
analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Розрахунок середньої кількості кидків для порівняння з теоретичними значеннями
average_rolls = sum(probabilities.values()) / len(probabilities)

# Побудова графіку
fig, ax = plt.subplots()
x = list(probabilities.keys())
y_simulation = list(probabilities.values())
y_analytical = [analytical_probabilities[i] for i in x]

ax.plot(x, y_simulation, label='Монте-Карло', marker='o')
ax.plot(x, y_analytical, label='Аналітичні', marker='x')
ax.set_xlabel('Сума')
ax.set_ylabel('Імовірність (%)')
ax.set_title('Ймовірності сум при киданні двох кубиків')
ax.legend()
plt.grid()
plt.show()

# Запис результатів у файл README.md
with open('README.md', 'w') as f:
    f.write("# Результати симуляції Монте-Карло та порівняння з аналітичними значеннями\n\n")
    f.write("### Результати симуляції Монте-Карло:\n")
    f.write("| Сума | Імовірність (%) |\n")
    f.write("|------|------------------|\n")
    for sum_val, prob in probabilities.items():
        f.write(f"| {sum_val} | {prob:.2f} |\n")

    f.write("\n### Аналітичні значення:\n")
    f.write("| Сума | Імовірність (%) |\n")
    f.write("|------|------------------|\n")
    for sum_val, prob in analytical_probabilities.items():
        f.write(f"| {sum_val} | {prob:.2f} |\n")

    f.write(f"\nСередня кількість кидків на одну суму: {average_rolls:.2f}")
