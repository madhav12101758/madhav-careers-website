from flask import Flask,render_template,jsonify

app=Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Banglore,India',
    'salary':'Rs.15,00,00'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi,India',
    'salary':'Rs.40,00,00'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'Rs.20,00,00'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco,USA',
    'salary':'$120,000'
  }
]
@app.route('/')
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name=' THE OASIS')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
  
  