## login_system


* step 1 - GitHub

  `git clone https://github.com/allis1002a/login_system.git`
  

* step 2 - Go to Docker links https://hub.docker.com/repository/docker/allis1002a/login_system/general

  (1) `docker pull allis1002a/login_system:v1`
  
  (2) `docker run --name create_account_test -p 4321:4321 allis1002a/login_system:v1`
  

* step 3 - links to the http://0.0.0.0:4321/docs

  (1) POST : /create_user/ 

      a. click Try it out.
      
      b. crearte the account and input the username and password that you want to create.
      
  (2) GET : /Verify/ 

      a. click Try it out.
      
      b. input username and password that you want to verify.
      
      
 
 ## Note
 
 (1) UI - 目前採用 Swagger UI, fastapi 內建。
 
 (2) data storage solutions
      a. 目前採用存入list
      b. 連結MySQL, 並開啟兩個container，一個為主程式，另一個是資料庫程式，並container接口對內。（尚未建立）
 
 


