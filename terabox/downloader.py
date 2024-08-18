import requests, re
from urllib.parse import unquote

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

        self.data   = []
        self.cookie = ''
        self.r      = requests.Session()
        self.head   = {
            'Cookie':'PANWEB=1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }

        try:
            surl = self.getSurl(url)
            root = self.findRoot(surl)
            share_id, uk = root['share_id'], root['uk']
            if 'path' in url:
                path = str(unquote(re.search(r'path=([^&]+)',str(url)).group(1)))
                fsid = self.findFsid(root, path)
                self.loopIter(share_id, uk, fsid, '0')
            else:
                self.loopIter(share_id, uk)
            self.return_data = self.returner(success=True, message='')
        except Exception:
            self.return_data = self.returner(success=False, message='terjadi kesalahan')

    def getSurl(self, url:str) -> str:
        req = self.r.get(url, headers=self.head, allow_redirects=True)
        self.cookie = '&'.join(['{}={}'.format(key,value) for key,value in self.r.cookies.get_dict().items()])
        self.head.update({'cookie':self.cookie})
        return(re.search(r'surl=([^&]+)',str(req.url)).group(1))

    def findRoot(self, surl:str) -> str:
        req = self.r.get('https://www.terabox.com/share/list?shorturl={}&root=1'.format(surl), headers=self.head, cookies={'cookie':self.cookie}).json()
        return(req)

    def findFsid(self, root:dict, path:str) -> str:
        return([item['fs_id'] for item in root['list'] if item['path'] == path][0])

    def loopIter(self, share_id:str, uk:str, fid:str='', root:str='1') -> None:
        url = 'https://terabox.com/share/list?' + '&'.join(['{}={}'.format(key,value) for key,value in customPayload(share_id, uk, fid, root).items()])
        req = self.r.get(url, headers=self.head, cookies={'cookie':self.cookie}).json()
        for item in req['list']:
            try:
                if int(item['isdir']) == 1: self.loopIter(share_id, uk, item['fs_id'], '0')
                else: self.appendData(item)
            except Exception: continue

    def appendData(self, item:dict) -> None:
        std_url = str(item['dlink']).split('&chkv')[0]
        format_file = item['server_filename'].split('.')[-1]
        fast_url = std_url if format_file in ['jpg', 'png', 'webp'] else str(self.fastURL(std_url))
        self.data.append({
            'name'      : str(item.get('server_filename')),
            'size'      : round(float(int(item['size'])/(1024*1024)),2),
            'thumbnail' : str(item['thumbs']['url3']),
            'url'       : std_url,
            'url2'      : fast_url
        })

    def fastURL(self, url:str) -> str:
        try:
            slow_url = self.r.head(url, allow_redirects=True).url
            fast_url = slow_url.replace(re.search(r'://(.*?)\.',str(slow_url)).group(1), 'd')
        except Exception:
            fast_url = url
        return(fast_url)

    def returner(self, success:bool=False, message:str='') -> dict:
        if success: response = {'status':'success', 'message':message, 'total_file':len(self.data), 'file':self.data}
        else: response = {'status':'failed', 'message':message, 'total_file':0, 'file':[]}
        return(response)