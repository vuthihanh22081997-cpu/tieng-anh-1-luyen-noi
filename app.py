import streamlit as st
import streamlit.components.v1 as components
import json

# Page config
st.set_page_config(
    page_title="Luyện Phát Âm Tiếng Anh Tiểu Học (Lớp 1 - Lớp 5)",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Luyện Phát Âm Tiếng Anh Tiểu Học")
st.caption("Chương trình Tiếng Anh Global Success (NXB Giáo dục Việt Nam)")

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
            "sentences": [{"en": "Look at the sea.", "vi": "Hãy nhìn ra biển kìa."}]
        },
        "Unit 4: In the countryside": {
            "phonics": "Ff",
            "words": [{"en": "field", "vi": "cánh đồng"}, {"en": "flowers", "vi": "những bông hoa"}, {"en": "frog", "vi": "con ếch"}],
            "sentences": [{"en": "There is a frog.", "vi": "Có một con ếch."}]
        }
    },
    "Lớp 3": {
        "Unit 1: Hello": {
            "phonics": "Hh / B3",
            "words": [{"en": "hello", "vi": "xin chào"}, {"en": "hi", "vi": "chào"}, {"en": "bye", "vi": "tạm biệt"}],
            "sentences": [{"en": "Hello, I am Ben.", "vi": "Xin chào, tớ là Ben."}]
        },
        "Unit 2: Our names": {
            "phonics": "Mm",
            "words": [{"en": "name", "vi": "tên"}, {"en": "spell", "vi": "đánh vần"}, {"en": "what", "vi": "cái gì"}],
            "sentences": [{"en": "What's your name?", "vi": "Tên bạn là gì?"}, {"en": "My name's Mai.", "vi": "Tên tớ là Mai."}]
        },
        "Unit 3: Our bodies": {
            "phonics": "Oo",
            "words": [{"en": "eye", "vi": "mắt"}, {"en": "ear", "vi": "tai"}, {"en": "face", "vi": "khuôn mặt"}, {"en": "hand", "vi": "bàn tay"}],
            "sentences": [{"en": "Touch your face.", "vi": "Chạm vào mặt của bạn."}]
        },
        "Unit 4: My hobbies": {
            "phonics": "Ing",
            "words": [{"en": "singing", "vi": "ca hát"}, {"en": "dancing", "vi": "khiêu vũ"}, {"en": "cooking", "vi": "nấu ăn"}, {"en": "drawing", "vi": "vẽ tranh"}],
            "sentences": [{"en": "I like singing.", "vi": "Tớ thích ca hát."}]
        }
    },
    "Lớp 4": {
        "Unit 1: My friends": {
            "phonics": "Am",
            "words": [{"en": "Britain", "vi": "nước Anh"}, {"en": "Vietnam", "vi": "Việt Nam"}, {"en": "America", "vi": "nước Mỹ"}, {"en": "Japan", "vi": "Nhật Bản"}],
            "sentences": [{"en": "Where are you from?", "vi": "Bạn từ đâu đến?"}, {"en": "I'm from Vietnam.", "vi": "Tớ đến từ Việt Nam."}]
        },
        "Unit 2: Time and daily routines": {
            "phonics": "Ck",
            "words": [{"en": "o'clock", "vi": "giờ đúng"}, {"en": "get up", "vi": "thức dậy"}, {"en": "have breakfast", "vi": "ăn sáng"}, {"en": "go to school", "vi": "đi học"}],
            "sentences": [{"en": "What time is it?", "vi": "Mấy giờ rồi?"}, {"en": "It's six o'clock.", "vi": "Bây giờ là 6 giờ."}]
        },
        "Unit 3: My week": {
            "phonics": "Days",
            "words": [{"en": "Monday", "vi": "Thứ Hai"}, {"en": "Wednesday", "vi": "Thứ Tư"}, {"en": "Friday", "vi": "Thứ Sáu"}, {"en": "Sunday", "vi": "Chủ Nhật"}],
            "sentences": [{"en": "What day is it today?", "vi": "Hôm nay là thứ mấy?"}, {"en": "It's Monday.", "vi": "Hôm nay là Thứ Hai."}]
        }
    },
    "Lớp 5": {
        "Unit 1: All about me!": {
            "phonics": "Address",
            "words": [{"en": "hometown", "vi": "quê hương"}, {"en": "address", "vi": "địa chỉ"}, {"en": "flat", "vi": "căn hộ"}, {"en": "lane", "vi": "ngõ/hẻm"}],
            "sentences": [{"en": "What's your address?", "vi": "Địa chỉ của bạn là gì?"}, {"en": "It's 75 Hai Ba Trung Street.", "vi": "Là số 75 đường Hai Bà Trưng."}]
        },
        "Unit 2: Our homes": {
            "phonics": "Home",
            "words": [{"en": "quiet", "vi": "yên tĩnh"}, {"en": "crowded", "vi": "đông đúc"}, {"en": "busy", "vi": "nhộn nhịp"}, {"en": "pretty", "vi": "xinh đẹp"}],
            "sentences": [{"en": "What's the city like?", "vi": "Thành phố như thế nào?"}, {"en": "It's big and busy.", "vi": "Nó to và nhộn nhịp."}]
        },
        "Unit 3: My foreign friends": {
            "phonics": "Friends",
            "words": [{"en": "Australian", "vi": "người Úc"}, {"en": "Malaysian", "vi": "người Mã Lai"}, {"en": "English", "vi": "người Anh"}],
            "sentences": [{"en": "What nationality is he?", "vi": "Cậu ấy quốc tịch gì?"}, {"en": "He's English.", "vi": "Cậu ấy là người Anh."}]
        }
    }
}

# Sidebar selection for Grade and Unit
st.sidebar.header("📚 Chọn Khối Lớp & Bài Học")
selected_grade = st.sidebar.selectbox("🎯 Chọn Lớp:", list(DATA.keys()))
units_in_grade = DATA[selected_grade]

selected_unit_name = st.sidebar.selectbox("📖 Chọn Unit (Bài học):", list(units_in_grade.keys()))
unit_info = units_in_grade[selected_unit_name]

st.subheader(f"📌 {selected_grade} - {selected_unit_name}")
st.write(f"🔤 **Âm / Trọng tâm (Phonics):** `{unit_info['phonics']}`")

# Practice Type
practice_type = st.radio("🎯 Chọn nội dung luyện tập:", ["Từ vựng (Vocabulary)", "Mẫu câu (Sentence Patterns)"], horizontal=True)

items = unit_info["words"] if practice_type == "Từ vựng (Vocabulary)" else unit_info["sentences"]
options = [f"{item['en']} ({item['vi']})" for item in items]

selected_option = st.selectbox("👉 Chọn từ/câu muốn luyện phát âm:", options)
target_text = selected_option.split(" (")[0].strip()
target_vi = selected_option.split(" (")[1].replace(")", "").strip()

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"### 🎯 Tiếng Anh: **{target_text}**")
with col2:
    st.markdown(f"### 💡 Tiếng Việt: **{target_vi}**")

# Instructions help box
with st.expander("⚙️ Hướng dẫn xử lý nhanh nếu gặp lỗi Micro hoặc Âm thanh"):
    st.markdown("""
    * **Không nghe thấy tiếng mẫu?** 
      * iPhone/iPad: Vui lòng **tắt Chế độ im lặng** (gạt nút bên hông máy sang chế độ Bật chuông).
      * Tăng âm lượng phương tiện trên điện thoại.
    * **Bấm "Bấm để nói" mà không hoạt động?**
      * Mở web bằng **Google Chrome**, **Microsoft Edge** hoặc **Safari**.
      * Khi Zalo/Facebook mở web, hãy bấm **dấu 3 chấm `...`** ở góc trên chọn **"Mở bằng trình duyệt ngoài"**.
      * Bấm vào **biểu tượng Ổ khóa 🔒** cạnh đường link web ➔ Chọn **Cho phép Micro**.
    """)

# Clean escaped HTML string
clean_target_text = target_text.replace('"', '\"').replace("'", "\'")

html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            text-align: center;
            background-color: #f8f9fa;
            margin: 0;
            padding: 10px;
        }}
        .btn-container {{
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 15px;
        }}
        .btn {{
            padding: 14px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .btn-audio {{
            background-color: #2e7d32;
            color: white;
        }}
        .btn-audio:active {{ background-color: #1b5e20; }}
        .btn-rec {{
            background-color: #0288d1;
            color: white;
        }}
        .btn-rec.recording {{
            background-color: #d32f2f;
            animation: pulse 1s infinite;
        }}
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}
        .result-box {{
            margin-top: 15px;
            padding: 18px;
            border-radius: 16px;
            background-color: #ffffff;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }}
        .score {{
            font-size: 32px;
            font-weight: bold;
            color: #2e7d32;
            margin: 8px 0;
        }}
        .text-said {{
            font-size: 18px;
            color: #444;
        }}
        .stars {{
            font-size: 28px;
            color: #ffc107;
        }}
        .status-msg {{
            font-size: 14px;
            color: #666;
            margin-top: 6px;
        }}
    </style>
</head>
<body>

    <div class="btn-container">
        <button class="btn btn-audio" onclick="playAudio()">🔊 Nghe phát âm mẫu</button>
        <button class="btn btn-rec" id="recBtn" onclick="toggleRecording()">🎙️ Bấm để nói</button>
    </div>

    <div class="result-box" id="resultBox" style="display:none;">
        <div class="text-said">Bạn đã nói: <b id="userSpeech" style="color:#0288d1;">...</b></div>
        <div class="score" id="scoreText">0%</div>
        <div class="stars" id="starText">⭐⭐⭐</div>
        <div id="feedbackText" style="font-weight:bold; font-size: 18px; margin-top:5px;"></div>
    </div>
    <div id="errMsg" class="status-msg"></div>

    <script>
        const targetText = "{clean_target_text}";
        let recognition = null;
        let isRecording = false;

        // Dual Engine Audio Player (Web Speech API + Audio Fallback)
        function playAudio() {{
            document.getElementById("errMsg").innerText = "";
            try {{
                window.speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(targetText);
                utterance.lang = 'en-US';
                utterance.rate = 0.8;
                
                let spoken = false;
                utterance.onstart = function() {{ spoken = true; }};
                
                window.speechSynthesis.speak(utterance);

                // Fallback to Google TTS Audio Stream if SpeechSynthesis is silent
                setTimeout(() => {{
                    if (!spoken && !window.speechSynthesis.speaking) {{
                        const audioUrl = "https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q=" + encodeURIComponent(targetText);
                        const audio = new Audio(audioUrl);
                        audio.play().catch(e => {{
                            console.log("Audio play error:", e);
                        }});
                    }}
                }}, 400);
            }} catch(e) {{
                const audioUrl = "https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q=" + encodeURIComponent(targetText);
                const audio = new Audio(audioUrl);
                audio.play().catch(err => {{
                    document.getElementById("errMsg").innerText = "Hãy bật âm lượng điện thoại hoặc tắt Chế độ im lặng!";
                }});
            }}
        }}

        // Similarity calculation for scoring
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

        // Speech Recognition Setup
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

        if (!SpeechRecognition) {{
            document.getElementById("errMsg").innerText = "⚠️ Trình duyệt chưa hỗ trợ thu âm trực tiếp. Hãy mở bằng Google Chrome hoặc Safari!";
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
                document.getElementById("errMsg").innerText = "";
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
                let errText = "Lỗi nhận diện: " + event.error;
                if (event.error === 'not-allowed') {{
                    errText = "⚠️ Bị chặn Micro! Bấm vào biểu tượng ổ khóa 🔒 cạnh link web để Cho phép Micro.";
                }}
                document.getElementById("errMsg").innerText = errText;
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
                alert("Trình duyệt không hỗ trợ thu âm. Vui lòng mở bằng Google Chrome hoặc Safari!");
                return;
            }}
            
            // Explicitly request microphone permission
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {{
                navigator.mediaDevices.getUserMedia({{ audio: true }}).then(function(stream) {{
                    stream.getTracks().forEach(track => track.stop());
                    if (isRecording) {{
                        recognition.stop();
                    }} else {{
                        recognition.start();
                    }}
                }}).catch(function(err) {{
                    document.getElementById("errMsg").innerText = "⚠️ Hãy cho phép quyền sử dụng Micro trong trình duyệt!";
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

components.html(html_code, height=320)
