from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})




#새로운 영화 데이터를 저장하는 API(약속)
@app.route('/new', methods=["POST"])
def test_new():

   #rank 받기
   rank_receive = int(request.form['rank_give'])

   #title 받기
   title_receive = request.form['title_give']

   #star 받기
   star_receive = request.form['star_give']

   #rank, title, star 임시 딕셔너리 생성
   doc = {
      'rank':rank_receive,
      'title':title_receive,
      'star':star_receive
   }

   #임시 딕셔너리를 movies 콜렉션에 저장
   db.movies.insert_one(doc)

   return jsonify({'status':'success'})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)