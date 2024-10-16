# Dockerfile

# 1. 기본 베이스 이미지로 Python 3.9 사용
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 파일을 컨테이너에 복사하고 설치
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 4. 애플리케이션 파일을 컨테이너로 복사
COPY . .

# 5. 컨테이너가 실행될 때 실행할 명령어 정의
CMD ["python", "app.py"]
