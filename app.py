import streamlit as st
import streamlit.components.v1 as components
import json

# Page config
st.set_page_config(
    page_title="Luyện Phát Âm Tiếng Anh 1 - Global Success",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Luyện Phát Âm Tiếng Anh 1")
st.caption("Chương trình Tiếng Anh 1 - Global Success")

# Database of Units from SGK Tiếng Anh 1 Global Success
DATA = {
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

# Sidebar selection
selected_unit = st.sidebar.selectbox("📚 Chọn Bài Học (Unit):", list(DATA.keys()))
unit_info = DATA[selected_unit]

st.subheader(f"📌 {selected_unit}")
st.write(f"🔤 **Âm chính (Phonics):** `{unit_info['phonics']}`")

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
        <button class="btn btn-rec" id="recBtn" onclick="toggleRecording()">🎙️ Bấm để nói</button>
    </div>

    <div class="result-box" id="resultBox" style="display:none;">
        <div id="statusText" style="font-size: 14px; color: #888;">Đã thu âm xong!</div>
        <div class="text-said">Bạn đã nói: <b id="userSpeech" style="color:#008CBA;">...</b></div>
        <div class="score" id="scoreText">0%</div>
        <div class="stars" id="starText">⭐⭐⭐</div>
        <div id="feedbackText" style="font-weight:bold; margin-top:5px;"></div>
    </div>

    <script>
        const targetText = "{target_text.lower().strip()}";
        let recognition = null;
        let isRecording = false;

        // Text To Speech
        function playAudio() {{
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance("{target_text}");
            utterance.lang = 'en-US';
            utterance.rate = 0.8; // Nói chậm chút cho học sinh tiểu học
            window.speechSynthesis.speak(utterance);
        }}

        // Levenshtein distance for similarity
        function similarity(s1, s2) {{
            s1 = s1.toLowerCase().replace(/[^a-z0-9 ]/g, "").trim();
            s2 = s2.toLowerCase().replace(/[^a-z0-9 ]/g, "").trim();
            
            if (s1 === s2) return 100;
            if (s1.length === 0 || s2.length === 0) return 0;
            
            // Check word inclusion for young learners
            const w1 = s1.split(" ");
            const w2 = s2.split(" ");
            let matches = 0;
            w2.forEach(w => {{ if (w1.includes(w)) matches++; }});
            let wordScore = (matches / Math.max(w1.length, w2.length)) * 100;

            return Math.min(100, Math.round(wordScore));
        }}

        // Speech Recognition
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

        if (!SpeechRecognition) {{
            alert("Trình duyệt của bạn chưa hỗ trợ thu âm trực tiếp. Hãy dùng Google Chrome, Safari hoặc Edge mới nhất!");
        }} else {{
            recognition = new SpeechRecognition();
            recognition.lang = 'en-US';
            recognition.interimResults = false;
            recognition.maxAlternatives = 1;

            recognition.onstart = function() {{
                isRecording = true;
                const btn = document.getElementById("recBtn");
                btn.innerText = "🛑 Đang nghe... Hãy nói!";
                btn.classList.add("recording");
            }};

            recognition.onresult = function(event) {{
                const transcript = event.results[0][0].transcript;
                document.getElementById("userSpeech").innerText = transcript;
                
                const matchScore = similarity(targetText, transcript);
                
                document.getElementById("resultBox").style.display = "block";
                document.getElementById("scoreText").innerText = matchScore + "%";

                let stars = "⭐";
                let feedback = "Cần cố gắng hơn nữa nhé! 💪";
                let color = "#d32f2f";

                if (matchScore >= 80) {{
                    stars = "⭐⭐⭐";
                    feedback = "Xuất sắc! Phát âm rất chuẩn! 🎉";
                    color = "#2e7d32";
                }} else if (matchScore >= 50) {{
                    stars = "⭐⭐";
                    feedback = "Rất tốt! Suýt soát chuẩn rồi! 👍";
                    color = "#f57c00";
                }}

                document.getElementById("starText").innerText = stars;
                document.getElementById("feedbackText").innerText = feedback;
                document.getElementById("feedbackText").style.color = color;
            }};

            recognition.onerror = function(event) {{
                alert("Không thể nhận diện giọng nói: " + event.error + ". Hãy cấp quyền Micro cho trình duyệt nhé!");
                stopRecState();
            }};

            recognition.onend = function() {{
                stopRecState();
            }};
        }}

        function stopRecState() {{
            isRecording = false;
            const btn = document.getElementById("recBtn");
            btn.innerText = "🎙️ Bấm để nói";
            btn.classList.remove("recording");
        }}

        function toggleRecording() {{
            if (!recognition) return;
            if (isRecording) {{
                recognition.stop();
            }} else {{
                recognition.start();
            }}
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=320)

st.info("💡 **Hướng dẫn học sinh:** Bấm **🔊 Nghe phát âm mẫu** để nghe cô giáo nói trước. Sau đó bấm **🎙️ Bấm để nói** và đọc to từ/câu đó lên để nhận điểm số nhé!")
