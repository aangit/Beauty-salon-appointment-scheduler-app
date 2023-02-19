from app.status.exceptions.status_exceptions import StatusExistsException
from app.status.repository import StatusRepository
from app.db.database import SessionLocal
from app.status.exceptions import *

class StatusServices:
    @staticmethod
    def create_status(status):
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
        try:
            with SessionLocal() as db:
                status_repository = StatusRepository(db)
                return status_repository.read_status_by_id(status_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_statuses():
        with SessionLocal() as db:
            status_repository = StatusRepository(db)
            return status_repository.read_all_statuses()

    @staticmethod
    def delete_status_by_id(status_id: str):
        try:
            with SessionLocal() as db:
                status_repository = StatusRepository(db)
                status_repository.delete_status_by_id(status_id)                      
        except Exception as e:
            raise e

    @staticmethod
    def update_status(status_id: str, status: str):
        try:
            with SessionLocal() as db:
                status_repository = StatusRepository(db)                  
                return status_repository.update_status(status_id, status)  
        except Exception as e:
            raise e