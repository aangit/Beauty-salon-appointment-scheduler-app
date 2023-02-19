from app.service_type.repository import ServiceTypeRepository
from app.db.database import SessionLocal
from app.service_type.exceptions import *

class ServiceTypeServices:
    @staticmethod
    def create_service_type(service_name, approximate_duration, price, available_at):
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                s_type = service_type_repository.read_service_type_by_name(service_name)            
                if s_type is None:
                    return service_type_repository.create_service_type(service_name, approximate_duration, price, available_at)      
                raise ServiceTypeExistsException(message="Service type already exists in database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def read_service_type_by_id(service_type_id: str):
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                return service_type_repository.read_service_type_by_id(service_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_service_types():
        with SessionLocal() as db:
            service_type_repository = ServiceTypeRepository(db)
            return service_type_repository.read_all_service_types()



    @staticmethod
    def delete_service_type_by_id(service_type_id: str):
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                service_type_repository.delete_service_type_by_id(service_type_id)    
        except Exception as e:
            raise e