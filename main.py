import random
from compiler import compile
import time
fnameraw = random.randint(1000,9999)
fname = f"shan/cache/{str(fnameraw)}.shan"
open(fname, "w")

def read():
  count = 1
  with open(fname, "r") as f:
   for line in f:
    line = f.read()
    compile(line)
    count += 1

def add(code):
  
  with open(fname, "a") as file:
    file.write(f"{code} \n")
    file.close()


count = 0
while True:
  count += 1
  code = input(str(count) + ": ")
  if code == "shan.compile":
    read()

  else:
    add(code)