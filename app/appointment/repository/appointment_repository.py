from datetime import date, datetime
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.appointment.models import Appointment
from app.status.models.status import Status


class AppointmentRepository:

    def __init__(self, db: Session):
        """
        This function is used to initialize the database session
        
        :param db: Session = Depends(get_db)
        :type db: Session
        """
        self.db = db

    def create_appointment(self, appointment_datetime, client_id, employee_id, pending_status_id):
        """
        It creates an appointment object, adds it to the database, commits the changes, and then
        refreshes the appointment object
        
        :param appointment_datetime: datetime.datetime(2020, 5, 1, 10, 0)
        :param client_id: 1
        :param employee_id: 1
        :param pending_status_id: 1
        :return: The appointment object
        """
        try:
            appointment = Appointment(appointment_datetime, client_id, employee_id, pending_status_id)
            self.db.add(appointment)
            self.db.commit()
            self.db.refresh(appointment)
            return appointment
        except IntegrityError as e:
            raise e


    def get_appointments_by_client_id(self, client_id: str):
        """
        It returns all appointments for a given client_id
        
        :param client_id: str
        :type client_id: str
        :return: A list of Appointment objects
        """
        return self.db.query(Appointment).filter(Appointment.client_id == client_id).all()

    def get_all_appointments_by_employee_id_and_status(self, employee_id : str, status_id: str):
        """
        Get all appointments by employee id and status
        
        :param employee_id: str
        :type employee_id: str
        :param status_id: 1 = Pending, 2 = Confirmed, 3 = Cancelled
        :type status_id: str
        :return: A list of Appointment objects
        """
        return self.db.query(Appointment).filter(Appointment.employee_id == employee_id, Appointment.status_id == status_id).all()

    def get_all_appointments_by_employee_id_by_status_for_date(self, employee_id : str, status_id: str, appointment_datetime: str = None):
        """
        Get all appointments for a given employee, status, and date
        
        :param employee_id: str
        :type employee_id: str
        :param status_id: str = '1'
        :type status_id: str
        :param appointment_datetime: str = None
        :type appointment_datetime: str
        :return: A list of Appointment objects
        """
        return self.db.query(Appointment).filter(Appointment.employee_id == employee_id, Appointment.status_id == status_id, func.date(Appointment.appointment_datetime) == appointment_datetime).all()


    def get_appointment_by_id(self, appointment_id: str):
        """
        It returns the first appointment in the database that matches the appointment_id
        
        :param appointment_id: str
        :type appointment_id: str
        :return: A single appointment object
        """
        appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()
        return appointment

    def get_all_appointments(self):
        """
        It returns all the appointments in the database
        :return: A list of all the appointments in the database.
        """
        appointments = self.db.query(Appointment).all()
        return appointments

    def delete_appointment_by_id(self, appointment_id:str):
        """
        It deletes an appointment from the database by its id
        
        :param appointment_id: The id of the appointment to be deleted
        :type appointment_id: str
        :return: The return value is a boolean value.
        """
        try:
            appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()
            self.db.delete(appointment)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def cancel_appointement(self, appointment_id: str):
        """
        It takes an appointment_id and sets the status of the appointment to 'rejected'
        
        :param appointment_id: str
        :type appointment_id: str
        :return: The appointment object
        """
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
        """
        It takes an appointment_id, finds the appointment in the database, changes the status_id to the
        id of the accepted status, and returns the appointment and sets status to accepted.
        
        :param appointment_id: str
        :type appointment_id: str
        :return: The appointment object
        """
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
        """
        It takes in an appointment_id, appointment_datetime, client_id, employee_id, and status_id, and
        updates the appointment with the given appointment_id with the given values
        
        :param appointment_id: 1
        :param appointment_datetime: datetime.datetime(2019, 1, 1, 0, 0)
        :param client_id: 1
        :param employee_id: 1
        :param status_id: 1
        :return: The appointment object
        """
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

    