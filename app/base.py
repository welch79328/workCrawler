import re
import os
import json
import locale
from selenium import webdriver


class Base():
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.path = os.path.dirname(os.path.abspath(__file__))

	def isset(self, dict, keys, errResult=''):

		for key in keys:
			if type(key) == int:
				dict = dict[key]
			else:		
				if key in dict.keys():
					dict = dict[key]
				else:
					dict = errResult
					break
		return dict

	def openFile(self, fileName):
		
		f = open(self.path+"/json/"+fileName, "r")
		data = json.loads(f.read())
		f.close()

		return data

	def youratorSalary(self, workSalary, searchSalary):

		locale.setlocale( locale.LC_ALL, 'en_US.UTF-8') 
		if workSalary.find("面議") >= 0:
			if int(searchSalary) != 40000:
				return False
		elif locale.atoi(workSalary.split(" ")[1]) < int(searchSalary):
			return False

		return workSalary

	def meetJobSalary(self, salary):
		
		string = salary['currency'] + " " + str(salary['minimum'])

		if salary['maximum']:
			string += " - " + str(salary['maximum'])
		else:
			string += " UP"

		string += " " + salary['paid_period']

		return string

class Selenium():

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.chrome_options = webdriver.ChromeOptions()

		self.chrome_options.add_argument('--headless')
		self.chrome_options.add_argument('no-sandbox')
		
	def getWebJson(self, url):

		driver = webdriver.Chrome('drivers/chromedriver',chrome_options=self.chrome_options)

		driver.get(url)

		data = json.loads(self.jsonFilter(driver.page_source))

		driver.quit()

		return data


	def jsonFilter(self, data):

		return re.sub(r'</?\w+[^>]*>', '', data)