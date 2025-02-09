def save_log(date, raw_text):
    file = open(f"./logs/{date}.log")
    file.write(raw_text)
    