# 台灣銀行代碼查詢

提供使用者查詢台灣各銀行及其分行詳細資訊

[網站連結](https://bankinfo-josh.fly.dev/)  

### 網站功能 
1. 查詢台灣各銀行名稱及代碼
2. 查詢台灣各銀行之分行詳細資訊，包含分行代碼/地址/電話
3. 輸入關鍵字立即查詢
4. 提供代碼及頁面連結複製

## 專案初始化
```
$ pip install poetry
$ poetry init -n
$ poetry shell
$ poetry install
```
## 政府開放平台資料抓取
```
$ python manage.py seed
```
## 啟動專案
```
$ python manage.py runserver
```

## 使用技術
 - **前端：** HTML5 / JavaScript / Tailwind CSS / Alpine.js  
 - **後端：** Python / Django  
 - **部署：** Fly.io  
 - **資料庫：** PostgreSQL  


*最後更新：2024/6/30*  