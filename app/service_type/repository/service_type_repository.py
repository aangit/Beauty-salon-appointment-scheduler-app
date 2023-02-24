from datetime import datetime
from time import time
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.service_type.models import ServiceType
from app.service_type.exceptions import ServiceTypeNotFound


class ServiceTypeRepository:

    def __init__(self, db: Session):
        """
        This function is used to initialize the database session
        
        :param db: Session = Depends(get_db)
        :type db: Session
        """
        self.db = db

    def create_service_type(self, service_name, approximate_duration, price, available_at):
        """
        It creates a new service type and adds it to the database
        
        :param service_name: The name of the service
        :param approximate_duration: int
        :param price: Decimal(precision=2, scale=2)
        :param available_at: a list of datetime objects
        :return: The service_type object
        """
        try:
            service_type = ServiceType(service_name, approximate_duration, price, available_at)
            self.db.add(service_type)
            self.db.commit()
            self.db.refresh(service_type)
            return service_type
        except IntegrityError as e:
            raise e

    def read_service_type_by_id(self, service_type_id: str):
        """
        It returns a service type object from the database if it exists, otherwise it raises an
        exception
        
        :param service_type_id: str
        :type service_type_id: str
        :return: The service_type object
        """
        service_type= self.db.query(ServiceType).filter(ServiceType.id == service_type_id).first()
        if service_type is None:
            raise ServiceTypeNotFound(f"Service type with provided ID: {service_type_id} not found.", 400)
        return service_type

    def read_service_type_by_name(self, service_name: str):
        """
        It takes a service_name as an argument and returns a ServiceType object
        
        :param service_name: str
        :type service_name: str
        :return: A ServiceType object
        """
        s_type = self.db.query(ServiceType).filter(ServiceType.service_name == service_name).first()
        return s_type

    def read_service_type_by_name_partially(self, service_name: str):
        """
        It returns a list of all the service types that have a service name that contains any part of the name passed in as an argument
        
        :param service_name: str
        :type service_name: str
        :return: A list of ServiceType objects
        """
        service_type = self.db.query(ServiceType).filter(ServiceType.service_name.ilike(f"%{service_name}%")).all()
        return service_type

    def read_all_service_types(self):
        """
        It returns all the service types from the database
        :return: A list of ServiceType objects.
        """
        service_types = self.db.query(ServiceType).all()
        return service_types

    def user_has_service_type(self, service_type_id: str):
        """
        It returns a list of users that have the service type with the provided ID
        
        :param service_type_id: str
        :type service_type_id: str
        :return: A list of users that have the service type.
        """
        service_type = self.db.query(ServiceType).filter(ServiceType.id == service_type_id).first()
        if service_type is None:
            raise ServiceTypeNotFound(f"Service type with provided ID: {service_type_id} not found.", 400)
        return service_type.users

    def read_users_per_service_type_name(self, service_name: str):
        """
        It takes a string, splits it into a list of words, then searches the database for any
        service_name that contains any of those words, then returns a list of all users that have any of
        those service_types
        
        :param service_name: str
        :type service_name: str
        :return: A set of users.
        """
        search_terms = service_name.split()
        service_types = self.db.query(ServiceType).filter(or_(*[ServiceType.service_name.ilike(f"%{term}%") for term in search_terms])).all()
        users = []
        for service_type in service_types:
            users += service_type.users
        if users:
            return set(users)
        else:
            raise ServiceTypeNotFound(f"Employee for {service_name} not found.", 400)

            
    def delete_service_type_by_id(self, service_type_id: str):
        """
        It deletes a service type from the database by its ID
        
        :param service_type_id: str
        :type service_type_id: str
        :return: True
        """
        try:
            service_type = self.db.query(ServiceType).filter(ServiceType.id == service_type_id).first()
            if service_type is None:
                raise  ServiceTypeNotFound(f"Service type with provided ID: {service_type_id} not found", 400)
            self.db.delete(service_type)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_service_type_by_id(self, service_type_id: str, service_name: str, approximate_duration: time, price: float, available_at: datetime):
        """
        It updates the service type by id
        
        :param service_type_id: str
        :type service_type_id: str
        :param service_name: str
        :type service_name: str
        :param approximate_duration: time
        :type approximate_duration: time
        :param price: float
        :type price: float
        :param available_at: datetime
        :type available_at: datetime
        :return: The service_type object
        """
        try:
            service_type = self.db.query(ServiceType).filter(ServiceType.id == service_type_id).first()
            service_type.service_name = service_name
            service_type.approximate_duration = approximate_duration
            service_type.price = price
            service_type.available_at = available_at
            self.db.add(service_type)
            self.db.commit()
            self.db.refresh(service_type)
            return service_type
        except IntegrityError as e:
            raise e

