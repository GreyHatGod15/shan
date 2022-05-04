def compile(line):
  
  words = line.split(" ")
  func = words[0]
  arg = line.split(" ", 0)[0]
  if func == "print":
   
    print(arg)

  elif func == "input":
    input(arg)
  elif func == "var":
    print("var")
    if words[2] == "=":
      print("equals")
      if words[3] == "input":
        
        print(line.split(" ", 4)[4])
 