### ❓question 1.1
class Instructor:
    degree = "PhD (Magic)" # this is a class attribute
    def __init__(self, name):
        self.name = name # this is an instance attribute

    def lecture(self, topic):
        print("Today we're learning about " + topic)


dumbledore = Instructor("Dumbledore")


class Student:
    instructor = dumbledore

    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        ta.add_student(self)

    def attend_lecture(self, topic):
        Student.instructor.lecture(topic)
        if Student.instructor == dumbledore:
            print(Student.instructor.name + " is awesome!")
        else:
            print("I miss Dumbledore.")
        self.understanding += 1

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)



class TeachingAssistant:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1   # 在原来student.understanding的基础上加1


snape = TeachingAssistant('Snape')
harry = Student("Harry", snape)
harry.attend_lecture("potions")

hermione = Student("Hermione", snape)
hermione.attend_lecture("herbology")

hermione.visit_office_hours(TeachingAssistant('Hagrid'))

print(harry.understanding)

print(snape.students['Hermione'].understanding)

Student.instructor = Instructor('Umbridge')   # class attribute assignment
Student.attend_lecture(harry, 'transfiguration')
# Equivalent to harry.attend_lecture("transfiguration")



### ❓question 1.2
class Email:
    """Every email object has 3 instance attributes:
    the message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Mailman:
    """Each Mailman has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):   # email应是来自于Email class的instance
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        """
        msg = email.msg   # 获取信息
        recipient = email.recipient_name   # 收件人
        recipient.inbox.append(msg)   # 添加inbox
        """
        client = self.clients[email.recipient_name]   # 收信人的名字
        client.receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it
        to the clients instance attribute.
        """
        """
        if client in self.clients:
            self.clients[client].append(client_name)
        else:
            self.clients[client] = [client_name]   # 假设client_name是一个list
        """
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), mailman
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received). """
    def __init__(self, mailman, name):
        self.inbox = []
        self.mailman = mailman
        self.name = name
        self.mailman.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        """
        send_email = Email(msg, self.name, recipient_name)
        Mailman.send(self.mailman, send_email)
        """
        email = Email(msg, self.name, recipient_name)
        self.mailman.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this client.
        """
        """
        msg = email.msg
        recipient = email.recipient_name
        if recipient == self.name:
            self.inbox.append(msg)
        """
        self.inbox.append(email)



### ❓question 2.1
class Dog:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name + " say woof!")

class Cat:
    def __init__(self, name, owner, lives=9):
        self.name = name
        self.owner = owner
        self.lives = lives

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name + " say meow!")

#### Notice that there’s a lot of repeated code!

class Pet:
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):
    def __init__(self, name, owner):
        Pet.__init__(self, name, owner)

    def talk(self):
        print(self.name + " say woof!")


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        print(self.name + " say meow!")

    def lose_life(self):
        """A cat can only lose a life if they have at
        least one life. When lives reaches zero, 'is_alive'
        becomes False.
        """
        if self.lives > 0:
            self.lives -= 1
        elif self.lives == 0:
            self.is_alive = False
        if not self.is_alive:
            print(self.name + ' this cat has no more lives to lose.')
c = Cat('mi', 'piggy', 3)
print(c.name, c.lives)
c.lose_life()


### ❓question 2.2
class NoisyCat(Cat): # Fill me in!

    """A Cat that repeats things twice."""
    # def __init__(self, name, owner, lives=9):
            # Is this method necessary? Why or why not?


    def talk(self):
        """Repeat what a Cat says twice."""
        Cat.talk(self)
        Cat.talk(self)

n = NoisyCat('mimi', 'mine')
n.talk()


### ❓question 2.3
class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4

x, y = A(), B()
print(x.f())   # 2
# print(B.f())   # 报错
print(x.g(x, 1))   # 4
print(y.g(x, 2))   # 8


class Yolo:

    def __init__(self, motto):
        self.motto = motto

    def g(self, x):
        return self.motto + x
x = Yolo(1)   # initialize motto = 1
print(x.g(3))
print(x.g(5))
x.motto = 5   # class assignment
print(x.g(5))
