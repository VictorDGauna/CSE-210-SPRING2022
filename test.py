list_words = ["LITERALLY","IRONIC","IRREGARDLESS","WHOM",
        "COLONEL","NONPLUSSED","DISINTERESTED"
        "ENORMITY","LIEUTENANT","UNABASHED"]

##for i in zip(list_words):
  #  print (i[0])

'''for i in zip(list_words):
    guion = len(i[0])
    j = 0
    while j < guion:
        new_word = []
        new_word.append("_")
        print(new_word[0])
        j += 1
    

for i, j in enumerate(list_words):
    print (f"el valor del indice {i} es {j}")
'''
gues = input("gues a letter:\n")
'''for i in zip(list_words):
    word = i[0]

    kiss = int(word.find(gues))
    rest = len(word)
    rest_letter = rest - kiss
    draw = kiss -1
    print("_" * draw, gues,"_" * rest_letter)'''
for i in zip(list_words):
   word = i[0]
   itter = " ".join(word)
   let = itter.split(" ")
   #look = int(word.find(gues.upper()))
   #letters = len(word) -1
   #print(word[0],"_" * letters)
   
   for j in let:
    up = gues.upper()
    
    if up == j[0]:
        print(j[0])
    else:
        print("_", end=" ")
   
