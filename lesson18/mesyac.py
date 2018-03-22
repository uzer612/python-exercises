#coding: utf8
def monthName(num, langStr):
    # str: ru/en
    ruList = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    enList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if langStr == 'ru':
        return ruList[num-1]
    else:
        return enList[num-1]


