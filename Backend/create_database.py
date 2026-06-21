"""
Script to create the chatgpt_assistant database and tables
Run this once before starting the server
"""
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mysql_host = os.getenv("MYSQL_HOST", "localhost")
mysql_user = os.getenv("MYSQL_USER", "root")
mysql_password = os.getenv("MYSQL_PASSWORD", "")
mysql_database = os.getenv("MYSQL_DATABASE", "chatgpt_assistant")

# Connect to MySQL server (without specifying database)
try:
    connection = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password
    )
    
    cursor = connection.cursor()
    
    # Create database if it doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {mysql_database}")
    print(f"✅ Database '{mysql_database}' created or already exists")
    
    # Use the database
    cursor.execute(f"USE {mysql_database}")
    
    # Create conversations table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            conversation_id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(200) NOT NULL DEFAULT 'New Conversation',
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            INDEX idx_created_at (created_at),
            INDEX idx_updated_at (updated_at)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    """)
    print("✅ Table 'conversations' created or already exists")
    
    # Create messages table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            message_id INT AUTO_INCREMENT PRIMARY KEY,
            conversation_id INT NOT NULL,
            role VARCHAR(20) NOT NULL,
            content TEXT NOT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (conversation_id) REFERENCES conversations(conversation_id) ON DELETE CASCADE,
            INDEX idx_conversation_id (conversation_id),
            INDEX idx_created_at (created_at)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    """)
    print("✅ Table 'messages' created or already exists")
    
    # Check tables
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print(f"\n📊 Tables in {mysql_database} database:")
    for table in tables:
        print(f"   - {table[0]}")
    
    connection.commit()
    cursor.close()
    connection.close()
    
    print("\n🎉 Database setup completed successfully!")
    
except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
    print("\nMake sure MySQL is running and the password is correct.")
