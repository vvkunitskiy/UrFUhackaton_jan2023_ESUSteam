import easyocr
#Нужен интерпритатор версии 3.10.7 64-bit, иначе Visual Code не видит easyocr
def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path)

    return result

#Да, это грубый костыль, и каждому придется менять значение этой переменной под свой компьютер, но зато позволяет ограничиться вводом номера искомой картинки, не растекаясь на полное имя.
adress = "c:/Users/Lenovo/Desktop/Project/UrFUhackaton_jan2023_ESUSteam"

#1. На данном этапе терминал выводит информацию в следующем формате: Координаты четырех точек "рамки", обводящей блок текста; Блок текста; Степень уверенности программы в своих выводах.
#2. Данный код я взял отсюда: https://youtu.be/H_nXZSM4WiU
#3. Загрузить датасет на гитхаб не вышло, так что, если кому надо, вот ссылка https://github.com/zzzDavid/ICDAR-2019-SROIE/tree/master/data

#Первая переменная - путь к изучаемой картинке.
#Вторая переменная - место, куда будет сохранен итоговый файл.
def text_print(adress, adress1):
    text = text_recognition(adress)
    f = open(adress1, 'w')
    for i in range(len(text)):
        f.write(str(text[i][0])+", "+str(text[i][1]))
        if(i != len(text)-1):
            f.write('\n')
    f.close()

file_path = input("Enter a file path: ")
text_print(adress + "/data/img/"+file_path+".jpg", adress+"/"+file_path+"-1.txt")
