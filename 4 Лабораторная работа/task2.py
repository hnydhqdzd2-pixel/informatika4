import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as f: #читаем CSV файл
        lines = f.readlines()  #читаем все строки файла в список

    headers = lines[0].strip().split(',')  #убираем лишние пробелы и разбиваем по запятым

    data = [] #создаём список для хранения словарей

    for i in range(1, len(lines)): #проходим по остальным строкам (начиная со второй)
        values = lines[i].strip().split(',')  #разбиваем строку на значения
        row_dict = {}  #создаём пустой словарь для текущей строки

        for j in range(len(headers)): #для каждого столбца создаём пару ключ-значение
            row_dict[headers[j]] = values[j]

        data.append(row_dict)  #добавляем словарь в список

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False) #записываем в JSON файл с отступом 4 пробела


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME,  'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="") #выводим результат

