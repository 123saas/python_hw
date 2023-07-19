# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import json
import jsonpickle

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "-", "-", " ", "-",
                      "-", " ", " ", " ", " ")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10),
            home_phone=random_string("home_phone", 10), mobile_phone=random_string("mobile_phone", 10), work_phone=random_string("work_phone", 10),
            fax=random_string("fax", 10), email=random_string("email", 0), email2=random_string("email2", 0),
            email3=random_string("email3", 0), homepage=random_string("homepage", 10), bday='16',
            bmonth='April', byear=random_string("b", 4), aday='18',
            amonth='May', ayear=random_string("a", 4), address2=random_string("address2", 10),
            home_phone2=random_string("home_phone2", 10), notes=random_string("notes", 10))
    for i in range(5)
]
# file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contacts.json")
#
# with open(file, "w") as f:
#     f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contacts.json")

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata)) # что кодировать? testdata