from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Owner, Pet, Job, Handler)

if __name__ == '__main__':

    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
   
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. ✅ One to Many - Testing
    
    # Getting an Owner's Pets
    
    # Use session.query and .first() to grab the first Owner
    first_owner = session.query(Owner).first()

    # Use session.query and filter_by to get the Owner's pets from Pet
    owner_pets = session.query(Pet).filter_by(id=first_owner.id)

    # Print out the Owner's pets
    print([pet for pet in owner_pets])
  
    # Getting a Pet's Owner
    
    # Use session.query and .first() to grab the first pet
    first_pet = session.query(Pet).first()

    # Use session.query and .filter_by() to get the owner associated with this pet
    pet_owner = session.query(Owner).filter_by(id=first_pet.id)

        # [ID: 1, Name: Stephen Munoz, Email: salazarmichael@example.net, Phone: 2449883715, Address: 800 Torres Road
        # Denisemouth, RI 72304]

    # 4. ✅ Head back to models.py to build out a Many to Many association
#--------------------------------------------

# 6. ✅ Many to Many 
    
    # Use session.query and .first() to get the first handler
    first_handler = session.query(Handler).first()

    # Use session.query and .filter_by() to grab the handler_jobs
    handler_jobs = session.query(Job).filter_by(handler_id=first_handler.id)

    # Print the handler_jobs
    print([job for job in handler_jobs])

    # Use 'handler_jobs' to query pets for the associated pet to each job
    handler_pets = [session.query(Pet).get(job.pet_id) for job in handler_jobs]

    # Optional breakpoint for debugging
    import ipdb; ipdb.set_trace()