import sys
import re
from pathlib import Path
from collections import Counter


def load_logs(file_path: str) -> list:
    """Loading logs from a file"""
    file_path = Path(file_path)
    pattern = r"\d+\-\d+\-\d+\s\d+\:\d+\:\d+\s\w+\s.*$"
    try:
        with open(file_path, "r", encoding="utf-8") as file:

            list_logs = [
                parse_log_line(line)
                for line in file.readlines()
                if line.strip() and re.match(pattern, line)
            ]

            if not list_logs:
                print("В файлі немає записів про логи!")
            return list_logs
    except Exception as e:
        print(f"""Помилка читання файлу: {e}. Перевірте файл.""")


def parse_log_line(line: str) -> dict:
    """Parser log file"""
    log_split = line.split()
    dict_logs = {}
    dict_logs["date"] = log_split[0]
    dict_logs["time"] = log_split[1]
    dict_logs["level"] = log_split[2]
    dict_logs["message"] = " ".join(log_split[3:])
    return dict_logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Filtering logs by level"""
    try:
        filtered_logs = list(filter(lambda log: log["level"] == level, logs))
        return filtered_logs
    except Exception as e:
        print(f"Помилка фільтру по логу {e}")
        return None


def count_logs_by_level(logs: list) -> dict:
    """Сounting records by log level"""
    try:
        dict_count_level = dict(Counter(log["level"] for log in logs))
        return dict_count_level
    except Exception as e:
        print(f"Помилка підрахунків логів {e}")
        return None


def display_log_counts(counts: dict):
    """formatting and output of results"""
    if counts:
        print(" Рівень логування | Кількість")
        print("------------------|-----------")
        for error, count in counts.items():
            print(f"  {error:<16}|  {count}")
        print()


def main():
    """Getting data from the user and output."""
    if len(sys.argv) < 2:
        print("Ви не ввели шлях до файлу!")
    else:
        file_open = sys.argv[1]
        if not Path(file_open).is_file():
            print("Невірний шлях! Введіть вірний шлях до файлу.")
            return
        else:
            logs = load_logs(file_open)
            dict_count_level = count_logs_by_level(logs)
            display_log_counts(dict_count_level)

    if len(sys.argv) == 3 and len(logs) > 0:
        level = sys.argv[2].upper()
        filter_logs = filter_logs_by_level(logs, level)

        if filter_logs:
            print(f"Деталі логів для рівня '{level}':")
            for log in filter_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(
                f"""Ви ввели невірну назву логу або логів з назвою '{level}' в файлі не має!"""
            )


if __name__ == "__main__":
    main()
