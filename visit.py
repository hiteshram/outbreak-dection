from person import Person
from place import Place

class Visit(Person,Place):

    def __init__(self,id,person_id,place_id,start_time,end_time):
        self.visit_id=id
        self.visit_person_id=person_id
        self.visit_place_id=place_id
        self.visit_start_time=start_time
        self.vist_end_time=end_time


    def print_visit_details(self):
        print('ID : ',self.visit_id)
        print('Person ',self.visit_person_id.get_person_name())
        print('Place : ',self.visit_place_id.get_place_name())
        print('Visit Start Time ',self.visit_start_time)
        print('Visit End Time : ',self.vist_end_time)


    def get_visit_id(self):
        return self.visit_id

    def get_visit_person_id(self):
        return self.visit_person_id

    def get_visit_place_id(self):
        return self.visit_place_id

    def get_visit_start_time(self):
        return self.visit_start_time
    
    def get_visit_end_time(self):
        return self.visit_end_time

    def set_visit_id(self,id):
        self.visit_id=id

    def set_visit_person_id(self,person_id):
        self.visit_person_id=person_id

    def set_visit_place_id(self,place_id):
        self.visit_place_id=place_id
    
    def set_visit_start_time(self,start_time):
        self.visit_start_time=start_time
    
    def set_visit_end_time(self,end_time):
        self.visit_end_time=end_time

