# 🏥 Hospital Management System

A full-featured Hospital Management System built using **Django**, **HTML**, **CSS**, and **SQL**. This system streamlines various hospital operations such as patient registration, medicine management, billing, staff management, and more.

## 🚀 Features

### 👥 User Roles
- **Admin**: Full control over the system.
- **Receptionist**: Handles patient registrations and appointments.
- **Doctors**: View patient records and prescribe medicines.
- **Staff**: Manage lab reports, billing, and room assignments.
- **Patients**: View medical history, request appointments, and pay bills.

### 🩺 Modules
- **Patient Registration & Management**
- **Appointment Scheduling**
- **Medicine Management & Stock**
- **Billing & Invoice Generation**
- **Room/Bed Allocation**
- **Staff Dashboard**
- **Medical History Tracking**
- **Payment Integration**
- **Responsive Dashboards for Roles**

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite / MySQL
- **Tools**: Git, GitHub, VS Code

## 📸 Screenshots

![add_medicalHistory](https://github.com/user-attachments/assets/7a4a350d-1999-4014-8007-4e789a9eac82)
![admin_dashboard 1](https://github.com/user-attachments/assets/55ab7951-6b06-4155-acef-93f49c07e232)
![admit_patient history](https://github.com/user-attachments/assets/000a83a0-562f-4658-8e63-2c4d15b6a200)
![after_approve reques](https://github.com/user-attachments/assets/845e6bfa-f75a-4be8-a646-3e641713bb85)
![All_bill](https://github.com/user-attachments/assets/1a14701a-4187-47e4-827a-df030eed4149)
![book](https://github.com/user-attachments/assets/09478983-13b7-4191-a423-8a21f6b7b0b3)
![create_bill](https://github.com/user-attachments/assets/1af05844-0903-4a8b-80da-22b627d0591c)
![doctor_dashboard](https://github.com/user-attachments/assets/8207b2bd-cd7e-48f7-bf9b-43df734e3581)
![home](https://github.com/user-attachments/assets/90d97d9a-b6bd-4bd2-9a96-02c2ce265937)
![inPatient](https://github.com/user-attachments/assets/bc21d50d-f15a-4f92-ab2d-faf0b2d10e70)
![login](https://github.com/user-attachments/assets/e7bd718c-0d78-4bf4-9d56-bc193e0b632c)
![medicine store](https://github.com/user-attachments/assets/943967f2-4d5e-483e-bba9-cb8357224a1a)
![Patient_dashboard](https://github.com/user-attachments/assets/00e592a6-26e4-49f8-9cce-3c91e50ec460)
![receptionist](https://github.com/user-attachments/assets/1f6c610a-1f80-4dda-8335-59ad98990f43)
![recieve_medicince request](https://github.com/user-attachments/assets/9936df76-0ca5-477e-af9d-da8c609dfa2b)
![request_medicine](https://github.com/user-attachments/assets/5aeb57a1-cd1c-4ff9-9a58-2a8c09f01f23)
![signup](https://github.com/user-attachments/assets/ba5b67d2-47d5-466c-b3bf-f9bb0198d117)
![staff_dashboard](https://github.com/user-attachments/assets/66f52462-9ca0-44b4-8240-be1402c7c574)
![success](https://github.com/user-attachments/assets/a32139b5-aab7-42e6-a936-9f0754c3a2cf)
![view_medicalHistory](https://github.com/user-attachments/assets/ae149bb6-68b6-4303-a781-eaaef6b5b1b5)







## 🧑‍💻 Setup Instructions
   
   ```bash
**Clone the repository**
   git clone https://github.com/Priyanshijha789/Project-django.git
   cd Project-django
   #Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   #install independencies
   pip install -r requirements.txt
   #Run migrations
   python manage.py makemigrations
   python manage.py migrate
   #create superuser
   python manage.py createsuperuser
   #Start the development server
   python manage.py runserver
   Visit the app(http://127.0.0.1:8000/)

