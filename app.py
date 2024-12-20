from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/land')
def land():
    return render_template('land.html')

@app.route('/land/history')
def history():
    return render_template('history.html')

@app.route('/land/developments')
def developments():
    return render_template('developments.html')

@app.route('/past_rulers')
def past_rulers():
    return render_template('past_rulers.html')

@app.route('/baale_profile')
def baale_profile():
    return render_template('baale_profile.html')

@app.route('/baale/palace')
def baale_palace():
    return render_template('baale_palace.html')

@app.route('/chiefs')
def chiefs():
    return render_template('chiefs.html')

@app.route('/chiefshons')
def chiefshons():
    return render_template('chiefshons.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/land_rectification')
def land_rectification():
    return render_template('land_rectification.html')

@app.route('/cda')
def cda():
    return render_template('cda.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run() 
