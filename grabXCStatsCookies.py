import requests

def grabCookies(email, password):
    global id
    global school
    global type
    s = requests.Session()

    payload = {
        'email': email,
        'password': password,
        'submitted': 'TRUE'
    }

    res = s.post('https://xcstats.com/team_page.php', data=payload, allow_redirects=False)
    id = res.cookies['user_id']
    school = res.cookies['school_id']
    type = res.cookies['user_type']
