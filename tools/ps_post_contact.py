import http.client, urllib.parse, http.cookiejar, urllib.request

# Create a cookie jar and opener
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# GET home page
resp = opener.open('http://127.0.0.1:8000/')
print('GET / status', resp.getcode())

# extract csrftoken cookie
csrftoken = None
for cookie in cj:
    if cookie.name == 'csrftoken':
        csrftoken = cookie.value
print('csrftoken:', csrftoken)

# Prepare POST data
data = urllib.parse.urlencode({'name': 'PS Tester', 'email': 'ps@test.local', 'subject': 'PS Test', 'message': 'Hello from PS'}).encode()
req = urllib.request.Request('http://127.0.0.1:8000/contact/', data=data, headers={
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRFToken': csrftoken or ''
})
try:
    r = opener.open(req)
    body = r.read().decode()
    print('POST status', r.getcode())
    print('body:', body)
except Exception as e:
    import traceback
    print('Exception during POST:')
    traceback.print_exc()
