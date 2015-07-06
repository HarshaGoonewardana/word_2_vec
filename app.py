#import os
from gensim.models import word2vec

from flask import Flask,render_template, request,json,jsonify


model_name = "300features_40minwords_10context.gensim"
# model.save(model_name)
# 
# print model.most_similar("man")


model =word2vec.Word2Vec.load(model_name)


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

#@app.route('/signUp')
#def signUp():
#    return render_template('index.html')

@app.route('/ajaxhandler', methods=['POST'])
def ajax_handler():
    first =  request.form['first']
    second = request.form['second']
    third= request.form['third']
    fourth =request.form['fourth']
#    model_name ="300features_40minwords_10context"
#    model =word2vec.Word2Vec.load(model_name)
    result = model.doesnt_match (("%s %s %s %s"%(first,second,third,fourth)).split())
    return jsonify({'result':result  })


if __name__=="__main__":
    app.run()
