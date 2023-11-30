from flask import Flask, Response, request, jsonify
from gensim.models import Word2Vec

app = Flask(__name__)

# 모델 설정 하는 공간
muchu_model = Word2Vec.load("경로 설정")


# 검색 함수 설정
@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()

    # 만약 단어가 사전에 존재 하지 않을 시
    if 'word' not in data:
        return jsonify({'error': '단어를 입력해 주세요.'}), 400

    word = data['word']

    # 검색 단어 벡터화 진행
    try:
        vector = muchu_model.wv[word]
        return jsonify({'word': word, 'vector': vector.tolist()})
    except KeyError:
        return jsonify({'error': f'존재 하지 않는 단어 입니다.'}), 404
    # 유사도 검사 진행
    # 만약 모델 및 서버 내부 오류 발생 시
    return Response('서버 내부 에러 입니다.', 500)

    # 적절한 단어가 들어와 유사도 진행도 완료 시
    response = {
        # 상위 20개 정도의 이미지 파일 항목값 혹은 해당 파일 이미지
    }
    return response, 200


if __name__ == '__main__':
    app.run(debug=True)
