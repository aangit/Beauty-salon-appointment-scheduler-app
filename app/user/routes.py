
from fastapi import APIRouter, Depends
from app.user.controller.user_controller import UserController
from app.user.schemas import *
from app.user.controller.user_authenification_controller import JWTBearer
user_router = APIRouter(tags=["user"], prefix="/api/user")


@user_router.post("/add-new-user", response_model=UserSchema, dependencies=[Depends(JWTBearer(["super_user", "employee", "customer"]))])
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.email, user.password, user.user_type_id)  

@user_router.post("/add-new-super-user", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(user.email, user.password)

@user_router.post("/login")
def login_user(user: UserLoginShemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.get("/id", response_model=UserSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)  


@user_router.get("/get-all-users", response_model=list[UserSchema],dependencies=[Depends(JWTBearer("super_user", "employee"))])
def get_all_users():
    return UserController.get_all_users()      

@user_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)

@user_router.get("/get-all-users-for-user_type", response_model= list[UserSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_all_users_by_type(user_type_id: str):
    return UserController.get_all_users_by_type(user_type_id)

@user_router.put("/assing-skills-to-employee", response_model= EmployeeSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def assign_skill_to_employee(employee_id: str, service_types: List[str]):
    return UserController.assign_skill_to_employee(employee_id, service_types)

@user_router.put("/removing-skills-from-employee", response_model= EmployeeSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def remove_skills_from_employee(employee_id: str, service_types: List[str]):
    return UserController.remove_skills_from_employee(employee_id, service_types)

@user_router.get("/get-all-skills-for-employee", response_model= list [ServiceTypeSchema], dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def employee_has_skills(employee_id: str):
    return UserController.employee_has_skills(employee_id)

