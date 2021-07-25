import requests
url ="https://sandbox.handelsbanken.com/openbanking/redirect/oauth2/authorize/1.0"
handels = requests.get(url, params="response_type=code&scope=AIS:a12c0b59-a431-4994-8931-fbdb16a44720&client_id=b340f766-a89e-4887-a7c2-a553bccf6100&state=bc4b933c-bfc2-44c8-b858-eba90f559f91&redirect_uri=https://example.com")

print(handels.status_code)

if handels.history:
    print("Request was redirected")
    for resp in handels.history:
        print(resp.status_code, resp.url)
    print("Final destination:")
    print(handels.status_code, handels.url)
