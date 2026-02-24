# Импортируем библиотеки
import pandas as pd          # работа с таблицами (DataFrame)
import numpy as np           # математика и генерация случайных данных

# Фиксируем random seed, чтобы результаты были воспроизводимы
np.random.seed(42)

# Количество заказов
n = 3000

# Создаем DataFrame (таблицу)
data = pd.DataFrame({

    # Уникальный номер заказа
    "order_id": range(1, n + 1),

    # Тип клиента (случайный выбор из списка)
    "customer_type": np.random.choice(
        ["Retail", "Distributor", "E-commerce"],
        n
    ),

    # Регион доставки
    "region": np.random.choice(
        ["North", "South", "Central", "East"],
        n
    ),

    # Объем спроса (целое число от 10 до 500)
    "demand_qty": np.random.randint(10, 500, n),

    # Задержка производства (распределение Пуассона)
    # lambda = 1.5 означает среднее значение ~1.5
    "production_delay": np.random.poisson(1.5, n),

    # Задержка транспорта
    "transport_delay": np.random.poisson(1.0, n),
})

# Общая задержка = производство + транспорт
data["total_delay"] = data["production_delay"] + data["transport_delay"]

# OTIF (On Time In Full)
# Если total_delay <= 2 дней → считаем доставку вовремя
data["otif"] = np.where(
    data["total_delay"] <= 2,
    1,  # вовремя
    0   # с опозданием
)

# Сохраняем в CSV файл
data.to_csv("sc_orders.csv", index=False)

# Показываем первые 5 строк
print(data.head())

# Выводим информацию о структуре таблицы
print("\nDataset info:")
print(data.info())

print("\nDataset created successfully.")
