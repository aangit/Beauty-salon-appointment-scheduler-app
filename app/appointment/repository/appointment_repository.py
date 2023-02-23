from datetime import date, datetime
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.appointment.models import Appointment
from app.status.models.status import Status


class AppointmentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_appointment(self, appointment_datetime, client_id, employee_id, pending_status_id):
        try:
            appointment = Appointment(appointment_datetime, client_id, employee_id, pending_status_id)
            self.db.add(appointment)
            self.db.commit()
            self.db.refresh(appointment)
            return appointment
        except IntegrityError as e:
            raise e


    def get_appointments_by_client_id(self, client_id: str):
        return self.db.query(Appointment).filter(Appointment.client_id == client_id).all()

    def get_all_appointments_by_employee_id_and_status(self, employee_id : str, status_id: str):
        return self.db.query(Appointment).filter(Appointment.employee_id == employee_id, Appointment.status_id == status_id).all()

    def get_all_appointments_by_employee_id_by_status_for_date(self, employee_id : str, status_id: str, appointment_datetime: str = None):
        return self.db.query(Appointment).filter(Appointment.employee_id == employee_id, Appointment.status_id == status_id, func.date(Appointment.appointment_datetime) == appointment_datetime).all()


    def get_appointment_by_id(self, appointment_id: str):
        appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()
        return appointment

    def get_all_appointments(self):
        appointments = self.db.query(Appointment).all()
        return appointments

    def delete_appointment_by_id(self, appointment_id:str):
        try:
            appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()
            self.db.delete(appointment)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def cancel_appointement(self, appointment_id: str):
        try:
            rejected_status = self.db.query(Status).filter_by(status = 'rejected').one() 
            appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()
            appointment.status_id = rejected_status.id
            self.db.add(appointment)
            self.db.commit()
            self.db.refresh(appointment)
            return appointment
        except IntegrityError as e:
            raise e

    def accept_appointment(self, appointment_id: str):
        try:
            accepted_status = self.db.query(Status).filter_by(status = 'accepted').one() 
            appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()
            appointment.status_id = accepted_status.id
            self.db.add(appointment)
            self.db.commit()
            self.db.refresh(appointment)
            return appointment
        except IntegrityError as e:
            raise e
            

    def update_appointment_by_id(self, appointment_id, appointment_datetime, client_id, employee_id, status_id):
        try:
            appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()
            appointment.appointment_datetime = appointment_datetime
            appointment.client_id = client_id
            appointment.employee_id = employee_id
            appointment.status_id = status_id
            self.db.add(appointment)
            self.db.commit()
            self.db.refresh(appointment)
            return appointment
        except IntegrityError as e:
            raise e

    