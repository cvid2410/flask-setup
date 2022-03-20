from app.models.user import User
import logging
logger = logging.getLogger(__name__)

class UserService:

    @classmethod
    def get_users(cls):
        """ Returns all users """
        data = []
        for user in User.get_users():
            item = {
                "username":user.username,
                "email":user.email,
            }
            data.append(item)
        return data
        
    @classmethod
    def create_user(cls, received_json_data):
        """ creates an user """
        # Check that all keys are in received_json_data
        # could've made a form for simplicity
        required_keys = ['username','email', 'password']
        cls.check_required_keys(received_json_data, required_keys)

        user = User.create_user(received_json_data)
        return {"username":user.username, "email":user.email}
    

    @classmethod
    def check_required_keys(cls, received_json_data, required_keys):
        try:
            required_dict = {x:received_json_data[x] for x in required_keys}
        except:
            logger.exception("Not all keys present.")
            raise ValueError("Not all keys present.")
        else:
            # Check that no required keys are None
            if not all(required_dict.values()):
                logger.exception("Required values can not be none.")
                raise ValueError("Required values can not be None.")   


        
