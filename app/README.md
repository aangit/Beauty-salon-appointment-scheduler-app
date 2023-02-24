# App for making appointments for various beauty salons

With this application, clients can schedule an appointment for verious services, also they can choose an employee, and therefore, each employee has its service types. 

Tables are:
* User
* User Type
* Contact
* Contact Type
* Appointment
* Status
* Service Type
* Appointment Service Type
* User Service Type

## User and User type

Both employee and client are derived from User, as well as super user and share similar characteristics, but their based on user type they represent, they behave differently based on the authorization their methods.

User types are:
* customer
* employee
* super_user

## Contact and Contact type

Similar like in user and user type, each contact has its type, and based on that users may insert or modify their contact (like phone, address, email, etc), and following that logic a foreign key from users exist in contact table.

## Appointment

Appointment has foreign keys from user (client_id and employee_id) and status, and by the change of status it is determined whether an appointment is set, or it is still in the requested status (*pending*).

## Status 

Status as its name says, is mainly used for setting a status for appointment. In this case we have accepted, pending and rejected. When user is creating an appointment, its default status is *pending*, and the moment an employee accepts the appointment, status changes to *accepted*, and an appointment is created.

## Service Type

Service type is further describing a service created by an employee, and its columns are service name, approximate duration, price and available at, which indicates the period for which this service can be scheduled (*in progress*).

## Appointment Service Type

Appointment Service Type is an intertable between appointment and service type (relationship many to many) and that way it is determined which appointment is set for which service. 

## User Service Type

User Service Type is as well an intertable, but between user and service type. In this case, user is an employee, and this way we know which employee is skilled for which service. So, when creating an appointment, if an employee doesn't have the necessary skill (service type), it is inpossible to create an appointment.

## In progress work 

One of the goals would be to create a timestamps. The first idea is to create Day of week table, where in day of week column would be inserted the days of week, and then an intertable User day of week, which would be in many to many relationship with the User and Day of week table, and it would connect an employee with the days of week he or she is available. That table would contain as well start and end (for example start and end of employee's shift).