# kim_args_history

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

### 주의사항
git push 하기전 git status로 swp파일 있는지 확인 (tmp파일을 굳이 push할 필요 없다)
gitignore에 해당 파일을 추가해서 제거하는 방법도 있다
