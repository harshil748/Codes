from openai import OpenAI

def check_api_key(api_key):
    try:
        client = OpenAI(api_key=api_key)
        client.models.list()
        print("✅ API key is valid.")
    except Exception as e:
        print("❌ API key is invalid or not working.")
        print(f"Error: {e}")

def main():
    while True:
        api_key = input("\nEnter OpenAI API key (or type 'exit' to quit): ").strip()

        if api_key.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not api_key:
            print("Please enter a valid API key.")
            continue

        check_api_key(api_key)

if __name__ == "__main__":
    main()