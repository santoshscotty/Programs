import scrapy,requests,json
from monitors.items import MonitorsItem

class monitor(scrapy.Spider):
    name="monitor"
    allowed_domains=["shopclues.com"]
    start_urls=[
        "http://www.shopclues.com/computers/desktops-and-monitors/monitors.html"
    ]
    
    def parse(self,response):
        urllist=[]
        for a in response.xpath('//div[@class="products-grid"]/div[@class="grid-product special category_grid_4 "]/a/@href').extract():
            urllist.append(a)
            if urllist.index(urllist[-1])==9:
                break
        for url in urllist:
            yield scrapy.Request(url, callback=self.parse_url)
    
    def parse_url(self,response):
        def CheckDelivery(pincode,productId):
            r=requests.get('http://www.shopclues.com/nss.php?pincode_no='+pincode+'&product_ids='+productId)
            d=json.loads(r.text)
            delivery={}
            if d['pin_result']!=0:
                delivery={'PinCode':pincode, 'Availability':'Yes', 'ExpectedDate':d['fdate']+' to '+d['sdate']}
            else:
                delivery={'PinCode':pincode, 'Availability':'No'}
            return delivery
        item = MonitorsItem()
        item['Url'] = response._url
        item['Title'] = response.xpath('//title/text()').extract()[0].strip()
        item['Name'] = response.xpath('//h1[@itemprop="name"]/text()').extract()
        item['Thumbnail'] = response.xpath('//div[@class="slide"]//img/@src2').extract()
        item['Price'] = (' ').join(response.xpath('//div[@class="price"]/text()').extract()).strip()
        item['ProductId'] = response.xpath('//div[@id="pincode_avail"]//input[@id="check_but"]/@onclick').extract()[0].split('(')[1].split(',')[0]
        DeliveryInfo = []
        DeliveryInfo.append(CheckDelivery('560070',item['ProductId']))
        DeliveryInfo.append(CheckDelivery('575001',item['ProductId']))
        DeliveryInfo.append(CheckDelivery('671551',item['ProductId']))
        item['DeliveryInfo'] = DeliveryInfo
        yield item
