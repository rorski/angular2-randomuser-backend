import requests
from sqlalchemy_utils import PhoneNumber
from src.models import *

def seed_users():
    ''' Add users to the DB, pulled from randomuser '''
    # Probably need something like the following to deal with unicode
    #engine = db.create_engine('sqlite:////tmp/test.db', convert_unicode=True)

    u = requests.get("https://randomuser.me/api/?nat=US&results=20")
    users = u.json()['results']

    for user in users:
        first = user['name']['first'].capitalize()
        last = user['name']['last'].capitalize()
        email = user['email']
        gender = user['gender']
        dob = user['dob']
        phone = PhoneNumber(user['phone'], 'US')
        password = user['login']['password']
        pic = user['picture']['large']
        city = user['location']['city'].title()
        state = user['location']['state'].title()
        # Get a random summary from bacon ipsum
        summary = requests.get("https://baconipsum.com/api/?type=meat-and-filler&paras=1&format=text").text

        u = User(firstname=first, lastname=last, email=email, gender=gender, dob=dob,
                 phone=phone, password=password, pic=pic, city=city, state=state, summary=summary)
        print "Adding user: {} {}".format(first, last)

        db.session.add(u)
    db.session.commit()


if __name__ == "__main__":
    db.create_all()
    seed_users()
