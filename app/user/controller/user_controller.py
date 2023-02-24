
from sqlalchemy.exc import IntegrityError
from app.user.service import UserServices, signJWT
from fastapi import HTTPException, Response
from app.user.exceptions import UserInvalidPassword, UserInvalidEmail, UserNotFound, UserNotEmployee
from app.service_type.exceptions import ServiceTypeNotFound

class UserController:
    @staticmethod
    def create_user(email, password, user_type_id):
        """
        It creates a user
        
        :param email: str
        :param password: "password"
        :param user_type_id: 1
        :return: The user object is being returned.
        """
        try:
            user = UserServices.create_user(email, password, user_type_id)
            return user
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email - {email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_super_user(email, password):
        """
        It creates a super user if the user doesn't exist, otherwise it raises an exception
        
        :param email: str
        :param password: "password"
        :return: The user object
        """
        try:
            user = UserServices.create_super_user(email, password)
            return user
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email - {email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def login_user(email, password):
        """
        It takes an email and password, and if the email and password are valid, it returns a JWT token
        
        :param email: str
        :param password: "12345678"
        :return: A JWT token
        """
        try:
            user = UserServices.login_user(email, password)
            if user:
                return signJWT(user.id, user.user_type.user_type)
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserInvalidEmail as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def get_user_by_id(user_id: str):
        """
        It gets a user by id, if the user exists, it returns the user, otherwise it raises an exception
        
        :param user_id: str
        :type user_id: str
        :return: The user object
        """
        user = UserServices.get_user_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=400, detail=f"user with provided id {user_id} does not exist")

    @staticmethod
    def get_all_users():
        """
        It returns a list of all users
        :return: A list of users
        """
        users = UserServices.get_all_users()
        return users

    @staticmethod
    def delete_user_by_id(user_id: str):
        """
        It deletes a user by id
        
        :param user_id: str - the id of the user to be deleted
        :type user_id: str
        :return: Response(content=f"User with id - {user_id} is deleted")
        """
        try:
            UserServices.delete_user_by_id(user_id)
            return Response(content=f"User with id - {user_id} is deleted")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    @staticmethod
    def get_all_users_by_type(user_type_id: str):
        """
        It returns all users of a given type
        
        :param user_type_id: str
        :type user_type_id: str
        :return: A list of users
        """
        users = UserServices.get_all_users_by_type(user_type_id)
        if users:
            return users
        else:
            raise HTTPException(status_code=400, detail=f"User with provided id {user_type_id} does not exist")


    @staticmethod
    def assign_skill_to_employee(employee_id, service_type_ids):
        """
        It takes an employee_id and a list of service_type_ids and assigns the service_type_ids to the
        employee_id
        
        :param employee_id
        :param service_type_ids
        """
        try:
            user_service_type = UserServices.assign_skill_to_employee(employee_id, service_type_ids)
            return user_service_type
        except UserNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def remove_skills_from_employee(employee_id, service_type_ids):
        """
        It removes skills from an employee
        
        :param employee_id: 1
        :param service_type_ids: [1,2,3]
        :return: The return value is a list of UserServiceType objects.
        """
        try:
            user_service_type = UserServices.remove_skills_from_employee(employee_id, service_type_ids)
            return user_service_type
        except UserNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def employee_has_skills(employee_id:str):
        """
        It returns a list of skills that an employee has.
        
        :param employee_id: str
        :type employee_id: str
        :return: A list of skills
        """
        try:
            employee_skills = UserServices.employee_has_skills(employee_id)
            return employee_skills
        except UserNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotEmployee as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))



