import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from colorama import init
init()
from colorama import Fore, Back, Style
from banner import banner
from pystyle import *

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

senders = {
'Gbuser50@gmail.com' : 'soso4ka111',
'smertbsmertbb@gmail.com' : 'oooGggrr71k',
'ebanator77@gmail.com' : 'djjdjeiskdkdsmskwlls',
'huysosal57@gmail.com' : 'jeiwiskxkxklslsls',
'kotyaraebanat@gmail.com' : 'Boeing_777-300er',
'mortkrutoy0@gmail.com' : 'pivo228_1000-7',
'entropov002@gmail.com' : 'entropovkakaha',
'tuouikiuo@gmail.com' : 'De34rfvC',
'vwgzucjej@gmail.com' : 'De34rfvC',
'vshsghw20@gmail.com' : 'De34rfvC',
'Issvloasu@gmail.com' : 'De34rfvC',
'hhdhehe011@gmail.com' : 'De34rfvC',
'rrkurkrok@gmail.com' : 'De34rfvC',
'eggejjw@gmail.com' : 'De34rfvC',
'eggwhdjwi@gmail.com' : 'De34rfvC',
'vvavavyavyay@gmail.com' : '456dd456zz',
'arimakaworii@gmail.com' : '456dd456zz',
'g0dtacc1@gmail.com' : '456dd456zz'
}
receivers = ['stopCA@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def logo():
    print(Colorate.Horizontal(Colors.blue_to_purple,Center.XCenter(banner)))
def menu():
    choice = input(f'{COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]} Выбрать >{COLOR_CODE["BOLD"]} ')
    return choice
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(0.4)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    logo()
    choice = menu()
    if choice == '1':
        print("1. Снос")
        print("2. Деанон")
        print("3. Троллинг")
        print("4. Снос сессий")
        print("5. Снос аккаунта с премиумом")
        print("6. Снос аккаунта с вирт номером")
        comp_choice = input("Выбирай: ")
        if comp_choice in ["1", "2", "3"]:
            print("Следуй за указаниям")
            username = input("Username: ")
            id = input("ID: ")
            chat_link = input("Ссылку на чат: ")
            violation_link = input("Ссылку на нарушение: ")
            print("Начинаю работу...")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 15560
                    time.sleep(0.4)

        elif comp_choice == "4":
            print("Следуй указаниям.")
            username = input("Username: ")
            id = input("ID: ")
            print("Начинаю работу...")
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Утеря доступа к аккаунту', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 1560
                    time.sleep(0.4)

        elif comp_choice in ["5", "6"]:
            print("Следуйте указаниям")
            username = input("Username: ")
            id = input("ID: ")
            print("Начинаю работу...")
            comp_texts = {
                "5": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "6": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 9999
                    time.sleep(0.4)


    elif choice == "2":
        
        print("1. С личными данными")
        print("2. С живодерством")
        print("3. С детским")
        print("4. С услугами")
        ch_choice = input("Выбор: ")

        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input("Ссылка на канал: ")
            channel_violation = input("Ссылка на нарушение (в канале): ")
            print("Начинаю работу...")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал, который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал, который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте, уважаемый модератор телеграмм,хочу пожаловаться вам на канал, который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 100000
                    time.sleep(0.4)


    elif choice == "3":
        print("1. ЖАЛОБАМИ" )
        bot_ch = input("INFO: Работает только с деанон ботами :")
        if bot_ch == "1":
            bot_user = input("Тег бота: ")
            print("Начинаю работу...")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Телеграм бот', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 10
                    time.sleep(0.4)

    elif choice == "4":
        print("Главный кодер - @septedecimov | Основатель - @mortmode")                
        main() 

    elif choice == "5":
        print("Успешный выход с системы! GODS SQUAD LOVE YOU")
        exit
        
        

  
if __name__ == "__main__":
    main()
