import json
from datetime import datetime, time
from typing import List

rating: List[list[time]] = []
competitors: json

def write_raw_data_to_rating(start: str, finish: str):
        line_list_start: List[str] = get_line_list(start)           # Лист слов строки старта
        line_list_finish: List[str] = get_line_list(finish)         # Лист слов строки финиша
        
        start_time :time = get_time_from_line(line_list_start)      # Получаем время старта и финиша нижу
        finish_time :time = get_time_from_line(line_list_finish)
        
        run_time: time = finish_time - start_time                   # Получаем время забега отнимая время старта от времени финиша
        number_of_person = get_number_of_person(line_list_start)    # из строки старта, получаем нагрудный номер
        
        rating.append([number_of_person, run_time])                 # Записываем в массив
            
def sort_rating():
    for i in range(len(rating)):
            for j in range(i, len(rating)):
                if rating[i][1] > rating[j][1]:
                    rating[i], rating[j] = rating[j], rating[i]
                    
def print_results():
    print("| Занятое место | Нагрудный номер | Имя | Фамилия | Результат |")
    for i in range(len(rating)):
        number = rating[i][0]
        name: str = competitors[number]["Name"]
        surname: str = competitors[number]["Surname"]
        print(f"| {i+1} | {rating[i][0]} | {name} | {surname} | {rating[i][1]} |")
        
def get_line_list(line: str):
    return line.split(" ")

def get_time_from_line(line_list: List[str]):
    return datetime.strptime(line_list[len(line_list) - 1], "%H:%M:%S,%f")

def get_number_of_person(line_list: List[str]):
    return line_list[0]

if __name__ == "__main__":
    with open("competitors2.json", "r", encoding="utf-8-sig") as file:
        competitors = json.loads(file.read())
    
    with open("results_RUN.txt", "r", encoding="utf-8-sig") as file:
        while True:
            start: str = file.readline().replace("\n", "")
            finish: str = file.readline().replace("\n", "")
            if(start == ''): break
            write_raw_data_to_rating(start, finish)
    sort_rating()
    print_results()
    

