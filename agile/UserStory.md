# Title: Login with Mobile OTP / Email OTP

# Description
As a Vendor, When I login on Murb using email and otp, I should be successfully logged in on platform and redirected to onboarding journey.

As a Vendor, When I login on Murb using mobile number and otp, I should be successfully logged in on platform and redirected to onboarding journey.

## Happy Path:

### New User registration
    - When new user comes on platform and tries to sign up, it should be able to get the otp using email or password
    - When user succesfully get valid otp, it should be able to signup with email or mobile and otp. 
    - User should be created in database with either or email.

### User Login
    - When new user comes on platform and tries to login, it should be able to get the otp using email or password
    - When user succesfully get valid otp, it should be able to login with email or mobile and otp. 
    - return user related information.

## Sad Path:

### New User registration
    - When new user comes on platform and tries to sign up, it should be able to get the otp using email or password
    - When user enters invalid otp, it get response {“status": “401", “message": “invalid otp”, data: {}}. 

### User Login
    - When new user comes on platform and tries to login, it should be able to get the otp using email or password
    - When user enters invalid otp, it get response {“status": “401", “message": “invalid otp”, data: {}}.

## API Specification
Endpoint: POST /api/auth/register
Description: Register a new user with email or mobile number and OTP.
Request Body:
{
    "identifier": "string", // email or mobile number
    "otp": "string"
}

Response Body:
201 Created: User registered successfully
{
    "status": "201",
    "message": "User registered successfully",
    "data": {
        "user": {
            "id": "string",
            "email": "string",
            "mobile": "string"
        }
    }
}

401 Unauthorized: Invalid OTP
{
    "status": "401",
    "message": "Invalid OTP",
    "data": {}
}
