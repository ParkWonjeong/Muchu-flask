from flask import Flask, Response

app = Flask(__name__)


# 검색 함수 설정
@app.route('/search', method=['POST'])
def search():
    # 검색 단어 벡터화 진행
    # 만약 단어가 사전에 없어 오류가 발생 한다면
    return Response('존재 하지 않는 단어 입니다.', 400)

    # 유사도 검사 진행
    # 만약 모델 및 서버 내부 오류 발생 시
    return Response('서버 내부 에러 입니다.', 500)

    # 적절한 단어가 들어와 유사도 진행도 완료 시
    response = {
        # 상위 20개 정도의 이미지 파일 항목값 혹은 해당 파일 이미지
    }
    return response, 200
