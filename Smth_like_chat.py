
# Simple Chat by means of file

def look():
    try:
        with open('chat_log.txt', 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        create_log()


def create_log():
    file = open('chat_log.txt', 'a', encoding='utf-8')
    file.write("{:*^100}\n".format('Chat successfully created!\n'))
    file.close()


def send(user, message):
    try:
        with open('chat_log.txt', 'a', encoding='utf-8') as file:
            file.write("{}: {}\n".format(user, message))
    except FileNotFoundError:
        create_log()

user_name = input("Enter username: ")

while True:
    action = input("What to do?"
                   "\nPress 'ENTER' to have a look at current chat text or type 'EXIT' for quitting"
                   "\nSend a message: ")
    if action == '':
        look()
    elif action == 'EXIT':
        break
    else:
        send(user_name, action)

