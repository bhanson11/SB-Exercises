from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it 
User.query.delete()

# Add seed users 
mj = User(first_name='Michael', last_name='Jordan', image_url='https://brobible.com/wp-content/uploads/2018/10/superfan-michael-jordan-jersey-tattoo-back.jpg?quality=90&w=650')
stock = User(first_name='John', last_name='Stockton', image_url='')
dwade = User(first_name='Dwyane', last_name='Wade', image_url='https://wallpapercave.com/wp/wc1772626.jpg')
ant = User(first_name='Anthony', last_name='Edwards', image_url='https://i2-prod.mirror.co.uk/news/us-news/article32735201.ece/ALTERNATES/s1200d/1_anthony-edwards-looks-to-take-down-nikola-jokic.jpg')

# Add new objects to session
db.session.add(mj)
db.session.add(stock)
db.session.add(dwade)
db.session.add(ant)

db.session.commit()
# Save or commit to database