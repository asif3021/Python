print("1 for add number\n2 for search number\n3 for delete number")
a=[10,20,30,40,50,60,500,110,8]
n=int(input("Enter choice: "))

      
while True:
      if n==1:
          a.append(int(input("Enter new number: ")))
      elif n==2:
            num=int(input("Enter a number to search: "))
            if num in a:
                    print(num, "is in list.")
            else:
                    print(num,"is not in list")
      elif n==0:
          break
      elif n==4:
          print(a)
      print("1 for add number\n2 for search number\n3 for delete number")
      n=int(input("Enter choice: "))




#print(a)
