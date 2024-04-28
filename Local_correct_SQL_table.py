import sqlite3
import datetime


user_id = 19
id = 5
conn = sqlite3.connect('habit_tracker1.db')
cursor = conn.cursor()
#h.habit_name, h.habit_description, h.habit_goal
cursor.execute("""
        SELECT *
        FROM habits h
        JOIN user_habits uh ON h.id = uh.habit_id
        WHERE (uh.user_id = ? AND uh.habit_id = ?)
        """, (user_id, id,))
habit_atributs = cursor.fetchall()
print(habit_atributs)
conn.commit()
conn.close()

#print(cursor.fetchall())
# result = []
# for i in cursor:
#     result.append(i[1])
# if len(result) > 10:
#     print(f'Слишком много привычек для контроля и исполнения')
# else:
#     print(result)

# result = cursor.fetchall.rowcount()
# print(result)

# cursor.execute('''
# SELECT user_id, habit_name FROM habits WHERE id = 45
# ''')
#
# info = cursor.fetchall()
#
# print(info)


# cursor.execute('''
# DELETE FROM habits WHERE id = 52
# ''')
#
# cursor.execute('''
# DELETE FROM user_habits WHERE habit_id = 52
# ''')


# print("Database and tables updated successfully.")
goal_time = '22.05.2024'
goal_time_t = datetime.datetime.strptime(goal_time, "%d.%m.%Y")
now = datetime.datetime.now()
period = goal_time_t-now
print(goal_time_t)
print(period)



# from datetime import datetime
#
# date_str = "22.05.2024"
# date_obj = datetime.strptime(date_str, "%d.%m.%Y")
#
# print(date_obj)
#
# from datetime import datetime
#
# # Получаем текущую дату
# current_date = datetime.now()
#
# # Преобразуем строку с целевой датой в объект datetime
# target_date_str = "22.05.2024"
# target_date = datetime.strptime(target_date_str, "%d.%m.%Y")
#
# # Вычисляем разницу между текущей датой и целевой датой
# time_difference = target_date - current_date
#
# print(f"Разница между текущей датой и 22.05.2024: {time_difference}")