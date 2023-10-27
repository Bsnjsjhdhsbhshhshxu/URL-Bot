from cloudscraper import CloudScraper as Session
import re

def run_directlink_bot(link, proxy=None, headless=None):
    ua='Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
    s=Session()
    s.proxies=dict(http=proxy, https=proxy)
    while link:
        r1 = s.get(link.replace('\\',''), headers={'User-Agent':ua, 'Referer': 'https://technicalzarir.blogspot.com'})
        match = re.findall(r'location.replace\("(.*?)"\)', r1.text)
        print(match)
        if match:
            link=match[0]
        else:
            link = None
            
    


if __name__=='__main__':
    from all_links import random_directlink
    run_directlink_bot(random_directlink, headless=False)
