from flask import Flask
app = Flask(__name__)

@app.route('/page2')
def html():
  return '<p>�ȳ��ϼ���!!</p>'

if __name__ == '__main__':
  app.run()
