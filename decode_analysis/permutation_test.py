import sklearn.model_selection
import random
import os
# f = open("decode_test.txt")
# all_lines = f.readlines()
# count = 0
# step = 8
#
# question_groups = [all_lines[i:i+step] for i in range(0, len(all_lines), step)]
#
# seed = 2
# sample_size = 200
#
# random.seed(seed)
#
# if os.path.exists("grades_seed_{}.txt".format(seed)):
#     os.remove("grades_seed_{}.txt".format(seed))
#
# if os.path.exists("good_explanation.txt".format(seed)):
#     os.remove("good_explanation.txt".format(seed))
#
# samples = random.sample(question_groups, sample_size)
# total_score = 0
# for sample in samples:
#     answered_correctly = 0
#     for line in sample:
#         if "*^" in line:
#             count += 1
#             answered_correctly = 1
#     if answered_correctly:
#         for line in sample:
#             print(line)
#         score = input("Input the score:")
#         if int(score) == 2:
#             with open("good_explanation.txt".format(seed), "a") as f:
#                 f.writelines(sample[1] + "\t" + score + "\n")
#         total_score += int(score)
#         with open("grades_seed_{}.txt".format(seed), "a") as f:
#             f.writelines(sample[1] + "\t" + score + "\n")
#
# print(count)
# print(total_score/count)
#
# with open("grades_seed_{}.txt".format(seed), "a") as f:
#     f.writelines(str(count) + "\t" + str(total_score) + "\n")

from mlxtend.evaluate import permutation_test
# http://rasbt.github.io/mlxtend/user_guide/evaluate/permutation_test/
treatment = [1] * 918 + [0] * (1000 - 918)
control = [1] * 925 + [0] * (1000 - 925)

p_value = permutation_test(control, treatment, method='approximate', num_rounds = 1000)

print(p_value)

