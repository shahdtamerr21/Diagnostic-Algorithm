class PatientDiagnosis:
    def __init__(self, symptom1, symptom2, symptom3):
        self.symptom1 = symptom1
        self.symptom2 = symptom2
        self.symptom3 = symptom3

    def diagnose(self):
        if self.symptom1 and self.symptom2:
            condition = "Condition A"
        elif self.symptom1 and not self.symptom2 and not self.symptom3:
            condition = "Condition B"
        elif not self.symptom1 and self.symptom3:
            condition = "Condition C"
        else:
            condition = "Unknown"
        return condition

# Define the set of symptoms
symptom1 = True
symptom2 = False
symptom3 = True

# Create an instance of the PatientDiagnosis class
diagnosis = PatientDiagnosis(symptom1, symptom2, symptom3)

# Perform diagnosis based on symptoms
result = diagnosis.diagnose()

# Output the diagnosis result
print("The most likely medical condition is:", result)

