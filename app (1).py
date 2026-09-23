import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

st.set_page_config(
    page_title="Luyện Phát Âm Tiếng Anh 1-5 Global Success",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Luyện Phát Âm Tiếng Anh 1 - 5")
st.caption("Chương trình Tiếng Anh Tiểu học - Bộ sách Global Success (NXB Giáo Dục Việt Nam)")

# Notice banner for mobile in-app browsers
st.info("💡 **Mẹo nhỏ:** Để Micro và Âm thanh hoạt động ổn định nhất trên điện thoại, hãy mở trang web bằng **Google Chrome** (Android) hoặc **Safari** (iPhone) thay vì mở trực tiếp trong Zalo/Facebook.")

# Comprehensive Database for Grades 1 to 5
DATA = {
    "Lớp 1": {
        "Unit 1: In the school playground": {
            "phonics": "Bb",
            "words": [{"en": "ball", "vi": "quả bóng"}, {"en": "bike", "vi": "xe đạp"}, {"en": "book", "vi": "quyển sách"}],
            "sentences": [{"en": "Hi, I'm Bill.", "vi": "Xin chào, tớ là Bill."}, {"en": "Bye, Bill.", "vi": "Tạm biệt Bill."}]
        },
        "Unit 2: In the dining room": {
            "phonics": "Cc",
            "words": [{"en": "cake", "vi": "cái bánh"}, {"en": "car", "vi": "xe ô tô"}, {"en": "cat", "vi": "con mèo"}, {"en": "cup", "vi": "cái tách"}],
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
        },
        "Unit 9: In the shop": {
            "phonics": "Oo",
            "words": [{"en": "clocks", "vi": "đồng hồ"}, {"en": "locks", "vi": "ổ khóa"}, {"en": "mops", "vi": "cây lau nhà"}, {"en": "pots", "vi": "cái nồi"}],
            "sentences": [{"en": "How many clocks?", "vi": "Có bao nhiêu cái đồng hồ?"}]
        },
        "Unit 10: At the zoo": {
            "phonics": "Mm",
            "words": [{"en": "mango", "vi": "quả xoài"}, {"en": "monkey", "vi": "con khỉ"}, {"en": "mother", "vi": "mẹ"}, {"en": "mouse", "vi": "con chuột"}],
            "sentences": [{"en": "That's a monkey.", "vi": "Kia là một con khỉ."}]
        },
        "Unit 11: At the bus stop": {
            "phonics": "Uu",
            "words": [{"en": "bus", "vi": "xe buýt"}, {"en": "run", "vi": "chạy"}, {"en": "sun", "vi": "mặt trời"}, {"en": "truck", "vi": "xe tải"}],
            "sentences": [{"en": "He's running.", "vi": "Cậu ấy đang chạy."}]
        },
        "Unit 12: At the lake": {
            "phonics": "Ll",
            "words": [{"en": "lake", "vi": "hồ nước"}, {"en": "leaf", "vi": "lá cây"}, {"en": "lemons", "vi": "quả chanh"}],
            "sentences": [{"en": "Look at the lemons.", "vi": "Hãy nhìn những quả chanh."}]
        },
        "Unit 13: In the school canteen": {
            "phonics": "Nn",
            "words": [{"en": "bananas", "vi": "quả chuối"}, {"en": "noodles", "vi": "mì"}, {"en": "nuts", "vi": "hạt lạc"}],
            "sentences": [{"en": "She's having noodles.", "vi": "Cô ấy đang ăn mì."}]
        },
        "Unit 14: In the toy shop": {
            "phonics": "Tt",
            "words": [{"en": "teddy bear", "vi": "gấu bông"}, {"en": "tiger", "vi": "con hổ"}, {"en": "top", "vi": "con quay"}, {"en": "turtle", "vi": "con rùa"}],
            "sentences": [{"en": "I can see a tiger.", "vi": "Tớ có thể thấy một con hổ."}]
        },
        "Unit 15: At the football match": {
            "phonics": "Ff",
            "words": [{"en": "face", "vi": "khuôn mặt"}, {"en": "father", "vi": "bố"}, {"en": "foot", "vi": "bàn chân"}, {"en": "football", "vi": "bóng đá"}],
            "sentences": [{"en": "Point to your hand.", "vi": "Chỉ vào bàn tay của bạn."}]
        },
        "Unit 16: At home": {
            "phonics": "Ww",
            "words": [{"en": "wash", "vi": "lau/rửa"}, {"en": "water", "vi": "nước"}, {"en": "window", "vi": "cửa sổ"}],
            "sentences": [{"en": "How many windows can you see?", "vi": "Bạn nhìn thấy bao nhiêu cửa sổ?"}, {"en": "I can see six.", "vi": "Tớ nhìn thấy sáu cái."}]
        }
    },
    "Lớp 2": {
        "Unit 1: At my birthday party": {
            "phonics": "Pp",
            "words": [{"en": "pasta", "vi": "mì Ý"}, {"en": "popcorn", "vi": "bỏng ngô"}, {"en": "pizza", "vi": "bánh pizza"}],
            "sentences": [{"en": "Pass me the pizza, please.", "vi": "Làm ơn đưa tớ bánh pizza."}]
        },
        "Unit 2: In the backyard": {
            "phonics": "Kk",
            "words": [{"en": "kite", "vi": "con diều"}, {"en": "bike", "vi": "xe đạp"}, {"en": "kitten", "vi": "mèo con"}],
            "sentences": [{"en": "Look at the kite.", "vi": "Hãy nhìn con diều."}]
        },
        "Unit 3: At the seaside": {
            "phonics": "Ss",
            "words": [{"en": "sail", "vi": "cánh buồm"}, {"en": "sand", "vi": "cát"}, {"en": "sea", "vi": "biển"}],
            "sentences": [{"en": "I can see the sea.", "vi": "Tớ thấy biển."}]
        },
        "Unit 4: In the countryside": {
            "phonics": "Rr",
            "words": [{"en": "rainbow", "vi": "cầu vồng"}, {"en": "river", "vi": "dòng sông"}, {"en": "road", "vi": "con đường"}],
            "sentences": [{"en": "Look at the rainbow.", "vi": "Hãy nhìn cầu vồng."}]
        },
        "Unit 5: In the classroom": {
            "phonics": "Qq",
            "words": [{"en": "question", "vi": "câu hỏi"}, {"en": "quiz", "vi": "câu đố"}, {"en": "square", "vi": "hình vuông"}],
            "sentences": [{"en": "It's a square.", "vi": "Đó là hình vuông."}]
        },
        "Unit 6: On the farm": {
            "phonics": "Xx",
            "words": [{"en": "box", "vi": "cái hộp"}, {"en": "fox", "vi": "con cáo"}, {"en": "ox", "vi": "con bò tót"}],
            "sentences": [{"en": "I can see a box.", "vi": "Tớ nhìn thấy cái hộp."}]
        },
        "Unit 7: In the kitchen": {
            "phonics": "Jj",
            "words": [{"en": "jam", "vi": "mứt"}, {"en": "jelly", "vi": "thạch"}, {"en": "juice", "vi": "nước ép"}],
            "sentences": [{"en": "Do you like jam? Yes, I do.", "vi": "Cậu có thích mứt không? Có, tớ thích."}]
        },
        "Unit 8: In the village": {
            "phonics": "Vv",
            "words": [{"en": "van", "vi": "xe tải"}, {"en": "village", "vi": "ngôi làng"}, {"en": "volleyball", "vi": "bóng chuyền"}],
            "sentences": [{"en": "Can you draw a van?", "vi": "Cậu có thể vẽ xe tải không?"}]
        },
        "Unit 9: In the grocery store": {
            "phonics": "Yy",
            "words": [{"en": "yam", "vi": "khoai từ"}, {"en": "yo-yo", "vi": "con yo-yo"}, {"en": "yogurt", "vi": "sữa chua"}],
            "sentences": [{"en": "I like yogurt.", "vi": "Tớ thích sữa chua."}]
        },
        "Unit 10: At the zoo": {
            "phonics": "Zz",
            "words": [{"en": "zebra", "vi": "ngựa vằn"}, {"en": "zebu", "vi": "bò u"}, {"en": "zoo", "vi": "sở thú"}],
            "sentences": [{"en": "Look at the zebra.", "vi": "Hãy nhìn con ngựa vằn."}]
        },
        "Unit 11: In the playground": {
            "phonics": "Phonics",
            "words": [{"en": "drive", "vi": "lái xe"}, {"en": "ride", "vi": "cưỡi/đi xe"}, {"en": "slide", "vi": "cầu trượt"}],
            "sentences": [{"en": "I can ride a bike.", "vi": "Tớ biết đi xe đạp."}]
        },
        "Unit 12: At the cafe": {
            "phonics": "Phonics",
            "words": [{"en": "cake", "vi": "bánh ngọt"}, {"en": "grape", "vi": "quả nho"}, {"en": "table", "vi": "cái bàn"}],
            "sentences": [{"en": "I'd like a cake, please.", "vi": "Tớ muốn một chiếc bánh ngọt."}]
        },
        "Unit 13: In the math class": {
            "phonics": "Numbers",
            "words": [{"en": "eleven", "vi": "mười một"}, {"en": "twelve", "vi": "mười hai"}, {"en": "thirteen", "vi": "mười ba"}, {"en": "fourteen", "vi": "mười bốn"}, {"en": "fifteen", "vi": "mười lăm"}],
            "sentences": [{"en": "How many pens?", "vi": "Có bao nhiêu cây bút?"}]
        },
        "Unit 14: At home": {
            "phonics": "Family",
            "words": [{"en": "brother", "vi": "anh/em trai"}, {"en": "sister", "vi": "chị/em gái"}, {"en": "grandmother", "vi": "bà"}],
            "sentences": [{"en": "This is my brother.", "vi": "Đây là anh trai tớ."}]
        },
        "Unit 15: In the clothes shop": {
            "phonics": "Clothes",
            "words": [{"en": "shirt", "vi": "áo sơ mi"}, {"en": "shoes", "vi": "đôi giày"}, {"en": "shorts", "vi": "quần đùi"}],
            "sentences": [{"en": "I have new shoes.", "vi": "Tớ có đôi giày mới."}]
        },
        "Unit 16: At the campsite": {
            "phonics": "Camping",
            "words": [{"en": "blanket", "vi": "cái chăn"}, {"en": "teapot", "vi": "ấm trà"}, {"en": "tent", "vi": "cái lều"}],
            "sentences": [{"en": "Where's the tent?", "vi": "Cái lều ở đâu?"}]
        }
    },
    "Lớp 3": {
        "Unit 1: Hello": {
            "phonics": "Hh / Bb",
            "words": [{"en": "hello", "vi": "xin chào"}, {"en": "hi", "vi": "chào"}, {"en": "goodbye", "vi": "tạm biệt"}],
            "sentences": [{"en": "Hello, I'm Ben. Nice to meet you.", "vi": "Xin chào, tớ là Ben. Rất vui được gặp bạn."}]
        },
        "Unit 2: Our names": {
            "phonics": "Mm / Nn",
            "words": [{"en": "name", "vi": "tên"}, {"en": "what", "vi": "cái gì"}, {"en": "spell", "vi": "đánh vần"}],
            "sentences": [{"en": "What's your name? My name's Linh.", "vi": "Tên bạn là gì? Tên tớ là Linh."}]
        },
        "Unit 3: Our friends": {
            "phonics": "Ff / Tt",
            "words": [{"en": "friend", "vi": "bạn bè"}, {"en": "teacher", "vi": "giáo viên"}, {"en": "Mr", "vi": "thầy/ông"}],
            "sentences": [{"en": "Is this Bill? Yes, it is.", "vi": "Đây có phải là Bill không? Đúng rồi."}]
        },
        "Unit 4: Our bodies": {
            "phonics": "Ee / Oo",
            "words": [{"en": "eye", "vi": "mắt"}, {"en": "ear", "vi": "tai"}, {"en": "nose", "vi": "mũi"}, {"en": "mouth", "vi": "miệng"}],
            "sentences": [{"en": "Touch your face. Open your mouth.", "vi": "Chạm vào mặt. Mở miệng ra."}]
        },
        "Unit 5: My hobbies": {
            "phonics": "Cc / Ss",
            "words": [{"en": "singing", "vi": "ca hát"}, {"en": "dancing", "vi": "múa/khiêu vũ"}, {"en": "drawing", "vi": "vẽ"}, {"en": "cooking", "vi": "nấu ăn"}],
            "sentences": [{"en": "What's your hobby? It's singing.", "vi": "Sở thích của bạn là gì? Là ca hát."}]
        },
        "Unit 6: Our school": {
            "phonics": "Sch",
            "words": [{"en": "school", "vi": "trường học"}, {"en": "classroom", "vi": "phòng học"}, {"en": "library", "vi": "thư viện"}],
            "sentences": [{"en": "Is this our school? Yes, it is.", "vi": "Đây có phải trường mình không? Đúng rồi."}]
        },
        "Unit 7: Classroom instructions": {
            "phonics": "Commands",
            "words": [{"en": "open", "vi": "mở"}, {"en": "close", "vi": "đóng"}, {"en": "sit down", "vi": "ngồi xuống"}, {"en": "stand up", "vi": "đứng lên"}],
            "sentences": [{"en": "Open your book, please.", "vi": "Mở sách ra nhé."}]
        },
        "Unit 8: My school things": {
            "phonics": "Things",
            "words": [{"en": "pen", "vi": "bút mực"}, {"en": "ruler", "vi": "thước kẻ"}, {"en": "eraser", "vi": "cục tẩy"}],
            "sentences": [{"en": "Do you have a pen? Yes, I do.", "vi": "Bạn có bút mực không? Có, tớ có."}]
        },
        "Unit 9: Colours": {
            "phonics": "Colors",
            "words": [{"en": "red", "vi": "màu đỏ"}, {"en": "blue", "vi": "màu xanh dương"}, {"en": "yellow", "vi": "màu vàng"}, {"en": "green", "vi": "màu xanh lá"}],
            "sentences": [{"en": "What colour is it? It's red.", "vi": "Nó màu gì? Nó màu đỏ."}]
        },
        "Unit 10: Break time activities": {
            "phonics": "Sports",
            "words": [{"en": "football", "vi": "bóng đá"}, {"en": "chess", "vi": "cờ vua"}, {"en": "badminton", "vi": "cầu lông"}],
            "sentences": [{"en": "What do you do at break time? I play football.", "vi": "Bạn làm gì vào giờ ra chơi? Tớ chơi bóng đá."}]
        }
    },
    "Lớp 4": {
        "Unit 1: My friends": {
            "phonics": "Countries",
            "words": [{"en": "Vietnam", "vi": "Việt Nam"}, {"en": "Britain", "vi": "Nước Anh"}, {"en": "America", "vi": "Nước Mỹ"}, {"en": "Japan", "vi": "Nhật Bản"}],
            "sentences": [{"en": "Where are you from? I'm from Vietnam.", "vi": "Bạn đến từ đâu? Tớ đến từ Việt Nam."}]
        },
        "Unit 2: Time and daily routines": {
            "phonics": "Routines",
            "words": [{"en": "get up", "vi": "thức dậy"}, {"en": "have breakfast", "vi": "ăn sáng"}, {"en": "go to school", "vi": "đi học"}],
            "sentences": [{"en": "What time is it? It's seven o'clock.", "vi": "Mấy giờ rồi? Mấy giờ rồi? Bảy giờ rồi."}]
        },
        "Unit 3: My week": {
            "phonics": "Days",
            "words": [{"en": "Monday", "vi": "Thứ Hai"}, {"en": "Tuesday", "vi": "Thứ Ba"}, {"en": "Wednesday", "vi": "Thứ Tư"}, {"en": "Friday", "vi": "Thứ Sáu"}],
            "sentences": [{"en": "What day is it today? It's Monday.", "vi": "Hôm nay là thứ mấy? Hôm nay là thứ Hai."}]
        },
        "Unit 4: My birthday": {
            "phonics": "Months",
            "words": [{"en": "January", "vi": "Tháng Một"}, {"en": "February", "vi": "Tháng Hai"}, {"en": "March", "vi": "Tháng Ba"}, {"en": "May", "vi": "Tháng Năm"}],
            "sentences": [{"en": "When is your birthday? It's in May.", "vi": "Sinh nhật bạn khi nào? Vào tháng Năm."}]
        },
        "Unit 5: Things we can do": {
            "phonics": "Abilities",
            "words": [{"en": "swim", "vi": "bơi"}, {"en": "cook", "vi": "nấu ăn"}, {"en": "play the guitar", "vi": "chơi đàn guitar"}],
            "sentences": [{"en": "Can you swim? Yes, I can.", "vi": "Bạn có biết bơi không? Có, tớ biết bơi."}]
        },
        "Unit 6: Our school": {
            "phonics": "Places",
            "words": [{"en": "computer room", "vi": "phòng máy tính"}, {"en": "playground", "vi": "sân trường"}, {"en": "mountain", "vi": "ngọn núi"}],
            "sentences": [{"en": "Where's your school? It's in the mountain.", "vi": "Trường bạn ở đâu? Ở trên núi."}]
        },
        "Unit 7: Our timetables": {
            "phonics": "Subjects",
            "words": [{"en": "Maths", "vi": "Môn Toán"}, {"en": "English", "vi": "Môn Tiếng Anh"}, {"en": "Science", "vi": "Môn Khoa học"}, {"en": "Art", "vi": "Môn Mỹ thuật"}],
            "sentences": [{"en": "What subjects do you have today? I have Maths.", "vi": "Hôm nay bạn có môn gì? Tớ có môn Toán."}]
        },
        "Unit 8: My favourite subject": {
            "phonics": "Interests",
            "words": [{"en": "favourite", "vi": "yêu thích"}, {"en": "reading", "vi": "đọc sách"}, {"en": "singing", "vi": "ca hát"}],
            "sentences": [{"en": "What's your favourite subject? It's English.", "vi": "Môn học yêu thích của bạn là gì? Là Tiếng Anh."}]
        },
        "Unit 9: Our sports day": {
            "phonics": "Events",
            "words": [{"en": "sports day", "vi": "ngày hội thể thao"}, {"en": "running", "vi": "chạy bộ"}, {"en": "jumping", "vi": "nhảy"}],
            "sentences": [{"en": "When is your sports day? It's in November.", "vi": "Khi nào đến ngày hội thể thao? Vào tháng 11."}]
        },
        "Unit 10: Our school trip": {
            "phonics": "Trips",
            "words": [{"en": "zoo", "vi": "sở thú"}, {"en": "farm", "vi": "trang trại"}, {"en": "museum", "vi": "bảo tàng"}],
            "sentences": [{"en": "Where were you yesterday? I was at the zoo.", "vi": "Hôm qua bạn ở đâu? Tớ ở sở thú."}]
        }
    },
    "Lớp 5": {
        "Unit 1: All about me!": {
            "phonics": "Personal",
            "words": [{"en": "address", "vi": "địa chỉ"}, {"en": "hometown", "vi": "quê hương"}, {"en": "flat", "vi": "căn hộ"}],
            "sentences": [{"en": "What's your address? It's 75 Hai Ba Trung Street.", "vi": "Địa chỉ nhà bạn ở đâu? Số 75 đường Hai Bà Trưng."}]
        },
        "Unit 2: Our homes": {
            "phonics": "Homes",
            "words": [{"en": "tower", "vi": "tòa tháp"}, {"en": "island", "vi": "hòn đảo"}, {"en": "countryside", "vi": "nông thôn"}],
            "sentences": [{"en": "What's your hometown like? It's small and quiet.", "vi": "Quê bạn thế nào? Nhỏ và yên bình."}]
        },
        "Unit 3: My foreign friends": {
            "phonics": "Personality",
            "words": [{"en": "friendly", "vi": "thân thiện"}, {"en": "helpful", "vi": "tốt bụng/hay giúp đỡ"}, {"en": "active", "vi": "năng động"}],
            "sentences": [{"en": "What's he like? He's friendly and helpful.", "vi": "Cậu ấy thế nào? Cậu ấy thân thiện và hay giúp đỡ."}]
        },
        "Unit 4: My favourite free-time activities": {
            "phonics": "Free time",
            "words": [{"en": "go swimming", "vi": "đi bơi"}, {"en": "read books", "vi": "đọc sách"}, {"en": "watch TV", "vi": "xem ti vi"}],
            "sentences": [{"en": "What do you like doing in your free time? I like reading books.", "vi": "Bạn thích làm gì lúc rảnh? Tớ thích đọc sách."}]
        },
        "Unit 5: My future job": {
            "phonics": "Jobs",
            "words": [{"en": "doctor", "vi": "bác sĩ"}, {"en": "pilot", "vi": "phi công"}, {"en": "writer", "vi": "nhà văn"}, {"en": "architect", "vi": "kiến trúc sư"}],
            "sentences": [{"en": "What would you like to be in the future? I'd like to be a doctor.", "vi": "Ước mơ tương lai của bạn làm gì? Tớ muốn làm bác sĩ."}]
        },
        "Unit 6: Our school rooms": {
            "phonics": "Frequency",
            "words": [{"en": "science lab", "vi": "phòng thí nghiệm"}, {"en": "library", "vi": "thư viện"}, {"en": "once a week", "vi": "mỗi tuần một lần"}],
            "sentences": [{"en": "How often do you go to the library? Once a week.", "vi": "Bạn đến thư viện mấy lần? Mỗi tuần một lần."}]
        },
        "Unit 7: Our favourite sports and games": {
            "phonics": "Sports",
            "words": [{"en": "table tennis", "vi": "bóng bàn"}, {"en": "volleyball", "vi": "bóng chuyền"}, {"en": "badminton", "vi": "cầu lông"}],
            "sentences": [{"en": "Which sport do you like better, table tennis or badminton?", "vi": "Bạn thích môn nào hơn, bóng bàn hay cầu lông?"}]
        },
        "Unit 8: In the countryside": {
            "phonics": "Nature",
            "words": [{"en": "cottage", "vi": "nhà tranh/nhà nhỏ"}, {"en": "stream", "vi": "dòng suối"}, {"en": "paddy field", "vi": "cánh đồng lúa"}],
            "sentences": [{"en": "What's the village like? It's peaceful and beautiful.", "vi": "Ngôi làng thế nào? Rất yên bình và đẹp."}]
        },
        "Unit 9: Our outdoor activities": {
            "phonics": "Past activities",
            "words": [{"en": "camping", "vi": "cắm trại"}, {"en": "hiking", "vi": "đi bộ đường dài"}, {"en": "picnic", "vi": "dã ngoại"}],
            "sentences": [{"en": "What did you do on your holiday? We went on a picnic.", "vi": "Kỳ nghỉ bạn làm gì? Chúng tớ đi dã ngoại."}]
        },
        "Unit 10: Our school trip memories": {
            "phonics": "Memories",
            "words": [{"en": "memories", "vi": "kỷ niệm"}, {"en": "souvenirs", "vi": "quà lưu niệm"}, {"en": "photos", "vi": "bức ảnh"}],
            "sentences": [{"en": "What did you do at the zoo? We saw the animals.", "vi": "Bạn đã làm gì ở sở thú? Chúng tớ ngắm các con vật."}]
        }
    }
}

# Sidebar selection
selected_grade = st.sidebar.selectbox("🏫 Chọn Khối Lớp:", list(DATA.keys()))
units = DATA[selected_grade]

selected_unit = st.sidebar.selectbox("📚 Chọn Bài Học (Unit):", list(units.keys()))
unit_info = units[selected_unit]

st.subheader(f"📌 [{selected_grade}] {selected_unit}")
if "phonics" in unit_info and unit_info["phonics"]:
    st.write(f"🔤 **Chủ đề / Phonics:** `{unit_info['phonics']}`")

practice_type = st.radio("🎯 Chọn nội dung luyện nói:", ["Từ vựng (Vocabulary)", "Mẫu câu (Sentence Patterns)"], horizontal=True)

if practice_type == "Từ vựng (Vocabulary)":
    items = unit_info.get("words", [])
else:
    items = unit_info.get("sentences", [])

if not items:
    st.warning("Chưa có dữ liệu cho mục này.")
else:
    selected_item = st.selectbox("👉 Chọn từ/câu muốn luyện:", [f"{item['en']} ({item['vi']})" for item in items])
    target_text = selected_item.split(" (")[0].strip()
    target_vi = selected_item.split(" (")[1].replace(")", "").strip()

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### 🎯 Mẫu tiếng Anh: **{target_text}**")
    with col2:
        st.markdown(f"### 💡 Nghĩa tiếng Việt: **{target_vi}**")

    # Fallback TTS URL using Google Translate TTS endpoint
    encoded_text = urllib.parse.quote(target_text)
    tts_fallback_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q={encoded_text}"

    # HTML / JavaScript component with robust audio & Web Speech API handling
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
            margin: 0;
        }}
        .btn {{
            padding: 12px 20px;
            font-size: 15px;
            font-weight: bold;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            margin: 6px;
            transition: all 0.2s ease-in-out;
            display: inline-flex;
            align-items: center;
            gap: 6px;
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
        .msg-box {{
            margin-top: 10px;
            padding: 10px;
            border-radius: 8px;
            font-size: 14px;
            display: none;
        }}
        .msg-error {{
            background-color: #ffebee;
            color: #c62828;
            border: 1px solid #ef9a9a;
        }}
        .msg-info {{
            background-color: #e3f2fd;
            color: #1565c0;
            border: 1px solid #90cafb;
        }}
    </style>
</head>
<body>

    <div>
        <button class="btn btn-audio" onclick="playAudio()">🔊 Nghe phát âm mẫu</button>
        <button class="btn btn-rec" id="recBtn" onclick="startListeningWithPermission()">🎙️ Bấm để thu âm</button>
    </div>

    <!-- Hidden audio element for fallback TTS -->
    <audio id="fallbackAudio" src="{tts_fallback_url}" preload="auto"></audio>

    <div id="msgBox" class="msg-box"></div>

    <div class="result-box" id="resultBox" style="display:none;">
        <div id="statusText" style="font-size: 14px; color: #888;">Kết quả phát âm của bạn:</div>
        <div class="text-said">Máy nghe được: <b id="userSpeech" style="color:#008CBA;">...</b></div>
        <div class="score" id="scoreText">0%</div>
        <div class="stars" id="starText">⭐⭐⭐</div>
        <div id="feedbackText" style="font-weight:bold; margin-top:5px;"></div>
    </div>

    <script>
        const targetText = "{target_text.lower().strip()}";
        let recognition = null;
        let isRecording = false;

        function showMsg(text, type='error') {{
            const box = document.getElementById('msgBox');
            box.style.display = 'block';
            box.className = 'msg-box ' + (type === 'error' ? 'msg-error' : 'msg-info');
            box.innerHTML = text;
        }}

        function hideMsg() {{
            document.getElementById('msgBox').style.display = 'none';
        }}

        // Audio Playback with dual engines (SpeechSynthesis + Fallback Audio)
        function playAudio() {{
            hideMsg();
            try {{
                if ('speechSynthesis' in window) {{
                    window.speechSynthesis.cancel();
                    const utterance = new SpeechSynthesisUtterance("{target_text}");
                    utterance.lang = 'en-US';
                    utterance.rate = 0.8;
                    
                    utterance.onerror = function() {{
                        playFallbackAudio();
                    }};

                    window.speechSynthesis.speak(utterance);
                }} else {{
                    playFallbackAudio();
                }}
            }} catch(e) {{
                playFallbackAudio();
            }}
        }}

        function playFallbackAudio() {{
            const audio = document.getElementById('fallbackAudio');
            if (audio) {{
                audio.play().catch(err => {{
                    showMsg('🔊 Không thể phát âm thanh. Vui lòng tắt <b>Chế độ im lặng (Silent mode)</b> trên điện thoại hoặc tăng âm lượng!', 'error');
                }});
            }}
        }}

        // Similarity algorithm
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

        // Explicit Microphone Permission & Speech Recognition
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

        async function startListeningWithPermission() {{
            hideMsg();
            if (!SpeechRecognition) {{
                showMsg('⚠️ Trình duyệt hiện tại chưa hỗ trợ thu âm trực tiếp. Hãy mở trang web bằng <b>Google Chrome</b> hoặc <b>Safari</b>!', 'error');
                return;
            }}

            if (isRecording) {{
                if (recognition) recognition.stop();
                return;
            }}

            try {{
                if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {{
                    await navigator.mediaDevices.getUserMedia({{ audio: true }});
                }}
                initAndStartRecognition();
            }} catch(err) {{
                showMsg('🔒 <b>Chưa được cấp quyền Micro!</b><br>Hãy bấm vào biểu tượng <b>Ổ khóa 🔒</b> bên cạnh đường link web và chọn <b>Cho phép Micro (Allow)</b>.', 'error');
            }}
        }}

        function initAndStartRecognition() {{
            recognition = new SpeechRecognition();
            recognition.lang = 'en-US';
            recognition.interimResults = false;
            recognition.maxAlternatives = 1;

            recognition.onstart = function() {{
                isRecording = true;
                const btn = document.getElementById("recBtn");
                btn.innerText = "🛑 Đang nghe... Hãy nói!";
                btn.classList.add("recording");
                showMsg('🎙️ Đang lắng nghe... Con hãy đọc rõ từ/câu nhé!', 'info');
            }};

            recognition.onresult = function(event) {{
                hideMsg();
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
                stopRecState();
                let errMsg = 'Không nhận diện được giọng nói. ';
                if (event.error === 'not-allowed' || event.error === 'service-not-allowed') {{
                    errMsg = '🔒 <b>Lỗi quyền Micro:</b> Trình duyệt chặn Micro. Hãy bấm biểu tượng <b>Ổ khóa 🔒</b> ở thanh địa chỉ web để bật Cho phép Micro.';
                }} else if (event.error === 'no-speech') {{
                    errMsg = '🤫 Máy chưa nghe thấy tiếng con nói. Hãy bấm nút và đọc to hơn một chút nhé!';
                }} else if (event.error === 'network') {{
                    errMsg = '🌐 Lỗi kết nối mạng. Vui lòng kiểm tra lại Wifi/4G.';
                }}
                showMsg(errMsg, 'error');
            }};

            recognition.onend = function() {{
                stopRecState();
            }};

            recognition.start();
        }}

        function stopRecState() {{
            isRecording = false;
            const btn = document.getElementById("recBtn");
            btn.innerText = "🎙️ Bấm để thu âm";
            btn.classList.remove("recording");
        }}
    </script>
</body>
</html>
"""

    components.html(html_code, height=310)

# Troubleshooting guide collapsible in Streamlit
with st.expander("⚙️ **Hướng dẫn xử lý nhanh nếu gặp lỗi Micro hoặc Âm thanh**"):
    st.markdown("""
    * **Lỗi không nghe được âm mẫu:**
      1. Tắt **Chế độ im lặng (Silent mode)** trên iPhone (gạt cần gạt bên hông máy sang chế độ Bật chuông).
      2. Tăng âm lượng loa điện thoại/máy tính.
    * **Lỗi bấm nút Micro không phản hồi / Không nhận giọng nói:**
      1. Đảm bảo mở trang web bằng trình duyệt **Google Chrome** hoặc **Safari** (không nên dùng trực tiếp giao diện trình duyệt trong Zalo/Facebook).
      2. Bấm vào biểu tượng **Ổ khóa 🔒** nằm bên cạnh đường link web ➔ Chọn **Cho phép Micro (Allow Microphone)**.
      3. Đọc to, rõ ràng và ở nơi yên tĩnh.
    """)
