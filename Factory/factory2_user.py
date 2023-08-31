# Using abstract class and method

from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username,password):
        self.username = username
        self.password = password
        
        
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def write(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass

        
        
class NormalUser(User):
    def __init__(self,username,password) :
        super().__init__(username,password)
        self.is_admin = False
        
    def read(self):
        print(f'{self.username} can read content')
    
    def write(self):        
        print(f'{self.username} cant write content because he is regular user')
    
    def delete(self):
        print(f'{self.username} cant delete content because he is regular user')
        
class AdminUser(User):
    def __init__(self,username,password) :
        super().__init__(username,password)
        self.email = 'admin@email.py'
        self.is_admin = True
        
    def read(self):
        print(f'{self.username} can read content')
    
    def write(self):        
        print(f'{self.username} can write content')
    
    def delete(self):
        print(f'{self.username} can delete content using {self.email}')
                
    
class UserFactory:
    def create_user(self,username,password='pass',is_admin= False):
        if is_admin:
            return AdminUser(username,password)
        else: 
            return NormalUser(username,password)
        
factory= UserFactory()
user1=factory.create_user("Deepti",'pass')
user1.read()
user1.write()
user1.delete()

user2=factory.create_user("Markus",'pass',is_admin=True)
user2.read()
user2.write()
user2.delete()