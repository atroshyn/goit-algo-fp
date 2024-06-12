items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    # Ініціалізуємо DP таблицю
    n = len(items)
    item_names = list(items.keys())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name = item_names[i - 1]
        cost = items[item_name]['cost']
        calories = items[item_name]['calories']
        
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]
    
    total_calories = dp[n][budget]
    
    # Визначаємо, які страви були вибрані
    selected_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append(item_names[i - 1])
            b -= items[item_names[i - 1]]['cost']
    
    return selected_items, total_calories

# Приклад використання
budget = 100

selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", selected_items_greedy)
print("Загальна калорійність:", total_calories_greedy)

selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("Динамічне програмування:")
print("Вибрані страви:", selected_items_dp)
print("Загальна калорійність:", total_calories_dp)
