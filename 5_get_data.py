import http.client

conn = http.client.HTTPSConnection("sandbox.handelsbanken.com")

headers = {
    'X-IBM-Client-Id': "b340f766-a89e-4887-a7c2-a553bccf6100",
    'Authorization': "Bearer MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI1",
    'PSU-IP-Address': "192.102.28.2",
    'TPP-Transaction-ID': "6b24ce42-237f-4303-a917-cf778e5013d6",
    'TPP-Request-ID': "c8271b81-4229-5a1f-bf9c-758f11c1f5b1",
    'accept': "application/json"
    }

conn.request("GET", "/openbanking/psd2/v2/accounts", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
