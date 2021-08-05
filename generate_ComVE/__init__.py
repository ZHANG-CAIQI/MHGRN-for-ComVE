import jsonlines
import json
# items = []
# with open("template_train.statement.jsonl", "r+", encoding="utf8") as f:
#     for item in jsonlines.Reader(f):
#         items.append(item)
#
# js = json.dumps(items[0], sort_keys=True, indent=4, separators=(',', ':'))
# print(js)
#
# items = []
# with open("train.statement.jsonl", "r+", encoding="utf8") as f:
#     for item in jsonlines.Reader(f):
#         items.append(item)
#
# js = json.dumps(items[0], sort_keys=True, indent=4, separators=(',', ':'))
# print(js)
#

dic = {'https://www.wikihow.com/Make-Windows-7-Search-File-Contents': {'url': 'https://www.wikihow.com/Make-Windows-7-Search-File-Contents', 'title': 'How to Make Windows 7 Search File Contents', 'annotations': {'section_0': [{'actionable_step': 0, 'precondition_step': 0, 'actionable_span': (12, 15), 'precondition_span': (0, 2)}, {'actionable_step': 0, 'precondition_step': 0, 'actionable_span': (38, 49), 'precondition_span': (52, 53)}, {'actionable_step': 2, 'precondition_step': 1, 'actionable_span': (0, 6), 'precondition_span': (0, 3)}, {'actionable_step': 2, 'precondition_step': 1, 'actionable_span': (8, 15), 'precondition_span': (0, 3)}, {'actionable_step': 3, 'precondition_step': 2, 'actionable_span': (0, 4), 'precondition_span': (0, 6)}, {'actionable_step': 4, 'precondition_step': 3, 'actionable_span': (0, 2), 'precondition_span': (0, 4)}], 'section_1': [{'actionable_step': 0, 'precondition_step': 0, 'actionable_span': (3, 6), 'precondition_span': (0, 1)}, {'actionable_step': 1, 'precondition_step': 0, 'actionable_span': (0, 7), 'precondition_span': (0, 1)}, {'actionable_step': 2, 'precondition_step': 1, 'actionable_span': (0, 7), 'precondition_span': (0, 7)}, {'actionable_step': 3, 'precondition_step': 2, 'actionable_span': (0, 10), 'precondition_span': (0, 7)}, {'actionable_step': 3, 'precondition_step': 3, 'actionable_span': (34, 41), 'precondition_span': (0, 10)}], 'section_2': [{'actionable_step': 1, 'precondition_step': 0, 'actionable_span': (0, 5), 'precondition_span': (0, 1)}, {'actionable_step': 2, 'precondition_step': 1, 'actionable_span': (0, 4), 'precondition_span': (0, 5)}, {'actionable_step': 3, 'precondition_step': 2, 'actionable_span': (0, 1), 'precondition_span': (0, 4)}, {'actionable_step': 4, 'precondition_step': 3, 'actionable_span': (0, 4), 'precondition_span': (0, 1)}, {'actionable_step': 5, 'precondition_step': 4, 'actionable_span': (0, 4), 'precondition_span': (0, 4)}, {'actionable_step': 5, 'precondition_step': 5, 'actionable_span': (20, 28), 'precondition_span': (6, 12)}, {'actionable_step': 5, 'precondition_step': 5, 'actionable_span': (31, 36), 'precondition_span': (20, 28)}, {'actionable_step': 6, 'precondition_step': 5, 'actionable_span': (0, 9), 'precondition_span': (0, 4)}, {'actionable_step': 7, 'precondition_step': 7, 'actionable_span': (15, 17), 'precondition_span': (0, 1)}, {'actionable_step': 7, 'precondition_step': 7, 'actionable_span': (19, 21), 'precondition_span': (0, 1)}]}}}
js = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
print(js)

