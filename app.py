from flask import Flask, render_template, request

app: Flask = Flask(__name__)
file_name: str

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/team-selector")
def subject_selector():
    return render_template("team-selector.html")

@app.route('/team-selector', methods = ["GET", "POST"])
def puller():
    global file_name
    
    if request.method == "POST":
        team: str = request.form['team']
        year: str = request.form['year']
        if team == "arsenal":
            if year == "2022-23":
                return render_template("arsenal22-23.html")
                # TODO: Update the HTML path for the specific image
                # file_name = "arsenal22-23"
            if year == "2021-22":
                return render_template("arsenal21-22.html")
                # TODO: Update the HTML path for the specific image
                # b: str = "arsenal21-22"
            if year == "2020-21":
                return render_template("arsenal20-21.html")
                # TODO: Update the HTML path for the specific image
                # c: str = "arsenal20-21"
            if year == "2019-20":
                return render_template("arsenal19-20.html")
                # TODO: Update the HTML path for the specific image
                # d: str = "arsenal19-20"
        if team == "chelsea":
            if year == "2022-23":
                return render_template("chelsea22-23.html")
            if year == "2021-22":
                return render_template("chelsea21-22.html")
            if year == "2020-21":
                return render_template("chelsea20-21.html")
            if year == "2019-20":
                return render_template("chelsea19-20.html")
        if team == "liverpool":
            if year == "2022-23":
                return render_template("liverpool22-23.html")
            if year == "2021-22":
                return render_template("liverpool21-22.html")
            if year == "2020-21":
                return render_template("liverpool20-21.html")
            if year == "2019-20":
                return render_template("liverpool19-20.html")
        if team == "manchester_city":
            if year == "2022-23":
                return render_template("manchester_city22-23.html")
            if year == "2021-22":
                return render_template("manchester_city21-22.html")
            if year == "2020-21":
                return render_template("manchester_city20-21.html")
            if year == "2019-20":
                return render_template("manchester_city19-20.html")
    return render_template("team-selector.html")

if __name__ == '__main__':
    app.run(debug = True)