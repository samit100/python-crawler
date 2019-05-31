from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
 
 
class QuotesSpider(Spider):
    name = 'quotes'
    start_urls = ('https://www.researchgate.net/institution/California_State_University_Fullerton',)
 
    def parse(self, response):
        token = response.xpath('//*[@name="request_token"]/@value').extract_first()
        print(token)
        return FormRequest.from_response(response,
                                         formdata={ "request_token":token,
                                                    "invalidPasswordCount":"0",
                                                    'email': 'zz-sasharma@fullerton.edu', 
                                                    'password': '23811986',
                                                    "setLoginCookie":"yes"},
                                         callback=self.scrape_pages)
 
    def scrape_pages(self, response):
        
        print("--------------------SUCCESS------------------------")
        print(response)
        #open_in_browser(response)
        

    # Complete your code here to scrape the pages that you are redirected to after logging in

    # ....
    # ....
