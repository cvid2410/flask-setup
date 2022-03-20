from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self) -> str:
        return f"{self.username}"

    @classmethod
    def get_users(cls):
        return User.query.all()
        
    @classmethod
    def create_user(cls, received_json_data):
        user = User(username=received_json_data['username'], 
                    email=received_json_data['email'],
                    password=received_json_data['password'])
        db.session.add(user)
        db.session.commit()
        return user
        
