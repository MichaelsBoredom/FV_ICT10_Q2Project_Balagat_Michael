from pyscript import display, document

clubs = {
    "marching_band": {
        "Name": "Marching Band",
        "Category": "Music",
        "Description": "A club for students passionate about music and marching performances.",
        "Meeting Time": "Tuesday and Wednesday, 3:00 PM - 4:30 PM",
        "Location": "Band Room",
        "Club Moderator": "Mr. Emilio Alumno",
        "Number of Members": 25
    },
    "glee_club": {
        "Name": "Glee Club",
        "Category": "Music",
        "Description": "A club for students who love singing and performing.",
        "Meeting Time": "Monday, 3:00 PM - 5:00 PM",
        "Location": "High School Music Room",
        "Club Moderator": "Mr. Denver Martin",
        "Number of Members": 20
    },
    "dance_club": {
        "Name": "Dance Club",
        "Category": "Performing Arts",
        "Description": "A club for students who enjoy dancing and choreography.",
        "Meeting Time": "Tuesday, 3:00 PM - 5:00 PM",
        "Location": "Teatro Preciosa",
        "Club Moderator": "Mr. Alfred Cases",
        "Number of Members": 30
    },
    "math_club": {
        "Name": "Math Club",
        "Category": "Academic",
        "Description": "A club for students who love solving math problems and puzzles.",
        "Meeting Time": "Monday, 2:30 PM - 3:00 PM",
        "Location": "Room 404",
        "Club Moderator": "Mr. Nicole Gabuya",
        "Number of Members": 15
    },
    "science_club": {
        "Name": "Science Club",
        "Category": "Academic",
        "Description": "A club for students passionate about science experiments and discoveries.",
        "Meeting Time": "Tuesday, 3:00 PM - 4:00 PM",
        "Location": "Room 404",
        "Club Moderator": "Ms. Jameelyn Maramag",
        "Number of Members": 20
    },
    "communications_arts_club": {
        "Name": "Communications Arts Club",
        "Category": "Creative Arts",
        "Description": "A club for students who enjoy creative writing and public speaking.",
        "Meeting Time": "Wednesday, 3:00 PM - 4:00 PM and Friday, 3:00 PM - 4:00 PM",
        "Location": "Room 406",
        "Club Moderator": "Ms. Yannis Fernandez",
        "Number of Members": 18
    },
    "cocc": {
        "Name": "COCC (Cadet Officer Candidate Course)",
        "Category": "Leadership",
        "Description": "A club for students who wants to participate in leadership and military training.",
        "Meeting Time": "Wednesday, 2:30 PM - 4:30 PM",
        "Location": "Quadrangle/Teatro Preciosa",
        "Club Moderator": "SSgt. Jemima David PA (Res)",
        "Number of Members": 35
    },
    "social_studies_club": {
        "Name": "Social Studies Club",
        "Category": "Academic",
        "Description": "A club for students who enjoy learning about history and culture.",
        "Meeting Time": "Tuesday, 3:00 PM - 4:00 PM",
        "Location": "Room 409",
        "Club Moderator": "Ms. Yannis Fernandez",
        "Number of Members": 22
    },
    "volleyball_varsity": {
        "Name": "Volleyball Varsity",
        "Category": "Sports",
        "Description": "A varsity team for students who love playing volleyball.",
        "Meeting Time": "Wednesday, 3:00 PM - 4:00 PM",
        "Location": "Quadrangle",
        "Club Moderator": "Mr. Adrian Ruiz",
        "Number of Members": 12
    },
    "basketball_varsity": {
        "Name": "Basketball Varsity",
        "Category": "Sports",
        "Description": "A varsity team for students who love playing basketball.",
        "Meeting Time": "Monday, 3:00 PM - 4:00 PM",
        "Location": "Quadrangle",
        "Club Moderator": "Mr. Adrian Ruiz",
        "Number of Members": 15
    }
}


def display_club_info(e):
    try:
        e.preventDefault()  # Prevent the default form submission behavior

        print("Button clicked. Function triggered.")  # Debugging output

        selected_club = document.getElementById("club-select").value

        if selected_club in clubs:
            club_info = clubs[selected_club]
            output = (
                f"<h3>{club_info['Name']}</h3>"
                f"<p><b>Category:</b> {club_info['Category']}</p>"
                f"<p><b>Description:</b> {club_info['Description']}</p>"
                f"<p><b>Meeting Time:</b> {club_info['Meeting Time']}</p>"
                f"<p><b>Location:</b> {club_info['Location']}</p>"
                f"<p><b>Club Moderator:</b> {club_info['Club Moderator']}</p>"
                f"<p><b>Number of Members:</b> {club_info['Number of Members']}</p>"
            )
        else:
            output = "<p>Please select a valid club.</p>"

        # Displays the output in the designated HTML element
        document.getElementById("club.info").innerHTML = output
    except Exception as ex:
        document.getElementById("club.info").innerHTML = "<p>An error occurred while displaying club information.</p>"
        display(f"Unexpected Error: {ex}", target="output")  # Fallback error display
