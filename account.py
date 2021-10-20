import grpc
import account_pb2
from models.db import Account as AccountModel
from models.db import Profile as ProfileModel
from account_pb2_grpc import AccountServiceServicer


class AccountService(AccountServiceServicer):

    def __init__(self, config):
        self.config = config

    def Login(self, request, context):
        metadata = context.invocation_metadata()
        username = request.username
        password = request.password
        metadata = dict(metadata)
        element = list(metadata.values())[0]
        print(element)
        print(ProfileModel.nodes.get(access_token=element).access_token)
        auth = ProfileModel.login(username, password)
        if element and element == ProfileModel.nodes.get(access_token=element).access_token:
            return account_pb2.LoginResponse(token=auth)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details('Invalid username or password')
        return account_pb2.LoginResponse()

    def SignUp(self, request, context):
        username = request.username
        password = request.password
        email = request.email
        result, success, users = AccountModel.create(username=username, password=password, email=email)
        if success:
            mod = ProfileModel(username=users.username, email=users.email, password=users.password, salt=users.salt, access_token=result)   # noqa
            print(mod)
            username_query = ProfileModel.nodes.filter(username=username)
            email_query = ProfileModel.nodes.filter(email=email)
            try:
                if (len(username_query) and len(email_query)) < 1:
                    mod.save()
                else:
                    raise Exception('username or email already exists')
            except ValueError:
                raise Exception('unknown value type or data')
            return account_pb2.SignUpResponse(token=result)

        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details(result)
        return account_pb2.SignUpResponse()
