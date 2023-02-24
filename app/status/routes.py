from fastapi import APIRouter, Depends
from app.status.controller.status_controller import StatusController
from app.status.schemas import *
from app.user.controller.user_authenification_controller import JWTBearer

status_router = APIRouter(tags=["status"], prefix="/api/status")


@status_router.post("/add-new-status", response_model=StatusSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def create_status(status: StatusSchemaIn):
    """
    It takes a `StatusSchemaIn` object, and returns the result of calling
    `StatusController.create_status` with the `status` attribute of the `StatusSchemaIn` object
    
    :param status: StatusSchemaIn
    :type status: StatusSchemaIn
    :return: The return value is a tuple of the form (status, headers, body)
    """
    return StatusController.create_status(status.status)

@status_router.get("/id", response_model=StatusSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_status_by_id(status_id: str):
    """
    This function returns a status object by its id
    
    :param status_id: str
    :type status_id: str
    :return: A status object
    """
    return StatusController.get_status_by_id(status_id)      


@status_router.get("/get-all-statuses", response_model=list[StatusSchema], dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_all_statuses():
    """
    It returns all statuses from the StatusController
    :return: A list of all the statuses in the database.
    """
    return StatusController.get_all_statuses()   

@status_router.delete("/", dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def delete_status_by_id(status_id: str):
    """
    Delete a status by id
    
    :param status_id: str
    :type status_id: str
    :return: The return value of the function is the return value of the function that is being called.
    """
    return StatusController.delete_status_by_id(status_id)      

@status_router.put("/update", response_model=StatusSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def update_status(status_id, status):
    """
    Update the status
    
    :param status_id: The id of the status you want to update
    :param status: The status to update
    :return: The return value of the function update_status()
    """
    return StatusController.update_status(status_id, status)
