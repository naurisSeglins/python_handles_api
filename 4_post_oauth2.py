import http.client

conn = http.client.HTTPSConnection("sandbox.handelsbanken.com")

payload = "client_id=b340f766-a89e-4887-a7c2-a553bccf6100&grant_type=authorization_code&scope=AIS:a12c0b59-a431-4994-8931-fbdb16a44720&code=360ad5ce-ecfe-4ad4-83d1-9254e89a3ccc&redirect_uri=https://example.com"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json"
    }

conn.request("POST", "/openbanking/redirect/oauth2/token/1.0", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))