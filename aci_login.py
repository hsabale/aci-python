import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_token(apic_ip, username, password):
    
    base_url = 'https://{apicurl}/api/'.format(apicurl=apic_ip)

    body = {
        'aaaUser': 
        {'attributes': 
            {'name': '{username}'.format(username=username),
            'pwd': '{password}'.format(password=password)
            }
        }
    }

    payload = json.dumps(body)

    headers = {
        'Content-Type' : 'application/json'
    }

    url = base_url + 'aaaLogin.json'

    response = requests.request(
        'POST',
        url,
        headers=headers,
        data=payload,
        timeout=2,
        verify=False
        )
    data = json.loads(response.text)
    token = data["imdata"][0]["aaaLogin"]["attributes"]["token"]
    return token

if __name__ == '__main__':
    apic_ip = input('Enter APIC IP:')
    username = input('Enter Username:')
    password = input('Enter Password:')
#    apic_ip = 'sandboxapicdc.cisco.com'
#    username = 'admin'
#    password = '!v3G@!4@Y'
    token = get_token(apic_ip, username, password)
    print("The token is : " , token)