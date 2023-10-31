import json
from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class CookieClicker(db.Model):
    __tablename__ = 'cookieclicker'
    #Define Class Schema
    id = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    cookieScore = db.Column(db.Integer, unique=False, nullable=False)
    clickerCost = db.Column(db.Integer, unique=False, nullable=False)
    clickerCount = db.Column(db.Integer, unique=False, nullable=False)
    doubleCost = db.Column(db.Integer, unique=False, nullable=False)
    doubleCount = db.Column(db.Integer, unique=False, nullable=False)
    plusCount = db.Column(db.Integer, unique=False, nullable=False)
    rateCost = db.Column(db.Integer, unique=False, nullable=False)
    rate = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, id, ccScore, cCost, cCount, dbCost, dbCount, pCount, rCost, rate):
        self.playerID = id
        self.cookieScore = ccScore
        self.clickerCost = cCost
        self.clickerCount = cCount
        self.doubleCost = dbCost
        self.doubleCount = dbCount
        self.plusCount = pCount
        self.rateCost = rCost
        self.rate = rate

    
    def __repr__(self):
        return "CookieClicker(" + str(self.playerID) + "," + str(self.cookieScore) + "," + str(self.clickerCost) + "," + str(self.clickerCount) + "," + str(self.doubleCost) + "," + str(self.doubleCount) + "," + str(self.plusCount) + "," + str(self.rateCost) + "," + str(self.rate) + ")"
    
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    def read(self):
        return {
            "playerID": self.playerID,
            "cookieScore": self.cookieScore,
            "clickerCost": self.clickerCost,
            "clickerCount": self.clickerCount,
            "doubleCost": self.doubleCost,
            "doubleCount": self.doubleCount,
            "plusCount": self.plusCount,
            "rateCost": self.rateCost,
            "rate": self.rate
        }
    
    def update(self, ccScore, cCost, cCount, dbCost, dbCount, pCount, rCost, rate):
        #Convvert values into integers
        ccScore = int(ccScore)
        cCost = int(cCost)
        cCount = int(cCount)
        dbCost = int(dbCost)
        dbCount = int(dbCount)
        pCount = int(pCount)
        rCost = int(rCost)
        rate = int(rate)

        #Check to see if values are higher than previous values
        if ccScore > self.cookieScore:
            self.cookieScore = ccScore
        if cCost > self.clickerCost:
            self.clickerCost = cCost
        if cCount > self.clickerCount:
            self.clickerCount = cCount
        if dbCost > self.doubleCost:
            self.doubleCost = dbCost
        if dbCount > self.doubleCount:
            self.doubleCount = dbCount
        if pCount > self.plusCount:
            self.plusCount = pCount
        if rCost > self.rateCost:
            self.rateCost = rCost
        if rate > self.rate:
            self.rate = rate

class BinaryGame(db.Model):
    __tablename__ = 'binarygame'
    #Define Class Schema
    id = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    binaryScore = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, id, bScore):
        self.playerID = id
        self.binaryScore = bScore
    
    def __repr__(self):
        return "BinaryGame(" + str(self.playerID) + "," + str(self.binaryScore) + ")"
    
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    def read(self):
        return {
            "playerID": self.playerID,
            "binaryScore": self.binaryScore
        }
    
    def update(self, bScore):
        #Convvert values into integers
        bScore = int(bScore)

        #Check to see if score is higher than previous score
        if bScore > self.binaryScore:
            self.binaryScore = bScore

class GuessGame(db.Model):
    __tablename__ = 'guessgame'
    #Define Class Schema
    id = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    guessScore = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, id, gScore):
        self.playerID = id
        self.guessScore = gScore
    
    def __repr__(self):
        return "GuessGame(" + str(self.playerID) + "," + str(self.guessScore) + ")"
    
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    def read(self):
        return {
            "playerID": self.playerID,
            "guessScore": self.guessScore
        }
    
    def update(self, gScore):
        #Convvert values into integers
        gScore = int(gScore)

        #Check to see if score is higher than previous score
        if gScore > self.guessScore:
            self.guessScore = gScore

class player(db.Model):
    __tablename__= 'players'

    id = db.Column(db.Integer, primary_key=True)

    _username = db.Column(db.Text, unique=True, nullable=False)

    #Relationships between the tables
    cookieclicker = db.relationship("CookieClicker", cascade='all, delete', backref='players', lazy=True)
    binarygame = db.relationship("BinaryGame", cascade='all, delete', backref='players', lazy=True)
    guessgame = db.relationship("GuessGame", cascade='all, delete', backref='players', lazy=True)

    def __init__(self, username, fullname):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username
    
    def get_id(self):
        return self.id
    
    def __str__(self):
        return json.dumps(self.read())
    
    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    #CRUD read: Read converts self to dictionary
    #Returns dictionary
    def read(self):
        return {
            "id": self.id,
            "username": self.username,
            "cookieScore": self.cookieScore,
            "binaryScore": self.binaryscore,
            "guessScore": self.guessScore
        }
    
    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, username=""):
        #only updates values with length
        if len(username) > 0:
            self.username = username
        db.session.commit()
        return self
    
    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
    
#Adding some users into the database
def initUsers():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()

        u1 = player(username='Vegapondz')
        u2 = player(username='Plate0')
        u3 = player(username='Drown')
        u4 = player(username='Jojajeto')
        
        # Inserting test data into CookieClicker table
        u1.cookieclicker.append(CookieClicker(id=u1.id, ccScore=100, cCost=100, cCount=100, dbCost=100, dbCount=100, pCount=100, rCost=100, rate=100))
        u2.cookieclicker.append(CookieClicker(id=u2.id, ccScore=200, cCost=200, cCount=200, dbCost=200, dbCount=200, pCount=200, rCost=200, rate=200))
        u3.cookieclicker.append(CookieClicker(id=u3.id, ccScore=300, cCost=300, cCount=300, dbCost=300, dbCount=300, pCount=300, rCost=300, rate=300))
        u4.cookieclicker.append(CookieClicker(id=u4.id, ccScore=400, cCost=400, cCount=400, dbCost=400, dbCount=400, pCount=400, rCost=400, rate=400))

        # Inserting test data into BinaryGame table
        u1.binarygame.append(BinaryGame(id=u1.id, bScore=10))
        u2.binarygame.append(BinaryGame(id=u2.id, bScore=15))
        u3.binarygame.append(BinaryGame(id=u3.id, bScore=20))
        u4.binarygame.append(BinaryGame(id=u4.id, bScore=25))

        # Inserting test data into GuessGame table
        u1.guessgame.append(GuessGame(id=u1.id, gScore=10))
        u2.guessgame.append(GuessGame(id=u2.id, gScore=10))
        u3.guessgame.append(GuessGame(id=u3.id, gScore=10))
        u4.guessgame.append(GuessGame(id=u4.id, gScore=10))

        #Attempt to create users
        users = [u1, u2, u3, u4]
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate uid, or error: {user.uid}")