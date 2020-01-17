#1.
#a = [1, 2, 3]
#b = [2, 3, 4]

#answer = [i * j for i in b for j in a]
#print (answer)

#2.
#a = [[1, 2],
 #   [3, 4],]
#b = [[5, 6],
  #  [7, 8]]

#answer = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))] 
#for l in answer:
 #   print (l)

#3.

#4. 
#listNum = [1, 2, 3, 4, 4, 5, 5]
#print(listNum)
#newList = []
#for i in listNum:
 #   if i not in newList:
  #      newList.append(i)
#print(newList)
#5
text = "The term leet is derived from the word elite"
leetUpper = text.upper()
leetList = list(leetUpper)
for i in leetList:
        if i == 'A':
            leet = leet.replace('A', '4')
        elif i == 'E':
            leet = leet.replace('E', '3')
        elif i == 'G':
            leet = leet.replace('G', '6')
        elif i == 'I':
            leet = leet.replace('I', '1')
        elif i == 'O':
            leet = leet.replace('O', '0')
        elif i == 'S':
            leet = leet.replace('S', '5')
        else:
            pass
print(text)


