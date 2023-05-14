import requests
import json
import urllib3
from aci_login import get_token

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def delete_tenant(tenantname):
    
    token = get_token(apic_ip, username, password)
        
    base_url = 'https://{apicurl}/api/'.format(apicurl=apic_ip)

    request_url = 'node/mo/uni/tn-{tenantname}.json'.format(tenantname=tenantname)

    login_url = base_url + request_url

    headers = {
        'Cookie' : f'APIC-Cookie={token}',
        'Content-Type' : 'application/json'
    }

    body = {
        "fvTenant" : {
            "attributes" : {
                "name":"{tenantname}".format(tenantname=tenantname),
                "status": "deleted"
                },
                "children":[]
        }
    }
    payload = json.dumps(body)

    response = requests.request(
        'POST',
        login_url,
        headers=headers,
        data=payload,
        timeout=2,
        verify=False
        )
    data = json.loads(response.text)
    
    if (response.status_code == 200):
      print("Successfully deleted tenant", tenantname)
    else:
      print("Issue in deleting tenant")

if __name__ == '__main__':
    apic_ip = input('Enter APIC IP:')
    username = input('Enter Username:')
    password = input('Enter Password:')
#    apic_ip = 'sandboxapicdc.cisco.com'
#    username = 'admin'
#    password = '!v3G@!4@Y'   
    tenantname = input('Enter Tenant Name Which need to delete: ')
    delete_tenant(tenantname)