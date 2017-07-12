import requests
from requests.auth import HTTPBasicAuth
import json
import uuid


url = "http://127.0.0.1:8000"
auth = HTTPBasicAuth('admin', 'admin001')


def call_api(entity, verb='GET', params=None):
    headers = {"Content-Type": "application/json"}

    # TODO complete with all verbs
    if verb == 'POST':
        response = requests.post(
            url + entity, data=json.dumps(params), auth=auth, headers=headers)
    else:
        response = requests.get(url + entity, auth=auth, headers=headers)
    if response.ok:
        return response.json()
    else:
        response.raise_for_status()


# users list
users = call_api('/users/')
print 'users', len(users)
for user in users:
    print user['username']
print

# comment create
new_sku = uuid.uuid1()
print "creating", new_sku
call_api('/comments/', 'POST', {
    'sku': str(new_sku),
    'content': 'This is an incredibly positive message!'
})

# comments list
comments = call_api('/comments/')
print 'comments', len(comments)
for comment in comments:
    print comment['sku'], comment['content'], comment['tone_is_positive']
