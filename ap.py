import json
from stt import transcribe_audio
from task_extractor import extract_tasks
from task_assigner import assign_tasks, load_team

AUDIO_FILE = r"C:\Users\dhara\OneDrive\Desktop\voice.wav\WhatsApp Audio 2025-11-29 at 11.23.23_80b9a493.mp3"

def main():
    print("\n--- STEP 1: Speech to Text ---")
    text = transcribe_audio(r"C:\Users\dhara\OneDrive\Desktop\voice.wav\WhatsApp Audio 2025-11-29 at 11.23.23_80b9a493.mp3")
    print("\nTRANSCRIBED TEXT:\n", text)

    print("\n--- STEP 2: Extracting Tasks ---")
    tasks = extract_tasks(text)

    print("\n--- STEP 3: Assigning Tasks ---")
    team = load_team()
    final = assign_tasks(tasks, team)

    print("\nFINAL OUTPUT:\n")
    for i, t in enumerate(final, 1):
        print(f"{i}. Task: {t['task']}")
        print(f"   Assigned To: {t['assigned_to']}")
        print(f"   Deadline: {t['deadline']}")
        print(f"   Priority: {t['priority']}")
        print(f"   Dependency: {t['dependency']}\n")

    # save JSON
    with open(r"C:\Users\dhara\OneDrive\Desktop\data\tasks.json", "w") as f:
        json.dump(final, f, indent=4)

    print("\nSaved output to output/tasks.json")


if __name__ == "__main__":
    main()
