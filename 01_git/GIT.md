# GIT
- 버전관리 : 변화를 기록하고 추적하는 것
- 분산 버전 관리 시스템 : 분산해서 다른 곳에서도 똑같은 방식으로 관리할 수 있도록 하는 것
    - 중앙집중식인 경우 똑같은 파일의 똑같은 줄을 다른 사람이 수정을 할 때 합치는 과정에서 에러가 발생할 수 있음 (이를 관리할 수 있는 방법이 없음)

    - 어딘가에 있는 .git 파일(각 버전에 따른 수정 사항을 기록한 파일)을 집에서 다운받으면 됨 -> a,b가 똑같은 파일을 수정할 때 문제가 없을까? a,b가 수정한 파일이 버전으로서 수정이 됨

  
- GIT은 세 가지로 나뉨
    - Working Directory : 현재 작업 중인 영역(.git파일)
    - Staging Area : Working Directory 에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역 (임시파일들을 기록한다)
    - Repository : 버전 이력과 파일들이 영구적으로 저장되는 영역, 모든 버전과 변경 이력이 기록됨 (버전을 하나 만들거다 -> 이후 수정사항은 다른 버전으로 가야함) -> 커밋을 통해 version1이 나왔다면 SA 영역의 임시파일들은 사라진다 그래야 다음 버전의 임시파일들이 저장할 수 있기 때문에다.
    - commit : 버전

---

# git 명령어

- `git init` : 로컬 저장소 설정(초기화)
- `git add` : staging area에 추가
- `git status` : 현재 git의 상태, master와 현재 버전을 추적하고 있는 파일들과 버전을 추적하지 않는 파일들에 대한 정보를 다 보여줌
- `git commit` : 버전을 만드는 명령어
  - commit을 할 때에는 이 작업을 누가 언제 했는지 기록을 해줘야 한다.
- `git config` : commit을 하기위해서는 사용자의 정보를 입력해야 하는데 그 때 사용한다.
- `git log` : commit된 파일의 정보를 보기 위해서 사용한다.


# 원격 저장소
- `git remote add 원격저장소이름 주소`
  - `git remote add origin https://github.com/silverlilyjane/TIL.git`
- `git remove -v`

- `git push -u origin master` 후 github 로그인

<숙제용 추가>
test
test2

원격저장소에서 추가
