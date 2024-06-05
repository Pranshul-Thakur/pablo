import pyautogui
import random
import tkinter as tk
x = 1400
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
impath = 'put da path here'
def event(cycle,check,event_number,x):
 if event_number in idle_num:
  check = 0
  print('idle')
  window.after(400,update,cycle,check,event_number,x)
 elif event_number == 5:
     check = 1
     print('from idle to sleep')
     window.after(100,update,cycle,check,event_number,x)
 elif event_number in walk_left:
     check = 4
     print('walking towards left')
     window.after(100,update,cycle,check,event_number,x)
 elif event_number in walk_right:
     check = 5
     print('walking towards right')
     window.after(100,update,cycle,check,event_number,x)
 elif event_number in sleep_num:
     check  = 2
     print('sleep')
     window.after(1000,update,cycle,check,event_number,x)
 elif event_number == 14:
     check = 3
     print('from sleep to idle')
     window.after(100,update,cycle,check,event_number,x)
