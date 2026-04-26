document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const fileInput = document.getElementById('file-input');
    const uploadArea = document.getElementById('upload-area');
    const fileNameDisplay = document.getElementById('file-name-display');
    const uploadBtn = document.getElementById('upload-btn');
    const uploadStatus = document.getElementById('upload-status');
    const statusIndicator = document.getElementById('status-indicator');

    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    const messagesArea = document.getElementById('messages-area');

    // State
    let currentFilePath = null;
    let selectedFile = null;

    // --- Startup Logic ---
    async function checkExistingFile() {
        console.log('[Startup] Checking for existing files...'); //f12 to check in console
        try {
            const response = await fetch('/api/files');
            const data = await response.json();

            if (data.filename && data.file_path) {
                console.log(`[Startup] Found existing file: ${data.filename}`);
                currentFilePath = data.file_path;
                fileNameDisplay.textContent = data.filename;
                uploadStatus.textContent = 'Existing file loaded.';
                uploadStatus.className = 'status-success';
                uploadBtn.textContent = 'Data Ready';

                // Enable chat
                chatInput.disabled = false;
                sendBtn.disabled = false;

                statusIndicator.textContent = 'Ready to Query';
                statusIndicator.classList.add('ready');

                addSystemMessage(`Welcome back! I've loaded the existing file: **${data.filename}**. What would you like to know?`);
            } else {
                console.log('[Startup] No existing files found.');
            }
        } catch (error) {
            console.error('[Startup] Error checking existing files:', error);
        }
    }

    checkExistingFile();

    // --- File Upload Logic ---

    // Handle drag and drop
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.classList.add('dragover');
    });

    uploadArea.addEventListener('dragleave', () => {
        uploadArea.classList.remove('dragover');
    });

    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.classList.remove('dragover');

        if (e.dataTransfer.files.length) {
            handleFileSelection(e.dataTransfer.files[0]);
        }
    });

    // Handle file input change
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) {
            handleFileSelection(e.target.files[0]);
        }
    });

    function handleFileSelection(file) {
        // Validate file type
        const validExtensions = ['.xlsx', '.xls', '.csv'];
        const isValid = validExtensions.some(ext => file.name.toLowerCase().endsWith(ext));

        if (!isValid) {
            uploadStatus.textContent = 'Invalid file type. Please upload Excel or CSV.';
            uploadStatus.className = 'status-error';
            uploadBtn.disabled = true;
            return;
        }

        selectedFile = file;
        fileNameDisplay.textContent = file.name;
        uploadStatus.textContent = '';
        uploadBtn.disabled = false;

        // Auto-trigger upload
        performUpload();
    }

    async function performUpload() {
        if (!selectedFile) return;

        const formData = new FormData();
        formData.append('file', selectedFile);

        uploadBtn.disabled = true;
        uploadBtn.textContent = 'Uploading...';
        uploadStatus.textContent = 'Uploading...';
        uploadStatus.className = '';

        try {
            const response = await fetch('/api/upload', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.ok) {
                currentFilePath = data.file_path;
                uploadStatus.textContent = 'Upload successful!';
                uploadStatus.className = 'status-success';
                uploadBtn.textContent = 'Data Ready';

                // Enable chat
                chatInput.disabled = false;
                sendBtn.disabled = false;
                chatInput.focus();

                statusIndicator.textContent = 'Ready to Query';
                statusIndicator.classList.add('ready');

                addSystemMessage(`I've analyzed the structure of **${data.filename}**. What would you like to know about this data?`);
            } else {
                throw new Error(data.detail || 'Upload failed');
            }
        } catch (error) {
            uploadStatus.textContent = error.message;
            uploadStatus.className = 'status-error';
            uploadBtn.disabled = false;
            uploadBtn.textContent = 'Upload Data';
        }
    }

    // Manual upload trigger (if needed)
    uploadBtn.addEventListener('click', performUpload);

    // --- Chat Logic ---

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const query = chatInput.value.trim();
        if (!query || !currentFilePath) return;

        // Clear input and disable temporarily
        chatInput.value = '';
        chatInput.disabled = true;
        sendBtn.disabled = true;

        // Add user message
        addUserMessage(query);

        // Show typing indicator
        const typingId = showTypingIndicator();

        try {
            const formData = new FormData();
            formData.append('file_path', currentFilePath);
            formData.append('query', query);

            const response = await fetch('/api/chat', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            removeTypingIndicator(typingId);

            if (response.ok) {
                addSystemMessage(data.answer);
            } else {
                throw new Error(data.detail || 'Failed to get answer');
            }
        } catch (error) {
            removeTypingIndicator(typingId);
            addSystemMessage(`Error: ${error.message}`);
        } finally {
            // Re-enable input
            chatInput.disabled = false;
            sendBtn.disabled = false;
            chatInput.focus();
        }
    });

    // --- UI Helpers ---

    function addUserMessage(text) {
        const div = document.createElement('div');
        div.className = 'message user-message';

        const formattedText = escapeHTML(text).replace(/\n/g, '<br>');

        div.innerHTML = `
            <div class="avatar">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            </div>
            <div class="message-content">${formattedText}</div>
        `;
        messagesArea.appendChild(div);
        scrollToBottom();
    }

    function addSystemMessage(text) {
        const div = document.createElement('div');
        div.className = 'message system-message';

        // 1. Escape HTML to prevent XSS
        // 2. Convert **bold** to <strong>
        // 3. Convert \n to <br> for line breaks
        const formattedText = escapeHTML(text)
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n/g, '<br>');

        div.innerHTML = `
            <div class="avatar">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            </div>
            <div class="message-content">${formattedText}</div>
        `;
        messagesArea.appendChild(div);
        scrollToBottom();
    }

    function showTypingIndicator() {
        const id = 'typing-' + Date.now();
        const div = document.createElement('div');
        div.className = 'message system-message';
        div.id = id;
        div.innerHTML = `
            <div class="avatar">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            </div>
            <div class="typing-indicator">
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
        `;
        messagesArea.appendChild(div);
        scrollToBottom();
        return id;
    }

    function removeTypingIndicator(id) {
        const el = document.getElementById(id);
        if (el) {
            el.remove();
        }
    }

    function scrollToBottom() {
        messagesArea.scrollTop = messagesArea.scrollHeight;
    }

    function escapeHTML(str) {
        return str.replace(/[&<>'"]/g,
            tag => ({
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                "'": '&#39;',
                '"': '&quot;'
            }[tag] || tag)
        );
    }
});
