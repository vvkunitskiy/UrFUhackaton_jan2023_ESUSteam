# UrFUhackaton_jan2023_ESUSteam

## **Runtime**
*Python 3.8.10*

## **SROIE Dataset**
https://drive.google.com/drive/folders/1UqIHGKX4_W6DpEXPKOpHRXCEcCah1Rfn?usp=sharing

## **Table of contents**
[1. Project description](#project-description)  
[2. Which case is being solved](#which-case-is-being-solved)  
[3. Data information](#data-information)  
[4. Project stages](#project-stages)  
[5. Results](#results)  
[6. Conclusions](#conclusions)  

### **Project description**
Решение задачи автоматизированной обработке сканов документов для хакатона от УрФУ в январе 2023 года. Команда Esus

[**⬆**](#table-of-contents) *to the contents*


### **Which case is being solved**
Распознавание на чеках блоков с нужной информацией и её структурированная фиксация в .txt файл.

**Task conditions**

Предоставлен набор данных со сканами чеков, датасет SROIE (создавался для соревнования ICDAR 2019). Необходимо:
* Выделить в изображении сегменты с текстовыми сущностями
* Найти 4 координаты вершин прямоугольника каждого сегмента и содержащуюся в нем информацию, представить в текстовом файле все сущности в виде строк вида
```
72,25,326,25,326,64,72,64,TAN WOON YANN
```
* Провести классификацию типа сущности: компания, дата, адрес, итоговая сумма. Информацию представить в виде файла txt следующей структуры
```
{
	"company": "BOOK TA .K (TAMAN DAYA) SDN BHD",
	"date": "25/12/2018",
	"address": "NO.53 55,57 & 59, JALAN SAGU 18, TAMAN DAYA, 81100 JOHOR BAHRU, JOHOR.",
	"total": "9.00"
}
```

**Quality metrics**  
   

**What is being pracrticed**
   

[**⬆**](#table-of-contents) *to the contents*

### **Data information**
   

[**⬆**](#table-of-contents) *to the contents*

### **Project stages**
* В папке [_PreSolution with easyocr](https://github.com/vvkunitskiy/UrFUhackaton_jan2023_ESUSteam/tree/main/_PreSolution%20with%20easyocr) первоначальная реализация распознавания с помощью easyocr без классификации сегментов
* Далее реализованна Google Colab версия первичного распознавания без классификации. Эта версия [тут]()
* Далее реализована предварительная Google Colab версия с распознаванием и классификацией сегментов. Эта версия [тут](https://drive.google.com/file/d/1Yqz4HqlrKp3LJg3SZBEMr20zkCgqKUo0/view?usp=sharing). Связаная с ней Google Drive папка [тут](https://drive.google.com/drive/folders/1UqIHGKX4_W6DpEXPKOpHRXCEcCah1Rfn?usp=sharing)

Основные этапы реализации задачи:

    1) Импорт модуля tkinter и filedialog для взаимодействия с графическим интерфейсом и диалоговыми окнами.
    2) Объявление функции parsing_data, которая принимает на вход набор из множества строк.
    3) Объявление нескольких переменных, таких как final_data, company, adress, date и total, которые будут использоваться для хранения информации о компаниях.
    4) Обработка данных построчно с использованием цикла for.
    5) Разделение строки на элементы с использованием метода split('\t')
    6) Проверка класса слова и заполнение соответствующих переменных (company, adress, date и total) с информацией о компании.
    7) По завершении обработки всех строк в блоке, формируется итоговая строка с информацией о компании в формате json, которая записывается в переменную final_data
    8) В конце функция возвращает итоговую строку с информацией о всех компаниях.
    9) После вызова функции parsing_data, результат может быть использован для дальнейшей обработки или сохранения в файл. 

[**⬆**](#table-of-contents) *to the contents*

### **Results:**
f1 = 0.9574013157894736

loss = 0.07235755896743451

precision = 0.9495921696574225

recall = 0.9653399668325041

Результаты выполнения задачи показывают, что модель достигла высокой точности в соответствии с тремя метриками: f1-score (0.957), precision (0.950), и recall (0.965).
Близкое к еденице значение f1-score отражает сбалансированность между precision и recall.
Precision демонстрирует, насколько часто модель правильно классифицирует положительные объекты.
Recall - насколько часто модель находит все положительные объекты.
Низкое значение метрики loss (0.072) говорит о том, что модель хорошо справляется с предсказанием и обобщением новых данных.

[**⬆**](#table-of-contents) *to the contents*

### **Conclusions:**
   

[**⬆**](#table-of-contents) *to the contents*


Please, rate this project with ⭐️-s if you consider its interesting or useful.

