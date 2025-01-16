
const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const messages = document.querySelector('.chat-messages');
    const newMessage = document.createElement('div');
    newMessage.textContent = `${data.sender}: ${data.message}`;
    messages.appendChild(newMessage);
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.getElementById('send-btn').addEventListener('click', function() {
    const messageInput = document.getElementById('message');
    const message = messageInput.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'sender': currentUser, // Pass the username of the sender dynamically
        'receiver': chatWith, // Pass the username of the receiver dynamically
    }));
    messageInput.value = '';
});

// Scroll chat to the bottom when a new message is added
const messagesContainer = document.querySelector('.chat-messages');
messagesContainer.scrollTop = messagesContainer.scrollHeight;

