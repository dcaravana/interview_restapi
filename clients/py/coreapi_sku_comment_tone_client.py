import coreapi
import uuid

# you don't want to use this kind of auth in code
auth = coreapi.auth.BasicAuthentication(
    username='admin',
    password='admin001'
)
client = coreapi.Client(auth=auth)
# client = coreapi.Client()
schema = client.get('http://127.0.0.1:8000/schema/')

# users list
users = client.action(schema, ['users', 'list'])
print 'users', len(users)
for user in users:
    print user['username']
print

# comment create
new_sku = uuid.uuid1()
print "creating", new_sku
data = client.action(schema, ['comments', 'create'], params={
    'sku': str(new_sku),
    'content': 'This is an incredibly positive message!'
})

# comments list
comments = client.action(schema, ['comments', 'list'])
print 'comments', len(comments)
for comment in comments:
    print comment['sku'], comment['content'], comment['tone_is_positive']
