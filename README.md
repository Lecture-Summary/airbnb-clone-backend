## poetry

---

```bash
# poetry 설치
curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

# 가상환경 생성
poetry init

# 가상환경 패키지 추가
poetry add django

# 가상환경 활성화
poetry shell

# 가상환경 비활성화
exit
```

[poetry 공식문서](https://python-poetry.org/)

`zsh: command not found: poetry` 에러가 발생하면 홈 디렉토리(~)에서 .local/bin 에 poetry 파일이 있는지 확인.

`.zshrc` 파일에 `export PATH=$HOME/.local/bin:$PATH`를 추가할 것
<br/><br/>

## startproject

---

```bash
# 현재 폴더에 config project를 생성한다.
django-admin startproject config .

# 장고 프로젝트 실행
python manage.py runserver

# 마이그레이션 적용
python manage.py migrate
```

- config: project name
- .: directory
