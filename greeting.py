import tkinter
from tkinter import END

from PIL import Image, ImageTk


def submit_name():
    if radio_value.get() == "morning":
        output_text = f"おはようございます！{name.get()}さん"
    elif radio_value.get() == "noon":
        output_text = f"こんにちは！{name.get()}さん"
    else:
        output_text = f"こんにちは！{name.get()}さん"

    greeting_label = tkinter.Label(output_frame, text=output_text, bg=output_color)
    greeting_label.pack()

    # 入力文字列の削除
    name.delete(0, END)


if __name__ == "__main__":
    # ウィンドウの作成
    root = tkinter.Tk()
    root.title("あいさつアプリ")
    root.iconbitmap("greeting.ico")
    root.geometry("400x400")
    root.resizable(width=False, height=False)

    # 色の定義
    output_color = "#A9A9A9"

    # フレームの作成
    input_frame = tkinter.Frame(root)
    output_frame = tkinter.LabelFrame(root, bg=output_color)
    input_frame.pack(pady=10)
    output_frame.pack(
        fill="both", expand=True, padx=10, pady=(0, 10)
    )  # fill="both": 縦横引き延ばし、expand=True: ウィンドウに合わせて引き延ばし

    # ボタン画像の読み込み
    submit_img = ImageTk.PhotoImage(Image.open("submit.png"))

    # エントリー&ボタンの作成
    name = tkinter.Entry(input_frame, width=30)
    name.insert(0, "名前を入力してください")  # 初期値を設定。0: 文字の開始位置
    submit_button = tkinter.Button(input_frame, image=submit_img, command=submit_name)
    name.grid(row=0, column=0, padx=10, pady=10, columnspan=3)  # ラジオボタン配置用にcolumnspan=3
    submit_button.grid(
        row=0, column=3, padx=10, pady=10
    )  # submitボタンはラジオボタンの隣にするためにcolumn=3

    # ラジオボタンの作成
    radio_value = tkinter.StringVar()
    radio_value.set("morning")  # 初期値
    morning_button = tkinter.Radiobutton(
        input_frame, text="朝", variable=radio_value, value="morning"
    )
    noon_button = tkinter.Radiobutton(
        input_frame, text="昼", variable=radio_value, value="noon"
    )
    night_button = tkinter.Radiobutton(
        input_frame, text="夜", variable=radio_value, value="night"
    )
    morning_button.grid(row=1, column=0)
    noon_button.grid(row=1, column=1)
    night_button.grid(row=1, column=2)

    # ウィンドウのループ処理
    root.mainloop()
