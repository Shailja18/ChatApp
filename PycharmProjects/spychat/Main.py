#here we are importing dictionary spydetails
from spydetails import spy,Spy,ChatMessage,friends,counter
from steganography.steganography import Steganography
from datetime import datetime

STATUS_MESSAGES=['Status1','I  m cool','Good Day','Busy','Urgent']



#use of backslash to escape character
# or we can use double quotes
print "Hello Let 's  get started."


# Application started  here
question="Do You want to continue as"+" "+ spy.sal+" "+ spy.name  +"(Y/N)?"
existing=raw_input(question)

#for adding status
def add_status(current_status_message):
    updated_status_message=None

    if spy.current_status_message!=None :
        print "Your current status Message is"+ spy.current_status_message +"\n"
    else:
        print "You dont have any status message update currently."

    ques=raw_input("Do you want to select status from old status(y/n)?")
    if ques.upper()=='N' :
        new_status_message=raw_input("Enter your new status")

        if len(new_status_message)>0 :
             STATUS_MESSAGES.append(new_status_message)
             updated_status_message=new_status_message


    elif ques.upper()=='Y' :
        pos=1

        for message in STATUS_MESSAGES:
            print '%d.%s'%(pos ,message)
            pos=pos+1

        message_selection=int(raw_input("Choose from above messages"))

        if len(STATUS_MESSAGES)>=message_selection :
               updated_status_message=STATUS_MESSAGES[message_selection-1]


    else:
       print "The option you chooses is not valid!Press either y or no"

    if updated_status_message:
        print "Your updated message is %s"%(updated_status_message)
    else :
        print "You currently don't have a status update."

    return updated_status_message


#for adding  friendlist to spy
def add_friend():
    #friends_name=[]
    #friends_age=[]
    #friends_rating=[]
    #friends_status=[]
    #we are adding dictionary instead of 4 lists
 new_friend=Spy('','',0,0.0)


 new_friend.name=raw_input("Please add your friend's name:")
 new_friend.sal =raw_input("Are they Mr. or Ms :")

 new_friend.name=new_friend.sal+" "+new_friend.name

 new_friend.age=raw_input("Age?")
 new_friend.age=int(new_friend.age)

 new_friend.rating = raw_input("Spy-rating?")
 new_friend.rating=float(new_friend.rating)


 if len(new_friend.name)>0 and new_friend.age>12  and new_friend.rating>=spy.rating :
 #add friend
  friends.append(new_friend)
  print "Friend Added!"
 else :
     print "Sorry!Invalid Entry We can't add spy with details you  provided."

 return len(friends) # to return no of friends added into list



#this function has 3 points
#Print out all the friends of the user.
#Ask the user to select from one of the friends.
#Return the index of the selected friend in the friends list.
def select_a_friend():
  item_number=0
  for friend in friends:

    print "%d %s%s aged  %d with rating %.2f is online " %(item_number+1,friend.sal, friend.name,
                                                            friend.age,friend.rating)
    item_number=item_number+1
  friend_choice=raw_input("Choose from your friends")
  friend_choice_position=int(friend_choice)-1
  return  friend_choice_position

def del_spychat( n):
   friends.remove(n);

def send_message():
    friend = select_a_friend()
    friend_choice= friend
    orignal_image=raw_input("What is the name of image?  ")
    output_path="C:\Users\user\Documents\ background.jpg"   #C:\Users\user\Documents\front1.jpg
    text=raw_input("What do you want to say? ")
    # for checking is there any special message from spy then print the message
    if text== "SOS":
        print " ITS URGENT "
    elif (text == "SAVE"):
        print "DO FAST"

    Steganography.encode(orignal_image,output_path,text)
    new_chat=ChatMessage(text,True)
    friends[friend_choice].chats.append(new_chat)
    #checking if spy is sending many messages than irritating me automatically delete that spy
    #condition on counter variable everytime we chat it increase by 1
    if counter > 2 :
        print "You are disturbing me.You are deleted from my list of friends"
        del_spychat(friend_choice)
    print "Your secret message is  ready! "


def read_message():
    sender=select_a_friend()
    output_path=raw_input("What is the name of file?")
    # checking if image contains any secret message or not
    secret_text=Steganography.decode(output_path)
    #if secret_text =="" :
    #   print "Does not contain any secret message.WRONG PATH is chosen"
   # else:
    new_chat=ChatMessage(secret_text,False)
    friends[sender].chats.append(new_chat)

    print "your secret message has been saved!"


def read_chat_history():
    read_for=select_a_friend()

    print '\n6'
    for chat in friends[read_for].chats:
      if chat.sent_by_me:
          print '[%s]%s:%s'%(chat.time.strftime("%d%B%Y"),'You said:',chat.message)
      else :
          print '[%s]%s:%s'%(chat.time.strftime("%d%B%Y"),friends[read_for].name,chat.message)



def start_chat(spy):

   current_status_message=None
   spy.name=spy.sal+" "+spy.name

   if spy.age>12 and spy.age<50:
        if spy.rating > 4.5:
         print "Great ace ! "
        elif spy.rating> 3.5 and spy.rating<=4.5:
          print " You are  one of the goodones."
        elif spy.rating> 2.5 and spy.rating<=3.5:
          print "You can always do better."
        else :
         print"We can always do  somebody to help in the office."

        print "Authentication Complete.Welcome" +spy.name + str(spy.age) +" and rating of:" + str(spy.rating) + "Proud to hav e you on board"
        show_menu=True
        while show_menu:
          menu_choices="What do you want to do?\n 1.Add a status update \n 2.Add a friend\n 3.Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
          menu_choice = raw_input(menu_choices)


          if len(menu_choice) >0:
            menu_choice=int(menu_choice)

            if menu_choice==1:
             print "Update a status"
             spy.current_status_message=add_status(current_status_message)
            elif menu_choice==2:
                 no_of_friends=add_friend()
                 print "You have %d friends"%(no_of_friends)
            elif menu_choice==3:
                 send_message()
            elif menu_choice==4:
                read_message()
            elif menu_choice==5:
                read_chat_history()
            elif menu_choice==6:
                show_menu=False
            else:
                print "Invalid choice .Please enter valid choice"

   else:
     print "Sorry you are not of correct age to be spy. "



if existing.upper()=='Y' :
        start_chat(spy)
        # continue with default user input from spydetails file
else :

   spy=Spy('','',0,0.0)

   spy.name=raw_input("Welcome to spychat,you must tell me your spyname first:")

 #Checking if name is enterd or not
   if len(spy.name)>0:
    #concating string

    print "Welcome"+ spy.name+ "Glad to have u back."

    spy.sal=raw_input("what sould I call u  Mr or Mrs ?")
    spy.name=spy.sal+" "+spy.name

    spy.age= raw_input("What is your age?")
    spy.age=int(spy.age)

    spy.rating=raw_input("What is your spy rating ?")
    spy.rating=float(spy.rating)

    spy.is_online=True
    start_chat(spy)

   else:
    print "Please add a valid spy_name"



   #Use of and keyword that is if 2 condition is satisfy
 # if spy_age>12 and spy_age<50 :

  #      if spy_rating>4.5:
   #         print "Great ace ! "
    #    elif spy_rating> 3.5 and spy_rating<=4.5:
     #       print " You are  one of the goodones."
     #   elif spy_rating> 2.5 and spy_rating<=3.5:
     #       print "you can always do better."
     #   else :
    #        print"We can always do  somebody to help in the office."

   # else :
    # print"Sorry you are not of the correct age to be spy."
    #spy_is_online = True
    #use of placeholders
  #  print "Authentication complete. Welcome %s having age %d rating of %f"%(spy_name,spy_age,spy_rating)

 #else:
#          print "A  spy needs to have a valid name.Please try this again. "

