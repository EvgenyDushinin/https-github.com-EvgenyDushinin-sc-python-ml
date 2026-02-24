# Импортируем библиотеки
import pandas as pd
import numpy as np

# Модели и инструменты ML
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ----------------------------
# 1. Загружаем данные
# ----------------------------

df = pd.read_csv("sc_orders.csv")

# ----------------------------
# 2. Выбираем признаки (X) и целевую переменную (y)
# ----------------------------

y = df["total_delay"]

# Убираем всё, что напрямую раскрывает target
X = df.drop(columns=[
    "total_delay",
    "order_id",
    "production_delay",
    "transport_delay"
])

# ----------------------------
# 3. Кодируем категориальные признаки
# ----------------------------

# Преобразуем строки в числовые dummy-переменные
X = pd.get_dummies(X, drop_first=True)

# ----------------------------
# 4. Делим данные на train и test
# ----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% на тест
    random_state=42     # фиксируем случайность
)

# ----------------------------
# 5. Обучаем модель
# ----------------------------

model = LinearRegression()
model.fit(X_train, y_train)

# ----------------------------
# 6. Делаем предсказания
# ----------------------------

y_pred = model.predict(X_test)

# ----------------------------
# 7. Оцениваем качество
# ----------------------------

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("MAE:", round(mae, 3))
print("RMSE:", round(rmse, 3))
