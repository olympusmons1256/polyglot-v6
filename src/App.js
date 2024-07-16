import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [fileContent, setFileContent] = useState('');
  const [chatMessages, setChatMessages] = useState([]);

  // Mock data for file list (replace with actual data from GitHub API later)
  const fileList = ['file1.js', 'file2.py', 'file3.txt'];

  const handleFileSelect = (file) => {
    setSelectedFile(file);
    // TODO: Fetch file content from GitHub API
    setFileContent(`Content of ${file}`);
  };

  const handleSendMessage = (message) => {
    // TODO: Send message to Claude API
    setChatMessages([...chatMessages, { role: 'user', content: message }]);
  };

  return (
    <div className="app">
      <div className="sidebar">
        <h2>Files</h2>
        <ul>
          {fileList.map((file) => (
            <li
              key={file}
              onClick={() => handleFileSelect(file)}
              className={selectedFile === file ? 'selected' : ''}
            >
              {file}
            </li>
          ))}
        </ul>
      </div>
      <div className="main-content">
        <div className="file-editor">
          <h2>{selectedFile || 'Select a file'}</h2>
          <textarea
            value={fileContent}
            onChange={(e) => setFileContent(e.target.value)}
            disabled={!selectedFile}
          />
        </div>
        <div className="chat-interface">
          <h2>Chat with Claude</h2>
          <div className="chat-messages">
            {chatMessages.map((msg, index) => (
              <div key={index} className={`message ${msg.role}`}>
                {msg.content}
              </div>
            ))}
          </div>
          <input
            type="text"
            placeholder="Type your message..."
            onKeyPress={(e) => {
              if (e.key === 'Enter') {
                handleSendMessage(e.target.value);
                e.target.value = '';
              }
            }}
          />
        </div>
      </div>
    </div>
  );
}

export default App;