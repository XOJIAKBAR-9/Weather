# user
#
# ism
# username
# password

# task
#
# title
# text
# deadline
# is_done
# user


from sqlite3 import connect
import datetime

with connect('todo.db') as db:
    kursor = db.cursor()
    kursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user(
        ism VARCHAR(30) NOT NULL,
        username VARCHAR(20) UNIQUE NOT NULL,
        password VARCHAR(8) NOT NULL
        )
        """
    )
    kursor.execute(
        """
        CREATE TABLE IF NOT EXISTS task(
        title VARCHAR(50),
        text VARCHAR(255),
        deadline DATE,
        is_done BOOLEAN,
        user VARCHAR(20)
        )
        """
    )



#################
def check_username(username):
    with connect('todo.db') as db:
        kursor = db.cursor()
        kursor.execute(
            """
            SELECT username FROM user
            """
        )
        all_usernames = kursor.fetchall()
        print(all_usernames)
        for i in all_usernames:
            if i[0] == username:
                return False
        return username


def authentication():
    while True:
        bolim = input("-------------------\n"
                      "1 -> Login.\n"
                      "2 -> Registration.\n"
                      "0 -> Chiqish.\n"
                      "-------------------\n"
                      "Bo'limni tanlang: ")
        match bolim:
            case "0":
                print('Dasturdan chiqildi!')
                exit(0)
            case "1":
                user_name = input('Username ni kiriting: ')
                password = input('Password ni kiriting: ')

                with connect('todo.db') as db:
                    kursor = db.cursor()
                    kursor.execute(
                        f"""
                        SELECT * FROM user
                        WHERE username = "{user_name}" AND password = "{password}"
                        """
                    )
                    user_data = kursor.fetchone()
                    if user_data:
                        print("Siz ro'yxatdan muvaffaqqiyatli o'tdingiz.")
                        global login_user
                        login_user = user_data
                        return
                    else:
                        print('Bunday foydalanuvchi ma\'lumotlari yo\'q')
                        continue
            case "2":  # registration
                ism = input("Ismingizni kiriting: ")
                user_name = input('Username ni kiriting: ')
                for i in range(5):
                    if check_username(user_name):
                        break
                    else:
                        user_name = input("Bu username band, \nboshqa username kiriting: ")
                else:
                    print("Urinishlar soni tugadi, birozdan so'ng qayta urinib ko'ring!!")
                    continue

                password = input('Password ni kiriting: ')

                with connect('todo.db') as db:
                    kursor = db.cursor()
                    kursor.execute(
                        """
                        INSERT INTO user VALUES(?, ?, ?)
                        """, (ism, user_name, password)
                    )
                print("Siz ro'yxatdan muvaffaqqiyatli o'tdingiz.")
                login_user = kursor.fetchone()
                return


authentication()

def format_tasks(header, tasks):
    if tasks:
        max_title_length = 0
        max_description_length = 0
        for task in tasks:
            if len(task[0]) > max_title_length:
                max_title_length = len(task[0])
            if task[1] and len(task[1]) > max_description_length:
                max_description_length = len(task[1])
        print(f"{'_' * (33 + max_description_length + max_title_length)}\n"
              f"{header}\n"
              f"{'_' * (33 + max_description_length + max_title_length)}")
        print(
            f"No | Title {' ' * (max_title_length - 6)} | Description {' ' * (max_description_length - 12)} | Due        | Completed")
        n = 1
        for task in tasks:
            print(
                f"{n}  | {task[0]:<{max_title_length}} | {task[1]:<{max_description_length}} | {"✅" if task[3] else "❌"} | {task[2]} |")
            n += 1
        print(f"{'_' * (33 + max_description_length + max_title_length)}\n")
    else:
        print("Tasklar topilmadim.")

while True:
    bolim = input("-------------------\n"
                  "1 -> Yangi topshiriq qo'shish.\n"
                  "2 -> Hamma topshiriqlarim.\n"
                  "3 -> Bajarilmagan topshiriqlarim.\n"
                  "4 -> Tugallangan topshiriqlarim.\n"
                  "0 -> Chiqish.\n"
                  "-------------------\n"
                  "Bo'limni tanlang: ")

    match bolim:
        case "0":
            print('Dasturdan chiqildi!')
            exit(0)
        case '1':
            title = input("Topshiriq uchun sarlavha kiriting: ")
            text = input("Topshiriq matnini kiriting: ")
            while True:
                deadline_str = input("So'nggi muddatni kiriting: \n(YYYY-MM-DD) Masalan: 2024-01-29 \nDavom etish uchun Enterni bosing >>> ")
                if len(deadline_str) < 1:
                    deadline_date = None
                    break
                try:
                    deadline_date = datetime.datetime.strptime(deadline_str, '%Y-%m-%d').date()
                    if deadline_date > datetime.date.today():
                        break
                    else:
                        print("Bugundan keyingi sanani kiriting: ")
                        continue
                except:
                    print("No'to'g'ri sana kiritdingiz, qaytadan kiriting: ")
                    continue
            with connect('todo.db') as db:
                kursor = db.cursor()
                kursor.execute(
                    """
                    INSERT INTO task VALUES(?, ?, ?, ?, ?) 
                    """, (title, text, deadline_date, False, login_user[1])
                )
            print("Sizning topshirig'ingiz muvaffaqqiyatli qo'shildi!")

        case "2":
            with connect('todo.db') as db:
                kursor = db.cursor()
                kursor.execute(
                    f"""
                    SELECT * FROM task
                    WHERE user = "{login_user[1]}"
                    """
                )
                tasks = kursor.fetchall()
                format_tasks("hamma topshiriqlar", tasks)
        case "3":
            with connect("todo.db") as db:
                kursor=db.cursor()
                kursor.execute(
                    f"""
                    
                    """
                )
