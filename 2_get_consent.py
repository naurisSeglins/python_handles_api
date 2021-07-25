import http.client

conn = http.client.HTTPSConnection("sandbox.handelsbanken.com")

payload = "{\"access\":\"ALL_ACCOUNTS\"}"

headers = {
    'X-IBM-Client-Id': "b340f766-a89e-4887-a7c2-a553bccf6100",
    'Authorization': "Bearer QVQ6YmNlZjI0M2QtZDBhZi00OGZiLWE0OTgtZGUwMTJhMDdjMjYz",
    'Country': "SE",
    'PSU-IP-Address': "192.102.28.2",
    'TPP-Transaction-ID': "c8271b81-4229-5a1f-bf9c-758f11c1f5b1",
    'TPP-Request-ID': "6b24ce42-237f-4303-a917-cf778e5013d6",
    'content-type': "application/json",
    'accept': "application/json"
    }

conn.request("POST", "/openbanking/psd2/v1/consents", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
