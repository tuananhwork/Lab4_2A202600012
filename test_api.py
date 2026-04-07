import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Nạp các biến môi trường từ file .env
load_dotenv()

# Lấy các giá trị đã cấu hình để không gọi vào OpenAI thật
base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
model_default = os.getenv("MODEL_DEFAULT")

# Khởi tạo mô hình ChatOpenAI với BASE_URL trỏ tới server API giả lập
llm = ChatOpenAI(
    model=model_default,
    api_key=api_key,
    base_url=base_url
)

print("Gọi API...")
response = llm.invoke("Xin chào?")
print("AI trả lời:", response.content)
