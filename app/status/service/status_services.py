from app.status.exceptions.status_exceptions import StatusExistsException
from app.status.repository import StatusRepository
from app.db.database import SessionLocal
from app.status.exceptions import *

class StatusServices:
    @staticmethod
    def create_status(status):
        """
        If the status doesn't exist in the database, create it. If it does exist, raise an exception.
        
        :param status: The status name
        :return: The return value is the status_repository.create_status(status)
        """
        try:
            with SessionLocal() as db:
                status_repository = StatusRepository(db)
                stat = status_repository.read_status_by_name(status)       
                if stat is None:
                    return status_repository.create_status(status) 
                raise StatusExistsException(message="Status already exists in database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def get_status_by_id(status_id: str):
        """
        It takes a status_id, and returns a status object
        
        :param status_id: str
        :type status_id: str
        :return: A Status object
        """
        try:
            with SessionLocal() as db:
                status_repository = StatusRepository(db)
                return status_repository.read_status_by_id(status_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_statuses():
        """
        It creates a database session, creates a status repository, and then returns all statuses from
        the database.
        :return: A list of Status objects
        """
        with SessionLocal() as db:
            status_repository = StatusRepository(db)
            return status_repository.read_all_statuses()

    @staticmethod
    def delete_status_by_id(status_id: str):
        """
        It deletes a status by id
        
        :param status_id: str
        :type status_id: str
        """
        try:
            with SessionLocal() as db:
                status_repository = StatusRepository(db)
                status_repository.delete_status_by_id(status_id)                      
        except Exception as e:
            raise e

    @staticmethod
    def update_status(status_id: str, status: str):
        """
        It updates the status of a status_id in the database
        
        :param status_id: str
        :type status_id: str
        :param status: str = "status"
        :type status: str
        :return: The return value is the result of the update_status method in the StatusRepository
        class.
        """
        try:
            with SessionLocal() as db:
                status_repository = StatusRepository(db)                  
                return status_repository.update_status(status_id, status)  
        except Exception as e:
            raise e