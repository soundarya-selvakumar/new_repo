from flask import Flask
import boto3


app = Flask(__name__)


@app.route('/')
def hello():
    s3 = boto3.client('s3',aws_access_key_id='AKIAZLEX3ECSXEJ4QGVO',aws_secret_access_key='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')
    contents = []
    for item in s3.list_objects_v2(Bucket='1557-test-bucket')['Contents']:
        contents.append(item)
    str_ret = str(contents)
    return str_ret

if __name__ == '__main__':
    app.run()