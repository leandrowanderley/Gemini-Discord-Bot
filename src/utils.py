
def split_message(message, limit=2000):
    return [message[i:i + limit] for i in range(0, len(message), limit)]
