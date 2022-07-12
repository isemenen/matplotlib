
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name
#        print(full_name)
    def greet_user(self):
        print('Hi, ', self.describe_user())
    def increment_login_attempts(self):
        print('before increment:',self.login_attempts)
        self.login_attempts += 1
        print('after increment:', self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts = 0
        print('reset:', self.login_attempts)

is_user = User('igor', 'semenenko')
is_user.describe_user()
print(is_user.describe_user())
#is_user.greet_user()
is_user.increment_login_attempts()
is_user.increment_login_attempts()
is_user.reset_login_attempts()