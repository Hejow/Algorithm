from itertools import combinations

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
combos = [{} for i in range(course[-1])]
result = []

for course in course:
    for order in orders:
        new_order = ''.join(sorted(order))
        for combo in [''.join(i) for i in list(combinations(new_order, course))]:
            if combo in combos[course-1]: combos[course-1][combo] += 1
            else: combos[course-1][combo] = 1
        
for combo in combos:
    for c in list(combo.keys()):
        if combo[c] < 2: del combo[c]

for combo in combos:
    if combo:
        max_val = max(combo.values())
        for ele in combo:
            if combo[ele] == max_val: result.append(ele)
        
print(sorted(result))