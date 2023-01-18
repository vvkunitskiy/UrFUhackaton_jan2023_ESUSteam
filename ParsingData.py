import json

#На вход будет подаваться набор из множества строк, хранящих в себе информацию о конкретной компании.
#Надо извлечь оттуда необходимый минимум и скомпилировать его в одну строку
def parsing_data(data):
    
    company = ""
    date = ""
    adress = ""
    total = ""

    data = data.split('\n')
    #Обрабатываем строки по очереди
    for i in range(len(data)):
        word = data[i].split(' ')

        if word[1]!= 'O':
            if data[i][1] == 'S-COMPANY':
                company += word[0]+ ' '

            if data[i][1] == 'S-ADDRESS':
                adress += word[0] + ' '

            if data[i][1] == 'S-DATE':
                date += word[0]

            if data[i][1] == 'S-TOTAL':
                total += word[0]

    value = {
        "company":company,
        "date":date,
        "adress":adress,
        "total":total
    }

    return json.dumps(value)