from flask import Flask, render_template, request

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/team-selector")
def subject_selector():
    return render_template("team-selector.html")

@app.route('/team-selector', methods = ["GET", "POST"])
def puller():
    if request.method == "POST":
        team: str = request.form['team']
        year: str = request.form['year']
        file_name: str = team + year
        team_data_file = open(f"static/team_data/{file_name}", "r")
        data: str = team_data_file.read()
        team_data_file.close()
        return render_template("image.html", file_name = file_name, team_data = data)
    return render_template("team-selector.html")

if __name__ == '__main__':
    app.run(debug = True)