from flask import Flask

app = Flask(__name__)    # create app



@app.route('/')   # this is decoretors
def hello():
    return "<h1>Hellow' World!!aaavbb</h1>"


# NOTE :- F() name should be diffrent
@app.route('/home')   # this is decoretors
def hello1():
    return "<h1>Welcome to sistec Bhopal</h1>"


@app.route('/sistec')
def sistec():
    return """
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <!-- Header with Navbar -->
    <header style="background-color: #333; color: white; padding: 10px 0;">
        <nav style="display: flex; justify-content: center; align-items: center;">
            <ul style="list-style: none; margin: 0; padding: 0; display: flex;">
                <li style="margin: 0 15px;"><a href="#" style="color: white; text-decoration: none;">Home</a></li>
                <li style="margin: 0 15px;"><a href="#" style="color: white; text-decoration: none;">About</a></li>
                <li style="margin: 0 15px;"><a href="#" style="color: white; text-decoration: none;">Academics</a></li>
                <li style="margin: 0 15px;"><a href="#" style="color: white; text-decoration: none;">Departments</a></li>
                <li style="margin: 0 15px;"><a href="#" style="color: white; text-decoration: none;">Campus Life</a></li>
                <li style="margin: 0 15px;"><a href="#" style="color: white; text-decoration: none;">R&D</a></li>
                <li style="margin: 0 15px;"><a href="#" style="color: white; text-decoration: none;">Accreditations</a></li>
                <li style="margin: 0 15px;"><a href="#" style="color: white; text-decoration: none;">NIRF</a></li>
                <li style="margin: 0 15px;"><a href="#" style="color: white; text-decoration: none;">Placements</a></li>
                <li style="margin: 0 15px;"><a href="#" style="color: white; text-decoration: none;">Admissions</a></li>
                <li style="margin: 0 15px;"><a href="#" style="color: white; text-decoration: none;">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Heading for the page -->
    <h1 style="text-align: center; margin: 0;">Sagar Institute of Science and Technology (SISTec)</h1>

    <!-- Centering the image with inline CSS -->
    <div style="display: flex; justify-content: center; align-items: center; height: 70vh;">
        <img src="https://www.sistecgn.ac.in/assets/admin/upload/events//nptel-workshop-and-felicitation-ceremony-img1.jpg" 
             alt="NPTEL Workshop and Felicitation Ceremony" 
             style="width: 80%; height: 80%; object-fit: cover;">
    </div>
    <div style="display: flex; justify-content: center; align-items: center; height: 70vh;">
     <img src="static/nptel-workshop-and-felicitation-ceremony-img1.jpg"  style="width: 80%; height: 80%; object-fit: cover;" >
    </div>


"""


if __name__=="__main__":
    app.run(debug=True)