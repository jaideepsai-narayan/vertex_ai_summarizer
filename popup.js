document.addEventListener('DOMContentLoaded', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    const currentUrl = tabs[0].url;
    document.getElementById('url').textContent = currentUrl;

    // Send URL to backend
    document.getElementById('sendUrl').addEventListener('click', () => {
      fetch('http://127.0.0.1:5000/process-url', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: currentUrl })
      })
      .then(res => res.json())
      .then(data => {
        document.getElementById('urlResponse').textContent = data.message;
      })
      .catch(error => {
        console.error('Error sending URL:', error);
        document.getElementById('urlResponse').textContent = 'Failed to send URL.';
      });
    });

    // Send question to backend
    document.getElementById('sendQuestion').addEventListener('click', () => {
      const question = document.getElementById('questionInput').value.trim();
      if (!question) {
        document.getElementById('questionResponse').textContent = 'Please enter a question.';
        return;
      }

      fetch('http://127.0.0.1:5000/process-question', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: question })
      })
      .then(res => res.json())
      .then(data => {
        document.getElementById('questionResponse').textContent = data.message;
      })
      .catch(error => {
        console.error('Error sending question:', error);
        document.getElementById('questionResponse').textContent = 'Failed to send question.';
      });
    });
  });
});
