import requests

url = "http://localhost:8000/api/chat"
data = {
    "sessionId": "test-session",
    "message": "test message"
}
# We need to simulate the gemini_send_message returning a <MIDI_DATA> block.
# Since gemini_send_message calls the actual LLM, I can't guarantee it will return MIDI.
