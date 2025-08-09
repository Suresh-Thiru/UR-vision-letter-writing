import os
from stroke import text_to_strokes
from ur_script import send_move_l, draw_stroke, HOME_POSITION
import time

os.system("python writing.py")

with open("recognized_text.txt", "r") as f:
    word = f.read().strip().upper()

if word == "":
    print("No text found.")
    exit()
  
strokes = text_to_strokes(word)

key = input("Press W to send to robot: ").strip().lower()
if key != 'w':
    print("Cancelled.")
    exit()

send_move_l(HOME_POSITION)
time.sleep(1)

for p1, p2 in strokes:
    draw_stroke(p1, p2, (HOME_POSITION[0], HOME_POSITION[1]))
    time.sleep(0.1)

send_move_l(HOME_POSITION)
print("Done.")
