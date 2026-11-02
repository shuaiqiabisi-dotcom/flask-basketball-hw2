from flask import Flask, render_template

app = Flask(__name__)

games = [
    {
        "title": "台大機械系隊",
        "author": "2026-10-15",
        "content": "比分 78:72 獲勝，全場投進 4 顆三分球，團隊防守快攻發揮出色。"
    },
    {
        "title": "清大機械系隊",
        "author": "2026-10-22",
        "content": "比分 65:68 殘念小輸，籃板球戰況拉鋸，下半場需要加強溝通與聯防。"
    },
    {
        "title": "交大資工系隊",
        "author": "2026-10-29",
        "content": "比分 82:70 獲勝，傳導順暢，第四節關鍵打出一波 12:2 的攻勢奠定勝基。"
    }
]

@app.route('/')
def index():
    return render_template('index.html', games=games)

if __name__ == '__main__':
    app.run(debug=True)
