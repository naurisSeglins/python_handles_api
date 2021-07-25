import http.client

conn = http.client.HTTPSConnection("sandbox.handelsbanken.com")

payload = "client_id=b340f766-a89e-4887-a7c2-a553bccf6100&grant_type=client_credentials&scope=AIS"

headers = {
    'Accept': "application\/json",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json"
    }

conn.request("POST", "/openbanking/oauth2/token/1.0", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
