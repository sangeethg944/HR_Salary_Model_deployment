import ml_model
from flask import Flask, request, render_template

app = Flask(__name__,template_folder="templates")

@app.route('/')
def home():
    return render_template('front.html')

# Route 'classify' accepts GET request
@app.route('/classify',methods=['POST','GET'])
def classify_type():
        d1 = request.args.get('age') # Get parameters for age
        d2 = request.args.get('hours_per_week') # Get parameters for working hours per week
        d3 = request.args.get('work_class') # Get parameters for working class
        d4 = request.args.get('edu_class') # Get parameters for education class
        d5 = request.args.get('marital_status') # Get parameters for marital status
        d6 = request.args.get('prev_occu') # Get parameters for previous occupation
        d7 = request.args.get('relation_status') # Get parameters for relation_status
        d8 = request.args.get('race') # Get parameters for race
        d9 = request.args.get('sex') # Get parameters for sex
        d10 = request.args.get('native_country') # Get parameters for native_country

        # Get the output from the classification model
        variety = ml_model.classify(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10)
        #print(variety)
        # Render the output in new HTML page
        return render_template('result.html', Income=variety)


# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=True)