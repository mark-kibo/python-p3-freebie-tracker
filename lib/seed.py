from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # # Create instances of Company, Dev, and Freebie
    # company1 = Company(name='Company 1', founding_year=2000)
    # company2 = Company(name='Company 2', founding_year=1995)

   

    dev1 = Dev(name='Developer 1')
    # dev2 = Dev(name='Developer 2')

    
    # session.add(company1)
    # session.add(company2)
    # session.add(dev1)
    # session.add(dev2)
    dev=session.query(Dev).filter(Dev.name == "Developer 1").first()
    company=session.query(Company).filter(Company.name == "Company 1").first()
    freebie1 = Freebie(item_name='Item 1', value=100, dev=dev.id, company=company.id)
    # # freebie2 = Freebie(item_name='Item 2', value=200, dev=dev2, Company=company2)
    # # Add instances to the session
    # print(dev, company, freebie1)
    
    # session.add(freebie1)
    # session.add(freebie2)

    
    # Associate data by setting relationships
    # company1.devs.append(dev1)
    # company1.freebies.append(freebie1)


    # dev1.companies.append(company1)
    # dev1.freebies.append(freebie1)  # Renamed the backref

    

    
    
    # Commit the changes to the database
    # session.commit()

    # Close the session
    # session.close()
    # dev3 = Dev(name='Developer 3')
    # session.add(dev3)
    # company=session.query(Company).filter(Company.name == "Company 1").first()
    # print(company.name)
    # company.give_freebie(dev1, "item 3", 400)

    dev=session.query(Dev).filter(Dev.name == "Developer 1").first()

    dev3 = Dev(name='Developer 3')
    
    print(dev.give_away(dev3, freebie1))
