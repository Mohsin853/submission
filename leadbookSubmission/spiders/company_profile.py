import scrapy

class LearnSpider(scrapy.Spider):
    name = 'profiles'
    start_urls = ['https://www.adapt.io/directory/industry/telecommunications/A-1']
    custom_settings = {"TELNETCONSOLE_ENABLED" : False,"ROBOTSTXT_OBEY" : False}

    def parse(self,response):
        for link in response.css('div.DirectoryList_linkItemWrapper__3F2UE a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_companies)

    def parse_companies(self,response):
        company_name= response.xpath( "//div[@class='CompanyTopInfo_leftContentWrap__3gIch']//h1//text()").get(),
        company_location =  response.xpath("//span[contains(@itemprop,'addressLocality')]").css('span::text').get(),
        company_website =  response.xpath("//div[contains(@itemprop,'url')]").css('div::text').get(),
        company_websiteDomain =  response.xpath("//div[contains(@itemprop,'url')]").css('div::text').get().split('http://www.')[-1],
        company_revenue= response.xpath("//div[contains(@class,'CompanyTopInfo_contentWrapper__2Jkic')]")[0].css('span::text').getall(),
        company_size= response.xpath("//div[contains(@class,'CompanyTopInfo_contentWrapper__2Jkic')]")[1].css('span::text').getall(),
        company_industry= response.xpath("//div[contains(@class,'CompanyTopInfo_contentWrapper__2Jkic')]")[2].css('span::text').getall(),
        contact_items = response.xpath("//div[@class='TopContacts_contactName__3N-_e']")
        contact_name =  contact_items.xpath('.//a//text()').get(),
        contact_email =  response.xpath("//button[contains(@itemprop,'email')]").css('button::text').get().split('@')[-1]
        contact_job =  response.xpath("//p[contains(@itemprop,'jobTitle')]").css('p::text').get()

    
        yield{
            'company_name':company_name,
            'company_location':company_location,
            'company_website': company_website,
            'company_webdomain': company_websiteDomain,
            'company_industry': company_industry,
            'company_employee_size': company_size,
            'company_revenue': company_revenue,
            
            
            
            'contact_details':[
        {
            'contact_name': contact_name,
            'contact_jobtitle': contact_job,
            'contact_email_domain': contact_email,
            }
      ]
            
        }

