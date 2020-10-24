class Place:

    def __init__(self,id,name,desc,latitude,longitude):
        self.place_id=id
        self.place_name=name
        self.place_type=desc
        self.place_lat=latitude
        self.place_long=longitude

    def print_place_details(self):
        print('Place ID : ',self.place_id)
        print('Place Name : ',self.place_name)
        print('Place Type : ',self.place_type)
        print('Place Latitude : ',self.place_lat)
        print('Place Longitude : ',self.place_long)

    def get_place_id(self):
        return self.place_id

    def get_place_name(self):
        return self.place_name

    def get_place_type(self):
        return self.place_type

    def get_place_latitude(self):
        return self.place_lat
    
    def get_place_longitude(self):
        return self.place_long

    def set_place_id(self,id):
        self.place_id=id

    def set_place_name(self,name):
        self.place_name=name

    def set_place_type(self,desc):
        self.place_type=desc

    def set_place_lat(self,latitude):
        self.place_lat=latitude

    def set_place_long(self,longitude):
        self.place_long=longitude

    