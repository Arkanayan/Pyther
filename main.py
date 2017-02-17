from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['city_name']
        if city_name is not None:
            result = []
            error = True
            from checkWeather import checkWeather
            temp, pressure, humidity, localtime, country = checkWeather(city_name)
            if temp is not None:
                error = False
                result = {'temp': temp, 'pressure': pressure, 'humidity': humidity, 'localtime': localtime, 'country': country }
            return render_template('index.html', result=result, error=error )
    
    return render_template('index.html', result=None, error=False)


if __name__ == '__main__':
    app.run(debug=True)