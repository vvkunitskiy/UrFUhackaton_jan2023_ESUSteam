# UrFUhackaton_jan2023_ESUSteam

## **Runtime**
*Python 3.8.10*

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
   

[**⬆**](#table-of-contents) *to the contents*

### **Results:**
   

[**⬆**](#table-of-contents) *to the contents*

### **Conclusions:**
   

[**⬆**](#table-of-contents) *to the contents*


Please, rate this project with ⭐️-s if you consider its interesting or useful.

