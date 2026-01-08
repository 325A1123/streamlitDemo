import streamlit as st
import random
import time

# ===============================
# 背景・全体文字色
# ===============================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #312e81, #020617);
    }

    html, body, .stApp,
    h1, h2, h3, h4, h5, h6,
    p, span, label {
        color: #ffffff !important;
    }

    .stTextInput label {
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===============================
# ネオンタイトル
# ===============================
st.markdown(
    """
    <style>
    .neon-title {
        text-align: center;
        font-size: 34px;
        font-weight: 900;
        white-space: nowrap;
        color: #e0f2fe;
        text-shadow:
            0 0 4px #38bdf8,
            0 0 8px #38bdf8,
            0 0 16px #0ea5e9,
            0 0 32px #0ea5e9;
        margin-bottom: 20px;
    }
    </style>

    <div class="neon-title">
        タイピングゲーム（10問クリア制）
    </div>
    """,
    unsafe_allow_html=True
)



# ===============================
# 単語リスト
# ===============================
words = [
    # 食べ物
    "りんご","ばなな","おれんじ","めろん","いちご","ぶどう","もも",
    "すいか","ぱいなっぷる","きうい","れもん","みかん",
    "らーめん","うどん","そば","かれー","しちゅー","やきにく",
    "すし","てんぷら","おにぎり","おべんとう","はんばーぐ",
    "おむらいす","たこやき","おこのみやき","からあげ",

    # 動物
    "ねこ","いぬ","うさぎ","はむすたー","ぱんだ","こあら",
    "きりん","ぞう","らいおん","とら","くま","さる",
    "ひよこ","ぺんぎん","いるか","くじら",

    # 身近なもの
    "えんぴつ","しゃーぷぺん","けしごむ","のーと","ちょうし",
    "ぱそこん","きーぼーど","まうす","すまーとふぉん",
    "かばん","さいふ","とけい","めがね","みずとう",

    # 場所・自然
    "がっこう","こうえん","えき","びょういん","としょかん",
    "やま","かわ","うみ","そら","たいよう","つき",

    # その他
    "げーむ","たいぴんぐ","ぷろぐらみんぐ",
    "たいぴんぐげーむ",
    "すとりーむりっとあぷり"
]

CLEAR_COUNT = 10

# ===============================
# セッション初期化
# ===============================
if "target" not in st.session_state:
    st.session_state.target = random.choice(words)

if "count" not in st.session_state:
    st.session_state.count = 0

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "input" not in st.session_state:
    st.session_state.input = ""

if "flash" not in st.session_state:
    st.session_state.flash = False

# ===============================
# 判定処理
# ===============================
def check_answer():
    if st.session_state.input == st.session_state.target:
        st.session_state.count += 1
        st.session_state.target = random.choice(words)
        st.session_state.flash = True
    st.session_state.input = ""

# ===============================
# クリア画面
# ===============================
if st.session_state.count >= CLEAR_COUNT:
    elapsed = time.time() - st.session_state.start_time
    st.balloons()
    st.success("🏆 ゲームクリア！")
    st.write(f"かかった時間：{elapsed:.2f} 秒")

    if st.button("もう一度遊ぶ"):
        st.session_state.count = 0
        st.session_state.target = random.choice(words)
        st.session_state.start_time = time.time()
        st.session_state.input = ""
        st.rerun()

    st.stop()

# ===============================
# ゲーム画面
# ===============================
st.markdown(
    f"""
    <div style="
        background-color:#020617;
        padding:30px;
        border-radius:20px;
        max-width:520px;
        margin:30px auto;
        box-shadow:0 20px 40px rgba(0,0,0,0.6);
        border:2px solid #2563eb;
        text-align:center;
    ">
        <div style="font-size:16px; color:#93c5fd;">
            進捗 {st.session_state.count} / {CLEAR_COUNT}
        </div>
        <div style="
            font-size:42px;
            font-weight:900;
            margin:20px 0;
            letter-spacing:3px;
        ">
            {st.session_state.target}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ===============================
# 入力欄
# ===============================
st.text_input(
    "ここに入力",
    key="input",
    on_change=check_answer
)
