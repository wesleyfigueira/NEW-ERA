import pyautogui
import time
import pandas



link ='https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

time.sleep(5)

pyautogui.write(link)
time.sleep(1)
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(x=447, y=628, clicks=2) 
time.sleep(3)

pyautogui.click(x=610, y=625)
time.sleep(3)
pyautogui.click(x=713, y=201)


caminho=r"C:\Users\wesle\Downloads\Vendas - Dez (3).xlsx"
tabela = pandas.read_excel(caminho)

qtde_produtos = tabela["Quantidade"].sum()
faturamento = (tabela["Valor Final"].sum()) 
tipo_produto = (tabela["Produto"] == "Pulseira Estampa").sum()


print(f"Quantidade de produtos vendidos: {qtde_produtos}")
print(f"Faturamento total: R${faturamento}")    
print(f"Tipos de produtos vendidos: {tipo_produto}")

texto= f'''Prezados, segue o relatório de vendas do mês de dezembro.  
Quantidade de produtos vendidos: {qtde_produtos}
Faturamento total: R${faturamento:,.2f}
Pulseira Estampa Vendidas: {tipo_produto}


Qualquer dúvida estou à disposição.

Att, Wesley Figueira'''



time.sleep(5)

pyautogui.hotkey('ctrl', 't')
pyautogui.write('http://mail.google.com')
pyautogui.press('enter')    
time.sleep(10)
pyautogui.click(x=202, y=217)
pyautogui.press('enter')
time.sleep(5)

pyautogui.write('ninofigueira2015@gmail.com')
time.sleep(5)
pyautogui.press('tab') 
time.sleep(2)
pyautogui.press('tab') 
pyautogui.write('Relatório de Vendas')
time.sleep(2)
pyautogui.press('tab')  
time.sleep(5)
pyautogui.write(texto)
time.sleep(5)
pyautogui.press('tab')  
time.sleep(5)
pyautogui.press('enter')




