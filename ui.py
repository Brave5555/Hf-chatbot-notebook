# ui.py
from Chatbot import chat_once, ChatSession

def run_single_turn():
    """
    Simple one-question test.
    """
    user_msg = input("Ask me: ")
    reply = chat_once(user_msg)
    print("Bot:", reply)


def run_chat_loop():
    """
    Multi-turn CLI chat using ChatSession.
    """
    session = ChatSession()
    print("Chat started. Type 'quit' to exit.")
    while True:
        user_msg = input("You: ").strip()
        if user_msg.lower() in {"quit", "exit"}:
            print("Bye!")
            break
        reply = session.send(user_msg)
        print("Bot:", reply)


if __name__ == "__main__":
    # pick one
    # run_single_turn()
    run_chat_loop()
