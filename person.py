class Person:

    def __init__(self,id,name,status,conf_time,latitude,longitude):
        self.person_id=id
        self.person_name=name
        self.person_status=status
        self.person_confirmed_time=conf_time
        self.addr_lat=latitude
        self.addr_long=longitude

    def print_person_details(self):
        print('ID : ',self.person_id)
        print('Name : ',self.person_name)
        print('Status : ',self.person_status)
        print('Confirmed Time : ',self.person_confirmed_time)
        print('Address Latitude : ',self.addr_lat)
        print('Address Longitude : ',self.addr_long)

    def get_person_id(self):
        return self.person_id

    def get_person_name(self):
        return self.person_name

    def get_person_health_status(self):
        return self.person_status

    def get_confirmed_time(self):
        return self.person_confirmed_time
    
    def get_addr_lat(self):
        return self.addr_lat

    def get_addr_long(self):
        return self.addr_long

    def set_person_id(self,id):
        self.person_id=id

    def set_person_name(self,name):
        self.person_name=name

    def set_person_health_status(self,status):
        self.person_status=status

    def set_confirmed_time(self,conf_time):
        self.person_confirmed_time=conf_time
    
    def set_addr_lat(self,latitude):
        self.addr_lat=latitude

    def set_addr_long(self,longitude):
        self.addr_long=longitude



    