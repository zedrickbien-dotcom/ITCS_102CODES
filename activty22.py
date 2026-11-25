anime_type = ["isekai","adventure","scifi",'manhwa"]
anime_title = []
while True:
   ans = input ("do you know any anime --> (yes/no)")

   if ans.lower() == "yes":
      print("what is its type -- / select from the list")
      for x in anime_type:
          print(x)

           a_type = input("type -->")

           title = input ("what is the title of the anime ")
           anime_title.append(title)
           continue
        else:
           print("thank you")
           break
