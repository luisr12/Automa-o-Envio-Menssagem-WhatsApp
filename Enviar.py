#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Codigo desenvolvido Por Luis Ricardo 16 de Abril de 2023
    
import pandas as pd #Faz a leitura da base de dados que esta presente na planilha em Excel


contatos_df = pd.read_excel("Enviar.xlsx")
display(contatos_df)

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib

navegador = webdriver.Chrome()

navegador.get("https://web.whatsapp.com/")


while len(navegador.find_elements(By.ID,"pane-side")) < 1:
    time.sleep(1)
     
# já estamos com o login feito no whatsapp   
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa=contatos_df.loc[i, "Pessoa"]
    numero=contatos_df.loc[i, "Número"]
    texto=urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"#substitui e recpnhece as variaveis 
    navegador.get(link)
    while len(navegador.find_elements(By.ID,"pane-side")) < 1: #cada pagina após login existe um id/elemento que da o retorno e informa se esta de fato com o login realizadp
        time.sleep(10)
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)
    time.sleep(10)  
  
   


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




