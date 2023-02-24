from app.db.database import SessionLocal
from app.user_service_type.repository import UserServiceTypeRepository

class UserServiceTypeServices:

    @staticmethod
    def create_user_service_type(user_id, service_type_id):
        """
        It creates a new user_service_type record in the database.
        
        :param user_id
        :param service_type_id
        :return: The return value is the newly created user_service_type object.
        """
        with SessionLocal() as db:
            try:
                users_service_types_repository = UserServiceTypeRepository(db)
                return users_service_types_repository.create_user_service_type(user_id, service_type_id)              
            except Exception as e:
                raise e


    @staticmethod
    def get_all_users_service_types():
        """
        It gets all the users service types from the database.
        :return: A list of UserServiceType objects
        """
        with SessionLocal() as db:
            users_service_types_repository = UserServiceTypeRepository(db)
            return users_service_types_repository.get_all_users_service_types()    

