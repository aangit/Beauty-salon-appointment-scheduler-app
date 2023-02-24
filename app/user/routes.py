
from fastapi import APIRouter, Depends
from app.user.controller.user_controller import UserController
from app.user.schemas import *
from app.user.controller.user_authenification_controller import JWTBearer
user_router = APIRouter(tags=["user"], prefix="/api/user")


@user_router.post("/add-new-user", response_model=UserSchema, dependencies=[Depends(JWTBearer(["super_user", "employee", "customer"]))])
def create_user(user: UserSchemaIn):
    """
    Create a user with the given email, password, and user_type_id
    
    :param user: UserSchemaIn
    :type user: UserSchemaIn
    :return: A UserSchemaOut object
    """
    return UserController.create_user(user.email, user.password, user.user_type_id)  

@user_router.post("/add-new-super-user", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_super_user(user: UserSchemaIn):
    """
    It takes a user object, and returns a user object
    
    :param user: UserSchemaIn
    :type user: UserSchemaIn
    :return: A User object
    """
    return UserController.create_super_user(user.email, user.password)

@user_router.post("/login")
def login_user(user: UserLoginShemaIn):
    """
    It takes a user object, which is a UserLoginShemaIn, and returns the result of calling the
    login_user function on the UserController class, passing in the user's email and password
    
    :param user: UserLoginShemaIn
    :type user: UserLoginShemaIn
    :return: A tuple of (user, token)
    """
    return UserController.login_user(user.email, user.password)


@user_router.get("/id", response_model=UserSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_user_by_id(user_id: str):
    """
    `get_user_by_id` returns a user object given a user id
    
    :param user_id: str
    :type user_id: str
    :return: A user object
    """
    return UserController.get_user_by_id(user_id)  


@user_router.get("/get-all-users", response_model=list[UserSchema],dependencies=[Depends(JWTBearer("super_user", "employee"))])
def get_all_users():
    """
    It returns a list of all users
    :return: A list of all users in the database.
    """
    return UserController.get_all_users()      

@user_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_by_id(user_id: str):
    """
    Delete a user by id
    
    :param user_id: str
    :type user_id: str
    :return: The return value of the function is the return value of the function that is being called.
    """
    return UserController.delete_user_by_id(user_id)

@user_router.get("/get-all-users-for-user_type", response_model= list[UserSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_all_users_by_type(user_type_id: str):
    """
    This function returns all users by type
    
    :param user_type_id: str
    :type user_type_id: str
    :return: A list of users
    """
    return UserController.get_all_users_by_type(user_type_id)

@user_router.put("/assing-skills-to-employee", response_model= EmployeeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def assign_skill_to_employee(employee_id: str, service_types: List[str]):
    """
    Assigns a skill to an employee
    
    :param employee_id: str
    :type employee_id: str
    :param service_types: List[str]
    :type service_types: List[str]
    :return: A list of strings
    """
    return UserController.assign_skill_to_employee(employee_id, service_types)

@user_router.put("/removing-skills-from-employee", response_model= EmployeeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def remove_skills_from_employee(employee_id: str, service_types: List[str]):
    """
    Remove skills from employee
    
    :param employee_id: str
    :type employee_id: str
    :param service_types: List[str]
    :type service_types: List[str]
    :return: A list of strings
    """
    return UserController.remove_skills_from_employee(employee_id, service_types)

@user_router.get("/get-all-skills-for-employee", response_model= list [ServiceTypeSchema], dependencies=[Depends(JWTBearer("super_user"))])
def employee_has_skills(employee_id: str):
    """
    This function returns a boolean value indicating whether or not the employee has skills
    
    :param employee_id: str
    :type employee_id: str
    :return: A list of skills
    """
    return UserController.employee_has_skills(employee_id)

