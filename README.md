# 📊 Excel Bot AI - Chat with your Spreadsheets

[Vietnamese below] | [Tiếng Việt ở bên dưới]

---

## 🌟 Overview
Excel Bot AI is a powerful, user-friendly tool that allows you to "talk" to your Excel or CSV files. Instead of manually filtering data or writing complex formulas, you can simply ask questions in plain English or Vietnamese.

### 🛠 Tech Stack (Simplified)
- **AI Brain**: Powered by **OpenAI (GPT-4o-mini)**. It understands your questions like a human would.
- **Data Analyst**: Uses **Python & Pandas** to scan through thousands of rows in seconds.
- **Interface**: A modern, easy-to-use web dashboard built with **HTML, CSS, and JavaScript**.
- **Engine**: Built with **FastAPI**, making it fast and reliable on your local machine.

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Before you begin, you need to install two things:
1. **Git**: [Download Git here](https://git-scm.com/downloads). (Select the "Windows" version). This allows you to download and update the app easily.
2. **Python**: [Download Python 3.10+ here](https://www.python.org/downloads/). **IMPORTANT:** During installation, check the box that says **"Add Python to PATH"**.

### 2. Installation
1. Open your terminal (type `cmd` in your Windows search bar).
2. Download the project:
   ```bash
   git clone https://github.com/your-username/excel-chat-bot.git
   cd "excel chat bot"
   ```
3. Install the required tools:
   ```bash
   pip install -r requirements.txt
   ```

### 3. API Key Configuration
The bot needs an "API Key" to use the OpenAI brain.
1. Get your key from [OpenAI Dashboard](https://platform.openai.com/api-keys).
2. In the project folder, find the file named **`.env`**.
3. Open it with Notepad and set your key:
   ```env
   OPENAI_API_KEY=your_actual_key_here
   ```
   *Note: This file is secret. Never share it with anyone!*

### 4. How to Run
- Simply double-click the **`run.bat`** file in the folder.
- Your browser will open automatically to `http://localhost:8000`.

---

# 📊 Trợ Lý AI Cho File Excel - Trò chuyện với bảng tính của bạn

---

## 🌟 Tổng quan
Excel Bot AI là một công cụ mạnh mẽ và dễ sử dụng, cho phép bạn "trò chuyện" trực tiếp với các tệp Excel hoặc CSV của mình. Thay vì phải lọc dữ liệu thủ công hoặc viết các công thức phức tạp, bạn chỉ cần đặt câu hỏi bằng ngôn ngữ tự nhiên.

### 🛠 Công nghệ sử dụng
- **Bộ não AI**: Sử dụng **OpenAI (GPT-4o-mini)**. Nó hiểu câu hỏi của bạn như một con người thực thụ.
- **Phân tích dữ liệu**: Sử dụng **Python & Pandas** để quét hàng nghìn dòng dữ liệu chỉ trong vài giây.
- **Giao diện**: Một bảng điều khiển web hiện đại, dễ sử dụng được xây dựng bằng **HTML, CSS và JavaScript**.
- **Hệ thống**: Được xây dựng bằng **FastAPI**, giúp ứng dụng chạy nhanh và ổn định trên máy tính của bạn.

---

## 🚀 Hướng dẫn bắt đầu nhanh

### 1. Chuẩn bị
Trước khi bắt đầu, bạn cần cài đặt hai phần mềm sau:
1. **Git**: [Tải Git tại đây](https://git-scm.com/downloads). (Chọn bản cho Windows). Phần mềm này giúp bạn tải và cập nhật ứng dụng dễ dàng.
2. **Python**: [Tải Python 3.10+ tại đây](https://www.python.org/downloads/). **QUAN TRỌNG:** Trong lúc cài đặt, hãy tích vào ô **"Add Python to PATH"**.

### 2. Cài đặt
1. Mở cửa sổ terminal (Gõ `cmd` vào thanh tìm kiếm Windows).
2. Tải dự án này về:
   ```bash
   git clone https://github.com/tminhtri1910/excel-chat-bot.git
   cd "excel chat bot"
   ```
3. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Cấu hình mã API (API Key)
Robot cần một "Mã API" để sử dụng trí tuệ nhân tạo của OpenAI.
1. Lấy mã của bạn tại [OpenAI Dashboard](https://platform.openai.com/api-keys).
2. Trong thư mục dự án, tìm tệp hoặc tạo tệp mới có tên **`.env`**.
3. Mở tệp bằng Notepad và dán mã của bạn vào:
   ```env
   OPENAI_API_KEY=mã_của_bạn_ở_đây
   ```
   *Lưu ý: Tệp này là bí mật. Không bao giờ chia sẻ nó với bất kỳ ai!*

### 4. Cách chạy ứng dụng
- Chỉ cần nhấp đúp vào tệp **`run.bat`** trong thư mục.
- Trình duyệt của bạn sẽ tự động mở trang `http://localhost:8000`.
