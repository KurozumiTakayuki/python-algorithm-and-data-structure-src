def my_naive_search_text(text, pattern):
    """ 力任せ法による文字列検索 """

    # パターン末尾のインデックス
    p_end_idx = len(pattern) - 1

    # テキスト側の照合開始位置を表すインデックス
    t_start_idx = 0
    while t_start_idx < len(text):

        # テキスト側の照合中の位置を表すインデックス
        t_idx = t_start_idx

        # パターン側の照合中の位置を表すインデックス
        p_idx = 0
        while t_idx < len(text) and text[t_idx] == pattern[p_idx]:
            if p_idx == p_end_idx:
                # パターン末尾まで一致していた場合、一致部分の先頭位置を返す
                return t_start_idx

            # 照合位置を右側に1つずつ移動
            t_idx += 1
            p_idx += 1

        # テキスト側の照合開始位置を1つ移動
        t_start_idx += 1

    # 見つからない場合は-1を返す
    return -1


def main():
    text = "Simple is better than complex."
    pattern = "tha"
    idx = my_naive_search_text(text, pattern)
    print(idx)


main()
