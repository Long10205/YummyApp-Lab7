BAI THUC HANH 7 - YUMMYAPP CI/CD

1) Doi ten thu muc MSSV_HoTen_Lab7 theo MSSV va ho ten cua ban.
2) Mo terminal tai thu muc, tao moi truong ao (khuyen nghi):
   python -m venv .venv
   .venv\Scripts\activate        (Windows)
   pip install -r requirements.txt
3) Chay test va tao local log:
   coverage run -m unittest discover -s . -p "test_*.py" > logs/local_test.log 2>&1
   coverage report -m >> logs/local_test.log
4) Kiem tra linter:
   flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
5) Git:
   git init
   git config user.name "MSSV - Ho Va Ten"
   git config user.email "mssv@dlu.edu.vn"
   git add .
   git commit -m "MSSV: complete lab 7"
   Tao repository GitHub, dat nhanh main va push theo lenh GitHub cung cap.
6) Sau khi workflow chay, vao GitHub Actions de xem ket qua; tai raw logs va
   luu thanh logs/github_actions_run.log. Tao git_history.log bang:
   git log --graph --pretty=format:"%h - %an (%ad): %s" > logs/git_history.log

Luu y: Khong gia lap logs, anh Actions, chu ky hay trang viet tay. Hay tu chay
tren may va bo sung minh chung viet tay co chu ky theo yeu cau giang vien.
