import easyocr
#Нужен интерпритатор версии 3.10.7 64-bit, иначе Visual Code не видит easyocr
def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path)

    return result

#1. Желательно, чтоб терминал запускался прямо из папки с исходным кодом, тогда можно будет не заморачиваться и писать адреса вроде "dada/img/000.jpg".
#2. На данном этапе терминал выводит информацию в следующем формате: Координаты четырех точек "рамки", обводящей блок текста; Блок текста; Степень уверенности программы в своих выводах.
#3. Данный код я взял отсюда: https://youtu.be/H_nXZSM4WiU
#4. Загрузить датасет на гитхаб не вышло, так что, если кому надо, вот ссылка https://github.com/zzzDavid/ICDAR-2019-SROIE/tree/master/data
file_path = input("Enter a file path: ")
print(text_recognition(file_path=file_path))
