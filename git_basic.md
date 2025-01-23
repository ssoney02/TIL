**버전관리**: 변화를 기록하고 추적

- 각 버전은 이전 버전으로부터의 변경사항을 기록
    
    ex. 버전 3음 전체 내용을 모두 포함하진 x
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/c7050496-98b1-4adc-9ae0-69c2970f2a5d/image.png)
    

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/dbd14b3f-8fd3-4b44-a94d-74d5094ae236/image.png)

---

**git**: 분산 버전 관리 시스템

: 코드의 변경 이력을 기록하고 협업을 원활하게 하는 도구

❗ **버전 = commit**

: 변경된 파일들 저장

- 중앙 집중식: 서버 하나가 전체 버전을 관리 (서버가 터지면 걍 다 날라감)
- 분산식: 버전을 여러 개의 복제된 저장소에 저장 및 관리

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/64ddb6d3-c5ba-479b-a75a-db8323949a55/image.png)

**working directory**: 실제 작업 중인 파일들이 위치하는 영역

**staging area**: working directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역 (대기중인 것, 버전을 작성하자마자 바로 중앙서버에 올라가는 건 x, 한번에 올리기 전까지 대기하는 공간)

**repository**: 버전 이력과 파일들이 영구적으로 저장되는 영역. 모든 버전, 변경이력이 기록됨

→ 중앙서버?

---

### p.77 git의 동작

- **git init**: 로컬 저장소 설정(초기화)  (여기서 버전관리를 시작하겠다고 선전포고하는 것) → git 버전관리를 시작할 디렉토리에서 진행 (이 폴더가 저장공간이 된다~)
- **git add**: 변경사항이 잇는 파일을 staging area에 추가

### commit 생성하기

git config —global [user.email](http://user.email) “”

git config —global [user.name](http://user.name) “”

alias: 별명

➕git config —global [alias.st](http://alias.st) ‘status’ → st를 git status로 (**단축어로**) 쓰겠다

→ git st

치면 바로 git status

git add test.txt test2,txt  하면 여러개 파일 저장됨(test.txt, test2.txt)

한번에 모든 파일을 추가하고 싶은 경우 → **git add .**

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/a7e2cfb1-d03e-4946-9d94-311342bc6e2e/image.png)

→ 상위 폴더의 test.txt가 수정되었다는 뜻

**git add -A** : 내가 작성한 모든 코드들이 다 스테이지로 올라감

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/04168e0b-c1ed-456f-bd35-f7460ad48864/image.png)

현재 위치: scamp_sy/newnew/newnewnew

⇒ 마지막에 modified ../../test.txt → 현재 newnewnew 디렉토리의 상위, 상위 디렉토리의 파일인 test.txt가 수정되었음

⚡git init → 한 디렉토리 안에 여러 git init이 들어가면 안됨..!!

제일 중요한 (업로드할) 파일 하나에만 지정

.gitignore도 그 중요한 디렉토리 안에다 생성

---

<팁>

- 방향키 누르면 내가 위에 썼던 명령어 순서대로 다 뜸
- 대충 비슷한거 쓰고 tab 하면 자동완성 됨

---

git init 취소 → 그냥 gui에서 숨긴폴더 **.git 삭제**하면됨

⚡로컬 디렉토리에 git  init해놓고 git clone 해버리면 git init 안에 git init이 생겨서 꼬여버림..

**git revert**: 특정 commit을 없었던 일로 만드는 작업

- “재설정” → 단일 commit을 실행 취소
- commit 취소한 기록은 남음

:w → 저장한다

:q → 나간다

**—soft**: 삭제된  commit의 기록을 staging area에 남김

**ls -alf** : 숨김파일도 다 보여줌

**git stash** → restore 대신 사용.. restore은 복구 불가, stash는 창고로 옮기는 느낌

- 다시 불러오기: **git stash pop**

(restore 어지간하면 사용하지 말고 차라리 stash를 쓰세요…/)

### staging area에 올라간 파일을 unstage 하기

1. **git restore —staged**를 많이 씀
    - git 저장소에 commit이 존재하는 경우
2. git rm —cached  → 잘 안씀..
    - git 저장소에 commit이 없는 경우