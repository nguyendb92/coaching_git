# **Repo để training git và lưu các bài tập đã làm**:

- mỗi khi muốn làm nhóm các bài tập hay ở các trang khác nhau thì cần phải:
    > git checkout main
    > git checkout -b <duc | viet >_baitap_< nơi làm bài tập>
    >
    > **Sau khi làm xong thì**
    > - git add -A
    > - git commit -m "<message>"
    > - git push -u origin <tên nhánh hiện tại>

- Tạo môi trường ảo nếu chưa tạo

  > python -m venv venv
  > - window:
  >      venv\Scripts\activate
  > - linux:
  >      source venv/bin/activate

- Install các thư viện cần thiết
  > pip ínstall -r requirements.txt

