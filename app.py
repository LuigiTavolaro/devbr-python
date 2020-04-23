from flask import Flask, jsonify, Response
from applicationinsights.flask.ext import AppInsights

app = Flask(__name__)
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = 'e6d450e4-8fc3-4084-a16b-7bd798c6fd0e'
appinsights = AppInsights(app)


def factors(num):
  return [x for x in range (1, num+1) if num%x==0]
# @app.route('/',methods=['GET'])
# def table():
#     return 'olá mundo'

# force flushing application insights handler after each request
@app.after_request
def after_request(response):
    appinsights.flush()
    return response    


@app.route('/')
def home():
  return '<a href="/factor_raw/100"> click here for an example</a>'
  
@app.route('/factor_raw/<int:n>')
def factors_display_raw_html(n):
  list_factor = factors(int(n))
  # adding "n" and placed at the top
  html = "<h1> Factors of "+str(n)+" are</h1>"+"\n"+"<ul>"
  # make a <li> item for every output (factor)
  for f in list_factor:
    html += "<li>"+str(f)+"</li>"+"\n"
  html += "</ul> </body>" # closes tag at the end
  return html



if __name__ == '__main__':
    app.run(debug=True)