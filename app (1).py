import streamlit as st
import streamlit.components.v1 as components
import json

# Page config
st.set_page_config(
    page_title="Luyện Phát Âm Tiếng Anh 1 & 2 - Global Success",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Luyện Phát Âm Tiếng Anh Tiêu Học")
st.caption("Chương trình SGK Tiếng Anh 1 & Tiếng Anh 2 - Global Success")

# Database of Units from SGK Tiếng Anh 1 & 2 Global Success
DATA_GRADE1 = {
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
            {"en": "cake", "vi": "bánh ngọt"},
            {"en": "car", "vi": "ô tô"},
            {"en": "cat", "vi": "con mèo"},
            {"en": "cup", "vi": "cái cốc"}
        ],
        "sentences": [
            {"en": "I have a car.", "vi": "Tớ có một chiếc ô tô."},
            {"en": "I have a cat.", "vi": "Tớ có một con mèo."}
        ]
    },
    "Unit 3: At the street market": {
        "phonics": "Aa",
        "words": [
            {"en": "apple", "vi": "quả táo"},
            {"en": "bag", "vi": "cặp sách/túi"},
            {"en": "can", "vi": "vỏ lon"},
            {"en": "hat", "vi": "cái mũ"}
        ],
        "sentences": [
            {"en": "This is my bag.", "vi": "Đây là cặp sách của tớ."},
            {"en": "This is an apple.", "vi": "Đây là một quả táo."}
        ]
    },
    "Unit 4: In the bedroom": {
        "phonics": "Dd",
        "words": [
            {"en": "door", "vi": "cánh cửa"},
            {"en": "desk", "vi": "bàn học"},
            {"en": "dog", "vi": "con chó"},
            {"en": "doll", "vi": "búp bê"}
        ],
        "sentences": [
            {"en": "Open the door.", "vi": "Mở cửa ra."},
            {"en": "Touch the desk.", "vi": "Chạm vào bàn học."}
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
            {"en": "I like milk.", "vi": "Tớ thích uống sữa."},
            {"en": "I like chicken.", "vi": "Tớ thích ăn thịt gà."}
        ]
    },
    "Unit 6: In the classroom": {
        "phonics": "Ee",
        "words": [
            {"en": "bell", "vi": "cái chuông"},
            {"en": "pen", "vi": "bút mực"},
            {"en": "pencil", "vi": "bút chì"},
            {"en": "eraser", "vi": "cục tẩy"}
        ],
        "sentences": [
            {"en": "It's a red pen.", "vi": "Nó là một cây bút mực màu đỏ."},
            {"en": "It's a blue pencil.", "vi": "Nó là một cây bút chì màu xanh."}
        ]
    },
    "Unit 7: In the garden": {
        "phonics": "Gg",
        "words": [
            {"en": "garden", "vi": "Khu vườn"},
            {"en": "girl", "vi": "Cô gái"},
            {"en": "goat", "vi": "Con dê"},
            {"en": "gate", "vi": "Cổng làng/cổng nhà"}
        ],
        "sentences": [
            {"en": "There's a garden.", "vi": "Có một khu vườn."},
            {"en": "There's a goat.", "vi": "Có một con dê."}
        ]
    },
    "Unit 8: In the park": {
        "phonics": "Hh",
        "words": [
            {"en": "hair", "vi": "Tóc"},
            {"en": "hand", "vi": "Bàn tay"},
            {"en": "head", "vi": "Cái đầu"},
            {"en": "horse", "vi": "Con ngựa"}
        ],
        "sentences": [
            {"en": "Touch your hair.", "vi": "Hãy chạm vào tóc của bạn."},
            {"en": "Touch your head.", "vi": "Hãy chạm vào đầu của bạn."}
        ]
    },
    "Unit 9: In the shop": {
        "phonics": "Oo",
        "words": [
            {"en": "clock", "vi": "Đồng hồ"},
            {"en": "lock", "vi": "Ổ khóa"},
            {"en": "mop", "vi": "Cây lau nhà"},
            {"en": "pot", "vi": "Cái nồi"}
        ],
        "sentences": [
            {"en": "How many clocks?", "vi": "Có bao nhiêu cái đồng hồ?"},
            {"en": "Three clocks.", "vi": "Ba cái đồng hồ."}
        ]
    },
    "Unit 10: At the zoo": {
        "phonics": "Mm",
        "words": [
            {"en": "monkey", "vi": "Con khỉ"},
            {"en": "mother", "vi": "Mẹ"},
            {"en": "mouse", "vi": "Con chuột"},
            {"en": "mango", "vi": "Quả xoài"}
        ],
        "sentences": [
            {"en": "This is a monkey.", "vi": "Đây là một con khỉ."},
            {"en": "I see a mouse.", "vi": "Tớ nhìn thấy một con chuột."}
        ]
    },
    "Unit 11: At the bus stop": {
        "phonics": "Uu",
        "words": [
            {"en": "bus", "vi": "Xe buýt"},
            {"en": "sun", "vi": "Mặt trời"},
            {"en": "truck", "vi": "Xe tải"},
            {"en": "runner", "vi": "Người chạy bộ"}
        ],
        "sentences": [
            {"en": "Look at the bus.", "vi": "Hãy nhìn chiếc xe buýt kìa."},
            {"en": "Look at the sun.", "vi": "Hãy nhìn mặt trời kìa."}
        ]
    },
    "Unit 12: At the lake": {
        "phonics": "Ll",
        "words": [
            {"en": "lake", "vi": "Hồ nước"},
            {"en": "leaf", "vi": "Chiếc lá"},
            {"en": "lemon", "vi": "Quả chanh vàng"},
            {"en": "Lucy", "vi": "Bạn Lucy"}
        ],
        "sentences": [
            {"en": "Look at the lake.", "vi": "Hãy nhìn vào hồ nước."},
            {"en": "This is a leaf.", "vi": "Đây là một chiếc lá."}
        ]
    },
    "Unit 13: In the toy shop": {
        "phonics": "Numbers 1-5",
        "words": [
            {"en": "one", "vi": "Số 1"},
            {"en": "two", "vi": "Số 2"},
            {"en": "three", "vi": "Số 3"},
            {"en": "four", "vi": "Số 4"},
            {"en": "five", "vi": "Số 5"}
        ],
        "sentences": [
            {"en": "I have three balls.", "vi": "Tớ có 3 quả bóng."},
            {"en": "I have four cars.", "vi": "Tớ có 4 chiếc ô tô."}
        ]
    },
    "Unit 14: At the park": {
        "phonics": "Tt",
        "words": [
            {"en": "tiger", "vi": "Con hổ"},
            {"en": "turtle", "vi": "Con rùa"},
            {"en": "tree", "vi": "Cây xanh"},
            {"en": "tent", "vi": "Cái lều"}
        ],
        "sentences": [
            {"en": "I can see a tiger.", "vi": "Tớ có thể nhìn thấy một con hổ."},
            {"en": "I can see a turtle.", "vi": "Tớ có thể nhìn thấy một con rùa."}
        ]
    },
    "Unit 15: At the clothes shop": {
        "phonics": "Nn",
        "words": [
            {"en": "nut", "vi": "Hạt ngũ cốc"},
            {"en": "nest", "vi": "Tổ chim"},
            {"en": "net", "vi": "Cái lưới"},
            {"en": "nose", "vi": "Cái mũi"}
        ],
        "sentences": [
            {"en": "Point to your nose.", "vi": "Chỉ vào mũi của bạn."},
            {"en": "Touch your nose.", "vi": "Chạm vào mũi của bạn."}
        ]
    },
    "Unit 16: At home": {
        "phonics": "Numbers 6-10",
        "words": [
            {"en": "six", "vi": "Số 6"},
            {"en": "seven", "vi": "Số 7"},
            {"en": "eight", "vi": "Số 8"},
            {"en": "nine", "vi": "Số 9"},
            {"en": "ten", "vi": "Số 10"}
        ],
        "sentences": [
            {"en": "I can see six windows.", "vi": "Tớ nhìn thấy 6 cái cửa sổ."},
            {"en": "I can see seven chairs.", "vi": "Tớ nhìn thấy 7 cái ghế."}
        ]
    }
}

DATA_GRADE2 = {
    "Unit 1: At my birthday party": {
        "phonics": "Pp",
        "words": [
            {"en": "pasta", "vi": "Mì Ý / Mì ống"},
            {"en": "popcorn", "vi": "Bắp rang bơ / Bỏng ngô"},
            {"en": "pizza", "vi": "Bánh pizza"}
        ],
        "sentences": [
            {"en": "I like pasta.", "vi": "Tớ thích ăn mì Ý."},
            {"en": "Pass me the pizza, please.", "vi": "Làm ơn chuyền giúp tớ bánh pizza."}
        ]
    },
    "Unit 2: In the backyard": {
        "phonics": "Kk",
        "words": [
            {"en": "kite", "vi": "Con diều"},
            {"en": "bike", "vi": "Xe đạp"},
            {"en": "kitten", "vi": "Con mèo con"}
        ],
        "sentences": [
            {"en": "I have a kite.", "vi": "Tớ có một con diều."},
            {"en": "Look at the kitten.", "vi": "Hãy nhìn con mèo con kìa."}
        ]
    },
    "Unit 3: At the seaside": {
        "phonics": "Ss",
        "words": [
            {"en": "sail", "vi": "Cánh buồm"},
            {"en": "sand", "vi": "Bãi cát"},
            {"en": "sea", "vi": "Biển"}
        ],
        "sentences": [
            {"en": "I can see the sea.", "vi": "Tớ có thể nhìn thấy biển."},
            {"en": "Look at the sail.", "vi": "Hãy nhìn cánh buồm kìa."}
        ]
    },
    "Unit 4: In the countryside": {
        "phonics": "Rr",
        "words": [
            {"en": "rainbow", "vi": "Cầu vồng"},
            {"en": "river", "vi": "Dòng sông"},
            {"en": "road", "vi": "Con đường"}
        ],
        "sentences": [
            {"en": "Look at the rainbow.", "vi": "Hãy nhìn cầu vồng kìa."},
            {"en": "There is a river.", "vi": "Có một dòng sông."}
        ]
    },
    "Unit 5: In the classroom": {
        "phonics": "Qq",
        "words": [
            {"en": "question", "vi": "Câu hỏi"},
            {"en": "quiz", "vi": "Bài kiểm tra ngắn / Câu đố"},
            {"en": "square", "vi": "Hình vuông"}
        ],
        "sentences": [
            {"en": "I can answer the question.", "vi": "Tớ có thể trả lời câu hỏi."},
            {"en": "It's a square.", "vi": "Nó là một hình vuông."}
        ]
    },
    "Unit 6: On the farm": {
        "phonics": "Xx",
        "words": [
            {"en": "box", "vi": "Cái hộp"},
            {"en": "fox", "vi": "Con cáo"},
            {"en": "ox", "vi": "Con bò tót"}
        ],
        "sentences": [
            {"en": "Look at the fox.", "vi": "Hãy nhìn con cáo kìa."},
            {"en": "It's in the box.", "vi": "Nó ở trong cái hộp."}
        ]
    },
    "Unit 7: In the kitchen": {
        "phonics": "Jj",
        "words": [
            {"en": "jam", "vi": "Mứt"},
            {"en": "jelly", "vi": "Thạch kẹo"},
            {"en": "juice", "vi": "Nước ép hoa quả"}
        ],
        "sentences": [
            {"en": "Pass me the jam, please.", "vi": "Làm ơn lấy giúp tớ lọ mứt."},
            {"en": "I like juice.", "vi": "Tớ thích uống nước ép."}
        ]
    },
    "Unit 8: In the village": {
        "phonics": "Vv",
        "words": [
            {"en": "van", "vi": "Xe tải van"},
            {"en": "village", "vi": "Ngôi làng"},
            {"en": "volleyball", "vi": "Bóng chuyền"}
        ],
        "sentences": [
            {"en": "Can you draw a van?", "vi": "Cậu có thể vẽ xe tải van không?"},
            {"en": "Yes, I can.", "vi": "Có, tớ có thể."}
        ]
    },
    "Unit 9: In the grocery store": {
        "phonics": "Yy",
        "words": [
            {"en": "yam", "vi": "Khoai từ"},
            {"en": "yo-yo", "vi": "Đồ chơi yo-yo"},
            {"en": "yogurt", "vi": "Sữa chua"}
        ],
        "sentences": [
            {"en": "I'd like some yogurt.", "vi": "Tớ muốn một ít sữa chua."},
            {"en": "I have a yo-yo.", "vi": "Tớ có một chiếc yo-yo."}
        ]
    },
    "Unit 10: At the zoo": {
        "phonics": "Zz",
        "words": [
            {"en": "zebra", "vi": "Ngựa vằn"},
            {"en": "zebu", "vi": "Con bò u"},
            {"en": "zoo", "vi": "Vườn bách thú"}
        ],
        "sentences": [
            {"en": "Look at the zebra.", "vi": "Hãy nhìn con ngựa vằn kìa."},
            {"en": "I am at the zoo.", "vi": "Tớ đang ở vườn thú."}
        ]
    },
    "Unit 11: In the playground": {
        "phonics": "a_e (Long A)",
        "words": [
            {"en": "drive", "vi": "Lái xe ô tô"},
            {"en": "ride", "vi": "Cưỡi xe / Chạy xe đạp"},
            {"en": "slide", "vi": "Cầu trượt"}
        ],
        "sentences": [
            {"en": "He is riding a bike.", "vi": "Cậu ấy đang đi xe đạp."},
            {"en": "I can slide.", "vi": "Tớ có thể chơi cầu trượt."}
        ]
    },
    "Unit 12: At the cafe": {
        "phonics": "a_e / e",
        "words": [
            {"en": "cake", "vi": "Bánh ngọt"},
            {"en": "grape", "vi": "Quả nho"},
            {"en": "table", "vi": "Cái bàn"}
        ],
        "sentences": [
            {"en": "I'd like a cake, please.", "vi": "Làm ơn cho tớ một chiếc bánh ngọt."},
            {"en": "Pass me the grapes.", "vi": "Làm ơn đưa tớ chùm nho."}
        ]
    },
    "Unit 13: In the Maths class": {
        "phonics": "Numbers 11-15",
        "words": [
            {"en": "eleven", "vi": "Số 11"},
            {"en": "twelve", "vi": "Số 12"},
            {"en": "thirteen", "vi": "Số 13"},
            {"en": "fourteen", "vi": "Số 14"},
            {"en": "fifteen", "vi": "Số 15"}
        ],
        "sentences": [
            {"en": "How many books? Fifteen.", "vi": "Có bao nhiêu quyển sách? 15 quyển."},
            {"en": "I have twelve pencils.", "vi": "Tớ có 12 cây bút chì."}
        ]
    },
    "Unit 14: At home": {
        "phonics": "Family",
        "words": [
            {"en": "brother", "vi": "Anh/Em trai"},
            {"en": "sister", "vi": "Chị/Em gái"},
            {"en": "grandmother", "vi": "Bà nội/ngoại"}
        ],
        "sentences": [
            {"en": "This is my brother.", "vi": "Đây là anh trai của tớ."},
            {"en": "I love my family.", "vi": "Tớ yêu gia đình tớ."}
        ]
    },
    "Unit 15: In the clothes shop": {
        "phonics": "Clothes & Numbers 16-20",
        "words": [
            {"en": "shirt", "vi": "Áo sơ mi"},
            {"en": "shoes", "vi": "Đôi giày"},
            {"en": "shorts", "vi": "Quần đùi"},
            {"en": "sixteen", "vi": "Số 16"},
            {"en": "twenty", "vi": "Số 20"}
        ],
        "sentences": [
            {"en": "I'm wearing shorts.", "vi": "Tớ đang mặc quần đùi."},
            {"en": "There are twenty shirts.", "vi": "Có 20 chiếc áo sơ mi."}
        ]
    },
    "Unit 16: At the campsite": {
        "phonics": "Tt / Near",
        "words": [
            {"en": "teapot", "vi": "Ấm trà"},
            {"en": "tent", "vi": "Cái lều"},
            {"en": "blanket", "vi": "Cái chăn / mền"}
        ],
        "sentences": [
            {"en": "The tent is near the tree.", "vi": "Cái lều ở gần cây."},
            {"en": "Pass me the teapot.", "vi": "Đưa giúp tớ cái ấm trà."}
        ]
    }
}

# Grade selection
selected_grade = st.sidebar.radio("📚 Chọn khối lớp:", ["Tiếng Anh 1 - Global Success", "Tiếng Anh 2 - Global Success"])

if selected_grade == "Tiếng Anh 1 - Global Success":
    current_db = DATA_GRADE1
else:
    current_db = DATA_GRADE2

# Unit Selection
selected_unit = st.selectbox("🎯 Chọn Unit bài học:", list(current_db.keys()))

unit_data = current_db[selected_unit]

st.subheader(f"🔤 Âm chính: {unit_data['phonics']}")

# Combine words and sentences into a items list
items_to_practice = []

st.markdown("### 1. Từ vựng (Vocabulary)")
for w in unit_data["words"]:
    items_to_practice.append({"text": w["en"], "meaning": w["vi"], "type": "word"})

st.markdown("### 2. Mẫu câu (Sentence Patterns)")
for s in unit_data["sentences"]:
    items_to_practice.append({"text": s["en"], "meaning": s["vi"], "type": "sentence"})

# HTML Component for Audio + Speech Recognition
for idx, item in enumerate(items_to_practice):
    text_en = item["en"] if "en" in item else item["text"]
    text_vi = item["meaning"]
    badge_type = "Từ vựng" if item["type"] == "word" else "Mẫu câu"
    
    component_html = f"""
    <div style="background-color: #f8f9fa; border-radius: 12px; padding: 16px; margin-bottom: 15px; border-left: 5px solid #4CAF50; font-family: sans-serif;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="background-color: #e8f5e9; color: #2e7d32; padding: 4px 8px; border-radius: 6px; font-size: 12px; font-weight: bold;">{badge_type}</span>
            <button onclick="playAudio('{text_en}')" style="background-color: #2196F3; color: white; border: none; padding: 6px 12px; border-radius: 20px; cursor: pointer; font-size: 14px; font-weight: bold;">
                🔊 Nghe mẫu
            </button>
        </div>
        <div style="margin-top: 10px;">
            <h3 style="margin: 0; color: #1a237e; font-size: 20px;">{text_en}</h3>
            <p style="margin: 4px 0 10px 0; color: #666; font-size: 14px;">👉 {text_vi}</p>
        </div>
        <div style="margin-top: 10px; display: flex; align-items: center; gap: 10px;">
            <button id="btn-{idx}" onclick="startRecognition('{text_en}', {idx})" style="background-color: #ff9800; color: white; border: none; padding: 8px 16px; border-radius: 20px; cursor: pointer; font-size: 14px; font-weight: bold;">
                🎙️ Thu âm đọc
            </button>
            <span id="status-{idx}" style="font-size: 14px; color: #666;"></span>
        </div>
        <div id="result-{idx}" style="margin-top: 10px; font-size: 14px; display: none;"></div>
    </div>

    <script>
    function playAudio(text) {{
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'en-US';
        utterance.rate = 0.8;
        window.speechSynthesis.speak(utterance);
    }}

    function calculateSimilarity(str1, str2) {{
        const s1 = str1.toLowerCase().replace(/[^a-z0-9]/g, '');
        const s2 = str2.toLowerCase().replace(/[^a-z0-9]/g, '');
        if (s1 === s2) return 100;
        if (s1.length === 0 || s2.length === 0) return 0;
        
        let matches = 0;
        const words1 = str1.toLowerCase().split(' ');
        const words2 = str2.toLowerCase().split(' ');
        
        words1.forEach(w => {{
            if (words2.includes(w)) matches++;
        }});
        
        return Math.round((matches / Math.max(words1.length, words2.length)) * 100);
    }}

    function startRecognition(targetText, index) {{
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) {{
            alert("Trình duyệt của bạn không hỗ trợ thu âm. Vui lòng dùng Chrome hoặc Safari.");
            return;
        }}

        const recognition = new SpeechRecognition();
        recognition.lang = 'en-US';
        recognition.interimResults = false;

        const btn = document.getElementById(`btn-${{index}}`);
        const status = document.getElementById(`status-${{index}}`);
        const resultDiv = document.getElementById(`result-${{index}}`);

        btn.disabled = true;
        btn.style.backgroundColor = "#ccc";
        status.innerHTML = "🔴 Đang nghe bé nói...";
        resultDiv.style.display = "none";

        recognition.start();

        recognition.onresult = function(event) {{
            const transcript = event.results[0][0].transcript;
            const score = calculateSimilarity(targetText, transcript);
            
            let stars = "⭐";
            let feedback = "Bé cần cố gắng thêm nhé!";
            let color = "#f44336";

            if (score >= 80) {{
                stars = "⭐⭐⭐";
                feedback = "Xuất sắc! Bé phát âm chuẩn lắm!";
                color = "#4CAF50";
            }} else if (score >= 50) {{
                stars = "⭐⭐";
                feedback = "Tốt lắm! Bé nói gần đúng rồi!";
                color = "#ff9800";
            }}

            resultDiv.innerHTML = `
                <div style="background-color: white; padding: 10px; border-radius: 8px; border: 1px solid ${{color}};">
                    <div><b>Bé đã nói:</b> "${{transcript}}"</div>
                    <div><b>Độ chính xác:</b> <span style="color: ${{color}}; font-weight: bold;">${{score}}%</span> ${{stars}}</div>
                    <div style="color: ${{color}}; font-size: 13px; margin-top: 4px;"><b>Phản hồi:</b> ${{feedback}}</div>
                </div>
            `;
            resultDiv.style.display = "block";
            status.innerHTML = "✅ Đã chấm điểm!";
            btn.disabled = false;
            btn.style.backgroundColor = "#ff9800";
        }};

        recognition.onerror = function(event) {{
            status.innerHTML = "⚠️ Chưa nghe rõ, bé bấm thu âm lại nhé!";
            btn.disabled = false;
            btn.style.backgroundColor = "#ff9800";
        }};

        recognition.onend = function() {{
            if (status.innerHTML.includes("Đang nghe")) {{
                status.innerHTML = "";
                btn.disabled = false;
                btn.style.backgroundColor = "#ff9800";
            }}
        }};
    }}
    </script>
    """
    components.html(component_html, height=190)

st.markdown("---")
st.caption("🎈 Chúc các con học tập vui vẻ và tự tin phát âm chuẩn tiếng Anh!")
