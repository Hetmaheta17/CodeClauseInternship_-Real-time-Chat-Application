# Live Chat Application 

Welcome to the Live Chat Application, a real-time messaging platform built using Django, WebSockets, and Tailwind CSS. This application provides an intuitive and seamless chatting experience with beautiful UI/UX, real-time updates, and essential chat features.

# Features 

Real-Time Messaging: Instant communication powered by WebSockets.

User Authentication: Secure login/logout and session management.

Group & Private Chats: Create and join chat rooms easily.

Read Receipts & Typing Indicators: Know when someone is typing or has read your message.

Responsive UI: Tailwind CSS for a beautiful and adaptive design.

Message History: View past messages for context.

Click Analytics: Track interactions and analyze engagement.

QR Code Payments (Upcoming): Effortless UPI-based payments via QR code scanning.

# Technologies Used
Backend: Python, Django, Channels, WebSockets

Frontend: HTML, Tailwind CSS, JavaScript

Database: SQLite/MySQL/PostgreSQL

Deployment: Daphne, Redis

# Installation 

Follow these steps to get the project running locally.

# Prerequisites 

Ensure you have the following installed:
Python 3.10+
Redis (for WebSocket connections)
Virtual environment setup
Setup Instructions

# Clone the repository
git clone https://github.com/Hetmaheta17/CodeClauseInternship_-Real-time-Chat-Application.git

cd live-chat-app

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start Redis server
redis-server

# Run the development server
python manage.py runserver

For WebSocket support via Daphne:

daphne chat_project.asgi:application -b 0.0.0.0 -p 8000

Usage

Open the app in your browser: http://127.0.0.1:8000/

Enter a chat room name and start chatting in real time.

Enjoy the sleek and responsive chat interface!

Project Structure

chat_project/
|-- chat_app/
|   |-- templates/
|   |   |-- home.html
|   |   |-- chatroom.html
|   |-- static/
|   |   |-- css/
|-- chat_project/
|-- db.sqlite3
|-- manage.py
|-- requirements.txt
|-- README.md


Contributing

We welcome contributions! If you'd like to improve this project, follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature-new)

Commit changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature-new)

Create a pull request

License

This project is licensed under the MIT License.

Contact

For any queries or suggestions, feel free to reach out:

Email: hetmaheta17@gmail.com

GitHub: Hetmaheta17

Enjoy chatting with Live Chat Application! 🚀

