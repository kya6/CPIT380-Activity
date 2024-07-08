import urllib.parse

# Define Mohammad's Info
name = "Mohammad Alkhayat"
picture = "MOX.jpg" 
career = "IT Junior | 3D Animator | Designer"
interests = ["Web Dev", "UI/UX", "Photography"]
email = "malkhayyt@stu.kau.edu.sa"
x = "https://x.com/ALKHIA6"
linktree = "https://linktr.ee/KHYA6"

# Create Tags
custom_topic_title = "Best Projects"
custom_topic_items = []
custom_topic_items += ["CPIT240 | Summer Activity Center : The project aims to make a database structure for Summer Activity Center, which includes all participants info, activities info, instructors, and departments."]
custom_topic_items += ["CPIT370 | Computer Networking : The project aims to make a network infrastructure for 4 rooms in a building, including the definition of all hardware devices used for it."]
custom_topic_items += ["CPIS334 | Building a Smart Home : The project aims to manage a software business project that provides smart home parts, we considered risks, costs, outcomes, and time."]

# Create Contact Info
email_link = f"mailto:{urllib.parse.quote(email)}"
x_link = urllib.parse.quote(x)
linktree_link = urllib.parse.quote(linktree)

# Create the HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}'s Profile</title>
    <style>
        body {{
            font-family: OCR A Extended;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 150vh;
        }}
        .profile-container {{
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            max-width: 400px;
            text-align: center;
        }}
        .profile-container img {{
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
        }}
        .profile-container h1 {{
            margin: 10px 0;
            font-size: 24px;
        }}
        .profile-container p {{
            margin: 5px 0;
            color: #555;
        }}
        .profile-container ul {{
            list-style-type: none;
            padding: 0;
        }}
        .profile-container ul li {{
            background-color: #e7e7e7;
            margin: 5px 0;
            padding: 10px;
            border-radius: 5px;
        }}
        .profile-container a {{
            display: inline-block;
            margin: 10px;
            text-decoration: none;
            color: #0073e6;
        }}
    </style>
</head>
<body>
    <div class="profile-container">
        <img src="{picture}" alt="{name}'s Picture">
        <h1>{name}</h1>
        <p>{career}</p>
        <h3>Interests</h3>
        <ul>
            {''.join(f'<li>{interest}</li>' for interest in interests)}
        </ul>
        <h3>Contact</h3>
        <a href="{email_link}">Email</a>
        <a href="{x}">Twitter</a>
        <a href="{linktree}">Other(Linktree)</a>
        <h3>{custom_topic_title}</h3>
        <ul>
            {''.join(f'<li>{item}</li>' for item in custom_topic_items)}
        </ul>
    </div>
</body>
</html>
"""

# Generating HTML File
with open("profile.html", "w") as file:
    file.write(html_content)
    file.close()

print("HTML file generated by Mohammad Alkhayat </>") # Once the file is done!