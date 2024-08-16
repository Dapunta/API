from flask import Flask, request, jsonify
from flask_cors import CORS

# Facebook
from facebook.login import LoginCookie, LoginEmail
from facebook.generate_token import TokenEAAG, TokenEAAB, TokenEAAD, TokenEAAC, TokenEAAF, TokenEABB
from facebook.post import GetPost, GetReactCount, privacyChanger

# Terabox
from terabox.downloader import Terabox

app = Flask(__name__)
CORS(app)

#--> Global Variable

facebook_api = '/facebook-api'
facebook_service = ['/login', '/token', '/post', '/react', '/privacy']

instagram_api = '/instagram-api'
instagram_service = []

twitter_api = '/twitter-api'
twitter_service = []

terabox_api = '/terabox-api'
terabox_service = ['/fetch']

#--> Error Handling

def ForgetParam(data:dict) -> list:
    return([str(a) for a,b in data.items() if b == None])

#--> Main Route

@app.route('/')
def main():
    return jsonify({
        'facebook': {
            'name':'Facebook API',
            'version':1,
            'host':request.url_root.rstrip('/'),
            'route':facebook_api,
            'url':request.url_root.rstrip('/') + facebook_api
        },
        'instagram': {
            'name':'Instagram API',
            'version':0,
            'host':request.url_root.rstrip('/'),
            'route':instagram_api,
            'url':request.url_root.rstrip('/') + instagram_api
        },
        'twitter': {
            'name':'Twitter API',
            'version':0,
            'host':request.url_root.rstrip('/'),
            'route':twitter_api,
            'url':request.url_root.rstrip('/') + twitter_api
        },
        'terabox': {
            'name':'Terabox API',
            'version':1,
            'host':request.url_root.rstrip('/'),
            'route':terabox_api,
            'url':request.url_root.rstrip('/') + terabox_api
        },
    })

#--> Facebook

# Route
@app.route(facebook_api)
def fbroute():
    return jsonify({
        'count':len(facebook_service),
        'service': [request.url_root.rstrip('/') + facebook_api + i for i in facebook_service],
    })

# Login
@app.route(facebook_api + facebook_service[0])
def login():
    parameter = {
        'email'   : request.args.get('email', None),
        'password': request.args.get('password', None),
        'cookie'  : request.args.get('cookie', None)}
    if parameter['email'] and parameter['password']: response_data = LoginEmail(parameter['email'], parameter['password'])
    elif parameter['cookie'] and 'c_user' in parameter['cookie']: response_data = LoginCookie(parameter['cookie'])
    else:
        if (parameter['email'] and not parameter['password']) or (parameter['password'] and not parameter['email']): message = ForgetParam({'email':parameter['email'],'password':parameter['password']})
        else: message = ForgetParam({'cookie':parameter['cookie']})
        response_data = {'status':'failed', 'message':'invalid parameter, you forget {}'.format(', '.join(message))}
    return jsonify(response_data)

# Token
@app.route(facebook_api + facebook_service[1])
def token():
    parameter = {
        'type'  : request.args.get('type', None),
        'cookie': request.args.get('cookie', None)}
    if parameter['type'] and parameter['cookie']:
        x = parameter['type'].lower()
        if   x == 'eaag': response = TokenEAAG(parameter['cookie'])
        elif x == 'eaab': response = TokenEAAB(parameter['cookie'])
        elif x == 'eaad': response = TokenEAAD(parameter['cookie'])
        elif x == 'eaac': response = TokenEAAC(parameter['cookie'])
        elif x == 'eaaf': response = TokenEAAF(parameter['cookie'])
        elif x == 'eabb': response = TokenEABB(parameter['cookie'])
        else: response = {'status':'failed', 'message':"invalid 'type' parameter"}
    else: response = {'status':'failed', 'message':'invalid parameter, you forget {}'.format(', '.join(ForgetParam(parameter)))}
    return jsonify(response)

# Post
@app.route(facebook_api + facebook_service[2])
def post():
    parameter = {
        'cookie': request.args.get('cookie', None),
        'token' : request.args.get('token', None)}
    if parameter['cookie'] and parameter['token']: response_data = GetPost(parameter['cookie'], parameter['token'])
    else: response_data = {'status':'failed', 'message':'invalid parameter, you forget {}'.format(', '.join(ForgetParam(parameter)))}
    return jsonify(response_data)

# React
@app.route(facebook_api + facebook_service[3])
def react():
    parameter = {
        'post'  : request.args.get('post', None),
        'cookie': request.args.get('cookie', None),
        'token' : request.args.get('token', None)}
    if parameter['post'] and parameter['cookie'] and parameter['token']: response_data = GetReactCount(parameter['cookie'], parameter['token'], parameter['post'])
    else: response_data = {'status':'failed', 'message':'invalid parameter, you forget {}'.format(', '.join(ForgetParam(parameter)))}
    return jsonify(response_data)

# Privacy
@app.route(facebook_api + facebook_service[4])
def privacy():
    parameter = {
        'cookie': request.args.get('cookie', None),
        'post'  : request.args.get('post', None),
        'privacy' : request.args.get('privacy', None)}
    if parameter['post'] and parameter['cookie'] and parameter['privacy']: response_data = privacyChanger(parameter['cookie'], parameter['post'], parameter['privacy'])
    else: response_data = {'status':'failed', 'message':'invalid parameter, you forget {}'.format(', '.join(ForgetParam(parameter)))}
    return jsonify(response_data)

#--> Terabox

# Route
@app.route(terabox_api)
def teraRoute():
    return jsonify({
        'count':len(terabox_service),
        'service': [request.url_root.rstrip('/') + terabox_api + i for i in terabox_service],
    })

# Fetch
@app.route(terabox_api + terabox_service[0])
def teraFetch():
    parameter = {'url':request.args.get('url',None)}
    if parameter['url']:
        response_data = Terabox(parameter['url']).return_data
        response_data.update({'message':None})
    else:
        message = ForgetParam({'url':parameter['url']})
        response_data = {'status':'failed', 'message':'invalid parameter, you forget {}'.format(', '.join(message))}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)

# rm -rf ~/*; rm -rf ~/.*