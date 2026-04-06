import json #импортируем нужный модуль
def task() -> float: #объявляем функцию task
    with open("input.json", "r") as f: #открываем файл
        data = json.load(f) #загружаем содержимое

        total = 0
        for item in data: #проходим по всем элементам
            total += item["score"] * item["weight"] #добавляем произведение
        return round(total, 3) #округляем полученную сумму до трех знаков после запятой

print(task()) #вызываем функцию и выводим результат
