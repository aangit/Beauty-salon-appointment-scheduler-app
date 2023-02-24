

from typing import List, Type

from app.db.database import SessionLocal
from app.service_type.repository import ServiceTypeRepository

from app.user.models.user import User
from app.user.repository import UserRepository
from app.user.exceptions import UserInvalidPassword, UserNotFound, UserInvalidEmail, UserNotEmployee
import hashlib
from app.service_type.exceptions import ServiceTypeNotFound


class UserServices:

    @staticmethod
    def create_user(email, password: str, user_type_id):
        """
        It creates a user in the database
        
        :param email: str
        :param password: str
        :type password: str
        :param user_type_id: 1
        :return: The return value is the user_id of the newly created user.
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(email, hashed_password, user_type_id)
            except Exception as e:
                raise e


    @staticmethod
    def create_super_user(email, password):
        """
        It creates a super user with the given email and password
        
        :param email: the email of the user
        :param password: "password"
        :return: The return value is the user object that was created.
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(email, hashed_password)
            except Exception as e:
                raise e


    @staticmethod
    def get_user_by_id(user_id: str):
        """
        It gets a user by id
        
        :param user_id: str
        :type user_id: str
        :return: A user object
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_id(user_id=user_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_users():
        """
        It creates a database session, creates a user repository, and then calls the get_all_users()
        function on the user repository.
        :return: A list of User objects
        """
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all_users()

    @staticmethod
    def delete_user_by_id(user_id: str):
        """
        It deletes a user from the database by their user_id
        
        :param user_id: str
        :type user_id: str
        :return: The return value is the result of the delete_user_by_id method in the UserRepository
        class.
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception as e:
            raise e


    @staticmethod
    def login_user(email: str, password: str):
        """
        It takes an email and password, checks if the email exists in the database, if it does, it
        checks if the password matches the password in the database, if it does, it returns the user
        object
        
        :param email: str
        :type email: str
        :param password: str = "password"
        :type password: str
        :return: The user object
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_email(email)
                if user is None:
                    raise UserInvalidEmail(message="Invalid email or password", code = 401)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e

    @staticmethod
    def get_all_users_by_type(user_type_id: str) -> Type[User]:
        """
        It gets all users by type
        
        :param user_type_id: str
        :type user_type_id: str
        :return: A list of User objects.
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                users= user_repository.get_all_users_by_type(user_type_id)
                return users 
            except Exception as e:
                raise e

    @staticmethod
    def assign_skill_to_employee(employee_id: str, service_type_ids: List[str]):
        """
        It takes an employee id and a list of service type ids and assigns the service types to the
        employee.

        So far it is only possible by super_user, will be changed when the application evolves.
        
        :param employee_id: str
        :type employee_id: str
        :param service_type_ids: List[str]
        :type service_type_ids: List[str]
        :return: The employee object with the new service_types added to it.
        """
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            service_type_repository = ServiceTypeRepository(db)
            employee = user_repository.get_user_by_id(employee_id)
            if employee is None:
                raise UserNotFound(message="User not found", code=404)
            service_types = []
            for service_type_id in service_type_ids:
                service_type = service_type_repository.read_service_type_by_id(service_type_id)
                if service_type is None:
                    raise ServiceTypeNotFound(message="Service type not found", code=404)
                service_types.append(service_type)
            employee.service_types += service_types
            db.add(employee)
            db.commit()
            db.refresh(employee)
            return employee


    @staticmethod
    def remove_skills_from_employee(employee_id: str, service_type_ids: List[str]):
        """
        It removes a list of service types from an employee.
        So far it is only possible by super_user, will be changed when the application evolves.

        :param employee_id: str
        :type employee_id: str
        :param service_type_ids: List[str]
        :type service_type_ids: List[str]
        :return: The employee object
        """
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            service_type_repository = ServiceTypeRepository(db)
            employee = user_repository.get_user_by_id(employee_id)
            if employee is None:
                raise UserNotFound(message="User not found", code=404)
            service_types = []
            for service_type_id in service_type_ids:
                service_type = service_type_repository.read_service_type_by_id(service_type_id)
                if service_type is None:
                    raise ServiceTypeNotFound(message="Service type not found", code=404)
                service_types.append(service_type)
            for service_type in service_types:
                if service_type in employee.service_types:
                    employee.service_types.remove(service_type)
            db.add(employee)
            db.commit()
            db.refresh(employee)
            return employee

    @staticmethod
    def employee_has_skills(employee_id:str):
        """
        It returns a list of service types that an employee has skills in.
        So far it is only possible by super_user, will be changed when the application evolves.
        
        :param employee_id: str
        :type employee_id: str
        :return: A list of service types
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                employee = user_repository.get_user_by_id(employee_id)
                if employee is None:
                    raise UserNotFound(message="User not found", code=404)
                if employee.user_type.user_type != "employee":
                    raise UserNotEmployee(message="User not an employee", code=400)
                return employee.service_types
            except Exception as e:
                raise e

