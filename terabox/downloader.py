import requests, re

def customPayload(share_id:str, uk:str, fid:str='', root:str='1') -> dict:
    return({
        #--> Static
        'page':'1',
        'needsublist':'1',
        'clienttype':'1',
        'version':'3.29.1',
        'devuid':'',
        'channel':'android_7.1.2_SM-G988N_bd-dubox_1024074a',
        #--> Dynamic
        'shareid':share_id,
        'uk':uk,
        'fid':fid,
        'root':root,
    })

class Terabox():

    def __init__(self, url:str) -> None:

        self.data = []
        self.r    = requests.Session()
        self.head = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding':'gzip, deflate, zstd',
            'Accept-Language':'en-US,en;q=0.9',
            'Connection':'keep-alive',
            'Cookie':'PANWEB=1',
            'Host':'www.terabox.com',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'none',
            'Sec-Fetch-User':'?1',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'sec-ch-ua':'""',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'""',
        }

        try:
            surl = self.getSurl(url)
            share_id, uk = self.findRoot(surl)
            self.loopIter(share_id, uk)
            if len(self.data) != 0: self.return_data = self.returner(success=True)
            else: self.return_data = self.returner(success=False)
        except Exception:
            self.return_data = self.returner(success=False)

    def getSurl(self, url:str) -> str:
        req = self.r.get(url, headers=self.head, allow_redirects=True)
        return(re.search(r'surl=([^&]+)',str(req.url)).group(1))

    def findRoot(self, surl:str) -> str:
        req = self.r.get('https://www.terabox.com/share/list?shorturl={}&root=1'.format(surl), headers=self.head).json()
        return(req['share_id'], req['uk'])

    def loopIter(self, share_id:str, uk:str, fid:str='', root:str='1') -> None:
        url = 'https://terabox.com/share/list?' + '&'.join(['{}={}'.format(key,value) for key,value in customPayload(share_id, uk, fid, root).items()])
        req = self.r.get(url, headers=self.head).json()
        for item in req['list']:
            try:
                if int(item['isdir']) == 1: self.loopIter(share_id, uk, item['fs_id'], '0')
                else: self.appendData(item)
            except Exception: continue

    def appendData(self, item:dict) -> None:
        self.data.append({
            'name'      : str(item.get('server_filename')),
            'size'      : round(float(int(item['size'])/(1024*1024)),2),
            'thumbnail' : str(item['thumbs']['url3']),
            'url'       : str(item['dlink']),
        })

    def returner(self, success:bool=False) -> dict:
        if success: response = {'status':'success', 'total_file':len(self.data), 'file':self.data}
        else: response = {'status':'failed', 'total_file':0, 'file':[]}
        return(response)