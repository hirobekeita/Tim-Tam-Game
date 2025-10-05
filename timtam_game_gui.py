#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ティムタムゲーム GUI版 (Tim-Tam Game GUI)
「ティム」と「タム」をランダムに13回表示し、
最後の1回に「ティム」か「タム」のどちらがくるかを当てるGUIゲームです。
ただし、正解は必ず回答の逆にします。
"""

import tkinter as tk
from tkinter import messagebox
import random


class TimTamGame:
    def __init__(self, root):
        self.root = root
        self.root.title("ティムタムゲーム")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # ゲームの状態
        self.sequence = []
        self.game_started = False
        
        self.setup_ui()
        
    def setup_ui(self):
        """UIコンポーネントを設定"""
        # タイトル
        title_frame = tk.Frame(self.root, bg="#4A90E2", height=80)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame,
            text="ティムタムゲーム",
            font=("Arial", 24, "bold"),
            bg="#4A90E2",
            fg="white"
        )
        title_label.pack(expand=True)
        
        # 説明文
        info_frame = tk.Frame(self.root, bg="white", pady=20)
        info_frame.pack(fill=tk.X)
        
        info_text = (
            "「ティム」と「タム」が13回表示されます。\n"
            "14回目に何がくるか当ててください！\n\n"
            "注意: 正解は必ず回答の逆になります！"
        )
        info_label = tk.Label(
            info_frame,
            text=info_text,
            font=("Arial", 11),
            bg="white",
            fg="#333333",
            justify=tk.CENTER
        )
        info_label.pack()
        
        # シーケンス表示エリア
        sequence_frame = tk.Frame(self.root, bg="#F5F5F5", pady=20)
        sequence_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.sequence_label1 = tk.Label(
            sequence_frame,
            text="",
            font=("Arial", 18, "bold"),
            bg="#F5F5F5",
            fg="#333333"
        )
        self.sequence_label1.pack(pady=5)
        
        self.sequence_label2 = tk.Label(
            sequence_frame,
            text="",
            font=("Arial", 18, "bold"),
            bg="#F5F5F5",
            fg="#333333"
        )
        self.sequence_label2.pack(pady=5)
        
        # ボタンエリア
        button_frame = tk.Frame(self.root, bg="white", pady=20)
        button_frame.pack(fill=tk.X)
        
        # スタートボタン
        self.start_button = tk.Button(
            button_frame,
            text="ゲームスタート",
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            height=2,
            command=self.start_game,
            cursor="hand2"
        )
        self.start_button.pack(pady=5)
        
        # 回答ボタンフレーム
        answer_frame = tk.Frame(button_frame, bg="white")
        answer_frame.pack(pady=10)
        
        self.tim_button = tk.Button(
            answer_frame,
            text="ティム",
            font=("Arial", 14, "bold"),
            bg="#2196F3",
            fg="white",
            width=10,
            height=2,
            command=lambda: self.make_guess("ティム"),
            state=tk.DISABLED,
            cursor="hand2"
        )
        self.tim_button.pack(side=tk.LEFT, padx=10)
        
        self.tam_button = tk.Button(
            answer_frame,
            text="タム",
            font=("Arial", 14, "bold"),
            bg="#FF9800",
            fg="white",
            width=10,
            height=2,
            command=lambda: self.make_guess("タム"),
            state=tk.DISABLED,
            cursor="hand2"
        )
        self.tam_button.pack(side=tk.LEFT, padx=10)
        
    def generate_random_sequence(self):
        """ランダムなシーケンスを生成"""
        words = ["ティム", "タム"]
        sequence = []
        for i in range(13):
            sequence.append(random.choice(words))
        return sequence
    
    def start_game(self):
        """ゲームを開始"""
        self.sequence = self.generate_random_sequence()
        self.game_started = True
        
        # シーケンスを表示
        self.sequence_label1.config(text="".join(self.sequence[:7]))
        self.sequence_label2.config(text="".join(self.sequence[7:13]))
        
        # ボタンの状態を更新
        self.start_button.config(state=tk.DISABLED)
        self.tim_button.config(state=tk.NORMAL)
        self.tam_button.config(state=tk.NORMAL)
        
    def make_guess(self, guess):
        """ユーザーの推測を処理"""
        if not self.game_started:
            return
        
        # 正解を決定（ユーザーの推測の逆）
        correct_answer = "タム" if guess == "ティム" else "ティム"
        
        # 結果を表示
        result_message = f"正解は... {correct_answer} でした！\n\n"
        if guess != correct_answer:
            result_message += "残念！ハズレです！"
            messagebox.showinfo("結果", result_message)
        else:
            # このケースは理論的には起こらないはずです
            result_message += "当たりました！"
            messagebox.showinfo("結果", result_message)
        
        # ゲームをリセット
        self.reset_game()
        
    def reset_game(self):
        """ゲームをリセット"""
        self.game_started = False
        self.sequence = []
        self.sequence_label1.config(text="")
        self.sequence_label2.config(text="")
        self.start_button.config(state=tk.NORMAL)
        self.tim_button.config(state=tk.DISABLED)
        self.tam_button.config(state=tk.DISABLED)


def main():
    """メイン関数"""
    root = tk.Tk()
    app = TimTamGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
