from bs4 import BeautifulSoup as B;import asyncio as a,aiohttp as A,mysql.connector as c
async def p(d):
    D=c.connect(host='',user='',password='');z=D.cursor();u='https://www.urbandictionary.com/random.php'
    while True:
        try:
            async with A.ClientSession() as I:
                async with I.get(u) as r:t=await r.text();u=B(t,'html.parser');w=u.find('div',{'class': 'mb-8 flex'}).get_text();i=u.find('div', {'class': 'break-words meaning mb-4'}).get_text();z.execute('INSERT INTO `words` (`w`, `d`) VALUES (%s, %s)',(w,i));D.commit();d+=1
        except:print('e')
a.run(p(0))
