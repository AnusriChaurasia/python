import os
img="/home/cs2017a106/i.jpg"
cmd="fswebcam -F 3 --fps 20 -r 800x600"+img
os.system(cmd)
print("pic taken")
  
