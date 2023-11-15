# TODO решите задачу
import json

imported_file = 'input.json'


def task() -> float:
    with open(imported_file, 'r') as file:
        data = json.load(file)

    hfbsj = []
    for i in data:
        fjhbvsjbh = lambda a, b: a * b
        hfbsj1 = fjhbvsjbh(i['score'], i['weight'])
        hfbsj.append(hfbsj1)
    return round(sum(hfbsj), 3)


print(task())
