import os
import sys  # 한글 출력 인코딩에 사용
import io  # 한글 출력 인코딩에 사용
import openai  # OpenAI 라이브러리 사용
from openai import OpenAI
from dotenv import load_dotenv

# 한글 출력 인코딩 설정 (콘솔 출력 시 한글 처리)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 환경 변수에서 API 키 로드
load_dotenv()

# OpenAI API 키 설정
openai.api_key = os.getenv('OPENAI_API_KEY')

# Prompt 템플릿 정의
prompt_template = """
너는 친절하고 능숙한 AI 바텐더야. 
손님의 취향을 들으면 그에 맞는 칵테일을 추천할 수 있어.
칵테일 말고는 추천을 하지 못해.

# 손님의 주문:
{user_tasts}

# 추천 칵테일:
"""

# 손님 질문 받기 (백엔드에서 전달된 sys.argv[1]로 받음)
if len(sys.argv) > 1:
    user_tasts = sys.argv[1]
else:
    user_tasts = "아무런 질문이 전달되지 않았습니다."

# 프롬프트 생성
prompt = prompt_template.format(user_tasts=user_tasts)

# OpenAI 모델을 사용하여 답변 생성

client = OpenAI()

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",  # 사용할 모델 (gpt-4로 변경 가능)
    messages=[{"role": "system", "content": "너는 AI 바텐더야."},
              {"role": "user", "content": prompt}],
    temperature=0.7  # 답변의 창의성 설정
)


# 응답에서 'content'만 추출
bot_response = response.choices[0].message.content

# 백엔드로 출력 (stdout으로 출력하여 백엔드가 이를 수신)
print(bot_response)