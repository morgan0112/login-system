# Login System

This is a start-up Django login system that includes all features to handle user configurations.
This is to get started on a project without needing to focus too much on setting up account components.

This app extracts basic user information, but it is
set up in a way so that custom fields can be added. Before 
migration, alter the User model to suit your needs. 
All error and redirect configurations for the forms have already been set up.

It comes with a basic template containing the following pages:
* Home
* Sign in
* Registration
* Account
* Change Password


## Home Page
Includes a basic layout which can be changed to suit your needs.

<img src="https://dsm01pap004files.storage.live.com/y4mx8bDW5oD2JZKi1Kw7UA3pkk7gSeZsWhBJZ-Du-Paaax2-MyYInTRXQDYv8ifJyunFG6dyae7F5Uh3oF1INMgaGjoDmVABiwl5ls3qy92620uZ0wWgD1In6bWnpJCk-yBUkFJan21s5ohI1wY-7kdWijQ2qQoAubiykK5GiaOgjPPC1g39j3XgKe1qQlAhBGh?width=1266&height=785&cropmode=none" width="1266" height="785" />


## Sign in Page
Straightforward layout that will redirect you to the home page 
after you signin, but if you came to the signin page from an 
unauthorized (signin required) page, you will be redirected back to
that page after you signin.

<img src="https://dsm01pap004files.storage.live.com/y4mYSideKlyTX7HF4M-JNMdBHp9nFI9OgyuqoSD0RfWXKqUiDFmPoP9OpZhFFEXei6vE3rzcW1EIGI_GAtHcifwRMQdIGIj64Bk--dB12Nhs8fKnVJZyBXJnKckU0XITnjiLdTf7s76kD7z3sd1sdjYXdm6FXz8Zzm4J7zKSC-BwJZ2x-j1MTbDxL8m1UA8ymvw?width=1271&height=766&cropmode=none" width="1271" height="766" />

## Registration Page
Extracts basic information and will signin users automatically
after registration. The password configuration can be altered to
make users enter strong passwords. Users are recommended to use
Google password generator for password strength and just in case the
admin strengthens the password configuration too much which will
make it difficult for users to enter their own custom password.

<img src="https://dsm01pap004files.storage.live.com/y4mpIhmiLxCoasaCLkTS13AC7z0aSBZw4LAwA1-i9fw92TkN04JK_H38E3ZEhNq0SnCUf5dzINooosMteUbXLyQpwnHsMtaiNwn_Rspc4FwPOJqqH7Li7gX2Yf8sJwJTAnnDecEbpRFLA99lqyV05wS-Ff1c1IUwI_elFT7M_CKdRsqeubtja478FQ4SXwK5kSr?width=1250&height=852&cropmode=none" width="1250" height="852" />

## Account Page
Allows users to update the existing information.

<img src="https://dsm01pap004files.storage.live.com/y4mgGKSSbqG4VXsQlexgBZ9ZMIQN0wZGP_SVDlyLp0oiwPC0CQ_4yBVDcSCsArsIR1TJMj2EQlPqy97T_Pu5rPyS8AXhAzxYrObnMc6lyv4ZSrH3EcedXRA762fbv2p5oIjFE1cfDqZAA6O-VwwmQzMmak06Cakq09vCeiGB68y2j5B8JF3sRIDzjvyUQWocssL?width=1251&height=823&cropmode=none" width="1251" height="823" />

## Change Password
Allows users to change their password. 

<img src="https://dsm01pap004files.storage.live.com/y4mdx3SyVCs_yOk7JMISSHuLeBSYZOT4lGxbH5DssCif1Z8XLJYNaFPuc9nHFSfqRRDh_5i76Wk9ZeYJgq7RdB_Gu5kAtS6c3cEUsnbO1PPcJ9ysGOSwbQp3xjQ87CH4qqGcQPZQnkNcPsRMT3mMHl3PnRBHCar59SLAZFfQNz4z35shHjI8F3bdSAo1O3N1eeH?width=1250&height=831&cropmode=none" width="1250" height="831" />
