# 📊 Excel Bot AI - Chat with your Spreadsheets

[Vietnamese below] | [Tiếng Việt ở bên dưới]

---

## 🌟 Overview
Excel Bot AI is a powerful, user-friendly tool that allows you to "talk" to your Excel or CSV files. Instead of manually filtering data or writing complex formulas, you can simply ask questions in plain English or Vietnamese.

### 💎 Key Features & Why it's Powerful
- **🚀 Handles Massive Files**: Unlike other AI tools that try to "read" the entire file (and fail on large ones), this app uses **Local Code Generation**. The AI writes Python code to find the answer, allowing you to query datasets with **hundreds of thousands of rows** instantly.
- **🛡️ Privacy First**: Your raw spreadsheet data **never leaves your machine**. Only your questions and column headers are sent to the AI.
- **💡 Smart Context**: The bot remembers your previous questions, allowing for complex follow-up conversations.
- **📂 Multi-File Manager**: Easily switch between multiple uploaded files with a single click.
- **💰 Cost Efficient**: Because the AI only writes the code and doesn't "read" every row, you save significantly on API costs.

### 🛠 Detailed Tech Stack
- **AI Orchestration**: **LangChain** – Manages the AI agent, conversation memory, and Python code generation.
- **LLM Model**: **OpenAI GPT-4o-mini** – Provides high-speed, intelligent reasoning for data analysis.
- **Data Engine**: **Python Pandas** – Handles complex data manipulation and spreadsheet scanning.
- **Excel Support**: **OpenPyXL** & **xlrd** – Libraries used to support both modern `.xlsx` and legacy `.xls` files.
- **Backend API**: **FastAPI** – A high-performance Python web framework for handling chat and file requests.
- **Frontend**: **Vanilla JS, CSS3, & HTML5** – A custom-built, responsive dashboard with a premium dark theme.

---

## 🔄 Developer Workflow (Technical Implementation)
The application is architected to handle data-driven conversations through a multi-layered pipeline:

### 🔹 1. API & State Layer (`main.py`)
- **Web Framework**: **FastAPI** handles asynchronous POST requests for chat and file uploads.
- **Session Management**: Chat history is persisted in a global `chat_histories` dictionary. To ensure consistency across OS environments, `file_path` keys are sanitized using `os.path.normpath()`.
- **Message Schema**: Conversation turns are stored as LangChain `HumanMessage` and `AIMessage` objects to maintain compatibility with LLM providers.

### 🔹 2. Data & AI Orchestration (`agent.py`)
- **Data Engine**: **Pandas** loads spreadsheets into DataFrames. All-NaN columns are automatically dropped via `df.dropna(axis=1, how='all')` to reduce token usage.
- **AI Agent**: Uses LangChain's **`create_pandas_dataframe_agent`** with the `openai-tools` agent type.
- **Manual Context Injection**: Due to version-specific constraints in `langchain-experimental`, chat history is manually serialized into a text block and prepended to the user query before invocation.

### 🔹 3. Execution & Security
- **Dynamic Analysis**: The agent utilizes **`PythonAstREPLTool`** to execute AI-generated Python code locally against the in-memory DataFrame.
- **Safety**: Code execution happens in a controlled environment where the agent only has access to the local scope of the spreadsheet data.

### 🔹 4. Frontend Layer (`script.js`)
- **Reactive UI**: Uses **Vanilla JavaScript** to handle file-selection states and asynchronous API calls.
- **Message Rendering**: Implements custom **RegEx** parsers to convert Markdown-style bolding (`**`) and newline characters (`\n`) into safe HTML tags (`<strong>`, `<br>`).

## 🚀 Quick Start Guide

### 1. Prerequisites
Before you begin, you need to install two things:
1. **Git**: [Download Git here](https://git-scm.com/downloads). (Select the "Windows" version). This allows you to download and update the app easily.
2. **Python**: [Download Python 3.10 here](https://www.python.org/downloads/windows/). **IMPORTANT:** During installation, check the box that says **"Add Python to PATH"**.

### 2. Installation
1. Open your terminal (type `cmd` in your Windows search bar).
2. Download the project:
   ```bash
   git clone https://github.com/tminhtri1910/excel-chat-bot.git
   cd excel-chat-bot
   ```
3. Create and activate a Virtual Environment (Recommended):
   ```bash
   # Create the environment
   py -3.10 -m venv venv
   
   # Activate via Command Prompt
   venv\Scripts\activate
   
   # OR Activate via PowerShell
   .\venv\Scripts\Activate.ps1
   
   # To stop using the environment later, just type:
   deactivate
   ```
4. Install the required tools:
   ```bash
   pip install -r requirements.txt
   ```

### 3. API Key Configuration
The bot needs an "API Key" to use the OpenAI brain.
1. Get your key from [OpenAI Dashboard](https://platform.openai.com/api-keys).
2. In the project folder, find the file, or create a new file named **`.env`**.
3. Open it with Notepad and set your key:
   ```env
   OPENAI_API_KEY=your_actual_key_here
   ```
   *Note: This file is secret. Never share it with anyone!*

### 4. How to Run
- Simply double-click the **`run.bat`** file in the folder.
- A terminal window will open—keep it open while using the app.
- If your browser doesn't open automatically, go to: **[http://localhost:8000](http://localhost:8000)**

---

# 📊 Trợ Lý AI Cho File Excel - Trò chuyện với bảng tính của bạn

---

## 🌟 Tổng quan
Excel Bot AI là một công cụ mạnh mẽ và dễ sử dụng, cho phép bạn "trò chuyện" trực tiếp với các tệp Excel hoặc CSV của mình. Thay vì phải lọc dữ liệu thủ công hoặc viết các công thức phức tạp, bạn chỉ cần đặt câu hỏi bằng ngôn ngữ tự nhiên.

### 💎 Điểm nổi bật & Tại sao nó mạnh mẽ
- **🚀 Xử lý tệp siêu lớn**: Không giống như các công cụ AI khác cố gắng "đọc" toàn bộ tệp (và thường thất bại với tệp lớn), ứng dụng này sử dụng công nghệ **Tạo mã cục bộ**. AI viết mã Python để tìm câu trả lời, cho phép bạn truy vấn các bộ dữ liệu hàng **trăm nghìn dòng** ngay lập tức.
- **🛡️ Bảo mật hàng đầu**: Dữ liệu bảng tính thô của bạn **không bao giờ rời khỏi máy tính**. Chỉ có câu hỏi và tên các tiêu đề cột được gửi đến AI.
- **💡 Ngữ cảnh thông minh**: Robot ghi nhớ các câu hỏi trước đó của bạn, cho phép thực hiện các cuộc hội thoại tiếp nối phức tạp.
- **📂 Quản lý đa tệp**: Dễ dàng chuyển đổi giữa nhiều tệp đã tải lên chỉ với một cú nhấp chuột.
- **💰 Tiết kiệm chi phí**: Vì AI chỉ viết mã và không phải "đọc" từng dòng dữ liệu, bạn sẽ tiết kiệm được đáng kể chi phí API.

### 🛠 Chi tiết công nghệ sử dụng
- **Điều phối AI**: **LangChain** – Quản lý tác vụ AI, bộ nhớ cuộc hội thoại và tự động tạo mã Python.
- **Mô hình LLM**: **OpenAI GPT-4o-mini** – Cung cấp khả năng suy luận thông minh và xử lý dữ liệu tốc độ cao.
- **Xử lý dữ liệu**: **Python Pandas** – Xử lý các thao tác dữ liệu phức tạp và quét bảng tính.
- **Hỗ trợ Excel**: **OpenPyXL** & **xlrd** – Các thư viện hỗ trợ cả tệp `.xlsx` hiện đại và `.xls` cũ.
- **Hệ thống Backend**: **FastAPI** – Khung web Python hiệu suất cao để xử lý các yêu cầu chat và tệp.
- **Giao diện Frontend**: **Vanilla JS, CSS3, & HTML5** – Giao diện tùy chỉnh, phản hồi nhanh với chủ đề tối (dark mode) cao cấp.

---

## 🔄 Luồng xử lý (Technical Workflow)
Ứng dụng được thiết kế để xử lý các cuộc hội thoại dựa trên dữ liệu thông qua quy trình nhiều lớp:

### 🔹 1. Lớp API & Trạng thái (`main.py`)
- **Web Framework**: **FastAPI** xử lý các yêu cầu POST bất đồng bộ cho chat và tải lên tệp tin.
- **Quản lý phiên**: Lịch sử chat được lưu trữ trong một từ điển `chat_histories` toàn cục. Để đảm bảo tính nhất quán trên các hệ điều hành, các khóa `file_path` được làm sạch bằng `os.path.normpath()`.
- **Cấu trúc tin nhắn**: Các lượt hội thoại được lưu trữ dưới dạng đối tượng LangChain `HumanMessage` và `AIMessage` để duy trì tính tương thích với các nhà cung cấp LLM.

### 🔹 2. Điều phối Dữ liệu & AI (`agent.py`)
- **Công cụ dữ liệu**: **Pandas** tải bảng tính vào DataFrames. Các cột chứa toàn giá trị NaN sẽ tự động bị loại bỏ qua `df.dropna(axis=1, how='all')` để tiết kiệm token.
- **AI Agent**: Sử dụng **`create_pandas_dataframe_agent`** của LangChain với loại agent `openai-tools`.
- **Chèn ngữ cảnh thủ công**: Do các hạn chế về phiên bản trong `langchain-experimental`, lịch sử chat được tuần tự hóa thủ công thành một khối văn bản và được thêm vào trước truy vấn của người dùng trước khi gọi AI.

### 🔹 3. Thực thi & Bảo mật
- **Phân tích động**: Agent sử dụng **`PythonAstREPLTool`** để thực thi mã Python do AI tạo ra cục bộ trên đối tượng DataFrame trong bộ nhớ.
- **An toàn**: Việc thực thi mã diễn ra trong một môi trường được kiểm soát, nơi agent chỉ có quyền truy cập vào phạm vi cục bộ của dữ liệu bảng tính.

### 🔹 4. Lớp Frontend (`script.js`)
- **Giao diện phản hồi**: Sử dụng **Vanilla JavaScript** để quản lý trạng thái chọn tệp và các cuộc gọi API bất đồng bộ.
- **Hiển thị tin nhắn**: Triển khai các bộ phân tích **RegEx** tùy chỉnh để chuyển đổi định dạng in đậm kiểu Markdown (`**`) và các ký tự xuống dòng (`\n`) thành các thẻ HTML an toàn (`<strong>`, `<br>`).

## 🚀 Hướng dẫn bắt đầu nhanh

### 1. Chuẩn bị
Trước khi bắt đầu, bạn cần cài đặt hai phần mềm sau:
1. **Git**: [Tải Git tại đây](https://git-scm.com/downloads). (Chọn bản cho Windows). Phần mềm này giúp bạn tải và cập nhật ứng dụng dễ dàng.
2. **Python**: [Tải Python 3.10 tại đây](https://www.python.org/downloads/windows/). **QUAN TRỌNG:** Trong lúc cài đặt, hãy tích vào ô **"Add Python to PATH"**.

### 2. Cài đặt
1. Mở cửa sổ terminal (Gõ `cmd` vào thanh tìm kiếm Windows).
2. Tải dự án này về:
   ```bash
   git clone https://github.com/tminhtri1910/excel-chat-bot.git
   cd excel-chat-bot
   ```
3. Tạo và kích hoạt Môi trường ảo (Khuyên dùng):
   ```bash
   # Tạo môi trường ảo
   py -3.10 -m venv venv
   
   # Kích hoạt bằng Command Prompt
   venv\Scripts\activate
   
   # HOẶC Kích hoạt bằng PowerShell
   .\venv\Scripts\Activate.ps1
   
   # Để dừng sử dụng môi trường ảo, chỉ cần gõ:
   deactivate
   ```
4. Cài đặt các thư viện cần thiết:
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
- Một cửa sổ terminal sẽ hiện ra—hãy giữ nó khi đang sử dụng ứng dụng.
- Nếu trình duyệt không tự động mở, hãy truy cập: **[http://localhost:8000](http://localhost:8000)**
