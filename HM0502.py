import re
from typing import Callable


def generator_numbers(text_uniforn: str) -> str:
    """Parses the text, identifies all valid numbers and returns them."""
    pattern = r"\s\d+\.\d+\s"
    for valid_number in re.findall(pattern, text_uniforn):
        yield valid_number


def sum_profit(text: str, generator_numbers: Callable) -> float:
    """Addition of real numbers and calculation of total profit."""
    total_profit = 0
    for text in generator_numbers(text):
        total_profit += float(text)
    return total_profit


text_uniforn = """Загальний дохід працівника складається з декількох частин:
1000.01 як основний дохід, доповнений додатковими надходженнями
27.45 i 324.00 доларів."""
total_income = sum_profit(text_uniforn, generator_numbers)
print(f"Загальний дохід: {total_income}")
