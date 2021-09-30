import requests
from bs4 import BeautifulSoup
import json

class ZillowScraper():
    results = []
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,',
        'accept-encoding':'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'zguid=23|%2400ff2660-497a-4653-8738-6b4bcac01665; zjs_user_id=null; _ga=GA1.2.449131967.1633015682; _gid=GA1.2.1423521492.1633015682; _gac_UA-21174015-56=1.1633015682.Cj0KCQjwwNWKBhDAARIsAJ8Hkhfm53Da5HQFMLuJX74kyvkUWOrF2IqAahMXz33f-srWZdGQN6aNoOoaAiBnEALw_wcB; zjs_utmmedium=%22cpc%22; zjs_utmsource=%22google%22; zjs_anonymous_id=%2200ff2660-497a-4653-8738-6b4bcac01665%22; zjs_utmcontent=%221471765354|65545421468|aud-352785741564:kwd-570802407|540282423994|%22; _gcl_aw=GCL.1633015683.Cj0KCQjwwNWKBhDAARIsAJ8Hkhfm53Da5HQFMLuJX74kyvkUWOrF2IqAahMXz33f-srWZdGQN6aNoOoaAiBnEALw_wcB; _gcl_au=1.1.684803995.1633015683; KruxPixel=true; _pxvid=ff4fc500-2202-11ec-9b44-68545044784a; __pdst=602bfa47e95c4e568074f494b01358be; _fbp=fb.1.1633015682894.1380198444; _pin_unauth=dWlkPU9UWmpOVFptT0RrdE0ySTVNaTAwTXpRNUxXRmpPRGN0T1dJd01EazJObVEyTUdVNA; utag_main=v_id:017c3751d6a1001d54cfd9a763ce0507200f706a00bd0$_sn:1$_se:1$_ss:1$_st:1633017482722$ses_id:1633015682722%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_visit:1$dc_event:1%3Bexp-session$dc_region:us-east-1%3Bexp-session$ttd_uuid:a9308c5d-d89f-4cd5-918d-af61a7333ebd%3Bexp-session; __gads=ID=81de51ca75ac2fcb:T=1633015691:S=ALNI_MYy9o2PNGGYxPSCuvddRtbaa8wOnQ; KruxAddition=true; zgsession=1|9e61ac71-fb10-4dc1-a86c-d7ec79001a1f; DoubleClickSession=true; JSESSIONID=60A26B24F5221A8EF2BB3250B5FD4EE6; _pxff_tm=1; search=6|1635608326229%7Crect%3D34.01181257012807%252C-84.25183804589844%252C33.535796041282055%252C-84.70914395410156%26rid%3D37211%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26excludeNullAvailabilityDates%3D0%09%0937211%09%09%09%09%09%09; AWSALB=lIu2dhoG0d/79jGysPz0sWY2kbk4P0i8UALZ+9UQJ0ZBxTMFZOryQiPAVeMIZZfLDr7V/kGX88+ZfO3+m7ZJH3zMdeW+GgQbNoaxLiqXXvZ+m3dqzRkbyqpbtA9l; AWSALBCORS=lIu2dhoG0d/79jGysPz0sWY2kbk4P0i8UALZ+9UQJ0ZBxTMFZOryQiPAVeMIZZfLDr7V/kGX88+ZfO3+m7ZJH3zMdeW+GgQbNoaxLiqXXvZ+m3dqzRkbyqpbtA9l; _uetsid=004d5e30220311ec9afd13256f70a277; _uetvid=004d4740220311ec8aab654910d0460b; _px3=6eef5ef9e0f322083179060ad8a2875988afd45471f0ecf15ce1b1d66e18d445:VMlGe9FIdUUQE+qhBm7YDjTizNPLrel6VqJNhNr2hc2nuCnO0rwJFWnovsIYF+NjwlZGvVcxfdlpsKzK88Dn3w==:1000:L7XDeJoaZdQ/ekih8JvK1NE7/6C38oTxKl7VDra5axsHpPheRKexPCDIEsBKMG12QTdJ1IfrLF4ZY7qu32jLGgASHZIZK3LBONy1w41lH8jrFEhR8iuwoGYyMzBjuwzz44cgVSZ1iBgATOwprshnLeKGRQToK7QmEv89hpi4fD4gs7AroAowFLRbG1cKobECZVmbndYT3i/lEKGaHpI3pw==',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    def fetch(self, url, params):
        response=requests.get(url, headers=self.headers, params=params)
        print(response)
        return response
    
    def parse(self, response):
        content = BeautifulSoup(response,"lxml")
        deck = content.find('ul', {'class': 'photo-cards photo-cards_wow photo-cards_short photo-cards_extra-attribution'})
        for card in deck.contents:
            script = card.find('script', {'type':'application/ld+json'})
            # avoid the advertisment card
            if script:
                #print(script.prettify())
                # because its a script and not HTML you cant use .text
                script_json = json.loads(script.contents[0])
                self.results.append({
                    'name': script_json['name'],
                    'floorSize': script_json['floorSize']['value'],
                    'type': script_json['@type'],
                    'street': script_json['address']['streetAddress'],
                    'city': script_json['address']['addressLocality'],
                    'state': script_json['address']['addressRegion'],
                    'postal_code': script_json['address']['postalCode'],
                    'latitude': script_json['geo']['latitude'],
                    'longitude': script_json['geo']['longitude'],
                    'url':  script_json['url']
                })
        print(self.results)
               # * name 
               # * floor size
               # * url
               # * geo
               # * @type -sfr
    def run(self):
        url = 'https://www.zillow.com/atlanta-ga/'
        params = {
             'searchQueryState': '{"pagination":{"currentPage": 1},"usersSearchTerm":"Atlanta, GA","mapBounds":{"west":-84.70914395410156,"east":-84.25183804589844,"south":33.53579604128204,"north":34.01181257012808},"regionSelection":[{"regionId":37211,"regionType":6}],"isMapVisible":true,"filterState":{"sort":{"value":"globalrelevanceex"},"ah":{"value":true}},"isListVisible":true,"mapZoom":11}'
        }
        res = self.fetch(url, params)
        self.parse(res.text)


if __name__ == "__main__":
    scraper = ZillowScraper()
    scraper.run()