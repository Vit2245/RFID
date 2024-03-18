import tkinter as tk
import mysql.connector
import root


def push_number():
    # Получение значения из текстового поля
    number_to_check = entry.get()
    print(type(number_to_check))
    # Подключение к базе данных
    try:
        conn = mysql.connector.connect(
            host=root.host,
            user=root.user,
            password=root.password,
            database=root.database
        )

    except mysql.connector.Error as e:
        result_label.config(text="Ошибка при подключении к базе данных")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (id) VALUES (%s)", (number_to_check,))
    cursor.fetchone()

def takedata():
    # Подключение к базе данных
    try:
        conn = mysql.connector.connect(
            host=root.host,
            user=root.user,
            password=root.password,
            database=root.database
        )

    except mysql.connector.Error as e:
        result_label.config(text="Ошибка при подключении к базе данных")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    cursor.fetchone()

    for i in cursor.fetchone():
        print(i)
    # Закрытие соединения с базой данных


def check_number():
    # Получение значения из текстового поля
    number_to_check = entry.get()

    # Подключение к базе данных
    try:
        conn = mysql.connector.connect(
            host=root.host,
            user=root.user,
            password=root.password,
            database=root.database

        )
        cursor = conn.cursor()

        # Выполнение запроса к базе данных
        cursor.execute("SELECT * FROM students WHERE номер=%s", (number_to_check,))
        result = cursor.fetchone()

        # Проверка наличия номера в базе данных
        if result:
            result_label.config(text="Номер найден в базе данных")
        else:
            result_label.config(text="Номер не найден в базе данных")

        # Закрытие соединения с базой данных
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        result_label.config(text="Ошибка при подключении к базе данных")

# Создание главного окна
root = tk.Tk()
root.title("Проверка номера в базе данных")

# Создание текстового поля
entry = tk.Entry(root)
entry.pack(pady=10)

# Создание кнопки
button = tk.Button(root, text="Проверить", command=check_number)
button.pack()
button = tk.Button(root, text="Добавить", command=push_number)
button.pack()
button = tk.Button(root, text="проверка", command=takedata)
button.pack()
# Метка для отображения результата проверки
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Запуск главного цикла обработки событий
root.mainloop()
