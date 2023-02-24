from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.user_type.models import UserType
from app.user_type.exceptions import UserTypeNotFoundException

class UserTypeRepository:

    def __init__(self, db: Session):
        """
        This function is used to initialize the database session
        
        :param db: Session = Depends(get_db)
        :type db: Session
        """
        self.db = db

    def create_user_type(self, user_type):
        """
        It creates a new user type and adds it to the database.
        
        :param user_type: {
        :return: The user_type object
        """
        try:
            user_type = UserType(user_type)
            self.db.add(user_type)
            self.db.commit()
            self.db.refresh(user_type)
            return user_type
        except IntegrityError as e:
            raise e

    def read_user_type_by_id(self, user_type_id: str):
        """
        It returns the first user type that matches the user_type_id
        
        :param user_type_id: str
        :type user_type_id: str
        :return: A UserType object
        """
        user_type= self.db.query(UserType).filter(UserType.id == user_type_id).first()
        return user_type

    def read_user_type_by_type(self, user_type: str):
        """
        It returns the first row of the UserType table where the user_type column is equal to the
        user_type parameter
        
        :param user_type: str
        :type user_type: str
        :return: A UserType object
        """
        u_type = self.db.query(UserType).filter(UserType.user_type == user_type).first()
        return u_type

    def read_all_user_types(self):
        """
        It returns all the user types from the database
        :return: A list of UserType objects
        """
        user_types = self.db.query(UserType).all()
        return user_types

    def delete_user_type_by_id(self, user_type_id: str):
        """
        It deletes a user type from the database
        
        :param user_type_id: str
        :type user_type_id: str
        :return: True
        """
        try:
            user_type = self.db.query(UserType).filter(UserType.id == user_type_id).first()
            if user_type is None:
                raise UserTypeNotFoundException(f"User type with provided ID: {user_type_id} not found", 404)
            self.db.delete(user_type)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_employee_type(self, user_type_id: str, user_type: str):
        """
        It updates the user_type column in the UserType table with the user_type value provided in the
        function call.
        
        :param user_type_id: str
        :type user_type_id: str
        :param user_type: str
        :type user_type: str
        :return: The updated user type
        """
        try:
            u_type = self.db.query(UserType).filter(UserType.id == user_type_id).first()
            if u_type is None:
                raise UserTypeNotFoundException(f"User type with provided ID: {user_type_id} not found", 404) 
            u_type.user_type = user_type
            self.db.add(u_type)
            self.db.commit()
            self.db.refresh(u_type)
            return u_type
        except Exception as e:
            raise e
