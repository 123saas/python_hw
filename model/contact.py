from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home_phone=None, mobile_phone=None,
                 work_phone=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None,
                 address2=None, home_phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.home_phone2 = home_phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id or self.id == other.id) \
               and (self.firstname == other.firstname and self.lastname == other.lastname is None or
                    self.middlename is None or other.middlename is None or self.nickname is None or other.nickname
                    is None or self.title is None or other.title is None or self.company is None or other.company is None or self.address is None or other.address
                    is None or self.home_phone is None or other.home_phone is None or self.mobile_phone is None or other.mobile_phone
                    is None or self.work_phone is None or other.work_phone is None or self.fax is None or other.fax
                    is None or self.email is None or other.email is None or self.email2 is None or other.email2 is None or self.email3 is None or other.email3
                    is None or self.homepage is None or other.homepage is None or self.bday is None or other.bday is None or self.bmonth is None or other.bmonth
                    is None or self.byear is None or other.byear is None or self.address2 is None or other.address2
                    is None or self.home_phone2 is None or other.home_phone2 is None or self.notes is None or other.notes)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

