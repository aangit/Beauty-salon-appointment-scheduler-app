
from sqlalchemy.exc import IntegrityError
from app.user.service import UserServices, signJWT
from fastapi import HTTPException, Response
from app.user.exceptions import UserInvalidPassword, UserInvalidEmail, UserNotFound, UserNotEmployee
from app.service_type.exceptions import ServiceTypeNotFound

class UserController:
    @staticmethod
    def create_user(email, password, user_type_id):
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
        user = UserServices.get_user_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=400, detail=f"user with provided id {user_id} does not exist")

    @staticmethod
    def get_all_users():
        users = UserServices.get_all_users()
        return users

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            UserServices.delete_user_by_id(user_id)
            return Response(content=f"User with id - {user_id} is deleted")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    @staticmethod
    def get_all_users_by_type(user_type_id: str):
        users = UserServices.get_all_users_by_type(user_type_id)
        if users:
            return users
        else:
            raise HTTPException(status_code=400, detail=f"User with provided id {user_type_id} does not exist")


    @staticmethod
    def assign_skill_to_employee(employee_id, service_type_ids):
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
        try:
            user_service_type = UserServices.remove_skills_from_employee(employee_id, service_type_ids)
            return user_service_type
        except UserNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # @staticmethod
    # def assign_day_to_employee(employee_id, day_of_week_id, start, end):
    #     try:
    #         user_day_of_week = UserServices.assign_day_to_employee(employee_id, day_of_week_id, start, end)
    #         return user_day_of_week
    #     except Exception as e:
    #         raise HTTPException(status_code=500, detail=str(e))



    # @staticmethod
    # def get_employees_by_service_type(service_type_name: str):
    #     try:
    #         user_service_type = UserServices.get_employees_by_service_type(service_type_name)
    #         return user_service_type
    #     except Exception as e:
    #         raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def employee_has_skills(employee_id:str):
        try:
            employee_skills = UserServices.employee_has_skills(employee_id)
            return employee_skills
        except UserNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotEmployee as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


