import requests, re, json, random

DefaultUAWindows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
HeadersGet  = lambda i=DefaultUAWindows : {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':i,'Viewport-Width':'924'}
HeadersPost = lambda i=DefaultUAWindows : {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':i}

def getData(r, cookie):
    try:
        req = r.get('https://web.facebook.com/', headers=HeadersGet(), cookies={'cookie':cookie}).text.replace('\\','')
        av = re.search(r'"actorID":"(.*?)"',str(req)).group(1)
        __user = av
        __a = str(random.randrange(1,6))
        __hs = re.search(r'"haste_session":"(.*?)"',str(req)).group(1)
        __ccg = re.search(r'"connectionClass":"(.*?)"',str(req)).group(1)
        __rev = re.search(r'"__spin_r":(.*?),',str(req)).group(1)
        __spin_r = __rev
        __spin_b = re.search(r'"__spin_b":"(.*?)"',str(req)).group(1)
        __spin_t = re.search(r'"__spin_t":(.*?),',str(req)).group(1)
        __hsi = re.search(r'"hsi":"(.*?)"',str(req)).group(1)
        fb_dtsg = re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
        jazoest = re.search(r'jazoest=(.*?)"',str(req)).group(1)
        lsd = re.search(r'"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
        Data = {'status':'success','av':av,'__user':__user,'__a':__a,'__hs':__hs,'dpr':'1.5','__ccg':__ccg,'__rev':__rev,'__spin_r':__spin_r,'__spin_b':__spin_b,'__spin_t':__spin_t,'__hsi':__hsi,'__comet_req':'15','fb_dtsg':fb_dtsg,'jazoest':jazoest,'lsd':lsd}
        return(Data)
    except Exception as e: return({'status':'failed'})