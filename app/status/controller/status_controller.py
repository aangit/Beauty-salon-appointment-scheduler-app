from app.status.exceptions.status_exceptions import StatusExistsException, StatusNotFoundException
from app.status.service.status_services import StatusServices
from app.status.exceptions import *
from fastapi import HTTPException, Response


class StatusController:

    @staticmethod
    def create_status(status):
        try:
            stat = StatusServices.create_status(status)        
            return stat

        except StatusExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_status_by_id(status_id: str):
        try:
            status = StatusServices.get_status_by_id(status_id)
            if status:
                return status
        except StatusNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_status_by_name(status_name: str):
        try:
            status = StatusServices.get_status_by_id(status_name)    
            if status:
                return status
        except StatusNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_statuses():
        statuses = StatusServices.get_all_statuses()
        return statuses
    
    
    @staticmethod
    def delete_status_by_id(status_id: str):
        try:
            StatusServices.delete_status_by_id(status_id)                 
            return Response(content=f"Status with id - {status_id} is deleted")
        except StatusNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_status(status_id: str, status: str):
        try:
            stat = StatusServices.update_status(status_id, status)  
            return stat
        except StatusNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))