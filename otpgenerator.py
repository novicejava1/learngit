import secrets
import string

OTP = ''
digit = string.digits

def generateOTP():

    global OTP

    for i in range(6):
        OTP +=str(''.join(secrets.choice(digit)))
    return OTP

if __name__ == '__main__':
    token = generateOTP()
    print(token)