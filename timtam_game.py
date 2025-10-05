#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ティムタムゲーム (Tim-Tam Game)
「ティム」と「タム」を順不同でランダムに7回表示し、改行して6回表示して、
最後の1回に「ティム」か「タム」のどちらがくるかを当てるゲームです。
ただし、正解は必ず回答の逆にします。
"""

import random


def generate_alternating_sequence():
    """
    「ティム」と「タム」がリズムよく一つずつ計13回表示される配列を生成します。
    ランダムに開始する単語を選び、その後交互に配置します。
    """
    words = ["ティム", "タム"]
    # ランダムに開始する単語を選択
    start_word = random.choice([0, 1])
    
    sequence = []
    for i in range(13):
        sequence.append(words[(start_word + i) % 2])
    
    return sequence


def display_sequence(sequence):
    """
    シーケンスを表示します。
    最初の7個を1行に、次の6個を2行目に表示します。
    """
    # 最初の7個を表示
    print("".join(sequence[:7]))
    # 次の6個を表示
    print("".join(sequence[7:13]))


def get_user_guess():
    """
    ユーザーの推測を取得します。
    """
    while True:
        guess = input("\n14回目は何がくると思いますか？（ティム または タム）: ").strip()
        if guess in ["ティム", "タム"]:
            return guess
        else:
            print("「ティム」または「タム」を入力してください。")


def determine_answer(guess):
    """
    ユーザーの推測の逆を正解として返します。
    """
    if guess == "ティム":
        return "タム"
    else:
        return "ティム"


def main():
    """
    ゲームのメイン関数
    """
    print("=" * 40)
    print("ティムタムゲームへようこそ！")
    print("=" * 40)
    print("\n「ティム」と「タム」が13回表示されます。")
    print("14回目に何がくるか当ててください！\n")
    
    # 交互に配置されたシーケンスを生成
    sequence = generate_alternating_sequence()
    
    # シーケンスを表示
    display_sequence(sequence)
    
    # ユーザーの推測を取得
    user_guess = get_user_guess()
    
    # 正解を決定（ユーザーの推測の逆）
    correct_answer = determine_answer(user_guess)
    
    # 結果を表示
    print(f"\n正解は... {correct_answer} でした！")
    
    if user_guess != correct_answer:
        print("残念！ハズレです！")
    else:
        # このケースは理論的には起こらないはずです
        print("当たりました！")
    
    print("\nゲーム終了！ありがとうございました！")


if __name__ == "__main__":
    main()
