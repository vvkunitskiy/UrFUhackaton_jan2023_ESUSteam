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
Набор данных содержит 1000 полных отсканированных изображений чеков, которые
используются для всех трех конкурсных заданий, но с разным
аннотации. Каждое изображение чека содержит около четырех
ключевые текстовые поля, такие как наименование товара, цена за единицу и общая стоимость,
и т. д. Текст, аннотированный в наборе данных, в основном состоит из цифр
и английские символы.
Набор данных разделен на набор для обучения/проверки («trainval»).
и тестовый набор («тест»). Комплект «trainval» состоит из 600 чеков.
изображения предоставляются участникам вместе с их
аннотации. «Тестовый» набор состоит из 400 изображений.
Для обнаружения квитанций и задач OCR каждое изображение в
набор данных аннотирован текстовыми рамками (bbox) и
расшифровка каждого текстового поля. Места обозначены как
прямоугольники с четырьмя вершинами, расположенные по часовой стрелке
начиная сверху. Аннотации к изображению хранятся в
текстовый файл с тем же именем. Формат аннотации
аналогично набору данных ICDAR2015.
Для задачи извлечения информации каждое изображение в
набор данных также аннотируется и сохраняется в текстовом файле.


[**⬆**](#table-of-contents) *to the contents*

### **Project stages**
* В папке [_PreSolution with easyocr](https://github.com/vvkunitskiy/UrFUhackaton_jan2023_ESUSteam/tree/main/_PreSolution%20with%20easyocr) первоначальная реализация распознавания с помощью easyocr без классификации сегментов
* Далее реализованна Google Colab версия первичного распознавания без классификации. Эта версия [тут]()
* Далее задача сегментации без классификации с помощью easyocr была доведена до финального решения. Для этого запустите файл [easyocr_run.py](https://github.com/vvkunitskiy/UrFUhackaton_jan2023_ESUSteam/blob/main/easyocr_run.py) (не требует для выполнения каких-либо иных файлов), установив зависимости:
```
pip install easyocr
```
* Далее реализована предварительная Google Colab версия с распознаванием и классификацией сегментов. Эта версия [тут](https://drive.google.com/file/d/1Yqz4HqlrKp3LJg3SZBEMr20zkCgqKUo0/view?usp=sharing). Связаная с ней Google Drive папка [тут](https://drive.google.com/drive/folders/1UqIHGKX4_W6DpEXPKOpHRXCEcCah1Rfn?usp=sharing). Так же код колаба можно скачать из текущего репозитория - файл [layoutlm_using_the_sroie_dataset.ipynb](https://github.com/vvkunitskiy/UrFUhackaton_jan2023_ESUSteam/blob/main/layoutlm_using_the_sroie_dataset.ipynb)

На данном этапе была взята модель из [LayoutLM Github project](https://github.com/microsoft/unilm) и обучена на данных из предостваленного датасета. Однако структура датасета была так же переработана для улучшения результатов обучения. Например, для обучения подавались данные, где сегменты с текстом были поделены до уровня каждого слова, а не строки.

![photo_2023-01-19_18-58-26](https://user-images.githubusercontent.com/46627206/213643690-8bdd549f-ad0d-45d3-bb15-372bc7a833ad.jpg)

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

Таким образом, поставленная задача распознавания объектов сканированных изображений чеков нашей командой была успешно решена.

[**⬆**](#table-of-contents) *to the contents*


Please, rate this project with ⭐️-s if you consider its interesting or useful!
