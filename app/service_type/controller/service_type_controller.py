from app.service_type.service import ServiceTypeServices
from app.service_type.exceptions import ServiceTypeNotFound, ServiceTypeExists
from fastapi import HTTPException, Response


class ServiceTypeController:

    @staticmethod
    def create_service_type(service_name, approximate_duration, price, available_at):
        try:
            s_type = ServiceTypeServices.create_service_type(service_name, approximate_duration, price, available_at)   
            return s_type

        except ServiceTypeExists as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_service_type_by_id(service_type_id: str):
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
        service_types = ServiceTypeServices.read_all_service_types() 
        return service_types

    @staticmethod
    def user_has_service_type(service_type_id: str):
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
        try:
            ServiceTypeServices.delete_service_type_by_id(service_type_id)                    
            return Response(content=f"Service type with id - {service_type_id} is deleted")
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    @staticmethod
    def update_service_type_by_id(service_type_id: str, service_type):
        try:
            ServiceTypeServices.update_service_type_by_id(service_type_id, service_type)        
            return Response(content=f"Service type with id - {service_type_id} is updated")
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

