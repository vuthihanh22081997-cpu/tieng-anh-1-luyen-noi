import streamlit as st
import streamlit.components.v1 as components
import json

# Page config
st.set_page_config(
    page_title="Luyện Phát Âm Tiếng Anh Tiểu Học - Global Success",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Luyện Phát Âm Tiếng Anh Tiểu Học")
st.caption("Chương trình Tiếng Anh Lớp 1 - 5 (Bộ sách Global Success)")

# Database for Grades 1 to 5
DATA = {
    "Lớp 1": {
        "Unit 1: In the school playground": {
            "phonics": "Bb",
            "words": [{"en": "ball", "vi": "quả bóng"}, {"en": "bike", "vi": "xe đạp"}, {"en": "book", "vi": "quyển sách"}],
            "sentences": [{"en": "Hi, I'm Bill.", "vi": "Xin chào, tớ là Bill."}, {"en": "Bye, Bill.", "vi": "Tạm biệt Bill."}]
        },
        "Unit 2: In the dining room": {
            "phonics": "Cc",
            "words": [{"en": "cake", "vi": "cái bánh"}, {"en": "car", "vi": "xe ô tô"}, {"en": "cat", "vi": "con mèo"}, {"en": "cup", "vi": "cái cốc"}],
            "sentences": [{"en": "I have a car.", "vi": "Tớ có một chiếc xe ô tô."}]
        },
        "Unit 3: At the street market": {
            "phonics": "Aa",
            "words": [{"en": "apple", "vi": "quả táo"}, {"en": "bag", "vi": "cái túi"}, {"en": "can", "vi": "lon nước"}, {"en": "hat", "vi": "cái mũ"}],
            "sentences": [{"en": "This is my bag.", "vi": "Đây là cái túi của tớ."}]
        },
        "Unit 4: In the bedroom": {
            "phonics": "Dd",
            "words": [{"en": "desk", "vi": "bàn học"}, {"en": "dog", "vi": "con chó"}, {"en": "door", "vi": "cửa ra vào"}, {"en": "duck", "vi": "con vịt"}],
            "sentences": [{"en": "This is a dog.", "vi": "Đây là một con chó."}]
        },
        "Unit 5: At the fish and chip shop": {
            "phonics": "Ii",
            "words": [{"en": "chicken", "vi": "thịt gà"}, {"en": "chips", "vi": "khoai tây chiên"}, {"en": "fish", "vi": "cá"}, {"en": "milk", "vi": "sữa"}],
            "sentences": [{"en": "I like milk.", "vi": "Tớ thích sữa."}]
        },
        "Unit 6: In the classroom": {
            "phonics": "Ee",
            "words": [{"en": "bell", "vi": "cái chuông"}, {"en": "pen", "vi": "bút mực"}, {"en": "pencil", "vi": "bút chì"}, {"en": "red", "vi": "màu đỏ"}],
            "sentences": [{"en": "It's a red pen.", "vi": "Đó là một cây bút mực màu đỏ."}]
        },
        "Unit 7: In the garden": {
            "phonics": "Gg",
            "words": [{"en": "garden", "vi": "khu vườn"}, {"en": "gate", "vi": "cổng vào"}, {"en": "girl", "vi": "cô bé"}, {"en": "goat", "vi": "con dê"}],
            "sentences": [{"en": "There's a garden.", "vi": "Có một khu vườn."}]
        },
        "Unit 8: In the park": {
            "phonics": "Hh",
            "words": [{"en": "hair", "vi": "tóc"}, {"en": "hand", "vi": "bàn tay"}, {"en": "head", "vi": "cái đầu"}, {"en": "horse", "vi": "con ngựa"}],
            "sentences": [{"en": "Touch your hair.", "vi": "Chạm vào tóc của bạn."}]
        }
    },
    "Lớp 2": {
        "Unit 1: At my birthday party": {
            "phonics": "Pp",
            "words": [{"en": "pasta", "vi": "mì Ý"}, {"en": "popcorn", "vi": "bỏng ngô"}, {"en": "pizza", "vi": "bánh pizza"}],
            "sentences": [{"en": "I like popcorn.", "vi": "Tớ thích ăn bỏng ngô."}]
        },
        "Unit 2: In the backyard": {
            "phonics": "Kk",
            "words": [{"en": "kite", "vi": "con diều"}, {"en": "bike", "vi": "xe đạp"}, {"en": "kitten", "vi": "mèo con"}],
            "sentences": [{"en": "He's flying a kite.", "vi": "Cậu ấy đang thả diều."}]
        },
        "Unit 3: At the seaside": {
            "phonics": "Ss",
            "words": [{"en": "sea", "vi": "biển"}, {"en": "sand", "vi": "cát"}, {"en": "sun", "vi": "mặt trời"}],
            "sentences": [{"en": "Let's look at the sea.", "vi": "Hãy cùng nhìn ra biển."}]
        },
        "Unit 4: In the countryside": {
            "phonics": "Ff",
            "words": [{"en": "field", "vi": "cánh đồng"}, {"en": "farm", "vi": "trang trại"}, {"en": "flower", "vi": "bông hoa"}],
            "sentences": [{"en": "There is a flower.", "vi": "Có một bông hoa."}]
        }
    },
    "Lớp 3": {
        "Unit 1: Hello": {
            "phonics": "h / m",
            "words": [{"en": "hello", "vi": "xin chào"}, {"en": "hi", "vi": "chào"}, {"en": "fine", "vi": "khỏe"}, {"en": "thanks", "vi": "cảm ơn"}],
            "sentences": [{"en": "How are you?", "vi": "Bạn khỏe không?"}, {"en": "I'm fine, thank you.", "vi": "Tớ khỏe, cảm ơn bạn."}]
        },
        "Unit 2: Our names": {
            "phonics": "b / m",
            "words": [{"en": "name", "vi": "tên"}, {"en": "what", "vi": "gì/cái gì"}, {"en": "my", "vi": "của tớ"}],
            "sentences": [{"en": "What's your name?", "vi": "Tên bạn là gì?"}, {"en": "My name's Ben.", "vi": "Tên tớ là Ben."}]
        },
        "Unit 3: Our bodies": {
            "phonics": "f / t",
            "words": [{"en": "face", "vi": "khuôn mặt"}, {"en": "hand", "vi": "bàn tay"}, {"en": "eye", "vi": "mắt"}, {"en": "ear", "vi": "tai"}],
            "sentences": [{"en": "Touch your face.", "vi": "Chạm vào mặt của bạn."}]
        }
    },
    "Lớp 4": {
        "Unit 1: My friends": {
            "phonics": "a / e",
            "words": [{"en": "Britain", "vi": "Nước Anh"}, {"en": "Japan", "vi": "Nhật Bản"}, {"en": "Vietnam", "vi": "Việt Nam"}, {"en": "America", "vi": "Mỹ"}],
            "sentences": [{"en": "Where are you from?", "vi": "Bạn từ đâu đến?"}, {"en": "I'm from Vietnam.", "vi": "Tớ đến từ Việt Nam."}]
        },
        "Unit 2: Time and daily routines": {
            "phonics": "o / i",
            "words": [{"en": "get up", "vi": "thức dậy"}, {"en": "have breakfast", "vi": "ăn sáng"}, {"en": "go to school", "vi": "đi học"}],
            "sentences": [{"en": "What time is it?", "vi": "Mấy giờ rồi?"}, {"en": "It's six o'clock.", "vi": "Bây giờ là sáu giờ."}]
        }
    },
    "Lớp 5": {
        "Unit 1: All about me!": {
            "phonics": "intending intonation",
            "words": [{"en": "address", "vi": "địa chỉ"}, {"en": "hometown", "vi": "quê hương"}, {"en": "street", "vi": "đường phố"}, {"en": "flat", "vi": "căn hộ"}],
            "sentences": [{"en": "What's your address?", "vi": "Địa chỉ của bạn là gì?"}, {"en": "It's 75 Hai Ba Trung Street.", "vi": "Là số 75 đường Hai Bà Trưng."}]
        },
        "Unit 2: Our homes": {
            "phonics": "stress patterns",
            "words": [{"en": "city", "vi": "thành phố"}, {"en": "village", "vi": "ngôi làng"}, {"en": "mountain", "vi": "ngọn núi"}, {"en": "tower", "vi": "tòa tháp"}],
            "sentences": [{"en": "Where do you live?", "vi": "Bạn sống ở đâu?"}, {"en": "I live in a quiet village.", "vi": "Tớ sống ở một ngôi làng yên bình."}]
        }
    }
}

# Sidebar selection for Grade and Unit
st.sidebar.header("🎯 Chọn Chương Trình Học")
selected_grade = st.sidebar.selectbox("📖 Chọn Lớp:", list(DATA.keys()))
grade_data = DATA[selected_grade]

selected_unit = st.sidebar.selectbox("📚 Chọn Bài Học (Unit):", list(grade_data.keys()))
unit_info = grade_data[selected_unit]

st.subheader(f"📌 [{selected_grade}] {selected_unit}")
st.write(f"🔤 **Âm chính (Phonics):** `{unit_info['phonics']}`")

# Type selection
practice_type = st.radio("🎯 Chọn nội dung luyện nói:", ["Từ vựng (Vocabulary)", "Mẫu câu (Sentence Patterns)"], horizontal=True)

items = unit_info["words"] if practice_type == "Từ vựng (Vocabulary)" else unit_info["sentences"]

selected_item = st.selectbox("👉 Chọn từ/câu muốn luyện:", [f"{item['en']} ({item['vi']})" for item in items])
target_text = selected_item.split(" (")[0].strip()
target_vi = selected_item.split(" (")[1].replace(")", "").strip()

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"### 🎯 Mẫu tiếng Anh: **{target_text}**")
with col2:
    st.markdown(f"### 💡 Nghĩa tiếng Việt: **{target_vi}**")

# HTML/JS component for Speech Recognition and Dual-Engine Speech Synthesis
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            background-color: #ffffff;
            padding: 10px;
            margin: 0;
        }}
        .btn-container {{
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 15px;
        }}
        .btn {{
            padding: 14px 28px;
            font-size: 17px;
            font-weight: bold;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}
        .btn-audio {{
            background: linear-gradient(135deg, #4CAF50, #2E7D32);
            color: white;
        }}
        .btn-audio:active {{ transform: scale(0.96); }}
        
        .btn-rec {{
            background: linear-gradient(135deg, #0288D1, #01579B);
            color: white;
        }}
        .btn-rec.recording {{
            background: linear-gradient(135deg, #E53935, #B71C1C);
            animation: pulse 1s infinite;
        }}
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.04); }}
            100% {{ transform: scale(1); }}
        }}
        .result-box {{
            margin-top: 15px;
            padding: 15px;
            border-radius: 15px;
            background-color: #f1f8e9;
            border: 2px solid #c5e1a5;
            box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        }}
        .score {{
            font-size: 32px;
            font-weight: bold;
            color: #2e7d32;
            margin: 5px 0;
        }}
        .text-said {{
            font-size: 18px;
            color: #333;
        }}
        .stars {{
            font-size: 28px;
            color: #fbc02d;
        }}
        .guide-box {{
            margin-top: 15px;
            padding: 10px;
            background-color: #fffde7;
            border-radius: 10px;
            font-size: 13px;
            color: #f57f17;
            text-align: left;
            border: 1px solid #fff59d;
        }}
    </style>
</head>
<body>

    <div class="btn-container">
        <button class="btn btn-audio" id="audioBtn" onclick="playAudio()">🔊 Nghe phát âm mẫu</button>
        <button class="btn btn-rec" id="recBtn" onclick="toggleRecording()">🎙️ Bấm để nói</button>
    </div>

    <div class="result-box" id="resultBox" style="display:none;">
        <div class="text-said">Bạn đã nói: <b id="userSpeech" style="color:#0288D1;">...</b></div>
        <div class="score" id="scoreText">0%</div>
        <div class="stars" id="starText">⭐⭐⭐</div>
        <div id="feedbackText" style="font-weight:bold; font-size:16px;"></div>
    </div>

    <div class="guide-box">
        💡 <b>Mẹo khắc phục nếu không nghe tiếng hoặc không thu âm được:</b><br>
        1. <b>Trình duyệt:</b> Mở web bằng Chrome/Safari (tránh mở trực tiếp trong Zalo/Facebook).<br>
        2. <b>iPhone/iPad:</b> Hãy gạt nút bên hông máy để <b>Tắt chế độ im lặng</b>.<br>
        3. <b>Micro:</b> Chọn "Cho phép" (Allow) khi trình duyệt hỏi quyền sử dụng Micro.
    </div>

    <script>
        const targetText = "{target_text.lower().strip()}";
        const rawTargetText = "{target_text}";
        let recognition = null;
        let isRecording = false;

        // DUAL-ENGINE AUDIO PLAYBACK
        function playAudio() {{
            const btn = document.getElementById("audioBtn");
            btn.innerText = "⏳ Đang phát...";

            let played = false;

            // Engine 1: Web SpeechSynthesis
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(rawTargetText);
                utterance.lang = 'en-US';
                utterance.rate = 0.8;

                utterance.onstart = function() {{
                    played = true;
                    btn.innerText = "🔊 Đang đọc mẫu...";
                }};

                utterance.onend = function() {{
                    btn.innerText = "🔊 Nghe phát âm mẫu";
                }};

                utterance.onerror = function() {{
                    fallbackAudio();
                }};

                window.speechSynthesis.speak(utterance);
            }}

            // Engine 2: HTML5 Audio Fallback (for mobile Safari / Zalo browser)
            setTimeout(function() {{
                if (!played) {{
                    fallbackAudio();
                }}
            }}, 400);
        }}

        function fallbackAudio() {{
            const btn = document.getElementById("audioBtn");
            btn.innerText = "🔊 Đang đọc mẫu...";
            
            // Google Translate Audio URL fallback
            const encoded = encodeURIComponent(rawTargetText);
            const audioUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q=${{encoded}}`;
            const audio = new Audio(audioUrl);

            audio.play().then(() => {{
                audio.onended = () => {{ btn.innerText = "🔊 Nghe phát âm mẫu"; }};
            }}).catch(err => {{
                btn.innerText = "🔊 Nghe phát âm mẫu";
                alert("Hãy kiểm tra nút âm lượng hoặc gạt TẮT chế độ im lặng trên điện thoại nhé!");
            }});
        }}

        // LEVENSHTEIN & WORD MATCHING SIMILARITY
        function similarity(s1, s2) {{
            s1 = s1.toLowerCase().replace(/[^a-z0-9 ]/g, "").trim();
            s2 = s2.toLowerCase().replace(/[^a-z0-9 ]/g, "").trim();
            
            if (s1 === s2) return 100;
            if (s1.length === 0 || s2.length === 0) return 0;
            
            const w1 = s1.split(" ");
            const w2 = s2.split(" ");
            let matches = 0;
            w2.forEach(w => {{ if (w1.includes(w)) matches++; }});
            let wordScore = (matches / Math.max(w1.length, w2.length)) * 100;

            return Math.min(100, Math.round(wordScore));
        }}

        // SPEECH RECOGNITION WITH EXPLICIT PERMISSION
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

        if (SpeechRecognition) {{
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
                let errMsg = "Không thể nhận diện giọng nói (" + event.error + ").";
                if (event.error === 'not-allowed') {{
                    errMsg = "Bạn chưa cho phép ứng dụng sử dụng Micro. Hãy bấm vào biểu tượng 🔒 cạnh đường link web để BẬT Micro nhé!";
                }}
                alert(errMsg);
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
            if (!recognition) {{
                alert("Trình duyệt hiện tại chưa hỗ trợ thu âm trực tiếp. Phụ huynh hãy mở web bằng Google Chrome hoặc Safari nhé!");
                return;
            }}

            // Request permission explicitly via getUserMedia first if needed
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {{
                navigator.mediaDevices.getUserMedia({{ audio: true }})
                .then(function(stream) {{
                    stream.getTracks().forEach(track => track.stop()); // close test stream
                    if (isRecording) {{
                        recognition.stop();
                    }} else {{
                        recognition.start();
                    }}
                }})
                .catch(function(err) {{
                    alert("Chưa cấp quyền Micro! Hãy bấm vào biểu tượng 🔒 cạnh link web và chọn CHO PHÉP Micro.");
                }});
            }} else {{
                if (isRecording) {{
                    recognition.stop();
                }} else {{
                    recognition.start();
                }}
            }}
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=380)

st.markdown("---")
st.caption("Ứng dụng phi thương mại hỗ trợ học sinh ôn tập phát âm Tiếng Anh Tiểu học (Global Success).")
