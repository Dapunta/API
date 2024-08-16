import requests, re

def TokenEAAG(cookie:str):
    r = requests.Session()
    try: return({'status':'success', 'token':re.search(r'(\["EAAG\w+)', r.get('https://business.facebook.com/business_locations',cookies={'cookie':cookie}).text).group(1).replace('["','')})
    except Exception: return({'status':'failed', 'token':None})

def TokenEAAB(cookie:str):
    r = requests.Session()
    try: return({'status':'success', 'token':re.search(r'accessToken="(.*?)"',str(r.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={}&breakdown_regrouping=1&nav_source=no_referrer'.format(re.search(r'act=(\d+)',str(r.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie':cookie}).text.replace('\\',''))).group(1)),cookies={'cookie':cookie}).text.replace('\\',''))).group(1)})
    except Exception: return({'status':'failed', 'token':None})

def TokenEAAD(cookie:str):
    r = requests.Session()
    try: return({'status':'success', 'token':re.search(r'{"accessToken":"(EAAd\w+)',(r.get('https://www.facebook.com/events_manager2/overview',cookies={'cookie':cookie})).text.replace('\\','')).group(1)})
    except Exception: return({'status':'failed', 'token':None})

def TokenEAAC(cookie:str):
    r = requests.Session()
    try: return({'status':'success', 'token':re.search(r'{"accessToken":"(EAAC\w+)',(r.get('https://www.facebook.com/brand_safety/controls',cookies={'cookie':cookie})).text.replace('\\','')).group(1)})
    except Exception: return({'status':'failed', 'token':None})

def TokenEAAF(cookie:str):
    r = requests.Session()
    try: return({'status':'success', 'token':re.search(r'{"accessToken":"(EAAF\w+)',(r.get('https://www.facebook.com/test-and-learn/test',cookies={'cookie':cookie})).text.replace('\\','')).group(1)})
    except Exception: return({'status':'failed', 'token':None})

def TokenEABB(cookie:str):
    r = requests.Session()
    try: return({'status':'success', 'token':re.search(r'"accessToken":"(EABB\w+)',(r.get('https://www.facebook.com/ads/adbuilder/home',cookies={'cookie':cookie})).text.replace('\\','')).group(1)})
    except Exception: return({'status':'failed', 'token':None})