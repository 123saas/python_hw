# -*- coding: utf-8 -*-
from model.contact import Contact


testdata = [
    Contact(firstname="firstname1", middlename="middlename1",
            lastname="lastname1", nickname="nickname1",
            title="title1", company="company1", address="address1",
            home_phone="home_phone1", mobile_phone="mobile_phone1", work_phone="work_phone1",
            fax="fax1", email="email11", email2="email21",
            email3="email31", homepage="homepage1", bday='16',
            bmonth='April', byear="byear", aday='18',
            amonth='May', ayear="ayear", address2="address21",
            home_phone2="home_phone2", notes="notes1"),
    Contact(firstname="firstname2", middlename="middlename2",
            lastname="lastname2", nickname="nickname2",
            title="title2", company="company2", address="address2",
            home_phone="home_phone2", mobile_phone="mobile_phone2", work_phone="work_phone2",
            fax="fax12", email="email12", email2="email22",
            email3="email32", homepage="homepage2", bday='12',
            bmonth='April', byear="byear", aday='12',
            amonth='May', ayear="ayear", address2="address22",
            home_phone2="home_phone22", notes="notes2"),
]


# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# testdata = [Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "-", "-", " ", "-",
#                       "-", " ", " ", " ", " ")] + [
#     Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
#             lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
#             title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10),
#             home_phone=random_string("home_phone", 10), mobile_phone=random_string("mobile_phone", 10), work_phone=random_string("work_phone", 10),
#             fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10),
#             email3=random_string("email3", 10), homepage=random_string("homepage", 10), bday='16',
#             bmonth='April', byear=random_string("b", 4), aday='18',
#             amonth='May', ayear=random_string("a", 4), address2=random_string("address2", 10),
#             home_phone2=random_string("home_phone2", 10), notes=random_string("notes", 10))
#     for i in range(5)
# ]