from flask import Flask,request,jsonify
import requests
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
sentiment_analysis_service_url = 'https://flask-server-sentiment-analysis-1.onrender.com' 
@app.route('/analyze', methods=['POST'])
def analyze():
    data=request.get_json()# converts stringified POST data to key value pair
    print(data[0])

    response=requests.post(sentiment_analysis_service_url,json=data)
    if response.status_code==200:
        sentiments=response.json()['averages']
        return jsonify({'status':'success','sentiments':sentiments})
    else:
        return jsonify({'status':'failure','message':'failed to get sentiment analysis results'})
    #return jsonify({'status': 'success', 'received_data': data})
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
#__name__ is a special variable and when the code is run directly its value is set to __main__

