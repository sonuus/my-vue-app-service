import boto3
import os
import sys
import json
from flask import request, Response,jsonify,Flask
from ssm_cache import SSMParameter

app = Flask(__name__)

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') if os.environ.get('AWS_ACCESS_KEY_ID') is not None else None
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') if os.environ.get('AWS_SECRET_ACCESS_KEY') is not None else None

@app.route('/')
def hello_world():    
    return "Hell0 -->>>>>>>>>>>>>>>>>>"


@app.route('/xxx')
def get_s3_buckets():
    s3 = boto3.resource('s3')
    # Print out bucket names
    lst=[]
    for bucket in s3.buckets.all():
        print(bucket.name)
        lst.append(bucket.name + "  777777777")
    return jsonify({'buckets':lst})

@app.route('/ppp')
def get_param_name_val():
    param = SSMParameter('prod.app1.db-user')
    value = param.value
    return jsonify({"prod.app1.db-user":value})

    

@app.route('/api')
def rest_hello_world():
    return '{"id":1,"message":"Flask: Hello World from Docker"}'

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0',port=80)

    # if os.environ.get('IS_AWS_ENV'):
    #     app.run(debug=True, host='0.0.0.0',port=80)
    # else:
    #     app.run(port=5000)









