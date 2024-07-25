# kim_args_history
- parquet 파일의 정보를 cli 기반으로 조회

### 사용법
```
$ my-history -s ls
ls 사용 횟수는 1234회 입니다.

$ my-history -t 10 -d 2024-07-17
  cmd  cnt
pyenv 4256
   cd 3472
  git 3396
mkdir 1932
  pip 1592
  cat 1368
   vi 1356
 sudo 1320
  pdm 1220
   rm 1104
```

### Dev env setting
```
$ git clone <URL>
$ cd <PJT_NAME>
$ pyenv virtualenv 3.11.9 clean 
$ pyenv global clean 
$ rm -rf .venv
$ pdm venv create
$ source .venv/bin/activate
$ pdm install
$ pdm list
$ pytest

# option
$ pdm add -dG test pytest pytest-cov
```

### deploy
```bash
# dev branch
$ pip install git+https://github.com/rlaehgus97/kim_args_history.git@0.2.0/args

# main 
pip install git+https://github.com/rlaehgus97/kim_args_history.git@main
```

### reference
https://pdm-project.org/en/latest/usage/dependency/

### 주의사항
git push 하기전 git status로 swp파일 있는지 확인 (tmp파일을 굳이 push할 필요 없다)
gitignore에 해당 파일을 추가해서 제거하는 방법도 있다
