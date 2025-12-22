import urllib.request
import json
import uuid

BASE_URL = "http://127.0.0.1:5031"

def register_user():
    unique_email = f"user_{uuid.uuid4()}@example.com"
    payload = {
        "name": "Test User",
        "uniEmail": unique_email,
        "password": "password123",
        "phoneNumber": "1234567890",
        "studentId": "S123",
        "branch": "CS",
        "bio": "Test Bio"
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(f"{BASE_URL}/api/User", data=data, headers={'Content-Type': 'application/json'})
    
    print(f"Registering user with email: {unique_email}")
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                print("Registration Successful!")
                print(response.read().decode('utf-8'))
                return unique_email
            else:
                print(f"Registration Failed: {response.status}")
                return None
    except urllib.error.HTTPError as e:
        print(f"Registration Failed: {e.code}")
        print(e.read().decode('utf-8'))
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def login_user(email):
    payload = {
        "email": email,
        "password": "password123"
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(f"{BASE_URL}/api/User/login", data=data, headers={'Content-Type': 'application/json'})
    
    print(f"Logging in user: {email}")
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print("Login Successful!")
                token = response.read().decode('utf-8')
                print(f"Token: {token[:50]}...")
                return True
            else:
                print(f"Login Failed: {response.status}")
                return False
    except urllib.error.HTTPError as e:
        print(f"Login Failed: {e.code}")
        print(e.read().decode('utf-8'))
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    email = register_user()
    if email:
        login_user(email)
