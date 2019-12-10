from bs4 import BeautifulSoup
from urllib.request import urlopen
from base import Base, Selenium
	
	
class Crawler(Base, Selenium):
	
	def __init__(self, post, **kwargs):
		super().__init__(**kwargs)
		self.array = []
		self.post = post
		self.page = 1


	def getWorkData(self):

		while len(self.array) < 100:
			self.searchYouratorWork()
			self.searchMeetJobsWork()
			self.search104Work()
			self.page += 1

		return self.array
		
			
	def search104Work(self):

		areaJson = self.openFile("104_area.json")

		url = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7" \
			"&keyword=%s&area=%s&order=15&asc=0&sctp=M&scmin=%s&scstrict=1&scneg=0&page=%s&mode=s" % \
			(self.post["keywords"], self.isset(areaJson, [self.post["area"]]), self.post["salary"], self.page)
		html = urlopen(url)

		bsObj = BeautifulSoup(html, 'lxml')

		workList = bsObj.findAll("article", {"class":"js-job-item"})

		for  work  in  workList:
			company = work["data-cust-name"]
			salary = work.find("span", {"class":"b-tag--default"})
			link = work.find("a", {"class":"js-job-link"})

			self.array.append({
				'image':"/static/img/00-01.jpg",
				'title':link.get_text(),
				'url':link["href"],
				'salary':salary.get_text(),
				'company':company
			})

	def searchYouratorWork(self):

		areaJson = self.openFile("yourator_area.json")

		url = "https://www.yourator.co/api/v2/jobs?area[]=%s&term[]=%s&page=%s" % \
			(self.isset(areaJson, [self.post['area']]), self.post['keywords'], self.page)
		workJson = self.getWebJson(url)

		for work in workJson['jobs']:

			salary = self.youratorSalary(work['salary'], self.post["salary"])
			if salary:
				self.array.append({
					'image':work['company']['banner'],
					'title':work['name'],
					'url':"https://www.yourator.co/"+work['path'],
					'salary':salary,
					'company':work['company']['brand']
				})


	def searchMeetJobsWork(self):

		url = "https://api.meet.jobs/api/v1/jobs?page=%s&order=match&q=%s&place=%s" % \
			(self.page, self.post['keywords'], self.post['area'])
		workJson = self.getWebJson(url)

		for work in workJson['collection']:

			if work['salary']['minimum'] < int(self.post["salary"]):
				continue

			salary = self.meetJobSalary(work['salary'])

			self.array.append({
				'image':work['employer']['logo']['url'],
				'title':work['title'],
				'url':"https://meet.jobs/en/jobs/"+str(work['id']),
				'salary':salary,
				'company':work['employer']['name']
			})
		

