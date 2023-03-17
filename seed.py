"""Seed file to make pets for testing out the adoption agency."""

from models import db, connect_db, Pet
from app import app


# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
# An alternative if you don't want to drop
# and recreate your tables:
# User.query.delete()

# Add Pets
sparky = Pet(
    name='Sparky',
    species='Dog',
    photo_url='https://media.gettyimages.com/id/977143864/photo/sparky.jpg?s=612x612&w=gi&k=20&c=55CfU6RU5d1C5n1IDwdRpnZ4TNAxVSHusxmRThr758k=',
    age='adult',
    notes='Likes to bite.',
    available=True
)

mr_chips = Pet(
    name='Mr. Chips',
    species='Cat',
    photo_url='https://www.rover.com/blog/wp-content/uploads/2020/06/cat-4756360_1280-960x540.jpg',
    age='young',
    notes='Likes to snuggle.',
    available=True
)

spot = Pet(
    name='Spot',
    species='Fish',
    photo_url='https://media-be.chewy.com/wp-content/uploads/red-cap-oranda.jpg',
    age='baby',
    notes='',
    available=False
)

db.session.add(sparky)
db.session.add(mr_chips)
db.session.add(spot)

db.session.commit()