from app.service_type.service import ServiceTypeServices
from app.service_type.exceptions import *
from fastapi import HTTPException, Response


class ServiceTypeController:

    @staticmethod
    def create_service_type(service_name, approximate_duration, price, available_at):
        try:
            s_type = ServiceTypeServices.create_service_type(service_name, approximate_duration, price, available_at)   
            return s_type

        except ServiceTypeExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_service_type_by_id(service_type_id: str):
        try:
            service_type = ServiceTypeServices.read_service_type_by_id(service_type_id)
            if service_type:
                return service_type
        except ServiceTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_service_type_by_service_name(service_name: str):
        try:
            service_type = ServiceTypeServices.read_service_type_by_id(service_name) 
            if service_type:
                return service_type
        except ServiceTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all_service_types():
        service_types = ServiceTypeServices.read_all_service_types() 
        return service_types

    @staticmethod
    def delete_service_type_by_id(service_type_id: str):
        try:
            ServiceTypeServices.delete_service_type_by_id(service_type_id)                    
            return Response(content=f"Service type with id - {service_type_id} is deleted")
        except ServiceTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
