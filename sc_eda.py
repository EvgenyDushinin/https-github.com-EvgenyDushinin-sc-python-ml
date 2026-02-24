# Импортируем библиотеки
import pandas as pd                  # работа с таблицами
import matplotlib.pyplot as plt      # построение графиков
import seaborn as sns                # более красивые графики поверх matplotlib

# Загружаем датасет из CSV файла
df = pd.read_csv("sc_orders.csv")

# ----------------------------
# 1. Общая информация о данных
# ----------------------------

print("Первые 5 строк:")
print(df.head())

print("\nИнформация о датасете:")
print(df.info())

print("\nСтатистика по числовым колонкам:")
print(df.describe())

# ----------------------------
# 2. Общий OTIF
# ----------------------------

# mean() для 0/1 колонки = доля единиц
otif_rate = df["otif"].mean()

print("\nОбщий OTIF rate:", round(otif_rate, 3))

# ----------------------------
# 3. OTIF по регионам
# ----------------------------

# groupby — группировка
# mean — среднее внутри каждой группы
otif_by_region = df.groupby("region")["otif"].mean()

print("\nOTIF по регионам:")
print(otif_by_region)

# ----------------------------
# 4. Средняя задержка по типу клиента
# ----------------------------

avg_delay_customer = df.groupby("customer_type")["total_delay"].mean()

print("\nСредняя задержка по типу клиента:")
print(avg_delay_customer)

# ----------------------------
# 5. Визуализация распределения задержек
# ----------------------------

# Гистограмма с легендой
sns.histplot(df["total_delay"], kde=True)
plt.title("Distribution of Total Delay")
plt.xlabel("Total Delay (days)")
plt.ylabel("Count")
plt.legend(["KDE curve", "Histogram"])
plt.show()

# Boxplot с понятными подписями
sns.boxplot(x="region", y="total_delay", data=df)
plt.title("Total Delay by Region")
plt.xlabel("Region")
plt.ylabel("Total Delay (days)")
plt.show()

# ----------------------------
# 6. Boxplot по регионам
# ----------------------------

sns.boxplot(x="region", y="total_delay", data=df)
plt.title("Задержка по регионам")
plt.show()
