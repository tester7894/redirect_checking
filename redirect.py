from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://digitaloctane.co')
driver.maximize_window()
time.sleep(2)

with open('list.txt', 'r') as file:
	domains = file.readlines()
	for domain in domains:
		driver.get(f'https://{domain}')
		print(f'Request to: {domain}')
		time.sleep(2)
