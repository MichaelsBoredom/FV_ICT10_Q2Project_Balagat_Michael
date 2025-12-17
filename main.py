from pyscript import display, document

def general_weighted_average(e):
    try:
        e.preventDefault()  # Prevent the default form submission behavior

        print("Button clicked. Function triggered.")  # Debugging output

        subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']

        first_name = document.getElementById('first_name').value
        last_name = document.getElementById('last_name').value

        grades = {
            'Science': float(document.getElementById('science').value),
            'Math': float(document.getElementById('math').value),
            'English': float(document.getElementById('english').value),
            'Filipino': float(document.getElementById('filipino').value),
            'ICT': float(document.getElementById('ict').value),
            'PE': float(document.getElementById('pe').value)
        }

        weighted_sum = sum(grades[subject] * weight for subject, weight in zip(subjects, [5, 5, 5, 3, 2, 1]))
        total_units = sum([5, 5, 5, 3, 2, 1])
        gwa = weighted_sum / total_units

        summary = "\n".join([f"{subject}: {grades[subject]:.0f}" for subject in subjects])

        display(f'Name: {first_name} {last_name}', target="student_info")
        display(f"Grades:\n{summary}\nYour general weighted average is {gwa:.2f}", target='output')
    except ValueError as ve:
        display("Please enter valid numeric grades for all subjects.", target='output')
        print(f"ValueError: {ve}")  # Debugging output
    except Exception as ex:
        display("An unexpected error occurred.", target='output')
        print(f"Unexpected Error: {ex}")  # Debugging output