from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.status.exceptions.status_exceptions import StatusNotFoundException
from app.status.models import Status
from app.status.exceptions import *


class StatusRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_status(self, status):
        try:
            status = Status(status)
            self.db.add(status)
            self.db.commit()
            self.db.refresh(status)
            return status
        except IntegrityError as e:
            raise e

    def read_status_by_id(self, status_id: str):
        status = self.db.query(Status).filter(Status.id == status_id).first()
        if status is None:
            raise StatusNotFoundException(f"Status with provided ID: {status_id} not found.", 400)
        return status

    def read_status_by_name(self, status: str):
        stat = self.db.query(Status).filter(Status.status == status).first()
        return stat

    def read_all_statuses(self):
        statuses = self.db.query(Status).all()
        return statuses

    def delete_status_by_id(self, status_id: str):
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
