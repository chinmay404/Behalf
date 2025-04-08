(() => {
    const recordButton = document.getElementById('recordButton');
    const timer = document.getElementById('timer');
    const contentArea = document.getElementById('contentArea');
    let isRecording = false;
    let timerInterval;
    let seconds = 0;

    // Start recording function
    const startRecording = async () => {
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
            alert("Your browser doesn't support audio recording.");
            return;
        }
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        const mediaRecorder = new MediaRecorder(stream);
        let chunks = [];

        mediaRecorder.ondataavailable = (e) => chunks.push(e.data);
        mediaRecorder.onstop = async () => {
            const blob = new Blob(chunks, { type: 'audio/wav' });
            const reader = new FileReader();
            reader.onload = async () => {
                const base64Audio = reader.result.split(',')[1];
                sendAudioToBackend(base64Audio);
            };
            reader.readAsDataURL(blob);
            chunks = [];
        };
        mediaRecorder.start();
        return mediaRecorder;
    };

    let mediaRecorder;

    // Record button event listener
    recordButton.addEventListener('click', async () => {
        isRecording = !isRecording;
        recordButton.classList.toggle('recording');
        timer.classList.toggle('active');
        document.body.classList.toggle('recording');

        if (isRecording) {
            seconds = 0;
            timerInterval = setInterval(() => {
                seconds++;
                const minutes = Math.floor(seconds / 60);
                const remainingSeconds = seconds % 60;
                timer.textContent = `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
            }, 1000);
            updateContent("Agent is listening...");
            mediaRecorder = await startRecording();
        } else {
            clearInterval(timerInterval);
            mediaRecorder.stop();
            updateContent("Processing your request...");
        }
    });

    // Update content in the textarea
    function updateContent(text) {
        contentArea.textContent = text;
    }

    // Send audio to backend
    async function sendAudioToBackend(audioData) {
        const response = await fetch('/process-audio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ audio: audioData }),
        });
        const result = await response.json();
        updateContent(result.response);
    }
})();
