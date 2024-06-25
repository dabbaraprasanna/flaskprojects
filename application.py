from flask import Flask,render_template
FAI=Flask(__name__)
@FAI.route('/shiva')

def shiva():
    return 'great god'

@FAI.route('/hi')
def hi():
    return render_template('hi.html',name='chitti')

FAI.run(debug=True,host='127.0.0.1',port=5000)