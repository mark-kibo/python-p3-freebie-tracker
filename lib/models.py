from sqlalchemy import ForeignKey, exists, create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
engine = create_engine('sqlite:///freebies.db')
Base = declarative_base(metadata=metadata)
sesssion=sessionmaker(bind=engine)()
    
association_table=Table(
    'association',
    Base.metadata,
    Column("dev_id", ForeignKey("devs.id")),
    Column("company_id", ForeignKey("companies.id"))
)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())
    freebies =relationship('Freebie', backref="freebies")
    devs = relationship('Dev', secondary=association_table, back_populates="companies")
    
    def give_freebie(self, devI, name, value):
        
        dev=sesssion.query(Dev).filter(Dev.name == devI.name).first()
        freebie_exist=sesssion.query(Freebie).filter(Freebie.dev == dev.id).exists()
        print(freebie_exist)
        if freebie_exist is None:
            freebie=Freebie(item_name=name, value=value, dev=dev.id, company=self.id)
            # Add the Freebie instance to the Company's freebies relationship
            print(freebie)
            self.freebies.append(freebie)
            sesssion.add(freebie)
            sesssion.commit()
            return "created"
        return "there exists that freebie"
    
    def oldest_company():
        company=sesssion.query(Company).filter(Company.founding_year < int(datetime.now().year)).order_by(Company.founding_year.asc()).first()
        print(company.founding_year)
        return company
    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    freebies =relationship('Freebie', backref="freebies_instances")
    companies = relationship('Company', secondary=association_table, back_populates="devs")

    def received_one(self, item_name):
        freebies=sesssion.query(Freebie).filter(Freebie.item_name == item_name).all()
        if freebies is not None:
            for x in freebies:
                if x.dev == self.id:
                    return True
        return False
    
    def give_away(self, dev, freebie):
        freebieObj=sesssion.query(Freebie).filter(Freebie.item_name == freebie.item_name).first()
        if freebieObj.dev == self.id:
            freebieObj.dev = self.id
            sesssion.commit()
            return "successful"
        return "Freebie doesn't belong to this dev"
    
    def __repr__(self):
        return f'<Dev {self.name}>'



class Freebie(Base):
    __tablename__ ="freebies"


    id=Column(Integer(), primary_key=True)
    item_name=Column(String(50), nullable=True)
    value=Column(Integer())

    dev=Column(Integer(), ForeignKey('devs.id'))
    company=Column(Integer(), ForeignKey('companies.id'))



    def print_details(self):
        return f"{self.dev} owns a {self.item_name} from {self.company}"