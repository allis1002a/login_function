import time
import asyncio

from fastapi import FastAPI, HTTPException

fake_db_username = []
fake_db_password = []
password_attempts = {}

app = FastAPI()


@app.post("/create_user/")
def create_item(username: str, password: str):

    if username in fake_db_username:
        return {"success": False, "reason": 'username already existed.'}

    if username is None or len(username) < 3 or len(username) > 33:
        return {"success": False, "reason": 'Username should be with a minimum length of 3 chars and a maximum length of 32 chars'}

    if password is None or len(password) < 8 or len(password) > 33:
        return {"success": False, "reason": 'Password should be with a minimum length of 8 chars and a maximum length of 32 chars'}

    if not any(map(str.islower, password)):
        return {"success": False, "reason": 'Password must contain a lowercase letter'}

    if not any(map(str.isupper, password)):
        return {"success": False, "reason": 'Password must contain an uppercase letter'}

    if not any(map(str.isdigit, password)):
        return {"success": False, "reason": 'Password must contain a digit'}

    fake_db_username.append(username)
    fake_db_password.append(password)

    print(f'fake_db_username contains {fake_db_username}')
    print(f'fake_db_password contains {fake_db_password}')

    return {"success": True}


@app.get("/verify/")
async def read_item(username: str, password: str):

    try:
        if username == fake_db_username[fake_db_username.index(username)]:
            if password == fake_db_password[fake_db_username.index(username)]:
                password_attempts[username] = 0
                return {"success": True}

            else:
                # 增加使用者輸入錯誤密碼的計數
                password_attempts[username] = password_attempts.get(
                    username, 0) + 1

                # 如果使用者輸入錯誤密碼超過五次，則等待 30 秒
                if password_attempts[username] > 5:
                    # 送至前端，請前端處理header中‘Retry-After': "10"。

                    raise HTTPException(
                        status_code=400,
                        detail={"success": False,
                                "reason": 'Wrong password, please wait 10 secs'},
                        headers={'Retry-After': "10"}
                    )
                    # 僅在後端呈現，而當前function無法使用。
                    # print('Input wrong password OVER 5 times. Retry after one minute!')
                    # await asyncio.sleep(60)

                raise HTTPException(
                    status_code=401, detail={"success": False, "reason": 'Invalid password'})
    except ValueError:
        return {"success": False, "reason": 'username does not exist.'}
