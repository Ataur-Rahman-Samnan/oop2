from abc import ABC, abstractmethod

# Person class (Base class)
class Person(ABC):
    def __init__(self, id, name, age, gender):
        self._id = id
        self._name = name
        self._age = age
        self._gender = gender
    
    @abstractmethod
    def get_details(self):
        pass
    
    # # Encapsulation er use hoise getter method er moddhe
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender

# Patient class Inheritance
class Patient(Person):
    def __init__(self, id, name, age, gender, ailment, doctor_id=None):
        super().__init__(id, name, age, gender)
        self._ailment = ailment
        self._doctor_id = doctor_id

    # ekhane polymorphism 
    def get_details(self):
        return f"Patient[ID={self._id}, Name={self._name}, Age={self._age}, Gender={self._gender}, Ailment={self._ailment}, DoctorID={self._doctor_id}]"

    def get_ailment(self):
        return self._ailment
    
    def get_doctor_id(self):
        return self._doctor_id

# Doctor class Inheritance
class Doctor(Person):
    def __init__(self, id, name, age, gender, specialty):
        super().__init__(id, name, age, gender)
        self._specialty = specialty

    # ekhane polymorphism
    def get_details(self):
        return f"Doctor[ID={self._id}, Name={self._name}, Age={self._age}, Gender={self._gender}, Specialty={self._specialty}]"

    def get_specialty(self):
        return self._specialty

# Hospital 
class Hospital:
    def __init__(self):
        self._patients = []
        self._doctors = []

    def add_patient(self, patient):
        self._patients.append(patient)

    def add_doctor(self, doctor):
        self._doctors.append(doctor)

    def get_patient(self, patient_id):
        for patient in self._patients:
            if patient.get_id() == patient_id:
                return patient
        return None

    def get_doctor(self, doctor_id):
        for doctor in self._doctors:
            if doctor.get_id() == doctor_id:
                return doctor
        return None

    def list_patients(self):
        return [patient.get_details() for patient in self._patients]

    def list_doctors(self):
        return [doctor.get_details() for doctor in self._doctors]

    def display_doctors(self):
        for doctor in self._doctors:
            print(doctor.get_details())

# user er input
def add_new_patient(hospital):
    try:
        id = int(input("\nEnter patient ID: "))
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        gender = input("Enter patient gender (Male/Female): ")
        ailment = input("Enter patient ailment: ")

        # Choosing doctor
        print("\nAvailable Doctors:")
        hospital.display_doctors()
        doctor_id = None
        while True:
            try:
                doctor_id_input = input("Enter the ID of the doctor for the appointment (or press Enter to skip): ")
                if doctor_id_input == "":
                    break
                doctor_id = int(doctor_id_input)
                if hospital.get_doctor(doctor_id) is not None:
                    break
                else:
                    print("Invalid doctor ID. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid doctor ID or press Enter to skip.")
        
        new_patient = Patient(id, name, age, gender, ailment, doctor_id)
        hospital.add_patient(new_patient)
        print("Patient added successfully!")
    except ValueError as e:
        print(f"Invalid input: {e}")

# Example 
if __name__ == "__main__":
    # hospital nam er instance/object
    hospital = Hospital()

    # doctor sob 
    doctor1 = Doctor(1, "Dr. Rowshon Ara", 45, "Female", "Cardiology")
    doctor2 = Doctor(2, "Dr. Ullash", 50, "Male", "Neurology")
    doctor3 = Doctor(3, "Dr. Tahsan", 39, "Male", "Pediatrics")
    doctor4 = Doctor(4, "Dr. Akram", 49, "Male", "ENT")
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)
    hospital.add_doctor(doctor3)
    hospital.add_doctor(doctor4)

    while True:
        print("\nWelcome to Our Hospital")
        print("1. Add a new patient")
        print("2. List all patients")
        print("3. List all doctors")
        print("4. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_new_patient(hospital)
        elif choice == '2':
            print("\nPatients in the hospital:")
            for patient_details in hospital.list_patients():
                print(patient_details)
        elif choice == '3':
            print("\nDoctors in the hospital:")
            for doctor_details in hospital.list_doctors():
                print(doctor_details)
        elif choice == '4':
            print("\nExiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
