from itertools import combinations

def solution(orders, course):
    answer = []
    combos = [{} for i in range(course[-1])]

    for course in course:
        for order in orders:
            n_order = ''.join(sorted(order))
            for combo in [''.join(i) for i in list(combinations(n_order, course))]:
                if combo in combos[course-1]: combos[course-1][combo] += 1
                else: combos[course-1][combo] = 1

    for combo in combos:
        for c in list(combo.keys()):
            if combo[c] < 2: del combo[c]

    for combo in combos:
        if combo:
            max_val = max(combo.values())
            for ele in combo:
                if combo[ele] == max_val: answer.append(ele)

    return sorted(answer)