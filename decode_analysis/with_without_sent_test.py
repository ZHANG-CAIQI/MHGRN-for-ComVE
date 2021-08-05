import numpy as np
from mlxtend.evaluate import permutation_test
import collections
def get_grades(file):
    f = open(file)

    all_lines = f.readlines()
    step = 2

    grades = []
    question_groups = [all_lines[i:i+step] for i in range(0, len(all_lines), step)]

    for item in question_groups[:-1]:
        grades.append(int(item[1].strip()))
    return grades


def truncate(list1, list2):
    min_len = min(len(list1), len(list2))
    return list1[:min_len], list2[:min_len]

alpha = 0.01

no_sent_grades = get_grades("grades_seed_2_no_sent.txt")
with_sent_grades = get_grades("grades_seed_2_with_sent.txt") + [1, 1, 1, 0, 1, 0, 1]

# print(collections.Counter(no_sent_grades))

print(collections.Counter(with_sent_grades))
print(len(with_sent_grades))
no_sent_grades, with_sent_grades = truncate(no_sent_grades, with_sent_grades)

print("The average of no_sent_grades is: {}".format(np.mean(no_sent_grades)))

print("The average of with_sent_grades is: {}".format(np.mean(with_sent_grades)))

p_value = permutation_test(no_sent_grades, with_sent_grades, method='approximate', num_rounds=1000)

print("The p_value is {}".format(p_value))

if p_value < alpha:
    print("We are confident to reject the nul hypothesis")