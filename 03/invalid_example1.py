def read_file_and_reverse_it(filename: str) -> str:
    with open(filename) as f:
        # bytesをstrに変換
        return f.read().encode('utf-8')[::-1]
