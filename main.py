from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    print(f'дата: {datetime.now().date()}')
# datetime.now() — получает текущие дату и время
# .date() — оставляет только дату (без времени)
# При запуске 8 июля 2025 выведет: дата: 2025-07-08
    calculate_salary()
    get_employees()