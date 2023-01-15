import easyocr
import tkinter as tk
from tkinter import filedialog


#Нужен интерпритатор версии 3.10.7 64-bit, иначе Visual Code не видит easyocr
def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path)

    return result

#1. На данном этапе терминал выводит информацию в следующем формате: Координаты четырех точек "рамки", обводящей блок текста; Блок текста; Степень уверенности программы в своих выводах.
#2. Данный код я взял отсюда: https://youtu.be/H_nXZSM4WiU
#3. Загрузить датасет на гитхаб не вышло, так что, если кому надо, вот ссылка https://github.com/zzzDavid/ICDAR-2019-SROIE/tree/master/data

#Первая переменная - путь к изучаемой картинке.
#Вторая переменная - место, куда будет сохранен файл с результатами.
def text_print(adress):
    text = text_recognition(adress)

    #Из полного имени выбранного файла удаляем все лишнее
    name = adress.split("/")
    name = name[len(name)-1]
    name = name.split(".")
    name = name[0]

    #Задаем адрес папки, в которой будет сохранен исходный файл.
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    f = open(file_path+"/"+name+"-1.txt", 'w')
    for i in range(len(text)):
        f.write("("+str(text[i][0])+", "+str(text[i][1])+")")
        if(i != len(text)-1):
            f.write('\n')
    f.close()

root = tk.Tk()
root.withdraw()

#Вводим в программу ссылку на путь к искомой картинке
file_path = filedialog.askopenfilename()

text_print(file_path)
