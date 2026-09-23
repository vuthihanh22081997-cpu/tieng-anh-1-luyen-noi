import streamlit as st
import streamlit.components.v1 as components
import json

# Page config
st.set_page_config(
    page_title="Luyện Phát Âm Tiếng Anh 1 & 2 - Global Success",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Luyện Phát Âm Tiếng Anh 1 & 2")
st.caption("Chương trình Tiếng Anh Global Success - Lớp 1 & Lớp 2")

# Sidebar - Select Grade
grade = st.sidebar.selectbox("🏫 Chọn Khối Lớp:", ["Lớp 1 - Global Success", "Lớp 2 - Global Success"])

# Database for Grade 1
DATA_GRADE_1 = {
    "Unit 1: In the school playground": {
        "phonics": "Bb",
        "words": [
            {"en": "ball", "vi": "quả bóng"},
            {"en": "bike", "vi": "xe đạp"},
            {"en": "book", "vi": "quyển sách"}
        ],
        "sentences": [
            {"en": "Hi, I'm Bill.", "vi": "Xin chào, tớ là Bill."},
            {"en": "Bye, Bill.", "vi": "Tạm biệt Bill."}
        ]
    },
    "Unit 2: In the dining room": {
        "phonics": "Cc",
        "words": [
            {"en": "cake", "vi": "cái bánh"},
            {"en": "car", "vi": "xe ô tô"},
            {"en": "cat", "vi": "con mèo"},
            {"en": "cup", "vi": "cái tách/cốc"}
        ],
        "sentences": [
            {"en": "I have a car.", "vi": "Tớ có một chiếc xe ô tô."}
        ]
    },
    "Unit 3: At the street market": {
        "phonics": "Aa",
        "words": [
            {"en": "apple", "vi": "quả táo"},
            {"en": "bag", "vi": "cái túi"},
            {"en": "can", "vi": "lon nước"},
            {"en": "hat", "vi": "cái mũ"}
        ],
        "sentences": [
            {"en": "This is my bag.", "vi": "Đây là cái túi của tớ."}
        ]
    },
    "Unit 4: In the bedroom": {
        "phonics": "Dd",
        "words": [
            {"en": "desk", "vi": "bàn học"},
            {"en": "dog", "vi": "con chó"},
            {"en": "door", "vi": "cửa ra vào"},
            {"en": "duck", "vi": "con vịt"}
        ],
        "sentences": [
            {"en": "This is a dog.", "vi": "Đây là một con chó."}
        ]
    },
    "Unit 5: At the fish and chip shop": {
        "phonics": "Ii",
        "words": [
            {"en": "chicken", "vi": "thịt gà"},
            {"en": "chips", "vi": "khoai tây chiên"},
            {"en": "fish", "vi": "cá"},
            {"en": "milk", "vi": "sữa"}
        ],
        "sentences": [
            {"en": "I like milk.", "vi": "Tớ thích sữa."}
        ]
    },
    "Unit 6: In the classroom": {
        "phonics": "Ee",
        "words": [
            {"en": "bell", "vi": "cái chuông"},
            {"en": "pen", "vi": "bút mực"},
            {"en": "pencil", "vi": "bút chì"},
            {"en": "red", "vi": "màu đỏ"}
        ],
        "sentences": [
            {"en": "It's a red pen.", "vi": "Đó là một cây bút mực màu đỏ."}
        ]
    },
    "Unit 7: In the garden": {
        "phonics": "Gg",
        "words": [
            {"en": "garden", "vi": "khu vườn"},
            {"en": "gate", "vi": "cổng vào"},
            {"en": "girl", "vi": "cô bé"},
            {"en": "goat", "vi": "con dê"}
        ],
        "sentences": [
            {"en": "There's a garden.", "vi": "Có một khu vườn."}
        ]
    },
    "Unit 8: In the park": {
        "phonics": "Hh",
        "words": [
            {"en": "hair", "vi": "tóc"},
            {"en": "hand", "vi": "bàn tay"},
            {"en": "head", "vi": "cái đầu"},
            {"en": "horse", "vi": "con ngựa"}
        ],
        "sentences": [
            {"en": "Touch your hair.", "vi": "Chạm vào tóc của bạn."}
        ]
    },
    "Unit 9: In the shop": {
        "phonics": "Oo",
        "words": [
            {"en": "clocks", "vi": "đồng hồ"},
            {"en": "locks", "vi": "ổ khóa"},
            {"en": "mops", "vi": "cây lau nhà"},
            {"en": "pots", "vi": "cái nồi"}
        ],
        "sentences": [
            {"en": "How many clocks?", "vi": "Có bao nhiêu cái đồng hồ?"}
        ]
    },
    "Unit 10: At the zoo": {
        "phonics": "Mm",
        "words": [
            {"en": "mango", "vi": "quả xoài"},
            {"en": "monkey", "vi": "con khỉ"},
            {"en": "mother", "vi": "mẹ"},
            {"en": "mouse", "vi": "con chuột"}
        ],
        "sentences": [
            {"en": "That's a monkey.", "vi": "Kia là một con khỉ."}
        ]
    },
    "Unit 11: At the bus stop": {
        "phonics": "Uu",
        "words": [
            {"en": "bus", "vi": "xe buýt"},
            {"en": "run", "vi": "chạy"},
            {"en": "sun", "vi": "mặt trời"},
            {"en": "truck", "vi": "xe tải"}
        ],
        "sentences": [
            {"en": "He's running.", "vi": "Cậu ấy đang chạy."}
        ]
    },
    "Unit 12: At the lake": {
        "phonics": "Ll",
        "words": [
            {"en": "lake", "vi": "hồ nước"},
            {"en": "leaf", "vi": "lá cây"},
            {"en": "lemons", "vi": "quả chanh"}
        ],
        "sentences": [
            {"en": "Look at the lemons.", "vi": "Hãy nhìn những quả chanh."}
        ]
    },
    "Unit 13: In the school canteen": {
        "phonics": "Nn",
        "words": [
            {"en": "bananas", "vi": "quả chuối"},
            {"en": "noodles", "vi": "mì"},
            {"en": "nuts", "vi": "hạt lạc"}
        ],
        "sentences": [
            {"en": "She's having noodles.", "vi": "Cô ấy đang ăn mì."}
        ]
    },
    "Unit 14: In the toy shop": {
        "phonics": "Tt",
        "words": [
            {"en": "teddy bear", "vi": "gấu bông"},
            {"en": "tiger", "vi": "con hổ"},
            {"en": "top", "vi": "con quay"},
            {"en": "turtle", "vi": "con rùa"}
        ],
        "sentences": [
            {"en": "I can see a tiger.", "vi": "Tớ có thể thấy một con hổ."}
        ]
    },
    "Unit 15: At the football match": {
        "phonics": "Ff",
        "words": [
            {"en": "face", "vi": "khuôn mặt"},
            {"en": "father", "vi": "bố"},
            {"en": "foot", "vi": "bàn chân"},
            {"en": "football", "vi": "bóng đá"}
        ],
        "sentences": [
            {"en": "Point to your hand.", "vi": "Chỉ vào bàn tay của bạn."}
        ]
    },
    "Unit 16: At home": {
        "phonics": "Ww",
        "words": [
            {"en": "wash", "vi": "lau/rửa"},
            {"en": "water", "vi": "nước"},
            {"en": "window", "vi": "cửa sổ"}
        ],
        "sentences": [
            {"en": "How many windows can you see?", "vi": "Bạn nhìn thấy bao nhiêu cửa sổ?"},
            {"en": "I can see six.", "vi": "Tớ nhìn thấy sáu cái."}
        ]
    }
}

# Database for Grade 2
DATA_GRADE_2 = {
    "Unit 1: At my birthday party": {
        "phonics": "Pp",
        "words": [
            {"en": "pasta", "vi": "mì Ý"},
            {"en": "popcorn", "vi": "bỏng ngô"},
            {"en": "pizza", "vi": "bánh pizza"}
        ],
        "sentences": [
            {"en": "I like pasta.", "vi": "Tớ thích mì Ý."},
            {"en": "Pass me the pizza, please.", "vi": "Làm ơn chuyển giúp tớ bánh pizza."}
        ]
    },
    "Unit 2: In the backyard": {
        "phonics": "Kk",
        "words": [
            {"en": "kite", "vi": "con diều"},
            {"en": "bike", "vi": "xe đạp"},
            {"en": "kitten", "vi": "con mèo con"}
        ],
        "sentences": [
            {"en": "Look at the kite.", "vi": "Hãy nhìn con diều kìa."}
        ]
    },
    "Unit 3: At the seaside": {
        "phonics": "Ss",
        "words": [
            {"en": "sail", "vi": "cánh buồm"},
            {"en": "sand", "vi": "bãi cát"},
            {"en": "sea", "vi": "biển"}
        ],
        "sentences": [
            {"en": "I can see the sea.", "vi": "Tớ có thể nhìn thấy biển."}
        ]
    },
    "Unit 4: In the countryside": {
        "phonics": "Rr",
        "words": [
            {"en": "rainbow", "vi": "cầu vồng"},
            {"en": "river", "vi": "dòng sông"},
            {"en": "road", "vi": "con đường"}
        ],
        "sentences": [
            {"en": "Look at the rainbow.", "vi": "Hãy nhìn cầu vồng kìa."}
        ]
    },
    "Unit 5: In the classroom": {
        "phonics": "Qq",
        "words": [
            {"en": "question", "vi": "câu hỏi"},
            {"en": "quiz", "vi": "câu đố"},
            {"en": "square", "vi": "hình vuông"}
        ],
        "sentences": [
            {"en": "Point to the square.", "vi": "Chỉ vào hình vuông."}
        ]
    },
    "Unit 6: On the farm": {
        "phonics": "Xx / C c",
        "words": [
            {"en": "chicken", "vi": "con gà"},
            {"en": "cow", "vi": "con bò"},
            {"en": "horse", "vi": "con ngựa"}
        ],
        "sentences": [
            {"en": "Look at the cow.", "vi": "Hãy nhìn con bò kìa."}
        ]
    },
    "Unit 7: In the kitchen": {
        "phonics": "Jj",
        "words": [
            {"en": "jam", "vi": "mứt"},
            {"en": "jelly", "vi": "thạch"},
            {"en": "juice", "vi": "nước ép"}
        ],
        "sentences": [
            {"en": "Pass me the jam, please.", "vi": "Làm ơn chuyền giúp tớ lọ mứt."}
        ]
    },
    "Unit 8: In the village": {
        "phonics": "Vv",
        "words": [
            {"en": "van", "vi": "xe tải van"},
            {"en": "village", "vi": "ngôi làng"},
            {"en": "volleyball", "vi": "bóng chuyền"}
        ],
        "sentences": [
            {"en": "Can you draw a van?", "vi": "Bạn có thể vẽ một chiếc xe tải không?"}
        ]
    },
    "Unit 9: In the grocery store": {
        "phonics": "Yy",
        "words": [
            {"en": "yam", "vi": "khoai từ"},
            {"en": "yogurt", "vi": "sữa chua"},
            {"en": "yoyo", "vi": "cái yo-yo"}
        ],
        "sentences": [
            {"en": "I like yogurt.", "vi": "Tớ thích sữa chua."}
        ]
    },
    "Unit 10: At the zoo": {
        "phonics": "Zz",
        "words": [
            {"en": "zebra", "vi": "ngựa vằn"},
            {"en": "zebu", "vi": "bò u"},
            {"en": "zoo", "vi": "vườn bách thú"}
        ],
        "sentences": [
            {"en": "Look at the zebra.", "vi": "Hãy nhìn con ngựa vằn kìa."}
        ]
    },
    "Unit 11: In the playground": {
        "phonics": "Sl / Sw",
        "words": [
            {"en": "slide", "vi": "cầu trượt"},
            {"en": "swing", "vi": "xích đu"},
            {"en": "seesaw", "vi": "bập bênh"}
        ],
        "sentences": [
            {"en": "He's on the slide.", "vi": "Cậu ấy đang ở trên cầu trượt."}
        ]
    },
    "Unit 12: At the cafe": {
        "phonics": "Cc",
        "words": [
            {"en": "cake", "vi": "bánh ngọt"},
            {"en": "cup", "vi": "cái tách"},
            {"en": "tea", "vi": "trà"}
        ],
        "sentences": [
            {"en": "I'd like some tea, please.", "vi": "Cho tớ xin một ít trà."}
        ]
    },
    "Unit 13: In the math class": {
        "phonics": "Numbers 11-15",
        "words": [
            {"en": "eleven", "vi": "số 11"},
            {"en": "twelve", "vi": "số 12"},
            {"en": "thirteen", "vi": "số 13"},
            {"en": "fourteen", "vi": "số 14"},
            {"en": "fifteen", "vi": "số 15"}
        ],
        "sentences": [
            {"en": "I can see fifteen desks.", "vi": "Tớ nhìn thấy 15 cái bàn."}
        ]
    },
    "Unit 14: At home": {
        "phonics": "Family",
        "words": [
            {"en": "brother", "vi": "anh/em trai"},
            {"en": "sister", "vi": "chị/em gái"},
            {"en": "grandmother", "vi": "bà"}
        ],
        "sentences": [
            {"en": "This is my brother.", "vi": "Đây là anh trai tớ."}
        ]
    },
    "Unit 15: In the clothes shop": {
        "phonics": "Clothes",
        "words": [
            {"en": "shirt", "vi": "áo sơ mi"},
            {"en": "shoes", "vi": "đôi giày"},
            {"en": "shorts", "vi": "quần đùi"}
        ],
        "sentences": [
            {"en": "Look at my new shoes.", "vi": "Hãy nhìn đôi giày mới của tớ."}
        ]
    },
    "Unit 16: At the campsite": {
        "phonics": "Camping",
        "words": [
            {"en": "tent", "vi": "cái lều"},
            {"en": "teapot", "vi": "ấm trà"},
            {"en": "blanket", "vi": "cái chăn"}
        ],
        "sentences": [
            {"en": "There's a tent.", "vi": "Có một cái lều."}
        ]
    }
}

DATA = DATA_GRADE_1 if "Lớp 1" in grade else DATA_GRADE_2

# Sidebar selection
selected_unit = st.sidebar.selectbox("📚 Chọn Bài Học (Unit):", list(DATA.keys()))
unit_info = DATA[selected_unit]

st.subheader(f"📌 {selected_unit}")
st.write(f"🔤 **Âm / Chủ đề chính:** `{unit_info['phonics']}`")

# Type selection
practice_type = st.radio("🎯 Chọn nội dung luyện nói:", ["Từ vựng (Vocabulary)", "Mẫu câu (Sentence Patterns)"], horizontal=True)

if practice_type == "Từ vựng (Vocabulary)":
    items = unit_info["words"]
else:
    items = unit_info["sentences"]

selected_item = st.selectbox("👉 Chọn từ/câu muốn luyện:", [f"{item['en']} ({item['vi']})" for item in items])
target_text = selected_item.split(" (")[0].strip()
target_vi = selected_item.split(" (")[1].replace(")", "").strip()

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"### 🎯 Mẫu tiếng Anh: **{target_text}**")
with col2:
    st.markdown(f"### 💡 Nghĩa tiếng Việt: **{target_vi}**")

# Speech recognition & TTS component in HTML/JS
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            background-color: #f8f9fa;
            padding: 10px;
        }}
        .btn {{
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            margin: 8px;
            transition: all 0.2s ease-in-out;
        }}
        .btn-audio {{
            background-color: #4CAF50;
            color: white;
        }}
        .btn-audio:hover {{ background-color: #45a049; }}
        .btn-rec {{
            background-color: #008CBA;
            color: white;
        }}
        .btn-rec.recording {{
            background-color: #f44336;
            animation: pulse 1s infinite;
        }}
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}
        .result-box {{
            margin-top: 15px;
            padding: 15px;
            border-radius: 12px;
            background-color: #ffffff;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .score {{
            font-size: 28px;
            font-weight: bold;
            color: #2e7d32;
        }}
        .text-said {{
            font-size: 18px;
            color: #555;
            margin-top: 5px;
        }}
        .stars {{
            font-size: 24px;
            color: #ffc107;
        }}
    </style>
</head>
<body>

<div>
    <button class="btn btn-audio" onclick="playAudio()">🔊 Nghe phát âm mẫu</button>
    <button id="recBtn" class="btn btn-rec" onclick="toggleRecording()">🎙️ Nhấn vào đây để Nói</button>
</div>

<div id="resultBox" class="result-box" style="display:none;">
    <div id="stars" class="stars"></div>
    <div id="scoreText" class="score"></div>
    <div id="saidText" class="text-said"></div>
</div>

<script>
    const targetText = "{target_text}".toLowerCase().replace(/[^a-z0-9 ]/g, "").trim();

    function playAudio() {{
        window.speechSynthesis.cancel();
        const msg = new SpeechSynthesisUtterance("{target_text}");
        msg.lang = 'en-US';
        msg.rate = 0.8;
        window.speechSynthesis.speak(msg);
    }}

    let recognition = null;
    let isRecording = false;

    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {{
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        recognition = new SpeechRecognition();
        recognition.lang = 'en-US';
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.onstart = function() {{
            isRecording = true;
            const btn = document.getElementById('recBtn');
            btn.innerHTML = '⏹️ Đang nghe... (Nói xong dừng)';
            btn.classList.add('recording');
        }};

        recognition.onresult = function(event) {{
            const transcript = event.results[0][0].transcript.toLowerCase().replace(/[^a-z0-9 ]/g, "").trim();
            evaluateSpeech(transcript);
        }};

        recognition.onerror = function(event) {{
            stopRecordingState();
            alert("Không nhận diện được giọng nói hoặc chưa cấp quyền Micro: " + event.error);
        }};

        recognition.onend = function() {{
            stopRecordingState();
        }};
    }} else {{
        document.getElementById('recBtn').onclick = function() {{
            alert("Trình duyệt của bạn chưa hỗ trợ thu âm trực tiếp. Hãy dùng Chrome hoặc Safari mới nhất.");
        }};
    }}

    function toggleRecording() {{
        if (!recognition) return;
        if (isRecording) {{
            recognition.stop();
        }} else {{
            recognition.start();
        }}
    }}

    function stopRecordingState() {{
        isRecording = false;
        const btn = document.getElementById('recBtn');
        btn.innerHTML = '🎙️ Nhấn vào đây để Nói';
        btn.classList.remove('recording');
    }}

    function calculateSimilarity(str1, str2) {{
        if (str1 === str2) return 100;
        const words1 = str1.split(" ");
        const words2 = str2.split(" ");
        let matches = 0;
        words2.forEach(w => {{
            if (words1.includes(w)) matches++;
        }});
        let score = Math.round((matches / Math.max(words1.length, words2.length)) * 100);
        if (str1.includes(str2) || str2.includes(str1)) score = Math.max(score, 75);
        return score;
    }}

    function evaluateSpeech(said) {{
        const score = calculateSimilarity(targetText, said);
        const resultBox = document.getElementById('resultBox');
        const scoreText = document.getElementById('scoreText');
        const saidText = document.getElementById('saidText');
        const stars = document.getElementById('stars');

        resultBox.style.display = 'block';
        saidText.innerHTML = '🗣️ Em vừa nói: <i>"' + said + '"</i>';

        if (score >= 80) {{
            stars.innerHTML = '⭐⭐⭐';
            scoreText.style.color = '#2e7d32';
            scoreText.innerHTML = 'Chính xác ' + score + '% - Tuyệt vời! 🎉';
        }} else if (score >= 50) {{
            stars.innerHTML = '⭐⭐';
            scoreText.style.color = '#f57c00';
            scoreText.innerHTML = 'Chính xác ' + score + '% - Khá lắm, cố lên nhé! 👍';
        }} else {{
            stars.innerHTML = '⭐';
            scoreText.style.color = '#d32f2f';
            scoreText.innerHTML = 'Chính xác ' + score + '% - Em nghe và thử lại nhé! 💪';
        }}
    }}
</script>

</body>
</html>
"""

components.html(html_code, height=320)
