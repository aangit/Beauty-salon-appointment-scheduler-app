from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.status.exceptions.status_exceptions import StatusNotFoundException
from app.status.models import Status
from app.status.exceptions import *


class StatusRepository:

    def __init__(self, db: Session):
        """
        This function is used to initialize the database session
        
        :param db: Session = Depends(get_db)
        :type db: Session
        """
        self.db = db

    def create_status(self, status):
        """
        It creates a new status object, adds it to the database, commits the changes, and then refreshes
        the status object
        
        :param status: The status of the order
        :return: The status object
        """
        try:
            status = Status(status)
            self.db.add(status)
            self.db.commit()
            self.db.refresh(status)
            return status
        except IntegrityError as e:
            raise e

    def read_status_by_id(self, status_id: str):
        """
        It takes a status_id, queries the database for a status with that id, and returns
        the status if it exists
        
        :param status_id: str
        :type status_id: str
        :return: A Status object
        """
        status = self.db.query(Status).filter(Status.id == status_id).first()
        if status is None:
            raise StatusNotFoundException(f"Status with provided ID: {status_id} not found.", 400)
        return status

    def read_status_by_name(self, status: str):
        """
        It takes a status's name as an argument, and returns a Status object from the database
        
        :param status: str
        :type status: str
        :return: A Status object
        """
        stat = self.db.query(Status).filter(Status.status == status).first()
        return stat

    def read_all_statuses(self):
        """
        It returns all the statuses in the database
        :return: A list of Status objects.
        """
        statuses = self.db.query(Status).all()
        return statuses

    def delete_status_by_id(self, status_id: str):
        """
        It deletes a status from the database by its ID
        
        :param status_id: str
        :type status_id: str
        :return: True
        """
        try:
            status = self.db.query(Status).filter(Status.id == status_id).first()
            if status is None:
                raise StatusNotFoundException(f"Status with provided ID: {status_id} not found", 400)
            self.db.delete(status)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_status(self, status_id: str, status: str):
        """
        It updates the status of a status with the provided status_id with the new provided status
        
        :param status_id: str
        :type status_id: str
        :param status: str
        :type status: str
        :return: The updated status object
        """
        try:
            stat = self.db.query(Status).filter(Status.id == status_id).first()
            if stat is None:
                raise StatusNotFoundException(f"Status with provided ID: {status_id} not found", 400) 
            stat.status = status
            self.db.add(stat)
            self.db.commit()
            self.db.refresh(stat)
            return stat
        except Exception as e:
            raise e
