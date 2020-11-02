from project import db

class Snakes(db.Model):
    __tablename__ = "snakes"

    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String)
    geo_name = db.Column(db.String)
    desc = db.Column(db.String)
    pic_url = db.Column(db.String)
    finds = db.relationship('Finds', backref="snakes")

    def __init__(self, species, geo_name, desc, pic_url):
        self.species = species
        self.geo_name = geo_name
        self.desc = desc
        self.pic_url = pic_url

    def __repr__(self):
        return f'{self.geo_name} - {self.species}'

class Finds(db.Model):
    __tablename__ = "finds"
    id = db.Column(db.Integer, primary_key=True)
    species_id = db.Column(db.Integer, db.ForeignKey('snakes.id'))
    location = db.Column(db.String)
    date = db.Column(db.DATETIME)
    pic_url = db.Column(db.String)

    def __init__(self, location, date, pic_url):
        self.location = location
        self.date = date
        self.pic_url = pic_url

    def __repr__(self):
        return f'{Snakes.geo_name}, ლოკაცია: {self.location}, თარიღი: {self}'
