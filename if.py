count = 1
while (count <= 5):
  marks = int(input("Please enter your marks:"))
  if (marks >= 70):
        print("A")
        if (marks == 100):
            print("Excellent!")
  elif (marks >= 55 and marks < 70):
      print("B")
  elif (marks >= 40 and marks < 55 ):
      print("C")
  else:
      print("F")
  count = count + 1


