MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU_STRING)
choice = input()
while  choice != "Q":
   if choice == "H":
       print("Hello " + name)
   elif choice == "G":
       print("Goodbye " + name)
   else:
       print("invalid message")
   print(MENU_STRING)
   choice = input()
print("Finished")