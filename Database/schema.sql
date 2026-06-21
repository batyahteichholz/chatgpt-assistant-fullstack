-- =============================================
-- ChatGPT Assistant Database Schema
-- Full Stack Web Developer Project
-- =============================================

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS chatgpt_assistant;
USE chatgpt_assistant;

-- =============================================
-- Table: conversations
-- Description: Stores chat conversations
-- =============================================
CREATE TABLE IF NOT EXISTS conversations (
    conversation_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) DEFAULT 'New Conversation',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_updated_at (updated_at DESC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================
-- Table: messages
-- Description: Stores individual messages in conversations
-- =============================================
CREATE TABLE IF NOT EXISTS messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    conversation_id INT NOT NULL,
    role VARCHAR(20) NOT NULL COMMENT 'user or assistant',
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_conversation_id (conversation_id),
    INDEX idx_created_at (created_at),
    CONSTRAINT fk_conversation
        FOREIGN KEY (conversation_id) 
        REFERENCES conversations(conversation_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================
-- Sample Data (Optional - for testing)
-- =============================================

-- Sample conversation 1
INSERT INTO conversations (conversation_id, title, created_at, updated_at) 
VALUES (1, 'Sample Conversation', NOW(), NOW());

-- Sample messages for conversation 1
INSERT INTO messages (conversation_id, role, content, created_at) VALUES
(1, 'user', 'Hello! What can you help me with?', NOW()),
(1, 'assistant', 'Hello! I can help you with a variety of topics including programming, general questions, creative writing, and more. What would you like to know?', NOW()),
(1, 'user', 'Tell me about Python', NOW()),
(1, 'assistant', 'Python is a high-level, interpreted programming language known for its simplicity and readability. It''s widely used in web development, data science, artificial intelligence, automation, and more. Python uses indentation to define code blocks and has a rich ecosystem of libraries and frameworks.', NOW());

-- =============================================
-- Verification Queries
-- =============================================

-- View all conversations
-- SELECT * FROM conversations ORDER BY updated_at DESC;

-- View all messages with conversation info
-- SELECT 
--     m.message_id,
--     m.conversation_id,
--     c.title,
--     m.role,
--     m.content,
--     m.created_at
-- FROM messages m
-- JOIN conversations c ON m.conversation_id = c.conversation_id
-- ORDER BY m.created_at;

-- Count messages per conversation
-- SELECT 
--     c.conversation_id,
--     c.title,
--     COUNT(m.message_id) as message_count
-- FROM conversations c
-- LEFT JOIN messages m ON c.conversation_id = m.conversation_id
-- GROUP BY c.conversation_id, c.title;

-- =============================================
-- Notes for Database Administrator
-- =============================================

-- 1. This schema supports:
--    - Multiple conversations
--    - Each conversation can have many messages
--    - Messages are identified as 'user' or 'assistant'
--    - Cascading delete: deleting a conversation removes all its messages
--
-- 2. Indexes are created on:
--    - conversation_id in messages table (for JOIN performance)
--    - updated_at in conversations table (for sorting)
--    - created_at in messages table (for chronological ordering)
--
-- 3. Character set: utf8mb4 (supports emoji and international characters)
--
-- 4. To export this database:
--    mysqldump -u root -p chatgpt_assistant > database_export.sql
--
-- 5. To import this schema:
--    mysql -u root -p < schema.sql
