def main():
    start_time = time.perf_counter()
    for _ in range(1000):
        text = ''.join(random.choices(string.ascii_letters, k=10000))
        pattern = "abc"
        my_bm_search_text(text, pattern)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(elapsed_time)
