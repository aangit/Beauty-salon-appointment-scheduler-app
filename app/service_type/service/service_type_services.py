from app.service_type.repository import ServiceTypeRepository
from app.db.database import SessionLocal
from app.service_type.exceptions import *
from app.service_type.schemas.service_type_schemas import UpdateServiceTypeSchemaIn
from fastapi.encoders import jsonable_encoder
from app.service_type.exceptions import ServiceTypeNotFound

class ServiceTypeServices:

    @staticmethod
    def create_service_type(service_name, approximate_duration, price, available_at):
        """
        It creates a service type if it doesn't exist in the database
        
        :param service_name: str
        :param approximate_duration: int
        :param price: Decimal(precision=2, scale=2)
        :param available_at: [{'day': 'Monday', 'start_time': '09:00', 'end_time': '17:00'}, {'day':
        'Tuesday', 'start_time': '09:00', 'end_time': '17:00'}, {'day
        :return: The return value is the newly created service type.
        """
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
        """
        It reads a service type by id
        
        :param service_type_id: str
        :type service_type_id: str
        :return: A ServiceType object
        """
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                return service_type_repository.read_service_type_by_id(service_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_service_type_by_name_partially(service_name: str):
        """
        It reads a service type by name partially
        
        :param service_name: str
        :type service_name: str
        :return: A list of ServiceType objects
        """
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                return service_type_repository.read_service_type_by_name_partially(service_name)
        except Exception as e:
            raise e

    
    @staticmethod
    def read_all_service_types():
        """
        It reads all service types from the database.
        :return: A list of ServiceType objects
        """
        with SessionLocal() as db:
            service_type_repository = ServiceTypeRepository(db)
            return service_type_repository.read_all_service_types()


    @staticmethod
    def user_has_service_type(service_type_id: str):
        """
        It checks if the user has a service type with the given id
        
        :param service_type_id: str
        :type service_type_id: str
        :return: A boolean value
        """
        with SessionLocal() as db:
            service_type_repository = ServiceTypeRepository(db)
            return service_type_repository.user_has_service_type(service_type_id)


    @staticmethod
    def read_users_per_service_type_name(service_name: str):
        """
        It reads the users per service type name.
        
        :param service_name: str
        :type service_name: str
        :return: A list of users
        """
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                return service_type_repository.read_users_per_service_type_name(service_name)
        except Exception as e:
            raise e
    
    @staticmethod
    def delete_service_type_by_id(service_type_id: str):
        """
        It deletes a service type by id
        
        :param service_type_id: str
        :type service_type_id: str
        """
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                service_type_repository.delete_service_type_by_id(service_type_id)    
        except Exception as e:
            raise e


    @staticmethod
    def update_service_type_by_id(service_type_id: str, service_type):
        """
        It takes in a service type id, and a service type object, and updates the service type in the
        database
        
        :param service_type_id: str
        :type service_type_id: str
        :param service_type: ServiceTypeOut
        :return: The return value is a tuple of the form (rowcount, lastrowid)
        """
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                stored_service_type_data = service_type_repository.read_service_type_by_id(service_type_id)
                if not stored_service_type_data:
                    raise ServiceTypeNotFound(message="Service type not found.", code=404)
                stored_service_type_model = UpdateServiceTypeSchemaIn(**jsonable_encoder(stored_service_type_data))
                update_data = service_type.dict(exclude_unset=True)
                updated_service_type = stored_service_type_model.copy(update=update_data)
                return service_type_repository.update_service_type_by_id(service_type_id, updated_service_type.service_name,updated_service_type.approximate_duration, updated_service_type.price, updated_service_type.available_at)
        except Exception as e:
            raise e


