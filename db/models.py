from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class Bus(Base):
    __tablename__ = 'buses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    vn_kv = Column(Float)  # nominal voltage
    type = Column(String)  # PQ, PV, Slack
    
    # Relationships
    branches = relationship("Branch", back_populates="bus")
    
class Branch(Base):
    __tablename__ = 'branches'
    id = Column(Integer, primary_key=True)
    from_bus = Column(Integer, ForeignKey('buses.id'))
    to_bus = Column(Integer, ForeignKey('buses.id'))
    r_ohm = Column(Float)
    x_ohm = Column(Float)
    
    # Relationships
    bus = relationship("Bus", back_populates="branches")