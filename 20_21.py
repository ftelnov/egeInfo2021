win_amount = 82  # Необходимо выставить общее число монеток для победы(минимальное необходимое, >=)


# генератор кучек, создает всевозможные выходы из текущей позиции
def generate_steps(first, second):
    return [(first + 1, second), (first, second + 1), (first, second * 4), (first * 4, second)]


# победа, если кучка находится в выигрышной позиции
def is_winning(heap):
    return heap[0] + heap[1] >= win_amount


# True, если из этой кучи можно победить своим первым ходом
def first_step_win(heap):
    return any(map(is_winning, generate_steps(heap[0], heap[1])))


# True, если из этой кучи можно победить своим вторым ходом
def second_step_win(heap):
    enemy_entries = generate_steps(heap[0], heap[1])
    for entry in enemy_entries:
        enemy_steps = generate_steps(entry[0], entry[1])
        if any(map(is_winning, enemy_steps)):
            continue
        if all(map(first_step_win, enemy_steps)):
            return True
    return False


# --- Алгоритм для 20 задачи ---
# for s in range(1, 69):
#     if second_step_win((7, s)):
#         print(s)


# --- Алгоритм для 21 задачи ---
for s in range(1, 69):
    flag = 1
    second_entries = generate_steps(4, s)
    if all(map(first_step_win, second_entries)):
        continue
    for _entry in second_entries:
        if not first_step_win(_entry) and not second_step_win(_entry):
            flag = 0
            break
    if flag:
        print(s)
