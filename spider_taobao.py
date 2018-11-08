import requests
import re
import json
 
def spider_tb(sn ,book_list=[]):
    url = 'https://s.taobao.com/search?q={0}'.format(sn)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'cookie': 'v=0; _tb_token_=85313680b514; cna=EhhJEwKs4U8CAXFDSSDeum+R; thw=cn; unb=654670617; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=U%2BGCWk%2F7pY%2FF&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTYN4fr5ZcONQ%3D%3D&tag=8&lng=zh_CN; sg=677; t=e6f3bce9ad0b5479d8d395b0a3bbdfa9; _l_g_=Ug%3D%3D; skt=c422c369c7de616c; cookie2=180de4f13d13b6c2986b7400cfd28ced; cookie1=VTwqmr0QBwbFGDtAh3gC%2BGysoufc69dbMpSfLJU%2B6VM%3D; csg=81537acb; uc3=vt3=F8dByR%2FIlsOXXvXl0XE%3D&id2=VWolnYzstf61&nk2=GgIJuytndLQ%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTU0MTY4NzkzMg%3D%3D; tracknick=yima1006; lgc=yima1006; _cc_=WqG3DMC9EA%3D%3D; dnk=yima1006; _nk_=yima1006; cookie17=VWolnYzstf61; tg=0; mt=np=; isg=BMXFMhEaMqB5nRdaHdsBfR0QwAE_KmaieT5OAccrhfwSXuHQqdFC5eZ_bMINGJHM'
    }
    #获取html内容
    text = requests.get(url, headers=headers).text
 
    # 使用正则表达式找到json对象
    p = re.compile(r'g_page_config = (\{.+\});\s*', re.M)
    rest = p.search(text)
    if rest:
        print(rest.group(1))
        data = json.loads(rest.group(1))
        bk_list = data['mods']['itemlist']['data']['auctions']
 
        print (len (bk_list))
        for bk in bk_list:
            #标题
            title = bk["raw_title"]
            print(title)
            #价格
            price = bk["view_price"]
            print(price)
            #购买链接
            link = bk["detail_url"]
            print(link)
            #商家
            store = bk["nick"]
            print(store)
            book_list.append({ 'title' : title, 'price' : price, 'link' : link, 'store' : store })
            print ('{title}:{price}:{link}:{store}'.format( title = title, price = price, link = link, store = store )) 
 
 
 
if __name__ == '__main__':
    spider_tb('9787115428028')