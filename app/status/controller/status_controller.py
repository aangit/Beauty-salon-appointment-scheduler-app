from app.status.exceptions import StatusExistsException, StatusNotFoundException
from app.status.service.status_services import StatusServices
from app.status.exceptions import *
from fastapi import HTTPException, Response


class StatusController:

    @staticmethod
    def create_status(status):
        """
        It creates a status
        
        :param status: {
        :return: The status object
        """
        try:
            stat = StatusServices.create_status(status)        
            return stat

        except StatusExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_status_by_id(status_id: str):
        """
        It gets a status by id, and if it doesn't find it, it raises an exception
        
        :param status_id: str
        :type status_id: str
        :return: The status object
        """
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
        """
        It gets a status by name, and if it doesn't find it, it raises an exception
        
        :param status_name: str
        :type status_name: str
        :return: A status object
        """
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
        """
        It returns a list of all statuses
        :return: A list of dictionaries.
        """
        statuses = StatusServices.get_all_statuses()
        return statuses
    
    
    @staticmethod
    def delete_status_by_id(status_id: str):
        """
        It deletes a status by id
        
        :param status_id: str - the id of the status to be deleted
        :type status_id: str
        :return: Response(content=f"Status with id - {status_id} is deleted")
        """
        try:
            StatusServices.delete_status_by_id(status_id)                 
            return Response(content=f"Status with id - {status_id} is deleted")
        except StatusNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_status(status_id: str, status: str):
        """
        It updates the status of a status
        
        :param status_id: str
        :type status_id: str
        :param status: str
        :type status: str
        :return: The return value is a dict with the following keys:
        """
        try:
            stat = StatusServices.update_status(status_id, status)  
            return stat
        except StatusNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))