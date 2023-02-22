from fastapi import APIRouter, Depends
from app.status.controller.status_controller import StatusController
from app.status.schemas import *
from app.user.controller.user_authenification_controller import JWTBearer

status_router = APIRouter(tags=["status"], prefix="/api/status")


@status_router.post("/add-new-status", response_model=StatusSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def create_status(status: StatusSchemaIn):
    return StatusController.create_status(status.status)

@status_router.get("/id", response_model=StatusSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_status_by_id(status_id: str):
    return StatusController.get_status_by_id(status_id)      


@status_router.get("/get-all-statuses", response_model=list[StatusSchema], dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_all_statuses():
    return StatusController.get_all_statuses()   

@status_router.delete("/", dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def delete_status_by_id(status_id: str):
    return StatusController.delete_status_by_id(status_id)      

@status_router.put("/update", response_model=StatusSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def update_status(status_id, status):
    return StatusController.update_status(status_id, status)
