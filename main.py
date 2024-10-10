string = str(input("Введите строку: "))
print("Длина строки:",len(string))

glasn = 0
soglasn = 0

for i in string:
    if i == "А" or i == "У" or i == "О"or i == "И"or i == "Э"or i == "Ы"or i == "Я"or i == "Ю" or i == "Е" or i == "Ё" or i == "а" or i == "у" or i == "о"or i == "и"or i == "э"or i == "ы"or i == "я"or i == "ю" or i == "е" or i == "ё":
        glasn+=1
    elif i ==" ":
        continue
    else:
        soglasn+=1
        
print("Количество гласных: ",glasn)
print("Количество согласных: ",soglasn)

