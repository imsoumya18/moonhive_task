import os
import shutil
import schedule
import time
from datetime import date


def xinit():
    global i
    i = 1


def job():
    global i
    x = i
    i += 1
    os.mkdir('Folder ' + str(x))
    for file in os.listdir(os.getcwd() + '\\A'):
        src = os.getcwd() + '\\A\\' + file
        if file == 'e.txt':
            break
        dst = os.getcwd() + '\\Folder ' + str(x) + '\\' + file
        shutil.copyfile(src, dst)


def monthly():
    if date.today().day != 1:
        return
    global i
    x = i
    i += 1
    os.mkdir('Folder ' + str(x))
    for file in os.listdir(os.getcwd() + '\\A'):
        src = os.getcwd() + '\\A\\' + file
        if file == 'e.txt':
            break
        dst = os.getcwd() + '\\Folder ' + str(x) + '\\' + file
        shutil.copyfile(src, dst)


print('Choose preferred option:\n'
      '1: Run One Time\n'
      '2: Run Every Minute\n'
      '3: Run Every Hour\n'
      '4: Run Daily\n'
      '5: Run Weekly\n'
      '6: Run Monthly\n')

n = int(input('Enter your schedule option: '))

xinit()

if n == 1:
    job()

elif n == 2:
    schedule.every().minute.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

elif n == 3:
    schedule.every().hour.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

elif n == 4:
    schedule.every().day.at('00:00').do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

elif n == 5:
    schedule.every().sunday.at('00:00').do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

elif n == 6:
    schedule.every().day.at('00:00').do(monthly)
    while True:
        schedule.run_pending()
        time.sleep(1)
