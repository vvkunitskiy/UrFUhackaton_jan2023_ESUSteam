import tkinter as tk
from tkinter import filedialog
def parsing_data(data,num):

    #То, что, по итогу, будет отправлено.
    company = ""
    adress = ""
    date = ""
    total = ""

    for line in data:
        line = line.split('\t')
        if num == 1:
            line[1] = line[1].replace('\n','')     
        if line[1] == 'S-COMPANY':
             company = company+str(line[0])+' '

        if line[1]=='S-ADDRESS':
           adress += str(line[0])+' '

        if line[1] =='S-DATE':
            date += str(line[0])

        if line[1] == 'S-TOTAL':
              total += str(line[0])
   
    company = company[:-1] 
    adress = adress[:-1]
    return '{' +  '"company": ' +'"'+ company+'"'+', '+  '"date": ' +'"'+ date+'"'+', '+  '"adress": ' +'"'+ adress+'"'+', '+  '"total": ' +'"'+ total+'"'+'}'

def data_from_file():
   root = tk.Tk()
   root.withdraw()

    #Вводим в программу ссылку на путь к искомому файлу
   file_path = filedialog.askopenfilename()
   file1 = open(file_path, "r")
   # считываем все строки
   lines = file1.readlines()
   for line in lines:
        line = line.split('\t')
        line[1] = line[1].replace('\n','')
       # print(line)
   # закрываем файл
   file1.close
   parsing_data(lines,1)



def data_not_from_file(data):
    data = data.split('\n')
    data.remove('')
    data.remove('')
    return parsing_data(data,2)

my_data ="""
TAN	O
CHAY	O
YEE	O
***	O
COPY	O
***	O
OJC1	S-COMPANY
MARKETING1	S-COMPANY
SDN1	S-COMPANY
BHD1	S-COMPANY
ROC	O
NO:	O
538358-H	O
NO1	S-ADDRESS
2	S-ADDRESS
&	S-ADDRESS
4,	S-ADDRESS
JALAN1	S-ADDRESS
BAYU1	S-ADDRESS
4,	S-ADDRESS
BANDAR1	S-ADDRESS
SERI1	S-ADDRESS
ALAM1,	S-ADDRESS
81750	S-ADDRESS
MASAI1,	S-ADDRESS
JOHOR1	S-ADDRESS
TEL:07-388	O
2218	O
FAX:07-388	O
8218	O
EMAIL:NG@OJCGROUP.COM	O
TAX	O
INVOICE	O
INVOICE	O
NO1	S-ADDRESS
:	O
PEGIV-1030765	O
DATE	O
:	O
15/01/2019	S-DATE
11:05:16	O
AM	O
CASHIER	O
:	O
NG	O
CHUAN	O
MIN	O
SALES	O
PERSON	O
:	O
FATIN	O
BILL	O
TO	O
:	O
THE	O
PEAK	O
QUARRY	O
WORKS	O
ADDRESS	O
:.	O
DESCRIPTION	O
QTY	O
PRICE	O
AMOUNT	O
000000111	O
1	O
193.00	O
193.00	S-TOTAL
SR	O
KINGS	O
SAFETY	O
SHOES	O
KWD	O
B05	O
QTY:	O
1	O
TOTAL	O
EXCLUDE	O
GST:	O
193.00	O
TOTAL	O
GST	O
@6%:	O
0.00	O
TOTAL	O
INCLUSIVE	O
GST:	O
193.00	O
ROUND	O
AMT:	O
0.00	O
TOTAL:	O
193.00	O
VISA	O
CARD	O
193.00	O
XXXXXXXXXXXX4318	O
APPROVAL	O
CODE:000	O
GOODS	O
SOLD	O
ARE	O
NOT	O
RETURNABLE	O
&	O
REFUNDABLE	O
****THANK	O
YOU.	O
PLEASE	O
COME	O
AGAIN.****	O
"""
data_from_file()
#data_not_from_file(my_data)