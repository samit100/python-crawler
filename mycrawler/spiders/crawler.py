from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
 
 
class QuotesSpider(Spider):
    name = 'quotes'
    start_urls = ('https://www.researchgate.net/institution/California_State_University_Fullerton',)
 
    def parse(self, response):
        token = response.xpath('//*[@name="Rg-Request-Token"]/@value').extract_first()
        print(token)
        return FormRequest.from_response(response,
                                         formdata={ 'rg-request-token':token,
                                                    'password': '23811986',
                                                    'username':'zz-sasharma@fullerton.edu'},
                                         callback=self.scrape_pages)
 
    def scrape_pages(self, response):
        
        print("--------------------success------------------------")
        print(response)
        open_in_browser(response)
        

    # Complete your code here to scrape the pages that you are redirected to after logging in

    # ....
    # ....

