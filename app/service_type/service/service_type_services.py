from app.service_type.repository import ServiceTypeRepository
from app.db.database import SessionLocal
from app.service_type.exceptions import *
from app.service_type.schemas.service_type_schemas import UpdateServiceTypeSchemaIn
from fastapi.encoders import jsonable_encoder
from app.service_type.exceptions import ServiceTypeNotFound

class ServiceTypeServices:
    @staticmethod
    def create_service_type(service_name, approximate_duration, price, available_at):
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                s_type = service_type_repository.read_service_type_by_name(service_name)            
                if s_type is None:
                    return service_type_repository.create_service_type(service_name, approximate_duration, price, available_at)      
                raise ServiceTypeNotFound(message="Service type already exists in database.", code=400)
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
    def read_service_type_by_name_partially(service_name: str):
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                return service_type_repository.read_service_type_by_name_partially(service_name)
        except Exception as e:
            raise e

    
    @staticmethod
    def read_all_service_types():
        with SessionLocal() as db:
            service_type_repository = ServiceTypeRepository(db)
            return service_type_repository.read_all_service_types()


    @staticmethod
    def user_has_service_type(service_type_id: str):
        with SessionLocal() as db:
            service_type_repository = ServiceTypeRepository(db)
            return service_type_repository.user_has_service_type(service_type_id)


    @staticmethod
    def read_users_per_service_type_name(service_name: str):
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                return service_type_repository.read_users_per_service_type_name(service_name)
        except Exception as e:
            raise e
    
    @staticmethod
    def delete_service_type_by_id(service_type_id: str):
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                service_type_repository.delete_service_type_by_id(service_type_id)    
        except Exception as e:
            raise e


    @staticmethod
    def update_service_type_by_id(service_type_id: str, service_type):
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                stored_service_type_data = service_type_repository.read_service_type_by_id(service_type_id)
                stored_service_type_model = UpdateServiceTypeSchemaIn(**jsonable_encoder(stored_service_type_data))
                update_data = service_type.dict(exclude_unset=True)
                updated_service_type = stored_service_type_model.copy(update=update_data)
                return service_type_repository.update_service_type_by_id(service_type_id, updated_service_type.service_name,updated_service_type.approximate_duration, updated_service_type.price, updated_service_type.available_at)
        except Exception as e:
            raise e


