import json
import os

PRIMARY_MEMORY_FILE = "data/memory.json"
FALLBACK_MEMORY_FILE = "/tmp/memory.json"

# Runtime pe decide karenge ki kaunsa path likhne layak hai
MEMORY_FILE = PRIMARY_MEMORY_FILE


def load_memory() -> list:
    for path in (PRIMARY_MEMORY_FILE, FALLBACK_MEMORY_FILE):
        if not os.path.exists(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            continue
    return []


def save_memory(memory: list) -> None:
    global MEMORY_FILE

    # Pehle primary (data/memory.json) pe try karein
    try:
        folder = os.path.dirname(PRIMARY_MEMORY_FILE)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(PRIMARY_MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(memory, file, ensure_ascii=False, indent=4)
        MEMORY_FILE = PRIMARY_MEMORY_FILE
        return
    except OSError:
        pass

    # Agar read-only filesystem hai (jaise Vercel), /tmp pe fallback karein
    with open(FALLBACK_MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, ensure_ascii=False, indent=4)
    MEMORY_FILE = FALLBACK_MEMORY_FILE


def add_message(memory: list, role: str, content: str) -> None:
    memory.append(
        {
            "role": role,
            "content": content
        }
    )
    return memory


if __name__ == "__main__":
    print("Loading memory...")
    memory = load_memory()

    print(memory)

    print("\nAdding messages...")

    memory = add_message(memory, "user", "Hello, how are you?")
    memory = add_message(memory, "assistant", "I'm good, thank you!")

    save_memory(memory)
    print(load_memory())