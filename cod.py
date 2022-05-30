from selenium import webdriver
import time



navegador = webdriver.Chrome()


navegador.get ("http://www.buzzr.com.br/chat.html")
time.sleep(4)
navegador.find_element_by_xpath('//*[@id="chatinput"]').send_keys('Ola, boa tarde...Seja bem vindo ao meu teste.')
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="btnsend"]').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="chatinput"]').send_keys('Instagram:gustavingz contato:teste')
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="btnsend"]').click()