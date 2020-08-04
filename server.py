import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import engine, User, Pet, Toy

Session = sessionmaker(bind=engine)

def main():
  # Step 1: Make a session (like a fork)
  session = Session()

  # Step 2: CRUD stuff
  # ----------- CREATE
  tosspot = User(name='Gavin Callandar', email='gav.cal@bigscot.com', nickname='Gav')
  session.add(tosspot)
  # session.add_all([
  #   User(name='Wendy Williams', email='wendwil@gmail.com', nickname='Windy'),
  #   User(name='Steven Peters', email='steven.peters@ga.co', nickname='Stevie'),
  #   User(name='Mary Contrary', email='marycontrary@gmail.com', nickname='Mar'),
  #   User(name='Michael Schull', email='mikeyboi@gmail.com', nickname='Mike'), 
  #   User(name='Madison Edminston', email='madison.edminston@ga.co', nickname='Mads')
  # ])
  # print('🗿')
  # print(session.new)

  # ----------- READ
  # Step 3: Flushing changes (like staging)
  go_to_gal = session.query(User).filter_by(nickname='Mads').first()
  print(f'⛱ {go_to_gal}')

  # ----------- UPDATE
  # go_to_gal.email = 'madison.edminston@generalassemb.ly'
  # Change Steve's email
  # session.query(User).filter_by(nickname='Stevie').first().email = 'stpets@bigdaddybezos.com'
  # print(f'🏮 {session.dirty}')

  # ----------- DESTROY
  # count = session.query(User).filter(User.nickname.in_(['Mar', 'Gav'])).count()
  # print(f'🐙 {count}')

  # session.query(User).filter_by(nickname='Mar').delete()
  # session.delete(tosspot)

  # count = session.query(User).filter(User.nickname.in_(['Mar', 'Gav'])).count()
  # print(f'🔥 {count}')

  # ----------- PETTTZZZZZ ----------------
  go_to_gal.pets = [Pet(name='Emmy', species='dog', age=2)]
  emmy = session.query(Pet).filter_by(name='Emmy').first()
  go_to_gal.pets += [Pet(name='Ballad', species='dog', age=9), Pet(name='Blub', species='fish')]
  print(go_to_gal.pets)

  session.query(User, Pet).filter(User.id==Pet.user_id).filter(User.nickname=='Mads')
  session.query(User).join(Pet).filter(User.nickname=='Mads').all()

  emmy.toys.append(Toy(type='ball', color='lime green'))
  print(f'🎾 {emmy.toys}')
  # Step 4: Commit the session to the db (like a commit or PR)
  session.commit()


# Allows us to import the script without calling its functions immediately
# Is magic, don't know how it works yet
if __name__ == '__main__':
  main()