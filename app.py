import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Luyện Phát Âm Tiếng Anh Tiểu Học - Global Success (Lớp 1-5)",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Luyện Phát Âm Tiếng Anh Tiểu Học")
st.caption("Chương trình Tiếng Anh Tiểu học (Lớp 1 - Lớp 5) - Global Success / Kết Nối Tri Thức")

# Database of Units for Grades 1, 2, 3, 4, 5
DATA = {
    "Lớp 1": {
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
    },
    "Lớp 2": {
        "Unit 1: At my birthday party": {
            "phonics": "Pp",
            "words": [
                {"en": "pasta", "vi": "mỳ Ý"},
                {"en": "pizza", "vi": "bánh pizza"},
                {"en": "popcorn", "vi": "bỏng ngô"}
            ],
            "sentences": [
                {"en": "I like pasta.", "vi": "Tớ thích mỳ Ý."},
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
                {"en": "Is he flying a kite?", "vi": "Cậu ấy đang thả diều phải không?"},
                {"en": "Yes, he is.", "vi": "Đúng vậy."}
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
                {"en": "Look at the sail.", "vi": "Hãy nhìn cánh buồm kìa."}
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
                {"en": "There's a rainbow.", "vi": "Có một cầu vồng kìa."}
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
                {"en": "Is there a question?", "vi": "Có câu hỏi nào không?"}
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
                {"en": "I see a fox.", "vi": "Tớ thấy một con cáo."}
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
                {"en": "Pass me the jam, please.", "vi": "Làm ơn chuyển giùm tớ hũ mứt."}
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
                {"en": "Can you draw a van?", "vi": "Bạn có thể vẽ một chiếc xe tải không?"}
            ]
        },
        "Unit 9: In the grocery store": {
            "phonics": "Yy",
            "words": [
                {"en": "yam", "vi": "củ khoai"},
                {"en": "yo-yo", "vi": "cái yo-yo"},
                {"en": "yogurt", "vi": "sữa chua"}
            ],
            "sentences": [
                {"en": "I want some yogurt.", "vi": "Tớ muốn ăn một ít sữa chua."}
            ]
        },
        "Unit 10: At the zoo": {
            "phonics": "Zz",
            "words": [
                {"en": "zebra", "vi": "ngựa vằn"},
                {"en": "zebu", "vi": "con bò u"},
                {"en": "zoo", "vi": "vườn thú"}
            ],
            "sentences": [
                {"en": "Look at the zebra.", "vi": "Hãy nhìn con ngựa vằn kìa."}
            ]
        },
        "Unit 11: In the playground": {
            "phonics": "Actions",
            "words": [
                {"en": "drive", "vi": "lái xe"},
                {"en": "ride", "vi": "cưỡi/đi xe đạp"},
                {"en": "slide", "vi": "cầu trượt"}
            ],
            "sentences": [
                {"en": "He's riding a bike.", "vi": "Cậu ấy đang đi xe đạp."}
            ]
        },
        "Unit 12: At the café": {
            "phonics": "Foods & Drinks",
            "words": [
                {"en": "cake", "vi": "bánh ngọt"},
                {"en": "grape", "vi": "quả nho"},
                {"en": "table", "vi": "cái bàn"}
            ],
            "sentences": [
                {"en": "She's having grapes.", "vi": "Cô ấy đang ăn nho."}
            ]
        },
        "Unit 13: In the math class": {
            "phonics": "Numbers 11-15",
            "words": [
                {"en": "eleven", "vi": "mười một (11)"},
                {"en": "twelve", "vi": "mười hai (12)"},
                {"en": "thirteen", "vi": "mười ba (13)"},
                {"en": "fourteen", "vi": "mười bốn (14)"},
                {"en": "fifteen", "vi": "mười lăm (15)"}
            ],
            "sentences": [
                {"en": "How many books? Thirteen.", "vi": "Có bao nhiêu quyển sách? Mười ba quyển."}
            ]
        },
        "Unit 14: At home": {
            "phonics": "Family & Numbers 16-20",
            "words": [
                {"en": "brother", "vi": "anh/em trai"},
                {"en": "sister", "vi": "chị/em gái"},
                {"en": "sixteen", "vi": "mười sáu (16)"},
                {"en": "twenty", "vi": "hai mươi (20)"}
            ],
            "sentences": [
                {"en": "How old is your brother?", "vi": "Anh/em trai của bạn bao nhiêu tuổi?"}
            ]
        },
        "Unit 15: In the clothes shop": {
            "phonics": "Sh",
            "words": [
                {"en": "shirt", "vi": "áo sơ mi"},
                {"en": "shoes", "vi": "đôi giày"},
                {"en": "shorts", "vi": "quần đùi"}
            ],
            "sentences": [
                {"en": "Where are the shoes?", "vi": "Đôi giày ở đâu?"}
            ]
        },
        "Unit 16: At the campsite": {
            "phonics": "Camping items",
            "words": [
                {"en": "blanket", "vi": "cái chăn"},
                {"en": "teapot", "vi": "ấm trà"},
                {"en": "tent", "vi": "cái lều"}
            ],
            "sentences": [
                {"en": "Is the teapot near the table?", "vi": "Ấm trà ở gần cái bàn phải không?"}
            ]
        }
    },
    "Lớp 3": {
        "Unit 1: Hello": {
            "phonics": "Greetings",
            "words": [
                {"en": "hello", "vi": "xin chào"},
                {"en": "goodbye", "vi": "tạm biệt"},
                {"en": "fine", "vi": "khỏe, tốt"},
                {"en": "thank you", "vi": "cảm ơn bạn"}
            ],
            "sentences": [
                {"en": "Hello. I'm Ben.", "vi": "Xin chào. Tớ là Ben."},
                {"en": "Nice to meet you.", "vi": "Rất vui được gặp bạn."}
            ]
        },
        "Unit 2: Our names": {
            "phonics": "Names & Spelling",
            "words": [
                {"en": "name", "vi": "tên"},
                {"en": "spell", "vi": "đánh vần"},
                {"en": "what", "vi": "cái gì/thế nào"}
            ],
            "sentences": [
                {"en": "What's your name?", "vi": "Tên bạn là gì?"},
                {"en": "My name's Mary.", "vi": "Tên tớ là Mary."}
            ]
        },
        "Unit 3: Our friends": {
            "phonics": "Friends & Teachers",
            "words": [
                {"en": "friend", "vi": "bạn bè"},
                {"en": "teacher", "vi": "giáo viên"},
                {"en": "this", "vi": "đây/cái này"}
            ],
            "sentences": [
                {"en": "This is my friend, Bill.", "vi": "Đây là bạn của tớ, Bill."},
                {"en": "Is this Ms Hoa?", "vi": "Đây là cô Hoa phải không?"}
            ]
        },
        "Unit 4: Our bodies": {
            "phonics": "Body parts",
            "words": [
                {"en": "eye", "vi": "mắt"},
                {"en": "ear", "vi": "tai"},
                {"en": "nose", "vi": "mũi"},
                {"en": "mouth", "vi": "miệng"},
                {"en": "hand", "vi": "bàn tay"}
            ],
            "sentences": [
                {"en": "Touch your nose.", "vi": "Chạm vào mũi của bạn."},
                {"en": "Open your mouth.", "vi": "Mở miệng ra."}
            ]
        },
        "Unit 5: My hobbies": {
            "phonics": "Hobbies",
            "words": [
                {"en": "sing", "vi": "hát"},
                {"en": "dance", "vi": "múa/nhảy"},
                {"en": "cook", "vi": "nấu ăn"},
                {"en": "swim", "vi": "bơi"},
                {"en": "draw", "vi": "vẽ"}
            ],
            "sentences": [
                {"en": "My hobby is singing.", "vi": "Sở thích của tớ là hát."},
                {"en": "I like cooking.", "vi": "Tớ thích nấu ăn."}
            ]
        },
        "Unit 6: Our school": {
            "phonics": "School facilities",
            "words": [
                {"en": "school", "vi": "trường học"},
                {"en": "classroom", "vi": "phòng học"},
                {"en": "library", "vi": "thư viện"},
                {"en": "gym", "vi": "phòng tập thể dục"}
            ],
            "sentences": [
                {"en": "Is this our school?", "vi": "Đây có phải trường học của chúng ta không?"},
                {"en": "Yes, it is.", "vi": "Đúng vậy."}
            ]
        },
        "Unit 7: Classroom instructions": {
            "phonics": "Commands",
            "words": [
                {"en": "open", "vi": "mở"},
                {"en": "close", "vi": "đóng"},
                {"en": "speak", "vi": "nói"},
                {"en": "ask", "vi": "hỏi"},
                {"en": "answer", "vi": "trả lời"}
            ],
            "sentences": [
                {"en": "Open your book, please.", "vi": "Làm ơn mở sách ra."},
                {"en": "May I come in?", "vi": "Em xin phép vào lớp ạ?"}
            ]
        },
        "Unit 8: My school things": {
            "phonics": "School supplies",
            "words": [
                {"en": "pen", "vi": "bút mực"},
                {"en": "pencil", "vi": "bút chì"},
                {"en": "ruler", "vi": "thước kẻ"},
                {"en": "rubber", "vi": "cục tẩy"},
                {"en": "school bag", "vi": "cặp sách"}
            ],
            "sentences": [
                {"en": "Do you have a pen?", "vi": "Bạn có bút mực không?"},
                {"en": "Yes, I do.", "vi": "Tớ có."}
            ]
        },
        "Unit 9: Colours": {
            "phonics": "Colours",
            "words": [
                {"en": "red", "vi": "màu đỏ"},
                {"en": "blue", "vi": "màu xanh nước biển"},
                {"en": "yellow", "vi": "màu vàng"},
                {"en": "green", "vi": "màu xanh lá cây"},
                {"en": "brown", "vi": "màu nâu"}
            ],
            "sentences": [
                {"en": "What colour is it?", "vi": "Nó có màu gì?"},
                {"en": "It's red.", "vi": "Nó màu đỏ."}
            ]
        },
        "Unit 10: Break time activities": {
            "phonics": "Sports & Games",
            "words": [
                {"en": "chess", "vi": "cờ vua"},
                {"en": "football", "vi": "bóng đá"},
                {"en": "badminton", "vi": "cầu lông"},
                {"en": "basketball", "vi": "bóng rổ"}
            ],
            "sentences": [
                {"en": "What do you do at break time?", "vi": "Bạn làm gì giờ ra chơi?"},
                {"en": "I play chess.", "vi": "Tớ chơi cờ vua."}
            ]
        }
    },
    "Lớp 4": {
        "Unit 1: My friends": {
            "phonics": "Countries & Nationalities",
            "words": [
                {"en": "America", "vi": "nước Mỹ"},
                {"en": "Australia", "vi": "nước Úc"},
                {"en": "Britain", "vi": "nước Anh"},
                {"en": "Japan", "vi": "nước Nhật"},
                {"en": "Malaysia", "vi": "nước Ma-lai-xi-a"}
            ],
            "sentences": [
                {"en": "Where are you from?", "vi": "Bạn từ đâu đến?"},
                {"en": "I'm from Viet Nam.", "vi": "Tớ đến từ Việt Nam."}
            ]
        },
        "Unit 2: Time and daily routines": {
            "phonics": "Daily routine",
            "words": [
                {"en": "get up", "vi": "thức dậy"},
                {"en": "go to school", "vi": "đi học"},
                {"en": "have lunch", "vi": "ăn trưa"},
                {"en": "go to bed", "vi": "đi ngủ"}
            ],
            "sentences": [
                {"en": "What time is it?", "vi": "Mấy giờ rồi?"},
                {"en": "It's seven o'clock.", "vi": "Bây giờ là 7 giờ."}
            ]
        },
        "Unit 3: My week": {
            "phonics": "Days of the week",
            "words": [
                {"en": "Monday", "vi": "Thứ Hai"},
                {"en": "Tuesday", "vi": "Thứ Ba"},
                {"en": "Wednesday", "vi": "Thứ Tư"},
                {"en": "Thursday", "vi": "Thứ Năm"},
                {"en": "Friday", "vi": "Thứ Sáu"},
                {"en": "Saturday", "vi": "Thứ Bảy"},
                {"en": "Sunday", "vi": "Chủ Nhật"}
            ],
            "sentences": [
                {"en": "What day is it today?", "vi": "Hôm nay là thứ mấy?"},
                {"en": "It's Monday.", "vi": "Hôm nay là thứ Hai."}
            ]
        },
        "Unit 4: My birthday party": {
            "phonics": "Months & Food",
            "words": [
                {"en": "January", "vi": "Tháng Một"},
                {"en": "February", "vi": "Tháng Hai"},
                {"en": "March", "vi": "Tháng Ba"},
                {"en": "April", "vi": "Tháng Tư"},
                {"en": "lemonade", "vi": "nước chanh"}
            ],
            "sentences": [
                {"en": "When's your birthday?", "vi": "Sinh nhật bạn khi nào?"},
                {"en": "It's in April.", "vi": "Nó vào tháng Tư."}
            ]
        },
        "Unit 5: Things we can do": {
            "phonics": "Abilities",
            "words": [
                {"en": "cook", "vi": "nấu ăn"},
                {"en": "play the piano", "vi": "chơi đàn piano"},
                {"en": "ride a bike", "vi": "đi xe đạp"},
                {"en": "roller skate", "vi": "trượt pa-tanh"}
            ],
            "sentences": [
                {"en": "Can you play the piano?", "vi": "Bạn có biết chơi đàn piano không?"},
                {"en": "Yes, I can.", "vi": "Có, tớ biết chơi."}
            ]
        },
        "Unit 6: Our school rooms": {
            "phonics": "School rooms",
            "words": [
                {"en": "computer room", "vi": "phòng máy tính"},
                {"en": "art room", "vi": "phòng mỹ thuật"},
                {"en": "music room", "vi": "phòng âm nhạc"}
            ],
            "sentences": [
                {"en": "Where's the computer room?", "vi": "Phòng máy tính ở đâu?"},
                {"en": "It's on the first floor.", "vi": "Nó ở tầng một."}
            ]
        },
        "Unit 7: Our timetables": {
            "phonics": "Subjects",
            "words": [
                {"en": "English", "vi": "môn Tiếng Anh"},
                {"en": "maths", "vi": "môn Toán"},
                {"en": "science", "vi": "môn Khoa học"},
                {"en": "Vietnamese", "vi": "môn Tiếng Việt"}
            ],
            "sentences": [
                {"en": "What subjects do you have today?", "vi": "Hôm nay bạn có những môn học nào?"},
                {"en": "I have English and maths.", "vi": "Tớ có môn Tiếng Anh và môn Toán."}
            ]
        },
        "Unit 8: My favourite subjects": {
            "phonics": "Jobs & Interests",
            "words": [
                {"en": "favourite", "vi": "yêu thích"},
                {"en": "reporter", "vi": "phóng viên"},
                {"en": "painter", "vi": "họa sĩ"},
                {"en": "singer", "vi": "ca sĩ"}
            ],
            "sentences": [
                {"en": "What's your favourite subject?", "vi": "Môn học yêu thích của bạn là gì?"},
                {"en": "It's English.", "vi": "Đó là môn Tiếng Anh."}
            ]
        },
        "Unit 9: Our outdoor activities": {
            "phonics": "Places",
            "words": [
                {"en": "campsite", "vi": "địa điểm cắm trại"},
                {"en": "theatre", "vi": "nhà hát"},
                {"en": "aquarium", "vi": "thủy cung"},
                {"en": "funfair", "vi": "hội chợ giải trí"}
            ],
            "sentences": [
                {"en": "Were you at the campsite yesterday?", "vi": "Hôm qua bạn ở địa điểm cắm trại phải không?"},
                {"en": "Yes, I was.", "vi": "Đúng vậy."}
            ]
        },
        "Unit 10: Our school trip": {
            "phonics": "Trips",
            "words": [
                {"en": "Ba Na Hills", "vi": "Bà Nà Hills"},
                {"en": "Hoan Kiem Lake", "vi": "Hồ Hoàn Kiếm"},
                {"en": "Suoi Tien Theme Park", "vi": "Công viên Suối Tiên"}
            ],
            "sentences": [
                {"en": "Did you go to Ba Na Hills last weekend?", "vi": "Cuối tuần trước bạn có đi Bà Nà Hills không?"},
                {"en": "Yes, we did.", "vi": "Có, chúng tớ có đi."}
            ]
        }
    },
    "Lớp 5": {
        "Unit 1: All about me!": {
            "phonics": "Self introduction",
            "words": [
                {"en": "city", "vi": "thành phố"},
                {"en": "countryside", "vi": "nông thôn"},
                {"en": "table tennis", "vi": "bóng bàn"},
                {"en": "sandwich", "vi": "bánh mì kẹp"}
            ],
            "sentences": [
                {"en": "Can you tell me about yourself?", "vi": "Bạn có thể giới thiệu về bản thân không?"},
                {"en": "I live in the city.", "vi": "Tớ sống ở thành phố."}
            ]
        },
        "Unit 2: Our homes": {
            "phonics": "Addresses",
            "words": [
                {"en": "building", "vi": "tòa nhà"},
                {"en": "flat", "vi": "căn hộ"},
                {"en": "tower", "vi": "tháp/tòa tháp"},
                {"en": "street", "vi": "con đường/phố"}
            ],
            "sentences": [
                {"en": "Do you live in this building?", "vi": "Bạn có sống ở tòa nhà này không?"},
                {"en": "What's your address?", "vi": "Địa chỉ của bạn là gì?"}
            ]
        },
        "Unit 3: My foreign friends": {
            "phonics": "Nationalities & Personalities",
            "words": [
                {"en": "Australian", "vi": "người Úc"},
                {"en": "Malaysian", "vi": "người Ma-lai-xi-a"},
                {"en": "American", "vi": "người Mỹ"},
                {"en": "Japanese", "vi": "người Nhật"},
                {"en": "active", "vi": "năng động"},
                {"en": "friendly", "vi": "thân thiện"}
            ],
            "sentences": [
                {"en": "What nationality is he?", "vi": "Cậu ấy mang quốc tịch gì?"},
                {"en": "He's Australian.", "vi": "Cậu ấy là người Úc."}
            ]
        },
        "Unit 4: Our free-time activities": {
            "phonics": "Free time",
            "words": [
                {"en": "go for a walk", "vi": "đi dạo bộ"},
                {"en": "play the violin", "vi": "chơi đàn vi-ô-lông"},
                {"en": "surf the Internet", "vi": "lướt mạng Internet"},
                {"en": "water the flowers", "vi": "tưới hoa"}
            ],
            "sentences": [
                {"en": "What do you like doing in your free time?", "vi": "Bạn thích làm gì vào thời gian rảnh?"},
                {"en": "I like watching cartoons.", "vi": "Tớ thích xem phim hoạt hình."}
            ]
        },
        "Unit 5: My future job": {
            "phonics": "Future jobs",
            "words": [
                {"en": "firefighter", "vi": "lính cứu hỏa"},
                {"en": "gardener", "vi": "người làm vườn"},
                {"en": "reporter", "vi": "phóng viên"},
                {"en": "writer", "vi": "nhà văn"},
                {"en": "doctor", "vi": "bác sĩ"}
            ],
            "sentences": [
                {"en": "What would you like to be in the future?", "vi": "Bạn muốn làm nghề gì trong tương lai?"},
                {"en": "I'd like to be a doctor.", "vi": "Tớ muốn trở thành bác sĩ."}
            ]
        },
        "Unit 6: Our school rooms": {
            "phonics": "Directions in school",
            "words": [
                {"en": "upstairs", "vi": "lên tầng/trên gác"},
                {"en": "downstairs", "vi": "xuống tầng/dưới gác"},
                {"en": "corridor", "vi": "hành lang"}
            ],
            "sentences": [
                {"en": "He's going upstairs.", "vi": "Cậu ấy đang đi lên tầng."},
                {"en": "She's running downstairs.", "vi": "Cô ấy đang chạy xuống tầng."}
            ]
        },
        "Unit 7: Our favourite school activities": {
            "phonics": "School activities",
            "words": [
                {"en": "solving maths problems", "vi": "giải bài tập toán"},
                {"en": "reading books", "vi": "đọc sách"},
                {"en": "doing projects", "vi": "làm dự án"}
            ],
            "sentences": [
                {"en": "What school activities does she like?", "vi": "Cô ấy thích hoạt động trường học nào?"},
                {"en": "She likes reading books.", "vi": "Cô ấy thích đọc sách."}
            ]
        },
        "Unit 8: My friend's study corner": {
            "phonics": "Stationery",
            "words": [
                {"en": "set square", "vi": "thước ê-ke"},
                {"en": "pencil sharpener", "vi": "gọt bút chì"},
                {"en": "crayon", "vi": "bút sáp màu"},
                {"en": "glue stick", "vi": "keo dán/hồ dán"}
            ],
            "sentences": [
                {"en": "Whose school bag is this?", "vi": "Cặp sách này của ai?"},
                {"en": "It's Mai's.", "vi": "Đó là của Mai."}
            ]
        },
        "Unit 9: Our outdoor activities": {
            "phonics": "Past activities",
            "words": [
                {"en": "theatre", "vi": "nhà hát"},
                {"en": "aquarium", "vi": "thủy cung"},
                {"en": "campsite", "vi": "địa điểm cắm trại"},
                {"en": "funfair", "vi": "hội chợ giải trí"}
            ],
            "sentences": [
                {"en": "Were you at the theatre yesterday?", "vi": "Hôm qua bạn có ở nhà hát không?"},
                {"en": "Yes, we were.", "vi": "Có, chúng tớ có ở đó."}
            ]
        },
        "Unit 10: Our school trip": {
            "phonics": "Past trips",
            "words": [
                {"en": "visit old buildings", "vi": "thăm các tòa nhà cổ"},
                {"en": "plant trees", "vi": "trồng cây"},
                {"en": "walk around the lake", "vi": "đi dạo quanh hồ"}
            ],
            "sentences": [
                {"en": "Did they go to Ba Na Hills last weekend?", "vi": "Cuối tuần trước họ có đi Bà Nà Hills không?"},
                {"en": "Yes, they did.", "vi": "Có, họ có đi."}
            ]
        }
    }
}

# Sidebar grade selection
st.sidebar.title("🏫 Chọn Khối Lớp")
selected_grade = st.sidebar.radio("Danh sách các lớp:", ["Lớp 1", "Lớp 2", "Lớp 3", "Lớp 4", "Lớp 5"])

grade_data = DATA[selected_grade]

# Sidebar unit selection
selected_unit = st.sidebar.selectbox("📚 Chọn Bài Học (Unit):", list(grade_data.keys()))
unit_info = grade_data[selected_unit]

st.subheader(f"📌 {selected_grade} - {selected_unit}")
st.write(f"🔤 **Chủ điểm / Âm chính (Phonics):** `{unit_info['phonics']}`")

# Practice type selection
practice_type = st.radio("🎯 Chọn nội dung luyện nói:", ["Từ vựng (Vocabulary)", "Mẫu câu (Sentence Patterns)"], horizontal=True)

if practice_type == "Từ vựng (Vocabulary)":
    items = unit_info["words"]
else:
    items = unit_info["sentences"]

selected_item = st.selectbox("👉 Chọn từ/câu muốn luyện phát âm:", [f"{item['en']} ({item['vi']})" for item in items])
target_text = selected_item.split(" (")[0].strip()
target_vi = selected_item.split(" (")[1].replace(")", "").strip()

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"### 🎯 Mẫu tiếng Anh: **{target_text}**")
with col2:
    st.markdown(f"### 💡 Nghĩa tiếng Việt: **{target_vi}**")

# Interactive Speech Recognition and Text-To-Speech Component using Web Speech API
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
        <button class="btn btn-audio" onclick="playAudio()">🔊 Nghe âm mẫu</button>
        <button id="recBtn" class="btn btn-rec" onclick="toggleRecording()">🎙️ Thu âm luyện đọc</button>
    </div>

    <div class="result-box" id="resultBox" style="display: none;">
        <div id="stars" class="stars"></div>
        <div id="score" class="score"></div>
        <div id="saidText" class="text-said"></div>
        <div id="feedback" style="margin-top: 10px; font-weight: 500; font-size: 16px;"></div>
    </div>

    <script>
        const targetText = "{target_text.lower()}";

        function playAudio() {{
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance("{target_text}");
            utterance.lang = 'en-US';
            utterance.rate = 0.85; // Slightly slower speed for primary students
            window.speechSynthesis.speak(utterance);
        }}

        // Speech Recognition Setup
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        let recognition = null;
        let isRecording = false;

        if (SpeechRecognition) {{
            recognition = new SpeechRecognition();
            recognition.lang = 'en-US';
            recognition.interimResults = false;
            recognition.maxAlternatives = 1;

            recognition.onstart = function() {{
                isRecording = true;
                const btn = document.getElementById('recBtn');
                btn.innerText = '🔴 Đang nghe... Hãy nói đi!';
                btn.classList.add('recording');
            }};

            recognition.onresult = function(event) {{
                const transcript = event.results[0][0].transcript.toLowerCase().trim();
                evaluateSpeech(transcript);
            }};

            recognition.onerror = function(event) {{
                alert('Không thể nhận diện giọng nói hoặc chưa cấp quyền Micro: ' + event.error);
                stopRecState();
            }};

            recognition.onend = function() {{
                stopRecState();
            }};
        }} else {{
            alert('Trình duyệt của bạn không hỗ trợ tính năng nhận diện giọng nói Web Speech API. Hãy thử dùng Google Chrome hoặc Microsoft Edge.');
        }}

        function toggleRecording() {{
            if (!recognition) return;
            if (isRecording) {{
                recognition.stop();
            }} else {{
                recognition.start();
            }}
        }}

        function stopRecState() {{
            isRecording = false;
            const btn = document.getElementById('recBtn');
            btn.innerText = '🎙️ Thu âm luyện đọc';
            btn.classList.remove('recording');
        }}

        function evaluateSpeech(said) {{
            document.getElementById('resultBox').style.display = 'block';
            document.getElementById('saidText').innerText = '🗣️ Bạn đã đọc: "' + said + '"';

            // Levenshtein distance for accuracy percentage
            let accuracy = calculateSimilarity(said, targetText);
            
            let starsStr = '';
            let feedbackStr = '';
            
            if (accuracy >= 85) {{
                starsStr = '⭐⭐⭐';
                feedbackStr = '🎉 Tuyệt vời! Bạn phát âm cực kỳ chuẩn xác!';
            }} else if (accuracy >= 50) {{
                starsStr = '⭐⭐';
                feedbackStr = '👍 Khá lắm! Cố gắng phát âm rõ hơn một chút nữa nhé!';
            }} else {{
                starsStr = '⭐';
                feedbackStr = '💪 Hãy nghe lại mẫu và thử đọc lại lần nữa nhé!';
            }}

            document.getElementById('stars').innerText = starsStr;
            document.getElementById('score').innerText = 'Độ chính xác: ' + accuracy + '%';
            document.getElementById('feedback').innerText = feedbackStr;
        }}

        function calculateSimilarity(s1, s2) {{
            s1 = s1.replace(/[^a-zA-Z0-9 ]/g, "");
            s2 = s2.replace(/[^a-zA-Z0-9 ]/g, "");
            
            if (s1 === s2) return 100;
            
            let words1 = s1.split(" ");
            let words2 = s2.split(" ");
            let matches = 0;
            
            words2.forEach(w => {{
                if (words1.includes(w)) matches++;
            }});
            
            let score = Math.round((matches / words2.length) * 100);
            
            // Edit distance bonus
            if (score === 0) {{
                let len = Math.max(s1.length, s2.length);
                if (len === 0) return 100;
                let dist = levenshtein(s1, s2);
                score = Math.max(0, Math.round((1 - dist / len) * 100));
            }}
            
            return Math.min(100, Math.max(10, score));
        }}

        function levenshtein(a, b) {{
            const matrix = [];
            for (let i = 0; i <= b.length; i++) matrix[i] = [i];
            for (let j = 0; j <= a.length; j++) matrix[0][j] = j;

            for (let i = 1; i <= b.length; i++) {{
                for (let j = 1; j <= a.length; j++) {{
                    if (b.charAt(i - 1) == a.charAt(j - 1)) {{
                        matrix[i][j] = matrix[i - 1][j - 1];
                    }} else {{
                        matrix[i][j] = Math.min(
                            matrix[i - 1][j - 1] + 1,
                            matrix[i][j - 1] + 1,
                            matrix[i - 1][j] + 1
                        );
                    }}
                }}
            }}
            return matrix[i][j];
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=320)
