import requests
import grabXCStatsCookies as cookie
import grabStravaInfo as info
import userInfo as user

def addWorkout(name, date, minutes, seconds, distance, school_id, user_id):
    s = requests.Session()
    f = open("result.html", 'wb')

    payload = {
        'datatype': 'addrunnerentrylog',
        'isupdaterec': 'no',
        'recid': '0',
        'workout_id': '0',
        'txt_log_name': name,
        'txt_log_date': date,
        'txt_log_mint_time': minutes,
        'txt_log_sec_time': seconds,
        'txt_log_distance': distance,
        'txt_log_distance_mrg': 'miles',
        #no way of currently getting effort and feel from Strava
        #may be able to get it in the future from a Garmin API
        'effort': '3',
        'runner_feel': '3'
    }

    cookies = {
        'school_id': school_id,
        'user_id': user_id,
        'user_type': 'runner'
    }

    res = s.post('https://xcstats.com/workoutData.php', data=payload, cookies=cookies)
    f.write(res.content)
    f.close()

user.getCredentials()
info.getRecentRun(user.userID)
cookie.grabCookies(user.email, user.password)
session = addWorkout(info.name, info.date, info.minutes, info.seconds, info.distance, cookie.school, cookie.id)
