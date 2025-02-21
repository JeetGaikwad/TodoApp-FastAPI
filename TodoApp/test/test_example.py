import pytest

#  assert: for test validation of the operation result in passed or failed

def test_equal_or_not():
    assert 3 == 3
    
def test_is_string():
    assert not isinstance('10', int)
    assert isinstance('this is text', str)
    
class Student:
    def __init__(self, first_name, last_name, major, years):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

@pytest.fixture
def default_emp():
    return Student('John','Doe','Computer Science',3)
            

def test_person_validation(default_emp):
    assert default_emp.first_name == 'John', 'First name should be John'
    assert default_emp.last_name == 'Doe', 'Last name should be Doe'
    assert default_emp.major == 'Computer Science', 'Computer Science'
    assert default_emp.years == 3
    

# fixture : Is use to create components that can be reused later