from datetime import datetime
counter=0

class Spy:
    def __init__(self, name, sal, age, rating):
        self.name = name
        self.sal = sal
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    counter=counter+1
    def __init__(self, message, sent_by_me):
        self.message = message

        self.time = datetime.now()

        self.sent_by_me = sent_by_me


spy = Spy('bond', 'Mr', 24, 7.4)

friend_one = Spy('Kanika', 'Ms', 27,4.7)
friend_two = Spy('Raja', 'Mr',32,8)
friends = [friend_one, friend_two]
