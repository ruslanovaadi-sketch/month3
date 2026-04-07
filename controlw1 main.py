from datetime import datetime

greetings = [
    {"text": "Доброе утро!", "hour": 9},
    {"text": "Пора завтракать", "hour": 10},
    {"text": "Добрый вечер!", "hour": 19},
    {"text": "Спокойной ночи", "hour": 22},
]

def get_filtered_greetings(filter_type):
    if filter_type == "morning":
        return [g for g in greetings if g["hour"] < 12]
    elif filter_type == "evening":
        return [g for g in greetings if g["hour"] >= 12]
    return greetings

morning_list = get_filtered_greetings("morning")
evening_list = get_filtered_greetings("evening")

print("Утро:", [g["text"] for g in morning_list])
print("Вечер:", [g["text"] for g in evening_list])




def save_history(text):
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")

def load_history():
    try:
        with open("history.txt", "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

save_history("Доброе утро! (09:00)")
history = load_history()
print(history)