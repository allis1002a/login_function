## login_system


* step 1 - GitHub

  `git clone https://github.com/allis1002a/login_system.git`
  

* step 2 - Go to Docker links https://hub.docker.com/repository/docker/allis1002a/login_system/general

  (1) `docker pull allis1002a/login_system:v1`
  
  (2) `docker run --name create_account_test -p 4321:4321 allis1002a/login_system:v1`
  
  (if not works, might meet the port conflict problem, try below instructions.)
  
  (1) `docker pull allis1002a/login_system:v2`
  
  (2) `docker run --name create_account_test -it -p (port):(port) allis1002a/login_system:v2`
      
      - (port) : Decide the port on your own, and check the two ports should be the same.
   
  (3) `uvicorn app.main:app --host 0.0.0.0 --port (port)`
   

* step 3 - links to the http://0.0.0.0:4321/docs

  (1) POST : /create_user/ 

      a. click Try it out.
      
      b. crearte the account and input the username and password that you want to create.
      
  (2) GET : /Verify/ 

      a. click Try it out.
      
      b. input username and password that you want to verify.
      
      
 
 ## Note
 
 (1) development env: macOS with M1 chip. 
 
 (2) UI - 目前採用 Swagger UI, fastapi 內建。
 
 (3) data storage solutions
      a. 目前採用存入list
      b. 連結MySQL, 並開啟兩個container，一個為主程式，另一個是資料庫程式，並container接口對內。（尚未建立）
 
 


