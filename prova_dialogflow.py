from samples.detect_intent_audio import detect_intent_audio
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
project_id = "newagent-882e5"
language_code = "it"
session_id = "prova"

for i in range(0, 10):
    detect_intent_audio(project_id, session_id, "audio/t" + str(i) + ".wav", "it")
