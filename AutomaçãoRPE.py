#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)


# In[13]:


#Teste automatizado fazer login
navegador.get("http://54.166.20.145:9080/desafioqa")
navegador.find_element('xpath','//*[@id="login-form"]/fieldset/section[1]/label[2]/input').send_keys("admin")
navegador.find_element('xpath','//*[@id="login-form"]/fieldset/section[2]/label[2]/input').send_keys("admin")
navegador.find_element('xpath','//*[@id="login-form"]/footer/button').click()


# In[10]:


#teste cadastro de cliente
navegador.get("http://54.166.20.145:9080/desafioqa/incluirCliente")
navegador.find_element('xpath', '//*[@id="nome"]').send_keys("Lucas Nobrega Pereira Barroso")
navegador.find_element('xpath','//*[@id="cpf"]').send_keys("459.047.618-56")
navegador.find_element('xpath','//*[@id="saldoCliente"]').send_keys("500.00")
navegador.find_element('xpath','//*[@id="botaoSalvar"]').click()


# In[14]:


#teste transação
navegador.get("http://54.166.20.145:9080/desafioqa/listarVenda")
navegador.find_element('xpath','//*[@id="formListarTransacao"]/div/div/fieldset[2]/div/div/div/input').click()


# In[ ]:




