import streamlit as st
import streamlit.components.v1 as components
import json

# Page config
st.set_page_config(
    page_title="Luyện Phát Âm Tiếng Anh 1 & 2 - Global Success",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Website Luyện Phát Âm Tiếng Anh")
st.caption("Chương trình Tiếng Anh Tiểu Học - Global Success (Bộ Giáo Dục & Đào Tạo)")

# Database for Grade 1 and Grade 2
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

DATA_GRADE_2 = {
    "Unit 1: At my birthday party": {
        "phonics": "Pp",
        "words": [
            {"en": "pasta", "vi": "mì Ý"},
            {"en": "popcorn", "vi": "bỏng ngô"},
            {"en": "pizza", "vi": "bánh pizza"},
            {"en": "cake", "vi": "bánh sinh nhật"}
        ],
        "sentences": [
            {"en": "I like pasta.", "vi": "Tớ thích mì Ý."},
            {"en": "Pass me the pizza, please.", "vi": "Làm ơn chuyển cho tớ bánh pizza."}
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
            {"en": "Look at the kite.", "vi": "Hãy nhìn con diều kìa."},
            {"en": "Is there a kitten?", "vi": "Có một con mèo con phải không?"}
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
            {"en": "Look at the sea.", "vi": "Hãy nhìn ngắm biển kìa."},
            {"en": "I like sand.", "vi": "Tớ thích cát biển."}
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
            {"en": "Look at the rainbow.", "vi": "Hãy nhìn cầu vồng kìa."},
            {"en": "There's a road.", "vi": "Có một con đường."}
        ]
    },
    "Unit 5: In the classroom": {
        "phonics": "Qq",
        "words": [
            {"en": "question", "vi": "câu hỏi"},
            {"en": "quiz", "vi": "câu đố/bài kiểm tra ngắn"},
            {"en": "square", "vi": "hình vuông"}
        ],
        "sentences": [
            {"en": "Answer the question.", "vi": "Trả lời câu hỏi."},
            {"en": "It's a quiz.", "vi": "Đó là một bài đố vui."}
        ]
    },
    "Unit 6: On the farm": {
        "phonics": "Xx",
        "words": [
            {"en": "box", "vi": "cái hộp"},
            {"en": "fox", "vi": "con cáo"},
            {"en": "ox", "vi": "con bò tót"}
        ],
        "sentences": [
            {"en": "Look at the fox.", "vi": "Hãy nhìn con cáo kìa."},
            {"en": "It's in the box.", "vi": "Nó ở trong cái hộp."}
        ]
    },
    "Unit 7: In the kitchen": {
        "phonics": "Jj",
        "words": [
            {"en": "jam", "vi": "mứt"},
            {"en": "jelly", "vi": "thạch"},
            {"en": "juice", "vi": "nước ép hoa quả"}
        ],
        "sentences": [
            {"en": "Pass me the jam, please.", "vi": "Làm ơn đưa tớ lọ mứt."},
            {"en": "I like juice.", "vi": "Tớ thích nước ép."}
        ]
    },
    "Unit 8: In the village": {
        "phonics": "Vv",
        "words": [
            {"en": "van", "vi": "xe tải nhỏ"},
            {"en": "village", "vi": "ngôi làng"},
            {"en": "volleyball", "vi": "bóng chuyền"}
        ],
        "sentences": [
            {"en": "Can you draw a van?", "vi": "Bạn có thể vẽ chiếc xe tải không?"},
            {"en": "Yes, I can.", "vi": "Tớ có thể."}
        ]
    },
    "Unit 9: In the grocery store": {
        "phonics": "Yy",
        "words": [
            {"en": "yam", "vi": "khoai từ"},
            {"en": "yo-yo", "vi": "cái yo-yo"},
            {"en": "yogurt", "vi": "sữa chua"}
        ],
        "sentences": [
            {"en": "I'd like some yogurt.", "vi": "Tớ muốn ăn một ít sữa chua."}
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
        "phonics": "Phát âm từ chỉ hoạt động",
        "words": [
            {"en": "slide", "vi": "cầu trượt"},
            {"en": "drive", "vi": "lái xe"},
            {"en": "ride", "vi": "cưỡi/đi xe đạp"}
        ],
        "sentences": [
            {"en": "I can ride a bike.", "vi": "Tớ có thể đi xe đạp."}
        ]
    },
    "Unit 12: At the café": {
        "phonics": "Âm nguyên âm",
        "words": [
            {"en": "cake", "vi": "bánh ngọt"},
            {"en": "grape", "vi": "quả nho"},
            {"en": "table", "vi": "cái bàn"}
        ],
        "sentences": [
            {"en": "She's eating a cake.", "vi": "Cô ấy đang ăn bánh."}
        ]
    },
    "Unit 13: In the Maths class": {
        "phonics": "Số đếm 11 - 15",
        "words": [
            {"en": "eleven", "vi": "số 11"},
            {"en": "twelve", "vi": "số 12"},
            {"en": "thirteen", "vi": "số 13"},
            {"en": "fourteen", "vi": "số 14"},
            {"en": "fifteen", "vi": "số 15"}
        ],
        "sentences": [
            {"en": "How many books?", "vi": "Có bao nhiêu quyển sách?"},
            {"en": "Eleven books.", "vi": "11 quyển sách."}
        ]
    },
    "Unit 14: At home": {
        "phonics": "Số đếm 16 - 20 & Gia đình",
        "words": [
            {"en": "sixteen", "vi": "số 16"},
            {"en": "seventeen", "vi": "số 17"},
            {"en": "eighteen", "vi": "số 18"},
            {"en": "nineteen", "vi": "số 19"},
            {"en": "twenty", "vi": "số 20"}
        ],
        "sentences": [
            {"en": "How old is your brother?", "vi": "Anh/em trai bạn bao nhiêu tuổi?"}
        ]
    },
    "Unit 15: In the clothes shop": {
        "phonics": "Trang phục",
        "words": [
            {"en": "shirt", "vi": "áo sơ mi"},
            {"en": "shoes", "vi": "đôi giày"},
            {"en": "shorts", "vi": "quần đùi"}
        ],
        "sentences": [
            {"en": "Put on your shoes.", "vi": "Hãy đi giày vào nào."}
        ]
    },
    "Unit 16: At the campsite": {
        "phonics": "Đồ dùng cắm trại",
        "words": [
            {"en": "blanket", "vi": "cái chăn"},
            {"en": "teapot", "vi": "ấm trà"},
            {"en": "tent", "vi": "cái lều"}
        ],
        "sentences": [
            {"en": "Pass me the blanket, please.", "vi": "Làm ơn đưa tớ cái chăn."}
        ]
    }
}

# Sidebar selection for Grade
st.sidebar.header("🏫 CHỌN LỚP HỌC")
selected_grade = st.sidebar.radio(
    "Chọn khối lớp:",
    ["Tiếng Anh 1 - Global Success", "Tiếng Anh 2 - Global Success"]
)

if selected_grade == "Tiếng Anh 1 - Global Success":
    current_data = DATA_GRADE_1
    st.sidebar.info("📘 Đang chọn: Tiếng Anh 1")
else:
    current_data = DATA_GRADE_2
    st.sidebar.info("📙 Đang chọn: Tiếng Anh 2")

st.sidebar.markdown("---")
st.sidebar.header("📚 CHỌN BÀI HỌC")
selected_unit = st.sidebar.selectbox("Danh sách Unit:", list(current_data.keys()))

unit_info = current_data[selected_unit]

st.subheader(f"📌 {selected_grade} - {selected_unit}")
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
            padding: 14px 28px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            margin: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.2s ease-in-out;
        }}
        .btn-audio {{
            background-color: #4CAF50;
            color: white;
        }}
        .btn-audio:hover {{ background-color: #45a049; transform: scale(1.03); }}
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
            padding: 20px;
            border-radius: 15px;
            background-color: #ffffff;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }}
        .score {{
            font-size: 32px;
            font-weight: bold;
            color: #2e7d32;
        }}
        .text-said {{
            font-size: 20px;
            color: #444;
            margin-top: 8px;
        }}
        .stars {{
            font-size: 30px;
            color: #ffc107;
            margin-top: 5px;
        }}
        .feedback {{
            font-size: 18px;
            font-weight: bold;
            color: #0277bd;
            margin-top: 8px;
        }}
    </style>
</head>
<body>

    <div>
        <button class="btn btn-audio" onclick="playAudio()">🔊 1. Nghe Phát Âm Mẫu</button>
        <button id="recBtn" class="btn btn-rec" onclick="toggleRecording()">🎙️ 2. Nhấn Vào Để Nói</button>
    </div>

    <div id="status" style="margin-top:10px; font-weight:bold; color:#666;"></div>

    <div id="result" class="result-box" style="display:none;">
        <div class="stars" id="starsDisplay"></div>
        <div class="score" id="scoreDisplay">0%</div>
        <div class="feedback" id="feedbackDisplay"></div>
        <div class="text-said" id="textSaidDisplay"></div>
    </div>

    <script>
        const targetText = "{target_text}";
        let recognition = null;
        let isRecording = false;

        function playAudio() {{
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(targetText);
            utterance.lang = 'en-US';
            utterance.rate = 0.85; // slightly slower for young learners
            window.speechSynthesis.speak(utterance);
        }}

        function initRecognition() {{
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRecognition) {{
                document.getElementById('status').innerHTML = '⚠️ Trình duyệt không hỗ trợ nhận diện giọng nói. Hãy dùng Chrome hoặc Safari nhé!';
                return null;
            }}
            const rec = new SpeechRecognition();
            rec.lang = 'en-US';
            rec.interimResults = false;
            rec.maxAlternatives = 1;

            rec.onstart = function() {{
                isRecording = true;
                document.getElementById('recBtn').classList.add('recording');
                document.getElementById('recBtn').innerText = '🔴 Đang nghe bé nói...';
                document.getElementById('status').innerText = 'Hãy nói rõ chữ tiếng Anh nhé!';
            }};

            rec.onresult = function(event) {{
                const transcript = event.results[0][0].transcript;
                evaluatePronunciation(transcript);
            }};

            rec.onerror = function(event) {{
                console.error(event.error);
                document.getElementById('status').innerText = '⚠️ Chưa nghe rõ, bé bấm nói lại nhé!';
                stopRecordingState();
            }};

            rec.onend = function() {{
                stopRecordingState();
            }};

            return rec;
        }}

        function stopRecordingState() {{
            isRecording = false;
            document.getElementById('recBtn').classList.remove('recording');
            document.getElementById('recBtn').innerText = '🎙️ 2. Nhấn Vào Để Nói';
        }}

        function toggleRecording() {{
            if (!recognition) {{
                recognition = initRecognition();
            }}
            if (!recognition) return;

            if (isRecording) {{
                recognition.stop();
            }} else {{
                recognition.start();
            }}
        }}

        function cleanString(str) {{
            return str.toLowerCase().replace(/[^a-z0-9 ]/g, '').trim();
        }}

        function evaluatePronunciation(saidText) {{
            const cleanTarget = cleanString(targetText);
            const cleanSaid = cleanString(saidText);

            document.getElementById('result').style.display = 'block';
            document.getElementById('textSaidDisplay').innerHTML = '🗣️ Bé vừa nói: <b>"' + saidText + '"</b>';

            let score = 0;
            if (cleanSaid === cleanTarget) {{
                score = 100;
            }} else {{
                // Calculate word overlap accuracy
                const targetWords = cleanTarget.split(' ');
                const saidWords = cleanSaid.split(' ');
                let matched = 0;
                targetWords.forEach(w => {{
                    if (saidWords.includes(w)) matched++;
                }});
                score = Math.round((matched / targetWords.length) * 100);
                if (score === 0 && cleanSaid.length > 0) {{
                    score = 40; // minimum score for attempt
                }}
            }}

            document.getElementById('scoreDisplay').innerText = score + '% Chính Xác';

            let stars = '';
            let feedback = '';
            if (score >= 85) {{
                stars = '⭐⭐⭐';
                feedback = '🎉 Xuất sắc! Bé phát âm rất chuẩn!';
            }} else if (score >= 60) {{
                stars = '⭐⭐';
                feedback = '👍 Rất tốt! Bé cố gắng phát âm rõ hơn nữa nhé!';
            }} else {{
                stars = '⭐';
                feedback = '💪 Bé lắng nghe mẫu và thử lại nào!';
            }}

            document.getElementById('starsDisplay').innerText = stars;
            document.getElementById('feedbackDisplay').innerText = feedback;
            document.getElementById('status').innerText = '✅ Đã hoàn thành đánh giá!';
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=350)
