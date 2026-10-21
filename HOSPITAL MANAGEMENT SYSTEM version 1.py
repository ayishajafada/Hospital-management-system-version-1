# ------------------ PATIENTS LIST ------------------
patients = [
    {"patient_id": 101, "name": "Ayisha jafada", "age": 27, "gender": "Female", "phone": "9876543210", "disease": "Fever", "blood_group": "A+"},
    {"patient_id": 102, "name": "Priya Nair", "age": 31, "gender": "Female", "phone": "9123456780", "disease": "Diabetes", "blood_group": "B+"},
    {"patient_id": 103, "name": "Jafar N V", "age": 55, "gender": "Male", "phone": "9988776655", "disease": "Hypertension", "blood_group": "A-"},
    {"patient_id": 104, "name": "Shamsudheen", "age": 45, "gender": "Male", "phone": "9988774655", "disease": "Cancer", "blood_group": "A+"},
    {"patient_id": 105, "name": "Harsha", "age": 35, "gender": "Male", "phone": "9988776655", "disease": "AKI", "blood_group": "B-"},
    {"patient_id": 106, "name": "Anjali", "age": 28, "gender": "Female", "phone": "98475662343", "disease": "Migraine", "blood_group": "AB+"},
    {"patient_id": 107, "name": "Rahul Menon", "age": 40, "gender": "Male", "phone": "9876501234", "disease": "Asthma", "blood_group": "O+"},
    {"patient_id": 108, "name": "Divya Suresh", "age": 29, "gender": "Female", "phone": "9123405678", "disease": "Thyroid", "blood_group": "B+"},
    {"patient_id": 109, "name": "Vikram Rao", "age": 50, "gender": "Male", "phone": "9988701122", "disease": "Arthritis", "blood_group": "A+"},
    {"patient_id": 110, "name": "Sneha Pillai", "age": 22, "gender": "Female", "phone": "9847509988", "disease": "Anemia", "blood_group": "O-"},
    {"patient_id": 111, "name": "Manoj Kumar", "age": 33, "gender": "Male", "phone": "9123459876", "disease": "Tuberculosis", "blood_group": "B-"},
    {"patient_id": 112, "name": "Lakshmi Devi", "age": 47, "gender": "Female", "phone": "9876543211", "disease": "Kidney Stone", "blood_group": "AB+"},
    {"patient_id": 113, "name": "Aravind Nair", "age": 36, "gender": "Male", "phone": "9988771122", "disease": "Migraine", "blood_group": "A-"},
    {"patient_id": 114, "name": "Pooja Sharma", "age": 26, "gender": "Female", "phone": "9123456789", "disease": "PCOS", "blood_group": "O+"},
    {"patient_id": 115, "name": "Sandeep Reddy", "age": 42, "gender": "Male", "phone": "9876509876", "disease": "Diabetes", "blood_group": "B+"},
    {"patient_id": 116, "name": "Neha Thomas", "age": 31, "gender": "Female", "phone": "9847566234", "disease": "Hypertension", "blood_group": "A+"},
    {"patient_id": 117, "name": "Rohit Sharma", "age": 38, "gender": "Male", "phone": "9876512345", "disease": "Liver Disease", "blood_group": "O+"}
]

# ------------------ DOCTORS LIST ------------------
doctors = [
    {"doctor_id": 1001, "name": "Dr. Harsha", "specialization": "Orthopaedic", "experience": 15, "consultation_fee": 1000.0},
    {"doctor_id": 1002, "name": "Dr. Sachin", "specialization": "Oncology", "experience": 9, "consultation_fee": 650.0},
    {"doctor_id": 1003, "name": "Dr. Prabha", "specialization": "ENT", "experience": 12, "consultation_fee": 900.0},
    {"doctor_id": 1004, "name": "Dr. Meera", "specialization": "Cardiology", "experience": 20, "consultation_fee": 1200.0},
    {"doctor_id": 1005, "name": "Dr. Arjun", "specialization": "Neurology", "experience": 14, "consultation_fee": 1500.0},
    {"doctor_id": 1006, "name": "Dr. Kavya", "specialization": "Dermatology", "experience": 8, "consultation_fee": 700.0},
    {"doctor_id": 1007, "name": "Dr. Ramesh", "specialization": "General Medicine", "experience": 18, "consultation_fee": 500.0},
    {"doctor_id": 1008, "name": "Dr. Anitha", "specialization": "Gynecology", "experience": 16, "consultation_fee": 1100.0},
    {"doctor_id": 1009, "name": "Dr. Varun", "specialization": "Pediatrics", "experience": 10, "consultation_fee": 800.0},
    {"doctor_id": 1010, "name": "Dr. Sneha", "specialization": "Psychiatry", "experience": 7, "consultation_fee": 950.0}
]

# ------------------ FUNCTIONS ------------------
def add_patient():
    try:
        patient_id = int(input("Enter Patient ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        if age <= 0:
            raise ValueError("Age must be positive.")
        gender = input("Enter Gender: ")
        phone = input("Enter Phone Number: ")
        disease = input("Enter Disease: ")
        blood_group = input("Enter Blood Group: ")

        new_patient = {
            "patient_id": patient_id,
            "name": name,
            "age": age,
            "gender": gender,
            "phone": phone,
            "disease": disease,
            "blood_group": blood_group
        }
        patients.append(new_patient)
        print("\n✅ Patient added successfully!\n")

    except ValueError as e:
        print("❌ Error:", e)

def display_single_patient(patient):
    print("---------------------Patient's Details----------------------")
    print("Patient ID:", patient["patient_id"])
    print("Name:", patient["name"])
    print("Age:", patient["age"])
    print("Gender:", patient["gender"])
    print("Phone:", patient["phone"])
    print("Disease:", patient["disease"])
    print("Blood group:", patient["blood_group"])
    print("------------------------------------")

def display_patients():
    if len(patients) == 0:
        print("No registered patients")
    else:
        print("--------------Patients List--------------")
        for patient in patients:
            display_single_patient(patient)

def search_patient():
    patient_id = int(input("Enter Patient ID to be searched: "))
    for patient in patients:
        if patient["patient_id"] == patient_id:
            print("Patient Found! ✅")
            display_single_patient(patient)
            return patient
    print("Patient Not Found! 👎🏻")
    return None

def add_doctor():
    doctor_id = int(input("Enter Doctor ID: "))
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")
    experience = int(input("Enter Years of Experience: "))
    consultation_fee = float(input("Enter Consultation Fee: "))

    new_doctor = {
        "doctor_id": doctor_id,
        "name": name,
        "specialization": specialization,
        "experience": experience,
        "consultation_fee": consultation_fee
    }
    doctors.append(new_doctor)
    print("\n✅ Doctor added successfully!\n")

def display_single_doctor(doctor):
    print("-----------Doctor's Details-------------")
    print("Doctor ID:", doctor["doctor_id"])
    print("Name:", doctor["name"])
    print("Specialization:", doctor["specialization"])
    print("Experience:", doctor["experience"], "years")
    print("Consultation Fee:", doctor["consultation_fee"])
    print("------------------------------------")

def display_doctors():
    if len(doctors) == 0:
        print("No registered doctors")
    else:
        print("------------Doctors List-------------")
        for doctor in doctors:
            display_single_doctor(doctor)

def search_doctor():
    try:
        doctor_id = int(input("Enter Doctor ID to search: "))
        for doctor in doctors:
            if doctor["doctor_id"] == doctor_id:
                print("Doctor Found! ✅")
                display_single_doctor(doctor)
                return doctor
        print("Doctor Not Found! 👎🏻")
        return None
    except ValueError:
        print("❌ Invalid input. Please enter a numeric Doctor ID.")


appointments = []

def book_appointment():
    try:
        patient_id = int(input("Enter Patient ID: "))
        doctor_id = int(input("Enter Doctor ID: "))
        date = input("Enter Appointment Date (DD/MM/YYYY): ")
        time = input("Enter Appointment Time (HH:MM): ")

        # Find doctor details
        doctor = None
        for d in doctors:
            if d["doctor_id"] == doctor_id:
                doctor = d
                break

        if doctor is None:
            print("❌ Doctor not found!")
            return

        appointment = {
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "date": date,
            "time": time,
            "consultation_fee": doctor["consultation_fee"]  # auto‑store fee
        }
        appointments.append(appointment)
        print("\n✅ Appointment booked successfully!\n")

        # Immediately generate bill
        generate_bill(appointment)

    except ValueError:
        print("❌ Invalid input. Please enter correct values.")

def view_appointments():
    if len(appointments) == 0:
        print("No appointments booked yet.")
    else:
        print("------------Appointments List-------------")
        for appt in appointments:
            print("Patient ID:", appt["patient_id"], "| Doctor ID:", appt["doctor_id"],
                  "| Date:", appt["date"], "| Time:", appt["time"])

def generate_bill(appointment=None):
    try:
        if appointment is None:
            print("❌ No appointment data provided.")
            return

        patient_id = appointment["patient_id"]
        doctor_id = appointment["doctor_id"]
        consultation_fee = appointment["consultation_fee"]

        medicine_charge = float(input("Enter Medicine Charges: "))
        lab_charge = float(input("Enter Lab Charges: "))
        room_charge = float(input("Enter Room Charges: "))

        total = consultation_fee + medicine_charge + lab_charge + room_charge

        if total >= 10000:
            discount = total * 0.10
        elif total >= 5000:
            discount = total * 0.05
        else:
            discount = 0

        final_amount = total - discount

        print("\n----------- BILL -----------")
        print("Patient ID:", patient_id)
        print("Doctor ID:", doctor_id)
        print("Consultation Fee: ₹", consultation_fee)
        print("Medicine Charges: ₹", medicine_charge)
        print("Lab Charges: ₹", lab_charge)
        print("Room Charges: ₹", room_charge)
        print("Total Amount: ₹", total)
        print("Discount: ₹", discount)
        print("Final Payable: ₹", final_amount)
        print("----------------------------")
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")



while True:
    print("\nWELCOME TO PEACE HOSPITAL")
    print("1. Register Patient")
    print("2. Display Patients")
    print("3. Search Patient")
    print("4. Add Doctor")
    print("5. Display Doctors")
    print("6. Search Doctor")
    print("7. Book Appointment")
    print("8. View Appointments")
    print("9. Generate Bill")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        display_patients()
    elif choice == "3":
        search_patient()
    elif choice == "4":
        add_doctor()
    elif choice == "5":
        display_doctors()
    elif choice == "6":
        search_doctor()
    elif choice == "7":
        book_appointment()
    elif choice == "8":
        view_appointments()
    elif choice == "9":
        generate_bill()
    elif choice == "10":
        print("Exiting system... Goodbye!")
        break
    else:
        print("❌ Invalid choice, please try again.")
