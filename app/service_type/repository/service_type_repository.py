from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.service_type.models import ServiceType
from app.service_type.exceptions import ServiceTypeNotFoundException

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
            raise ServiceTypeNotFoundException(f"Service type with provided ID: {service_type_id} not found.", 400)
        return service_type

    def read_service_type_by_name(self, service_name: str):
        s_type = self.db.query(ServiceType).filter(ServiceType.service_name == service_name).first()
        return s_type

    def read_all_service_types(self):
        service_types = self.db.query(ServiceType).all()
        return service_types

    def delete_service_type_by_id(self, service_type_id: str):
        try:
            service_type = self.db.query(ServiceType).filter(ServiceType.id == service_type_id).first()
            if service_type is None:
                raise  ServiceTypeNotFoundException(f"Service type with provided ID: {service_type_id} not found", 400)
            self.db.delete(service_type)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    # def update_contact_type(self, contact_type_id: str, contact_type: str):
    #     try:
    #         c_type = self.db.query(ContactType).filter(ContactType.id == contact_type_id).first()
    #         if c_type is None:
    #             raise ContactTypeNotFoundException(f"Contact type with provided ID: {contact_type_id} not found", 400) 
    #         c_type.contact_type = contact_type
    #         self.db.add(c_type)
    #         self.db.commit()
    #         self.db.refresh(c_type)
    #         return c_type
    #     except Exception as e:
    #         raise e