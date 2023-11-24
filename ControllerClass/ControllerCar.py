from selenium import webdriver;
from selenium.webdriver.common.by import By;
from datetime import datetime
import time as time
import re

class ControllerCar:
	def __init__(self, site, url, carro, valor, filtro, filtroValor, ano, km = 'NULL'):
		self.site = site
		self.url = url
		self.carro = carro
		self.valor = valor
		self.filtro = filtro
		self.filtroValor = filtroValor
		self.ano = ano
		self.km = km

	def varrerDados(self):
		driver = webdriver.Chrome()
		driver.get(f"{self.url}")
		time.sleep(5)
		
		#BARRA LATERAL AUTO SCROLL
		scroll = driver.execute_script('return document.body.scrollHeight')

		for contador in range(200):
			driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
			time.sleep(2)
			new_scroll = driver.execute_script('return document.body.scrollHeight')
			if new_scroll == scroll:
				break
			scroll = new_scroll

		data_e_hora_atuais = datetime.now()
		data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')

		print(f'{self.site} {data_e_hora_em_texto}')
		car = driver.find_elements(By.XPATH, f"{self.carro}")
		valor = driver.find_elements(By.XPATH, f"{self.valor}")
		filtro = driver.find_elements(By.XPATH, f"{self.filtro}")
		filtroValor = driver.find_elements(By.XPATH, f"{self.filtroValor}")
		ano = driver.find_elements(By.XPATH, f"{self.ano}")
		km = driver.find_elements(By.XPATH, f"{self.km}")

		for carsList, valorList, filtroList, filtroValorList, anoList, kmList in zip(car, valor, filtro, filtroValor, ano, km):
			anoFabricacao = re.findall(r"20\d{2}\/\d{4}|20\d{2}", anoList.text)
			kmAtual = re.findall(r"\d{1,}.\d+\s\w[KMkm]|Km\s\d+", kmList.text)
			if filtro != '':
				text = f'CARRO: {filtroList.text} {valorList.text} ANO/FABRICAÇÃO: {anoFabricacao[0]} KM: {kmAtual[0]} \n' 
				print(text.replace("\n", " ").replace(" • ", " ").replace(" | ", " ").replace(" km ", " ").replace(" Km ", " ").replace(" KM ", " ").upper())
			elif filtroValor != '':
				text = f'CARRO: {carsList.text} \n{filtroValorList.text} \n ANO/FABRICAÇÃO: {anoFabricacao[0]} \n KM: {kmAtual[0]} \n'
				print(text.replace("\n", " ").replace(" • ", " ").replace(" | ", " ").replace(" km ", " ").replace(" Km ", " ").replace(" KM ", " ").upper())
			else:
				text = f'CARRO: {carsList.text} \n{valorList.text} \n ANO/FABRICAÇÃO: {anoFabricacao[0]} \n KM: {kmAtual[0]} \n'
				print(text.replace("\n", " ").replace(" • ", " ").replace(" | ", " ").replace(" km ", " ").replace(" Km ", " ").replace(" KM ", " ").upper())
		
		print(f"TOTAL DE VEÍCULOS ENCONTRADO: {len(filtro)}")
