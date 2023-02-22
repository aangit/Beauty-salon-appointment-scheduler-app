from datetime import datetime
from time import time
from typing import List
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.service_type.models import ServiceType
from app.service_type.exceptions import ServiceTypeNotFound


class ServiceTypeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_service_type(self, service_name, approximate_duration, price, available_at):
        try:
            service_type = ServiceType(service_name, approximate_duration, price, available_at)
            self.db.add(service_type)
            self.db.commit()
            self.db.refresh(service_type)
            return service_type
        except IntegrityError as e:
            raise e

    def read_service_type_by_id(self, service_type_id: str):
        service_type= self.db.query(ServiceType).filter(ServiceType.id == service_type_id).first()
        if service_type is None:
            raise ServiceTypeNotFound(f"Service type with provided ID: {service_type_id} not found.", 400)
        return service_type

    def read_service_type_by_name(self, service_name: str):
        s_type = self.db.query(ServiceType).filter(ServiceType.service_name == service_name).first()
        return s_type

    def read_service_type_by_name_partially(self, service_name: str):
        service_type = self.db.query(ServiceType).filter(ServiceType.service_name.ilike(f"%{service_name}%")).all()
        return service_type

    def read_all_service_types(self):
        service_types = self.db.query(ServiceType).all()
        return service_types

    def user_has_service_type(self, service_type_id: str):
        service_type = self.db.query(ServiceType).filter(ServiceType.id == service_type_id).first()
        if service_type is None:
            raise ServiceTypeNotFound(f"Service type with provided ID: {service_type_id} not found.", 400)
        return service_type.users

    def read_users_per_service_type_name(self, service_name: str):
        search_terms = service_name.split()
        service_types = self.db.query(ServiceType).filter(or_(*[ServiceType.service_name.ilike(f"%{term}%") for term in search_terms])).all()
        users = []
        for service_type in service_types:
            users += service_type.users
        if users:
            return set(users)
        else:
            raise ServiceTypeNotFound(f"Employee for {service_name} not found.", 400)


    # def read_users_per_service_type_name(self, service_name: str):
    #     search_terms = service_name.split()
    #     service_types = self.db.query(ServiceType).filter(or_(*[ServiceType.service_name.ilike(f"%{term}%") for term in search_terms])).all()
    #     users = set(service_types[0].users) if service_types else set()
    #     for service_type in service_types:
    #         users = users.intersection(set(service_type.users))
    #     if users:
    #         return list(users)
    #     else:
    #         raise ServiceTypeNotFoundException(f"Employee for {service_name} not found.", 400)

    # def read_users_per_service_type_name(self, service_type_names: List[str]):
    #     search_terms = [name.lower() for name in service_type_names]
    #     service_types = self.db.query(ServiceType).filter(ServiceType.service_name.ilike(search_terms[0]))
    #     for term in search_terms[1:]:
    #         service_types = service_types.filter(ServiceType.service_name.ilike(f'%{term}%'))
    #     service_types = service_types.all()

    #     users = None
    #     for service_type in service_types:
    #         if users is None:
    #             users = set(service_type.users)
    #         else:
    #             users = users.intersection(service_type.users)

    #     if users:
    #         return users
    #     else:
    #         raise ServiceTypeNotFoundException(f"Users for {', '.join(service_type_names)} not found.", 400)

    # def read_users_per_service_type_name(self, service_name: str):
    #     search_terms = service_name.split()
    #     service_types = self.db.query(ServiceType).filter(or_(*[ServiceType.service_name.ilike(f"%{term}%") for term in search_terms])).all()
    #     users = set()
    #     for user in set(service_types[0].users) if service_types else set():
    #         if all(term in [service_type.service_name for service_type in user.service_types] for term in search_terms):
    #             users.add(user)
    #     if users:
    #         return list(users)
    #     else:
    #         raise ServiceTypeNotFoundException(f"Employee for {service_name} not found.", 400)
            
    def delete_service_type_by_id(self, service_type_id: str):
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

