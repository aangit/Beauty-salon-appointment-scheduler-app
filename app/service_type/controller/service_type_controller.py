from app.service_type.service import ServiceTypeServices
from app.service_type.exceptions import ServiceTypeNotFound, ServiceTypeExists
from fastapi import HTTPException, Response


class ServiceTypeController:

    @staticmethod
    def create_service_type(service_name, approximate_duration, price, available_at):
        """
        It creates a service type
        
        :param service_name: String
        :param approximate_duration: int
        :param price: Decimal
        :param available_at: [{'day': 'Monday', 'start_time': '10:00', 'end_time': '18:00'}, {'day':
        'Tuesday', 'start_time': '10:00', 'end_time': '18:00'}, {'day
        :return: The service type object
        """
        try:
            s_type = ServiceTypeServices.create_service_type(service_name, approximate_duration, price, available_at)   
            return s_type

        except ServiceTypeExists as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_service_type_by_id(service_type_id: str):
        """
        It reads a service type by id
        
        :param service_type_id: str
        :type service_type_id: str
        :return: The return value is a ServiceType object.
        """
        try:
            service_type = ServiceTypeServices.read_service_type_by_id(service_type_id)
            if service_type:
                return service_type
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_service_type_by_service_name(service_name: str):
        """
        It takes a service name passed in as argument, and returns the service type that matches the passed criteria
        
        :param service_name: str
        :type service_name: str
        :return: A ServiceType object
        """
        try:
            service_type = ServiceTypeServices.read_service_type_by_id(service_name) 
            if service_type:
                return service_type
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def read_service_type_by_name_partially(service_name: str):
        """
        It reads a service type by name partially and returnes all the result that match that criteria
        
        :param service_name: str
        :type service_name: str
        :return: A list of ServiceType objects
        """
        try:
            service_type = ServiceTypeServices.read_service_type_by_name_partially(service_name) 
            if service_type:
                return service_type
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))



    @staticmethod
    def read_all_service_types():
        """
        Read all service types from the database and return them
        :return: A list of ServiceType objects
        """
        service_types = ServiceTypeServices.read_all_service_types() 
        return service_types

    @staticmethod
    def user_has_service_type(service_type_id: str):
        """
        It checks if the user has a service type and if they do, it returns the service type
        
        :param service_type_id: str
        :type service_type_id: str
        :return: A list of dictionaries.
        """
        try:
            user_services = ServiceTypeServices.user_has_service_type(service_type_id)
            if user_services:
                return user_services
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_users_per_service_type_name(service_name: str):
        """
        It reads the users per service type name
        
        :param service_name: str
        :type service_name: str
        :return: A list of users
        """
        try:
            users_services = ServiceTypeServices.read_users_per_service_type_name(service_name)
            if users_services:
                return users_services
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def delete_service_type_by_id(service_type_id: str):
        """
        It deletes a service type by id
        
        :param service_type_id: str
        :type service_type_id: str
        :return: Response(content=f"Service type with id - {service_type_id} is deleted")
        """
        try:
            ServiceTypeServices.delete_service_type_by_id(service_type_id)                    
            return Response(content=f"Service type with id - {service_type_id} is deleted")
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    @staticmethod
    def update_service_type_by_id(service_type_id: str, service_type):
        """
        It updates a service type by id
        
        :param service_type_id: str
        :type service_type_id: str
        :param service_type: ServiceType
        :return: Response
        """
        try:
            ServiceTypeServices.update_service_type_by_id(service_type_id, service_type)        
            return Response(content=f"Service type with id - {service_type_id} is updated")
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

