import os
from gensim.models import word2vec

from flask import Flask,render_template, request,json,jsonify

#this part to get the absloute path to our model file
import sys
from imp import reload
reload(sys)
sys.setdefaultencoding('utf8')
#type here the model name you have during kaggle's tutorial.
model_name = "300features_40minwords_10context.gensim"
my_dir = os.path.dirname(__file__)
model_file_path = os.path.join(my_dir, model_name)
model = word2vec.Word2Vec.load(model_file_path)

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/ajaxhandler', methods=['POST'])
def ajax_handler():
    first =  request.form['first']
    second = request.form['second']
    third= request.form['third']
    fourth =request.form['fourth']
    result = model.doesnt_match (("%s %s %s %s"%(first,second,third,fourth)).split())
    return jsonify({'result':result  })


if __name__=="__main__":
    app.run()
