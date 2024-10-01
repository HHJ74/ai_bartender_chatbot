import os
import sys  # 한글 출력 인코딩에 사용
import io  # 한글 출력 인코딩에 사용
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

# 한글 출력 인코딩 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 환경 변수에서 API 키 로드
load_dotenv()

# Google Generative AI API 키 설정
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')


# Google Generative AI 모델 로딩
llm = GoogleGenerativeAI(model='gemini-pro', temperature=0.7)

# LangChain의 PromptTemplate 사용하여 템플릿 정의
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

# LangChain에서 사용할 프롬프트 생성
prompt = prompt_template.format(user_tasts=user_tasts)

# LLM을 사용하여 프롬프트에 대한 답변 생성
response = llm(prompt)

# 백엔드로 출력 (stdout으로 출력하여 백엔드가 이를 수신)
print(response)
