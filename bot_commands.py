from random import randint 
from telegram import Update
from telegram.ext import CallbackContext
from time import sleep

candys = None
flag = False
def checkcandy(update: Update, context: CallbackContext):
    global candys
    global flag
    if(candys >0):
        SetMessageToUser(update,context,"Осталось шариков: "+ str(candys))
        if(flag == True):
            SetMessageToUser(update,context,"Ваш ход")
            flag = False
        else:
            SetMessageToUser(update,context,"Ход бота")
            flag = True
    else:
        candys = 0
        SetMessageToUser(update,context,"Осталось шариков: "+ str(candys))
        if(flag == True):
            SetMessageToUser(update,context,update.effective_user.first_name + " выйграл!")
        else:
            SetMessageToUser(update,context,"Бот выйграл!")

def start_command(update: Update, context: CallbackContext):
    global candys
    candys = 21
    update.message.reply_text(f'Привет {update.effective_user.first_name}! Игра началась')
    SetMessageToUser(update,context,"Всего шариков: " + str(candys))
    SetMessageToUser(update,context,"Ваш ход")
    

def SetMessageToUser(update: Update, context: CallbackContext,message:str):
    update.message.reply_text(message)

def UserStep(update: Update, context: CallbackContext):
    global candys
    if(update.message.text.isnumeric()):
        if(0<int(update.message.text) and int(update.message.text)<=3):
            candys -= int(update.message.text)
            checkcandy(update,context)
            if(candys == 3):
                candys -= 2
                SetMessageToUser(update,context,"2")
            elif(candys == 2):
                candys -= 1
                SetMessageToUser(update,context,"1")
            else:
                buf = randint(1,3)
                candys = candys -  buf
                SetMessageToUser(update,context,str(buf))
            checkcandy(update,context)
    else:
        update.message.reply_text("Не понятно")
