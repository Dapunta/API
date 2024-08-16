import requests, re, uuid, random, time, hashlib, json

def headersMobile(tipe:str) -> dict:
    base = {
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'en-US,en;q=0.9',
        'Sec-Ch-Prefers-Color-Scheme':'dark',
        'Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Full-Version-List':'"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
        'Sec-Ch-Ua-Model':'"Nexus 5"',
        'Sec-Ch-Ua-Platform':'"Android"',
        'Sec-Ch-Ua-Platform-Version':'"6.0"',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36'}
    if tipe.lower() == 'get':
        headers = {
            **base,
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Cache-Control':'max-age=0',
            'Dpr':'1',
            'Priority':'u=0, i',
            'Sec-Ch-Ua-Mobile':'?1',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-User':'?1',
            'Upgrade-Insecure-Requests':'1',
            'Viewport-Width':'360'}
    elif tipe.lower() == 'post':
        headers = {
            **base,
            'Accept':'*/*',
            'Content-Length':'1577',
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
            'Origin':'https://m.facebook.com',
            'Priority':'u=1, i',
            'Referer':'https://m.facebook.com/',
            'Sec-Ch-Ua-Mobile':'?1',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors'}
    return(headers)

def convertCookie(raw:dict) -> str:
    return('datr={};fr={};c_user={};xs={};'.format(raw['datr'],raw['fr'],raw['c_user'],raw['xs']))

def LoginEmail(email:str, password:str):
    try:
        r = requests.Session()
        head = {'Host':'b-graph.facebook.com','X-Fb-Connection-Quality':'EXCELLENT','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; RMX3740 Build/QP1A.190711.020) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/480086274;FBCR/Corporation Tbk;FBMF/realme;FBBD/realme;FBDV/RMX3740;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.0,width=540,height=960};FB_FW/1;FBRV/483172840;]','X-Tigon-Is-Retry':'false','X-Fb-Friendly-Name':'authenticate','X-Fb-Connection-Bandwidth':str(random.randrange(70000000,80000000)),'Zero-Rated':'0','X-Fb-Net-Hni':str(random.randrange(50000,60000)),'X-Fb-Sim-Hni':str(random.randrange(50000,60000)),'X-Fb-Request-Analytics-Tags':'{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}','Content-Type':'application/x-www-form-urlencoded','X-Fb-Connection-Type':'WIFI','X-Fb-Device-Group':str(random.randrange(4700,5000)),'Priority':'u=3,i','Accept-Encoding':'gzip, deflate','X-Fb-Http-Engine':'Liger','X-Fb-Client-Ip':'true','X-Fb-Server-Cluster':'true','Content-Length':str(random.randrange(1500,2000))}
        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':email,'password':'#PWD_FB4A:0:{}:{}'.format(str(time.time())[:10], password),'generate_analytics_claim':'1','community_id':'','linked_guest_account_userid':'','cpl':True,'try_num':'1','family_device_id':str(uuid.uuid4()),'secure_family_device_id':str(uuid.uuid4()),'credentials_type':'password','account_switcher_uids':[],'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3','fb4a_shared_phone_cpl_group':'enable_v3_at_risk','enroll_misauth':False,'generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'login','machine_id':str(''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(24)])),'jazoest':str(random.randrange(22000,23000)),'meta_inf_fbmeta':'V2_UNTAGGED','advertiser_id':str(uuid.uuid4()),'encrypted_msisdn':'','currently_logged_in_userid':'0','locale':'id_ID','client_country_code':'ID','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d','sig':str(hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32]),'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
        pos  = r.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
        print(pos)
        if ('session_key' in str(pos)) and ('access_token' in str(pos)):
            token  = pos['access_token']
            cookie = convertCookie({i['name']:i['value'] for i in pos['session_cookies']})
            return(LoginCookie(cookie))
        else: return({'status':'failed', 'id':None, 'name':None, 'gender':None, 'picture':None, 'friend':None, 'follower':None, 'post':None, 'cookie':None, 'token_eaab':None, 'token_eaag':None})
    except Exception as e: return({'status':'failed', 'id':None, 'name':None, 'gender':None, 'picture':None, 'friend':None, 'follower':None, 'post':None, 'cookie':None, 'token_eaab':None, 'token_eaag':None})

def LoginEmail2(email:str, password:str):
    r = requests.Session()
    req = r.get('https://m.facebook.com/', headers=headersMobile('get'), allow_redirects=True).text.replace('\\','')
    param = {
        "params":json.dumps({
            "server_params":{
                "transparency_event_type":"affirmative_action",
                "header_transparency_event_name":"login_button_clicked",
                "header_transparency_event_location":"login",
                "headers_flow_id":re.search(r'"login", "(.*?)"',str(req)).group(1),
                "INTERNAL__latency_qpl_marker_id":re.search(r'bk.action.array.Make, "", (.*?), \(bk.action.i64.Const',str(req)).group(1),
                "INTERNAL__latency_qpl_instance_id":re.search(r'\(bk.action.i64.Const, (.*?)\)',str(req)).group(1),
                "device_id":"null",
                "family_device_id":"null",
                "waterfall_id":re.search(r'bk.action.array.Make, "(.*?)", false, false, "F2_FLOW"',str(req)).group(1),
                "offline_experiment_group":"null",
                "layered_homepage_experiment_group":"null",
                "machine_id":"null",
                "is_platform_login":"0",
                "is_from_logged_in_switcher":"0",
                "is_from_logged_out":"0",
                "access_flow_version":"F2_FLOW",
                "INTERNAL_INFRA_THEME":"harm_f"},
            "client_input_params":{"lois_settings":{"lois_token":"","lara_override":""}}})}
    param = {
        "params":json.dumps({
            "server_params":{
                "credential_type":"password",
                "username_text_input_id":"yubcjs:61",
                "password_text_input_id":"yubcjs:62",
                "login_source":"Login",
                "login_credential_type":"none",
                "server_login_source":"login",
                "ar_event_source":"login_home_page",
                "should_trigger_override_login_success_action":'0',
                "should_trigger_override_login_2fa_action":'0',
                "is_caa_perf_enabled":'0',
                "reg_flow_source":"login_home_native_integration_point",
                "caller":"gslr",
                # "ar_context":"AR1zAhDhsBflWVM6VFBUCVXgm46S_fk8CVUwzjote2XADAjHmIXwtgoRbiasE01uZQJo2THPHD27jAWrpojIGoR92whlK1xnxdY_PQCfO_ArnwNP1YpVVg5Zj60puCS7qCBIxmmerMWSY7_ua3rDpPrWHUR0B5qFfg5Hf2Wy_84SRKi9CYv7TgZBwOb571wfGMhihyy2ppmKqGIJNaqkxbWUwSNgUAmPtPauxMY47_XvFxIG2GFoZ90qYjVltRxefEQV_HSvy9mBYOZtulehdg1zPntBoUG7X6gz0GOQ1iFIaGXOBl4Uk5BKi1Y2xjKVQ7kr1c9EMP4O5wguVPDglOL-e_3Vwt6_Eoi6VgZDXV5zD9YOd6vuIPyQZd2-NB9iqhfvLUr2rRQXEBc|arm",
                "is_from_landing_page":'0',
                "is_from_empty_password":'0',
                "is_from_password_entry_page":'0',
                "INTERNAL__latency_qpl_marker_id":re.search(r'bk.action.array.Make, "", (.*?), \(bk.action.i64.Const',str(req)).group(1),
                "INTERNAL__latency_qpl_instance_id":re.search(r'\(bk.action.i64.Const, (.*?)\)',str(req)).group(1),
                "device_id":'null',
                "family_device_id":'null',
                "waterfall_id":re.search(r'bk.action.array.Make, "(.*?)", false, false, "F2_FLOW"',str(req)).group(1),
                "offline_experiment_group":'null',
                "layered_homepage_experiment_group":'null',
                "is_platform_login":'0',
                "is_from_logged_in_switcher":'0',
                "is_from_logged_out":'0',
                "access_flow_version":"F2_FLOW",
                "INTERNAL_INFRA_THEME":"harm_f"},
            "client_input_params":{
                "machine_id":"",
                "contact_point":email,
                "password":"#PWD_BROWSER:{}:{}:{}".format(str(0), str(time.time()), str(password)),
                "accounts_list":[],
                "fb_ig_device_id":[],
                "secure_family_device_id":"",
                "encrypted_msisdn":"",
                "headers_infra_flow_id":"",
                "try_num":'1',
                "login_attempt_count":'1',
                "event_flow":"login_manual",
                "event_step":"home_page",
                "openid_tokens":{},
                "auth_secure_device_id":"",
                "client_known_key_hash":"",
                "has_whatsapp_installed":'0',
                "sso_token_map_json_string":"",
                "should_show_nested_nta_from_aymh":'0',
                "lois_settings":{"lois_token":"","lara_override":""}}})}
    data = {
        '__aaid':'0',
        '__user':'0',
        '__a':'1',
        '__req':'d',
        '__hs':re.search(r'"haste_session":"(.*?)"',str(req)).group(1),
        'dpr':'1',
        '__ccg':'EXCELLENT',
        '__rev':re.search(r'"server_revision":(.*?),',str(req)).group(1),
        '__hsi':re.search(r'"hsi":"(.*?)"',str(req)).group(1),
        '__csr':'',
        'fb_dtsg':re.search(r'"dtsg":{"token":"(.*?)"',str(req)).group(1),
        'jazoest':re.search(r'"jazoest", "(.*?)"',str(req)).group(1),
        'lsd':re.search(r'"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1),
        'params':json.dumps(param)}
    query = {
        'appid':'com.bloks.www.bloks.caa.login.async.send_login_request',
        'type':'action',
        '__bkv':'b12ba24e6c7328a7dc3b351bc5cc86130f203876c77c9b8111fa1dfc37baacb6'}
    url = 'https://m.facebook.com/async/wbloks/fetch/?' + '&'.join(['{}={}'.format(a,b) for a,b in query.items()])
    pos = r.post(url, data=data, headers=headersMobile('post'), allow_redirects=True).text.replace('\\','')
    print(r.cookies.get_dict())


def LoginCookie(cookie:str) -> dict:
    try:
        r = requests.Session()
        id = GetUserID(cookie)
        token_eaab = TokenEAAB(r, cookie)
        token_eaag = TokenEAAG(r, cookie)
        return({
            'status':'success',
            **GeneralData(r, cookie, token_eaab),
            **FriendCount(r, cookie, token_eaab),
            **FollowerCount(r, cookie, token_eaag),
            **PostCount(r, cookie, token_eaag),
            **{'cookie':cookie, 'token_eaab':token_eaab, 'token_eaag':token_eaag}
        })
    except Exception:
        return({'status':'failed', 'id':None, 'name':None, 'gender':None, 'picture':None, 'friend':None, 'follower':None, 'post':None, 'cookie':None, 'token_eaab':None, 'token_eaag':None})
    
def GetUserID(cookie:str):
    return(re.search(r'c_user=(\d+)',str(cookie)).group(1))

def TokenEAAB(r, cookie:str):
    return(re.search(r'accessToken="(.*?)"',str(r.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={}&breakdown_regrouping=1&nav_source=no_referrer'.format(re.search(r'act=(\d+)',str(r.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie':cookie}).text.replace('\\',''))).group(1)),cookies={'cookie':cookie}).text.replace('\\',''))).group(1))

def TokenEAAG(r, cookie:str):
    return(re.search(r'(\["EAAG\w+)', r.get('https://business.facebook.com/business_locations',cookies={'cookie':cookie}).text).group(1).replace('["',''))

def GeneralData(r, cookie:str, token:str):
    req = r.get('https://graph.facebook.com/me?fields=id,name,gender,picture.width(1080)&access_token={}'.format(token), cookies={'cookie':cookie}).json()
    return({'id':req['id'], 'name':req['name'], 'gender':req['gender'], 'picture':req['picture']['data']['url']})

def FriendCount(r, cookie:str, token:str):
    req = r.get('https://graph.facebook.com/me/friends?limit=0&access_token={}'.format(token), cookies={'cookie':cookie}).json()
    return({'friend':req['summary']['total_count']})

def FollowerCount(r, cookie:str, token:str):
    req = r.get('https://graph.facebook.com/me?fields=subscribers.fields(id).limit(0)&access_token={}'.format(token), cookies={'cookie':cookie}).json()
    return({'follower':req['subscribers']['summary']['total_count']})

def PostCount(r, cookie:str, token:str):
    req = r.get('https://graph.facebook.com/me?fields=posts.fields(id).limit(5000)&access_token={}'.format(token), cookies={'cookie':cookie}).json()
    return({'post':len(req['posts']['data'])})