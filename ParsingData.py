#На вход будет подаваться набор из множества строк, хранящих в себе информацию о конкретной компании.
#Надо извлечь оттуда необходимый минимум и скомпилировать его в одну строку
def parsing_data(data):
    
    company = ""
    date = ""
    adress = ""
    total = ""

    #Обрабатываем строки по очереди
    for i in range(len(data)):

        if data[i][1]!= 'O':
            if data[i][1] == 'S-COMPANY':
                company += data[i][0]+ ' '

            if data[i][1] == 'S-ADDRESS':
                adress += data[i][0] + ' '

            if data[i][1] == 'S-DATE':
                date += data[i][0]

            if data[i][1] == 'S-TOTAL':
                total += data[i][0]

    return f"company: {company}, date: {date}, adress: {adress}, total: {total}"