import csv
import jsonlines

paths = {
    "train": ["/Users/caiqis/Desktop/MHGRN-for explanation/generate_ComVE/train/subtaskB_data_all.csv",
              "/Users/caiqis/Desktop/MHGRN-for explanation/generate_ComVE/train/subtaskB_answers_all.csv"],
    "dev": ["/Users/caiqis/Desktop/MHGRN-for explanation/generate_ComVE/dev/subtaskB_dev_data.csv",
            "/Users/caiqis/Desktop/MHGRN-for explanation/generate_ComVE/dev/subtaskB_gold_answers.csv"],
    "test": ["/Users/caiqis/Desktop/MHGRN-for explanation/generate_ComVE/test/subtaskB_test_data.csv",
             "/Users/caiqis/Desktop/MHGRN-for explanation/generate_ComVE/test/subtaskB_gold_answers.csv"]
}
for file in ["train", "dev", "test"]:
    data = []
    csv_reader = csv.reader(open(paths[file][0]))
    for line in csv_reader:
        data.append(line)

    answer = []
    csv_reader = csv.reader(open(paths[file][1]))
    for line in csv_reader:
        answer.append(line)

    # ['0', 'He poured orange juice on his cereal.', 'Orange juice is usually bright orange.', "Orange juice doesn't taste good on cereal.", 'Orange juice is sticky if you spill it on the table.']
    # ['0', 'B']
    train_set = []
    for question, answer in zip(data[1:], answer):
        if answer[1] == "A":
            answer_idx = 0
        elif answer[1] == "B":
            answer_idx = 1
        else:
            answer_idx = 2
        statements = []

        for index, reason in enumerate(question[2:]):
            if len(reason) == 0:
                print(file, question, answer)
            if index == answer_idx:
                statements.append({
                    "label": True,
                    "statement": reason
                })
            else:
                statements.append({
                    "label": False,
                    "statement": reason
                })

        train_set.append({
            "answerKey": answer[1],
            "id": "{}-{}".format(file, question[0]),
            "question":{
                "choices":[
                    {
                        "label":"A",
                        "text":question[2]
                    },
                    {
                        "label":"B",
                        "text":question[3]
                    },
                    {
                        "label":"C",
                        "text":question[4]
                    }
                ],
                # "question_concept": "punishing",
                "stem": question[1]
            },
            "statements":statements
        })

    file = jsonlines.open("./statement/"+file+".statement.jsonl","w")
    for item in train_set:
        jsonlines.Writer.write(file, item)
    file.close()