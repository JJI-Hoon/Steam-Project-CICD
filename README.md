# ✅ CI/CD Architecture - 인디안 프로젝트
![](https://velog.velcdn.com/images/jjjjj/post/7ae60992-c219-4a39-957d-bec648067cc5/image.png)

> CI/CD Architecture 그림을 Draw.io를 활용해서 작성


# ✅ CI/CD 작업 순서

> 1. API, DEV Branch에 개발 내용이 푸쉬가 필요
2. 해당 레포지를 나의 레포지로 Fork 진행
3. 레포지 Clone 진행 및 Docker Image Build (버전 관리 파일인 Requirements.txt → Api Requirements로 진행 / Issue 가능성 있음)
4. 생성된 Image를 GCR에 Push
5. VM Instance 생성 및 GCR의 이미지 VM에 Push
6. Github Action에 필요한 Key 값들 GCP에서 가져와야 함
7. 추가적으로, Slack Webhook Key 역시 필요
8. 모든 Keys가 깃헙 레포지에 추가된다면, dev 브랜치에 푸쉬하여 깃헙 액션이 잘 작동하는 확인
9. Action 진행 현황 파악 및 배포 완료 시 성공


# CI/CD 작업 순서

## 1. Dockerfile 구축 및 Docker Image 빌드

- Dockerfile

> 1. Backend
2. Frontend


```python
FROM python:3.8.5-slim-buster

RUN mkdir steamrec

COPY start.sh /steamrec/start.sh
COPY /backend /steamrec/backend
COPY /frontend /steamrec/frontend
COPY requirements.txt /steamrec/requirements.txt

RUN pip install --upgrade pip \ 
&& pip install -r /steamrec/requirements.txt

WORKDIR /steamrec

EXPOSE 8001
CMD ["sh", "start.sh"]
```

## 2. Image → GCR Push

- GCR API 이용 허용 필요

## 3. VM Instance 생성 및 서비스 계정 생성 필요

- GCP Console에서 작업
- 서비스 계정 생성 후 키 값 생성 필요
- 이후, 권한 부여 작업도 필요


## 4. Git Repository Secrets에 KEY 값 등 설정

![](https://velog.velcdn.com/images/jjjjj/post/535b123a-9383-4870-a8bf-0fdbc1560864/image.png)


## 5. ✅ Git workflow 작성

- **어려웠던 점** : Github Action 실행 과정에 있어서 gcloud 환경을 세팅하는데 있어서 Python의 버전 충돌로 인한 에러를 마주하여 원인을 학습하는 부분에 고충을 겪음
- **해결 과정** : 학습을 통해 CI/CD를 진행하는데 있어서 Cloud환경과 사용하는 언어의 버전을 맞춰줘야 함을 알 수 있었고, Workflow에 Python 버전을 업데이트 하는 과정을 통해 해결함

```python

   # Python 버전 관리 및 gcloud CLI 설정
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
          
      - uses: google-github-actions/setup-gcloud@v0
        with:
          version: '318.0.0'
          service_account_key: ${{ secrets.SERVICE_ACCOUNT_KEY }}
          project_id: ${{ secrets.GCP_PROJECT_ID }}
```

# CICD 환경 구동 자료

- Github Action 작동

![](https://velog.velcdn.com/images/jjjjj/post/932bb92a-e645-4de3-9679-10a291a8f777/image.png)

- Slack Team 채널에 알림

![](https://velog.velcdn.com/images/jjjjj/post/b59076c8-b751-4c2a-bc7a-daa49e1a124a/image.png)

