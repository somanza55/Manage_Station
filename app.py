from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template("index.html")


@app.route('/map_brand')
def map_brand():    
    return render_template("map_brand.html")

@app.route('/check_coupon')
def check_coupon():    
    return render_template("check_coupon.html")

@app.route('/station')
def station():    
    return render_template("station.html")

@app.route('/list_station')
def list_station():    
    return render_template("station_list.html")

@app.route('/export_tax')
def export_tax():    
    return render_template("export_tax.html")   

@app.route('/snake')
def snake():    
    return render_template("snake.php")

if __name__ =="__main__":
    app.run(debug=True)