# one key example of where we used inheritance in js, was this:
# class IndexBooks extends React.Component

# We'll a Phone class, then some sub-classes of Phone, namely IPhone and AndroidPhone.

# All phones

# have a phone number
# can place phone calls
# can send text messages

class Phone:
    def __init__(self, phone_number):
        self.number = phone_number
    
    def __str__(self):
        return f"This phone's number is : {self.number}"
    
    # call method
    def call(self, other_number):
        print(f"Calling {other_number} from {self.number}")
    # text method
    def text(self, other_number, message):
        print(f"Sending: {message} \n from {self.number} to {other_number}")

p1 = Phone(1111111111)
# p2 = Phone(2222222222)
# print(f"phone 1: {p1} \n phone 2: {p2}")

# p1.call(p2.number)

# p1.text(p2.number, "whats up?")
# p2.text(p1.number, "nm hbu")

class Iphone(Phone):
    def __init__(self, phone_number, generation, color):
        # to keep some of the original aspects and utilize them, we add a super method
        super().__init__(phone_number)
        self.generation = generation
        self.color = color
        self.fingerprint = None
        self.locked = True
    
    def __str__(self):
        return f"{self.color} Iphone {self.generation} \n Phone number is {self.number}. \n Phone locked? {self.locked}"
    
    # set_fingerprint method
    def set_fingerprint(self, fingerprint):
        self.fingerprint = fingerprint
    # unlock method
    def unlock(self, fingerprint=None):
        if (not self.fingerprint):
            print("Phone unlocked because fingerprint hasnt been set")
        elif (fingerprint == self.fingerprint):
            self.locked = False
            print("Phone unlocked. Fingerprint matches")
        else :
            print("Phone locked. Fingerprint does not match.")


iphone_twelve = Iphone(3333333333, '12', 'black')
# print(p1)
# print(iphone_twelve)
# iphone_twelve.call(p1.number)
# iphone_twelve.text(p1.number, "hows things?")

# iphone_twelve.unlock()
# iphone_twelve.set_fingerprint("timm's pinky")
# iphone_twelve.unlock()
# iphone_twelve.unlock("timm's pinky")
# print(iphone_twelve)

class Android(Phone):
    def __init__(self, phone_number, brand):
        # to keep some of the original aspects and utilize them, we add a super method
        super().__init__(phone_number)
        self.keyboard = 'Default'
        self.brand = brand

    def __str__(self):
        return f"Android Phone made by {self.brand}\n Phone number is {self.number}.\nThis phone uses the {self.keyboard} keyboard "
    
    def set_keyboard(self, keyboard):
        self.keyboard = keyboard
        print(f'changing keyboard settings to {keyboard}...')

samsungS23 = Android(4444444444, 'samsung')
print(samsungS23)
samsungS23.set_keyboard('Google')
print(samsungS23)
