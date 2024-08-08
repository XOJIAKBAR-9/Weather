# from sqlite3 import connect
# import datetime
#
# with connect("todo.db") as db:
#     c = db.cursor()
#     c.execute(
#         """
#         CREATE TABLE IF NOT EXISTS user(
#         ism VARCHAR(30),
#         username VARCHAR(20) UNIQUE NOT NULL,
#         password VARCHAR(8)
#         )
#         """
#     )
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS task(
#         title VARCHAR(50),
#         text VARCHAR(255),
#         deadline DATETIME,
#         is_done BOOLEAN,
#         user VARCHAR(20)
#             )
#         """
#               )
# #################
# global login_user
#
#
# #################
# def check_username(username):
#     with connect("todo.db") as db:
#         c = db.cursor()
#         c.execute(
#             """
#             SELECT username FROM user
#             """
#         )
#         all_usernames = c.fetchall()
#         print(all_usernames)
#         for i in all_usernames:
#             if i[0] == username:
#                 return False
#         return username
#
#
# def authentification():
#     while True:
#         bolim = input("-------------------\n"
#                       "1 -> Login.\n"
#                       "2 -> Registration.\n"
#                       "3 -> Exit.\n"
#                       "-------------------\n"
#                       "Bo'limni tanlang: ")
#         match bolim:
#             case "0":
#                 print("Dasturdan chiqildi!!!")
#                 exit(0)
#             case "1":
#                 user_name = input("Usernameni kiriting: ")
#                 password = input("Passwordni kiriting: ")
#
#                 with connect("todo.db") as db:
#                     c = db.cursor()
#                     c.execute(
#                         f"""
#                         SELECT * FROM user
#                         WHERE username = {user_name} AND password = {password}
#                         """
#                     )
#                     user_data = c.fetchone()
#                     if user_data:
#                         print("You have registered succesfully!!!")
#                         login_user = user_data
#                         return
#                     else:
#                         print("There is no any data of a user!!!")
#                         continue
#             case "2":  # registration
#                 ism = input("Isminggizni kiriting: ")
#                 user_data = input("Usernameni kiriting: ")
#                 for i in range(5):
#                     if check_username(user_name):
#                         break
#                     else:
#                         user_name = input("This place is busy, \nEnter other username: ")
#                 else:
#                     print("The number of trials has ended, try again later!")
#                     continue
#
#                 password = input("Passwordni kiriting: ")
#
#                 with connect("todo.db") as db:
#                     c = db.cursor()
#                     c.execute(
#                         """
#                         INSERT INTO user VALUES(?, ?, ?)
#                         """, (ism, user_name, password)
#                     )
#
#                 print("You have registered succesfully🏆")
#                 login_user = c.fetchone()
#                 return
#
#
# authentification()
# def format_tasks(header, tasks):
#     if tasks:
#         max_title_length = 0
#         max_description_length = 0
#         for task in tasks:
#             if len(task[0]) > max_title_length:
#                 max_title_length = len(task[0])
#             if task[1] and len(task[1]) > max_description_length:
#                 max_description_length = len(task[1])
#         print(f"{'_' * (33 + max_description_length + max_title_length)}\n"
#               f"{header}\n"
#               f"{'_' * (33 + max_description_length + max_title_length)}")
#         print(
#             f"No | Title {' ' * (max_title_length - 6)} | Description {' ' * (max_description_length - 12)} | Due        | Completed")
#         n = 1
#         for task in tasks:
#             print(
#                 f"{n}  | {task[0]:<{max_title_length}} | {task[1]:<{max_description_length}} | {task[2]} | {'Yes' if task[3] else 'No'}")
#             n += 1
#         print(f"{'_' * (33 + max_description_length + max_title_length)}\n")
#     else:
#         print("Tasklar topilmadi.")
#
# while True:
#     bolim = input("-------------------\n"
#                   "1 -> Yangi topshiriq qo'shish.\n"
#                   "2 -> Hamma topshiriqlarim.\n"
#                   "3 -> Bajarilmagan topshiriqlarim.\n"
#                   "4 -> Tugallangan topshiriqlarim.\n"
#                   "5 -> Topshiriqni o'chirish.\n"
#                   "0 -> Chiqish.\n"
#                   "-------------------\n"
#                   "Bo'limni tanlang: ")
#     match bolim:
#         case "0":
#             print("Dasturdan chiqildi!")
#             exit(0)
#         case '1':
#             title = input("Topshiriq uchun sarlavha kiriting: ")
#             text = input("TOPSHIRIQ MATNINI KIRITING: ")
#             deadline_str = input("So`ngi muddatni kiriting: (YYYY-MM-OD) Masalan:2024-01-29")
#             deadline_date = datetime.datetime.strptime(deadline_str, '%Y-%m-%d').date()
#             with connect('todo.db') as db:
#                 kursor = db.cursor()
#                 kursor.execute("""
#                 INSERT INTO task VALUES(?,?,?,?,?)
#                 """, (title, text, deadline_date, False, login_user[2])
#                                )
#             print("Sizning topshiriginggiz muvaffaqiyatli qo'shildi!!!")
#         case "2":
#             with connect ('todo.db') as db:
#                 kursor=db.cursor()
#                 kursor.execute(
#                     f"""
#                     SELECT*FROM task
#                     WHERE user="{login_user[1]}"
#                     """
#                 )
#                 tasks=kursor.fetchall()
#                 format_tasks("hamma topshiriqlar",tasks)
# python standard libraries!!!
from collections import Counter
# matn="bugun havo juda ham issiq"
# print(Counter(matn))
#
# with open("believer.txt") as file:
#     matn=file.read()
#     matn=matn.replace(",","")
# with open("believer.txt","w") as file:
#     file.write(matn)
# with open("believer.txt") as file:
#     matn=file.read()
#     print(Counter(matn.split()))
#     print(Counter(matn.split()).most_common(3))
# deque
# from collections import deque
#
# mevalar = ["olma", "banan", "apelsin", "anor"]
# sabzavotlar = ["sabzi", "oshqovoq", "qovun", "pomidor"]
# mevalar = deque(mevalar)
# mevalar.appendleft("behi")
# mevalar.popleft()
# mevalar.extendleft(sabzavotlar)
# print(mevalar)
#
from bisect import bisect
# sabzavotlar = ["sabzi", "oshqovoq", "qovun", "pomidor"]
# sabzavotlar.sort()
# print(sabzavotlar)
# index=bisect(sabzavotlar,"behi")
# sabzavotlar.insert(index,"behi")
# print(sabzavotlar)
#
# tizim=[0.26,56,72,86]
# print(bisect(tizim,91),"ball")
#
# from random import shuffle,choice
# mevalar = ["olma", "banan", "apelsin", "anor"]
# shuffle(mevalar)
# print(mevalar)
# print(choice(mevalar))
#
# from turtle import Turtle
# import turtle
# t=Turtle()
# t.color("red")
# t.width(10)
# turtle.bgcolor('blue')
# t.forward(120)
# t.left(180)
# t.forward(100)
# t.left(90)
# t.forward(120)
# t.left(180)
# t.forward(100)
# t.left(90)
# t.forward(120)
# t.left(180)
# t.forward(100)
# t.left(90)
# t.forward(120)
# t.left(180)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(135)
# t.forward(100)
# t.left(135)
# t.forward(100)
# t.left(135)
# t.forward(100)
# t.left(135)
# t.forward(100)
# t.left(135)
# t.forward(100)
# t.left(135)
# t.forward(100)
# t.left(135)
# t.forward(100)
# t.left(135)
# for i in range(10):
#     t.forward(100)
#     t.left(135)
# from turtle import *
# color('red', 'green')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos())<1:
#         break
# end_fill()
# done()
# new theme PIP!!!
# import requests
# api=requests.get("https://iamawesome.com/")
# print(api)
# import requests
# oylar=dict()
# for i in range(1,13):
#     oylar.update(
#         {
#             i: requests.get(f"https://islomapi.uz/api/monthly?region=Farg'ona&month={i}").json()
#         }
#     )
# for kun in oylar.get(1):
#     print(kun.get('day'),kun.get('times'))

