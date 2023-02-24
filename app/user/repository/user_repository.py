
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.user.models import User


class UserRepository:

    def __init__(self, db: Session):
        """
        This function is used to initialize the database session
        
        :param db: Session = Depends(get_db)
        :type db: Session
        """
        self.db = db

    def create_user(self, email, password, user_type_id):
        """
        It creates a user and returns the user object.
        
        :param email: string
        :param password: the password to be hashed
        :param user_type_id: 1
        :return: The user object
        """
        try:
            user = User(email, password, user_type_id)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def create_super_user(self, email, password):
        """
        It creates a user with the given email and password, and returns the user object
        
        :param email: The email address of the user
        :param password: The password to be hashed
        :return: The user object
        """
        try:
            user = User(email=email, password=password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def get_user_by_id(self, user_id: str):
        """
        It returns the first user in the database with the given user_id
        
        :param user_id: str
        :type user_id: str
        :return: A user object
        """
        user = self.db.query(User).filter(User.id == user_id).first()
        return user

    def get_all_users(self):
        """
        It returns all the users in the database
        :return: A list of User objects
        """
        users = self.db.query(User).all()
        return users

    def delete_user_by_id(self, user_id: str):
        """
        It deletes a user from the database by their id
        
        :param user_id: The id of the user to be deleted
        :type user_id: str
        :return: True
        """
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def read_user_by_email(self, email: str):
        """
        It takes an email address as a string, and returns a user object if the email address is found
        in the database
        
        :param email: str
        :type email: str
        :return: A user object
        """
        user = self.db.query(User).filter(User.email == email).first()
        return user

    def get_all_users_by_type(self, user_type_id: str):
        """
        It returns all users with a given user_type_id
        
        :param user_type_id: str
        :type user_type_id: str
        :return: A list of User objects
        """
        return self.db.query(User).filter(User.user_type_id == user_type_id).all()

    def employee_has_skills(self, employee_id: str):
        """
        It returns the first user in the database with the given employee_id
        
        :param employee_id: str
        :type employee_id: str
        :return: A list of User objects
        """
        return self.db.query(User).filter(User.id == employee_id).first()
