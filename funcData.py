dia =  int(input('Digite um dia:'))
mes = int(input('Digite um mês:'))
ano =int(input('Digite um ano:'))

def func(d=dia,m=mes,y=ano):
    if m == 1:
        m = 'Janeiro'
    if m == 2:
        m = 'Fevereiro'
    if m == 3:
        m = 'Março'
    if m == 4:
        m = 'Abril'
    if m == 5:
        m = 'Maio'
    if m == 6:
        m = 'Junho'
    if m == 7:
        m = 'Julho'
    if m == 8:
        m = 'Agosto'
    if m == 9:
        m = 'Setembro'
    if m == 10:
        m = 'Outubro'
    if m == 11:
        m = 'Novembro'
    if m == 12:
        m = 'dezembro'
    print(f'{d} de {m} de {y}')
    return

func()