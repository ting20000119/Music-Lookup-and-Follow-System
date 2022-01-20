# Music Lookup and Follow System

## Installation

- [Python](https://www.python.org/)

* [SQLite](https://www.sqlite.org/index.html)

- [Pip Package Manager](https://pypi.org/)

---

## Running the app

資料庫初始:

```
python3 init_db.py
```

啟用後端 server : ( run on localhost:5000 )

```
python3 app.py
```

UI 介面使用：

- 使用者介面 : 點選 frontend 資料夾裡的 login.html

* 後台介面 : 點選 frontend 資料夾裡的 backstage.html

---

## Functions of the app

### Insert

- 使用者可自行註冊會員帳號
- 會員可藉由訂閱的方式來根據喜好客製化他們的 4 種訂閱清單
  - 歌曲清單
  - 歌手清單
  - 製作人清單
  - 作曲者清單

* 後台可讓管理者新增歌曲

### Delete

- 後台可讓管理者刪除會員帳號

### Search

- 查詢歌曲
  - 透過歌曲名稱查詢
  - 透過歌手名稱查詢他所演唱過的所有歌曲
  - 透過製作人名稱查詢他所製作過的所有歌曲
  - 透過作曲者名稱查詢他所作曲過的所有歌曲

* 會員的 4 種訂閱清單查詢
  - 可查詢會員所訂閱的
    - 歌曲
    - 歌手
    - 製作人
    - 作曲者

### Update

- 後台可讓管理者更改會員名稱
