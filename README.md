# UrFUhackaton_jan2023_ESUSteam

## **Runtime**
*Python 3.8.10*

## **Dataset**
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

[**⬆**](#table-of-contents) *to the contents*

### **Results:**
f1 = 0.9574013157894736
loss = 0.07235755896743451
precision = 0.9495921696574225
recall = 0.9653399668325041

[**⬆**](#table-of-contents) *to the contents*

### **Conclusions:**
   

[**⬆**](#table-of-contents) *to the contents*


Please, rate this project with ⭐️-s if you consider its interesting or useful.

