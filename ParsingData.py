#На вход будет подаваться набор из множества строк, хранящих в себе информацию о множестве различных компаний.
#На выход надо будет подать строку, хранящую в себе общую информацию по каждой из компаний.
def parsing_data(data):

    #То, что, по итогу, будет отправлено.
    final_data = ""
    company = ""
    adress = ""
    date = ""
    total = ""
    #Обрабатываем текст построчно
    for i in range(len(data)):

        #По тобуляции делим строку на элементы, каждая строка состоит из 2-х элементов: слово, класс слова
        if data[i] != '\n':
           block = data[i].split('\t')

           if block[1] == 'S-COMPANY\n':
              company = company+str(block[0])+' '

           if block[1]=='S-ADDRESS\n':
              adress += block[0]+' '

           if block[1] =='S-DATE\n':
                date += block[0]

           if block[1] == 'S-TOTAL\n':
              total += block[0]

        #Итак, мы прошлись по всем строкам данного блока, пора подготовить полученные данные к отправке.
        if total != '': 
           company = company[:-1] 
           adress = adress[:-1]         
           final_data= final_data +'{' +  '"company": ' +'"'+ company+'"'+', '+  '"date": ' +'"'+ date+'"'+', '+  '"adress": ' +'"'+ adress+'"'+', '+  '"total": ' +'"'+ total+'"'+'}'+'\n'
           print(final_data)
           company = ""
           adress = ""
           date = ""
    return final_data