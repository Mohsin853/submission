import scrapy

class CompanySpider(scrapy.Spider):
    name = 'company'
    start_urls = ['https://www.adapt.io/directory/industry/telecommunications/A-1']
    custom_settings = {"TELNETCONSOLE_ENABLED" : False,"ROBOTSTXT_OBEY" : False}
    
    def parse(self,response):
        for company in response.xpath("//div[contains(@class,'DirectoryList_link')]"):
            yield{
                'company_name' : company.xpath("./a/text()").get(),
                'source_url' : company.xpath("./a/@href").get().split('https://www.adapt.io')[-1]
            }