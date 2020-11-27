def main():
  # Program Variables

  # Main Program Loop
  loop = True
  while loop:
    selection = getMenuSelection()

    if selection == "1":
      option1()
    elif selection == "2":
      option2()
    elif selection == "3":
      option3()
    elif selection == "4":
      print("Exit")
      loop = False

  print("Goodbye")
# end main()

def getMenuSelection():
  print("\nMAIN MENU")
  print("1: Adding to a html file")
  print("2: clearing an html file")
  print("3: preview html file")
  print("4: Exit")
  return input("\nEnter menu selection: ")

def option1():
  html_file = open("index.html", "a")

  html_file.write(input("\nwrite some html code to add to the empty index file: ") + "\n")
  
  html_file.close()

def option2():
  html_file = open("index.html", "w")

  html_file.write("")

  html_file.close()

  print("\nHTML file succesfully cleared")

def option3():
  html_file = open("index.html", "r")
  print("\nNow viewing index.html---------------------------------------------------------------\n")
  for lines in html_file.readlines():
    
    print(lines)
    
  
  html_file.close()
  print("-------------------------------------------------------------------------------------")

# Call main to begin program
main()
