# 1
# class Matn:
#     def __init__(self,matn,matncha):
#         self.matn=matn
#         self.matncha=matncha
#     def about(self):
#         return (f"{self.matn},ga{self.matn} dan salom")
# i=Matn("xojiakbar","Homidov")
# print(i.about().title())
# 2
# from sqlite3 import connect
# with connect("ustozlar.db") as db:
#     cursor = db.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS ustozlar(
#         ism VARCHAR(50),
#         familiya VARCHAR(255),
#         fan VARCHAR(50),
#         yosh INTEGER)
#         """
#     )
# # 3
# with connect('ustozlar.db') as db:
#     cursor=db.cursor()
#     cursor.execute(
#         """
#         INSERT INTO ustozlar(ism,familiya,fan,yosh)
#         VALUES ("axrorbek","saydolimov","texnika",23),
#         ("asadbek","homidov","iqtisod",17),
#         ("gulnoza","shukurova","xorijiy",19),
#         ("shukrona","nematova","tabiiy",23)
#         """
#     )
# 4
# import sqlite3
# ism=input("ismingizni kiriting: ")
# with sqlite3.connect('ustozlar.db') as db:
#     cursor=db.cursor()
#     cursor.execute("SELECT* FROM ustozlar where ism=?",(ism,))
#     result=cursor.fetchall()
#     if len(result)==0:
#         print(f"{ism} nomli ustoz topilmadi.")
#     else:
#         for row in result:
#             print(f"Ism: {row[0]}, Familiya: {row[1]}, Fan: {row[2]}, Yosh: {row[3]}")
# 5

# 6
# class matem:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def hisoblash(self):
#         return self.x**self.y
# daraja=matem(5,3)
# natija=daraja.hisoblash()
# 7
# class matem:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def qoldiqli_bol(self):
#         return self.a//self.b
#     def qoldiqsiz_bol(self):
#         return self.a%self.b
#     def qoldiqni_top(self):
#         self.a/self.b
# 8
# yil=int(input("yilni kiriting: "))
# if yil%4==0 and yil%400==0:
#     print("kabisa yili boladi")
# else:
#     print("kabisa emas")
# 9
# class Matn:
#     def init(self, mine):
#         self.mine = mine
#
#     def intro(self):
#         return f"Mening ismim-{self.me}!!!"
# class Matn2(Matn):
#     def teskari_qiymat(self):
#         return self.mine[::-1]
# a = Matn2("Asadbek")
# print(a.teskari_qiymat())
# 10
# def my_function(login):
# 11
# 11_ex
# class Queue:
#     def init(self):
#         self.boshlist = []
#     def add_element(self, ism, age):
#         return self.boshlist.append((ism, age))
#     def pop(self):
#         return self.boshlist.pop()
# a = Queue()
# a.push("XOJIAKBAR", 18)
# a.pop()
# print(a)
# 12\
# agar son 10 ga teng bolib qolsa sikl toxtaydi son 15dan kichikligi un 10ga borguncha osib boradi 1ga
# 13
# class Queue:
#     def init(self):
#         self.boshlist = []
#
#     def add_element(self, ism, age):
#         return self.boshlist.append((ism, age))
#
#     def pop(self):
#         return self.boshlist.pop()
# a = Queue()
# a.push("Xojiakbar", 18)
# a.pop()
# print(len(a))
# 14
# import bisect
# son=int(input("son kiriting: "))
# oraliqlar=[20,40,60,80,100]
# baxolar=[1,2,3,4,5]
# index=bisect.bisect_right(oraliqlar,son)
# if index<len(baxolar):
#     baxo=baxolar[index]
# else:
#     baxo=None
# if baxo is not None:
#     print(f"{son} soni {baxo} baxo")
# else:
#     print("salomlar")
# 17
# matn = "bugun codialda imtihon bolyapti va bizga omad yordam bersn!"
# letters = []
# for character in matn:
#     letters.append(character)
# print(character, character.isalpha())
# 16
# num=(ord('d'))
# print(num)

# Tic Tac Toe
# template = """
#  ____ ____ ____
# |  1 |  2 |  3 |
#  ____ ____ ____
# |  4 |  5 |  6 |
#  ____ ____ ____
# |  7 |  8 |  9 |
#  ---- ---- ----
# """
# galabalar = ['123', '456', '789', '147', '258', '369', '159', '357']
#
# indekslar = {
#     "1": template.index("1"),
#     "2": template.index("2"),
#     "3": template.index("3"),
#     "4": template.index("4"),
#     "5": template.index("5"),
#     "6": template.index("6"),
#     "7": template.index("7"),
#     "8": template.index("8"),
#     "9": template.index("9"),
# }
# x_list = ''
# o_list = ''
#
# toxta = False
# galaba = False
# for i in range(1, 10):
#     print(i)
#     if i % 2 == 1:
#         x = input(template + "\n(X) o'yinchi (1-9) oraqlig'ida joy tanlang: ")
#         for j in range(3):
#             if x not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#                 print("Noto'g'ri kiritish!")
#                 x = input(template + "\n(X) o'yinchi (1-9) oraqlig'ida joy tanlang: ")
#         if x not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             print("Dastur to'xtadi!")
#             toxta = True
#
#         x_list += x
#         template = template.replace(f" {x}", "❎")
#         x_list = ''.join(sorted(x_list))
#         for g in galabalar:
#             count = 0
#             for k in g:
#                 if g in x_list:
#                     count += 1
#             if count == 3:
#                 print("\n---------------------------------------------------\n(X) lar g'alaba qozondi🎉🎉🎉!\n" + template)
#                 galaba = True
#                 break
#         if galaba:
#             break
#
#     if toxta:
#         break
#     if i % 2 == 0:
#         o = input(template + "\n(O) o'yinchi (1-9) oraqlig'ida joy tanlang: ")
#         for j in range(3):
#             if o not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#                 print("Noto'g'ri kiritish!")
#                 o = input(template + "\n(0) o'yinchi (1-9) oraqlig'ida joy tanlang: ")
#         if o not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             print("Dastur to'xtadi!")
#             toxta = True
#         o_list += o
#         template = template.replace(f" {o}", "0️⃣")
#
#         o_list = ''.join(sorted(o_list))
#         for g in galabalar:
#             count = 0
#             for k in g:
#                 if g in o_list:
#                     count += 1
#             if count == 3:
#                 print("\n---------------------------------------------------\n(0) lar g'alaba qozondi🎉🎉🎉!\n" + template)
#                 galaba = True
#                 break
#         if galaba:
#             break
#         if toxta:
#             break
# if toxta:
#     print("\n-----------------------------------------\nO'yin qoidalari buzildi")
# elif galaba == False:
#     print("\n---------------------------------------------------\nDurrang!" + template)

# x = input(template + "\nX o'yinchi (1-9) oraqlig'ida joy tanlang: ")
#
# from flask import Flask
# import requests
# dastur=Flask("Namoz")
# oylar=dict()
# # api_data_month = requests.get("https://islomapi.uz/api/monthly?region=Farg'ona&month=4")
#
# @dastur.route("/oylik_namoz_vaqtlari")
# def oylik():
#     template = f"""<h1 style="color: green;"> Namoz vaqtlari oylik</h1>"""
#     for i in range(1,13):
#         for i in range(1, 13):
#             oylar.update(
#                 {
#                     i: requests.get(f"https://islomapi.uz/api/monthly?region=Farg'ona&month={i}").json()
#                 }
#          )
#     for i in range(1, 13):
#         print(oylar[i])
#         # <hr>
#         for kun in oylar.get(1):
#             saharlik = kun.get('times').get('tong_saharlik')
#             quyosh = kun.get('times').get('quyosh')
#             peshin = kun.get('times').get('peshin')
#             asr = kun.get('times').get('asr')
#             shom_iftor = kun.get('times').get('shom_iftor')
#             hufton = kun.get('times').get('hufton')
#         template += f"""<hr>
#                 <p style="color: teal;">{kun.get('oylar')}</p>
#                 <ul style="color: teal; display: flex; flex-wrap: wrap; justify-content: center; gap: 25px;">
#                 <li>Saharlik: {saharlik}</li>
#                 <li>Quyosh: {quyosh}</li>
#                 <li>Peshin: {peshin}</li>
#                 <li>Asr: {asr}</li>
#                 <li>Shom: {shom_iftor}</li>
#                 <li>Xufton: {hufton}</li>
#                 </ul>
#                 """
#         return template
#     dastur.run(debug=True)