import requests, json, base64
from facebook.tools import getData

def GetPost(cookie:str, token:str) -> list:
    data = []
    try:
        r = requests.Session()
        req = r.get('https://graph.facebook.com/me?fields=posts.fields(id,message,privacy.value).limit(5000)&access_token={}'.format(token), cookies={'cookie':cookie}).json()
        for i in req['posts']['data']:
            try: data.append({'id':i['id'], 'privacy':i['privacy']['value'], 'caption':i.get('message')})
            except Exception: continue
        return({'status':'success', 'count':len(data), 'data':data})
    except Exception as e:
        print(e)
        return({'status':'failed', 'count':0, 'data':[]})

def GetReactCount(cookie:str, token:str, id_post:str):
    response = {
        'status' : 'failed',
        'total'  : 0,
        'id'     : id_post,
        'like'   : {'count':0, 'reactor':[]},
        'love'   : {'count':0, 'reactor':[]},
        'care'   : {'count':0, 'reactor':[]},
        'haha'   : {'count':0, 'reactor':[]},
        'wow'    : {'count':0, 'reactor':[]},
        'sad'    : {'count':0, 'reactor':[]},
        'angry'  : {'count':0, 'reactor':[]},
    }
    try:
        r = requests.Session()
        req = r.get('https://graph.facebook.com/{}?fields=reactions.limit(5000)&access_token={}'.format(id_post, token), cookies={'cookie':cookie}).json()
        for item in req['reactions']['data']:
            try:
                base = response[item['type'].lower()]
                base['reactor'].append({'id':item['id'],'name':item['name']})
                base['count'] += 1
                response['total'] += 1
            except Exception: continue
        response['status'] = 'success' if response['total'] != 0 else 'failed'
        return(response)
    except Exception:
        response.update({'status' :'failed'})
        return(response)

def privacyChanger(cookie:str, post_id:str, privacy:str):
    try:
        r = requests.Session()
        base_data = getData(r, cookie)
        privacy = privacy.split('_')[-1].upper()
        var = {
            "input":{
                "privacy_mutation_token":"null",
                "privacy_row_input":{
                    "allow":[],
                    "base_state":privacy,
                    "deny":[],
                    "tag_expansion_state":"UNSPECIFIED"},
                "privacy_write_id":base64.b64encode(('privacy_scope_renderer:{"id":%s}'%(post_id.split('_')[-1])).encode('utf-8')).decode('utf-8'),
                "render_location":"COMET_STORY_MENU",
                "actor_id":base_data["__user"],
                "client_mutation_id":"1"},
            "privacySelectorRenderLocation":"COMET_STORY_MENU",
            "scale":"1",
            "storyRenderLocation":"timeline",
            "tags":"null",
            "__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":"true"}
        data = {
            **base_data,
            'fb_api_caller_class':'RelayModern',
            'fb_api_req_friendly_name':'CometPrivacySelectorSavePrivacyMutation',
            'variables':json.dumps(var),
            'server_timestamps':'true',
            'doc_id':'26411441695122178'}
        pos = r.post('https://web.facebook.com/api/graphql/', data=data, cookies={'cookie':cookie}).json()
        x = pos['data']['privacy_selector_save']['privacy_scope']['privacy_scope_renderer']['privacy_row_input']['base_state']
        if x == privacy: return({'status':'success','privacy':x})
        else: return({'status':'failed','privacy':x})
    except Exception: return({'status':'failed','privacy':'unknown'})