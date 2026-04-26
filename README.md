# 📊 Excel Bot AI - Chat with your Spreadsheets

[Vietnamese below] | [Tiếng Việt ở bên dưới]

---

## 🇺🇸 English Version

### 🌟 What is this?
Excel Bot AI is a simple tool that allows you to "talk" to your Excel or CSV files. Instead of manually filtering or writing complex formulas, you just ask a question in plain English (or any language) and the AI will analyze the data for you.

### 🛠 Setup Instructions (For Non-Tech Users)

#### 1. Install Python
If you don't have it yet, download and install Python from [python.org](https://www.python.org/downloads/). 
*   **Important:** During installation, make sure to check the box that says **"Add Python to PATH"**.

#### 2. Get an API Key
This app uses OpenRouter to talk to the AI.
1.  Go to [openrouter.ai](https://openrouter.ai/).
2.  Create an account and generate an **API Key**.
3.  Add some credits (even $1 is enough for thousands of questions).

#### 3. Configure the App
1.  In the project folder, find the file named `.env`.
2.  Open it with Notepad.
3.  Paste your key after the equals sign: `OPENROUTER_API_KEY=your_key_here`
4.  Save and close the file.

#### 4. First-Time Install
Open your project folder, click on the address bar at the top, type `cmd`, and press Enter. In the black window that opens, type:
```bash
pip install -r requirements.txt
```
Wait for it to finish. You only need to do this once!

---

### 🚀 How to Run
1.  Double-click the **`run.bat`** file.
2.  A window will open. Leave it open while you use the app.
3.  Open your web browser and go to: **http://127.0.0.1:8000**
4.  Drag and drop your Excel file and start chatting!

---
---

## 🇻🇳 Tiếng Việt

### 🌟 Đây là ứng dụng gì?
Excel Bot AI là một công cụ đơn giản cho phép bạn "trò chuyện" với các tệp Excel hoặc CSV của mình. Thay vì phải lọc dữ liệu thủ công hoặc viết các công thức phức tạp, bạn chỉ cần đặt câu hỏi bằng ngôn ngữ tự nhiên và AI sẽ phân tích dữ liệu cho bạn.

### 🛠 Hướng dẫn cài đặt (Dành cho người không chuyên)

#### 1. Cài đặt Python
Nếu bạn chưa có, hãy tải và cài đặt Python từ [python.org](https://www.python.org/downloads/).
*   **Quan trọng:** Trong khi cài đặt, hãy nhớ tích vào ô **"Add Python to PATH"**.

#### 2. Lấy API Key
Ứng dụng này sử dụng OpenRouter để kết nối với AI.
1.  Truy cập [openrouter.ai](https://openrouter.ai/).
2.  Tạo tài khoản và tạo một **API Key**.
3.  Nạp một ít tiền (chỉ cần $1 là đủ cho hàng ngàn câu hỏi).

#### 3. Cấu hình ứng dụng
1.  Trong thư mục dự án, tìm tệp có tên `.env`.
2.  Mở tệp bằng Notepad.
3.  Dán mã khóa của bạn vào sau dấu bằng: `OPENROUTER_API_KEY=mã_của_bạn_ở_đây`
4.  Lưu và đóng tệp.

#### 4. Cài đặt lần đầu
Mở thư mục dự án, nhấn vào thanh địa chỉ ở trên cùng, gõ `cmd` và nhấn Enter. Trong cửa sổ màu đen hiện ra, gõ:
```bash
pip install -r requirements.txt
```
Đợi quá trình chạy xong. Bạn chỉ cần làm việc này một lần duy nhất!

---

### 🚀 Cách sử dụng
1.  Nhấn đúp chuột vào tệp **`run.bat`**.
2.  Một cửa sổ sẽ hiện ra. Hãy giữ nguyên cửa sổ đó khi đang sử dụng ứng dụng.
3.  Mở trình duyệt web và truy cập địa chỉ: **http://127.0.0.1:8000**
4.  Kéo và thả tệp Excel của bạn vào và bắt đầu đặt câu hỏi!
