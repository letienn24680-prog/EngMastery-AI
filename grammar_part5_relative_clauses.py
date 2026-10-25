# -*- coding: utf-8 -*-
"""
Part 5: 5 Relative Clauses Structures (Items 39-43)
"""

RELATIVE_ITEMS = [
    {
        "order": 39,
        "id": "g39-defining-relative",
        "number": "#39",
        "title": "Mệnh đề quan hệ xác định (Defining Relative Clauses)",
        "category": "relative_clauses",
        "categoryLabel": "5. Mệnh đề quan hệ",
        "sectionTitle": "Phần 5: Mệnh Đề Quan Hệ Toàn Diện",
        "formula": "S + Defining Relative Clause + V_main...\n- Không có dấu phẩy\n- Mệnh đề bắt buộc phải có để xác định danh từ phía trước\n- Có thể dùng đại từ \"THAT\" thay cho who, whom, which\n- Có thể lược bỏ đại từ quan hệ khi nó đóng vai trò làm tân ngữ (O)",
        "essence": "Cung cấp thông tin thiết yếu để định danh chính xác đối tượng được nhắc đến. Nếu lược bỏ mệnh đề này, câu sẽ tối nghĩa hoặc không hoàn chỉnh.",
        "examples": [
            {
                "en": "The scholarship that was awarded to Lan helped her cover all university tuition fees.",
                "vi": "Suất học bổng được trao cho Lan đã giúp cô ấy trang trải toàn bộ học phí đại học.",
                "breakdown": "Mệnh đề quan hệ xác định không có dấu phẩy, dùng 'that' thay cho 'which'."
            },
            {
                "en": "The professor (whom) I interviewed yesterday has published over 50 scientific papers.",
                "vi": "Vị giáo sư mà tôi phỏng vấn ngày hôm qua đã xuất bản hơn 50 bài báo khoa học.",
                "breakdown": "Đại từ quan hệ làm tân ngữ (whom/that) có thể được lược bỏ."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The candidate ________ scored highest on the entrance exam received a full scholarship.",
                "options": ["A. who", "B. which", "C. whose", "D. whom"],
                "answer": 0,
                "explanation": "Chủ ngữ chỉ người 'The candidate' làm chủ từ cho động từ 'scored' -> Dùng 'who' (hoặc that)."
            },
            {
                "question": "The scientific software ________ my team developed won first prize in the national tech contest.",
                "options": ["A. which", "B. who", "C. whom", "D. whose"],
                "answer": 0,
                "explanation": "Chỉ vật 'software' làm tân ngữ cho 'developed' -> Dùng 'which' (hoặc that)."
            }
        ]
    },
    {
        "order": 40,
        "id": "g40-non-defining-relative",
        "number": "#40",
        "title": "Mệnh đề quan hệ không xác định (Non-defining Relative Clauses)",
        "category": "relative_clauses",
        "categoryLabel": "5. Mệnh đề quan hệ",
        "sectionTitle": "Phần 5: Mệnh Đề Quan Hệ Toàn Diện",
        "formula": "S , Non-defining Relative Clause , V_main...\n- BẮT BUỘC có dấu phẩy ngăn cách\n- TUYỆT ĐỐI KHÔNG dùng đại từ \"THAT\"\n- TUYỆT ĐỐI KHÔNG được lược bỏ đại từ quan hệ\n- Dùng sau danh từ riêng, danh từ có this/that/these/those, hoặc sở hữu (my, his, their...)",
        "essence": "Cung cấp thêm thông tin bổ trợ (extra information) cho một đối tượng vốn đã được xác định rõ ràng. Nếu bỏ mệnh đề này thì câu vẫn hoàn toàn đầy đủ nghĩa.",
        "examples": [
            {
                "en": "Ha Long Bay, which was recognized by UNESCO as a World Natural Heritage site, attracts millions of visitors.",
                "vi": "Vịnh Hạ Long, nơi được UNESCO công nhận là di sản thiên nhiên thế giới, thu hút hàng triệu du khách.",
                "breakdown": "Ha Long Bay là danh từ riêng -> ngăn cách bằng 2 dấu phẩy, dùng 'which', không dùng 'that'."
            }
        ],
        "practiceQuestions": [
            {
                "question": "Albert Einstein, ________ developed the theory of relativity, was awarded the Nobel Prize in Physics.",
                "options": ["A. who", "B. that", "C. whom", "D. which"],
                "answer": 0,
                "explanation": "Tên riêng có dấu phẩy ngăn cách (Non-defining) chỉ người làm chủ từ -> Dùng 'who' (tuyệt đối không dùng that)."
            },
            {
                "question": "My father's vintage car, ________ was manufactured in 1968, still operates smoothly.",
                "options": ["A. that", "B. which", "C. whom", "D. who"],
                "answer": 1,
                "explanation": "Danh từ có sở hữu 'My father's vintage car' đi kèm dấu phẩy chỉ vật -> Dùng 'which'."
            }
        ]
    },
    {
        "order": 41,
        "id": "g41-relative-pronouns-adverbs",
        "number": "#41",
        "title": "Đại từ quan hệ và Trạng từ quan hệ (Who, Whom, Which, That, Whose, Where, When, Why)",
        "category": "relative_clauses",
        "categoryLabel": "5. Mệnh đề quan hệ",
        "sectionTitle": "Phần 5: Mệnh Đề Quan Hệ Toàn Diện",
        "formula": "1. Đại từ quan hệ:\n- WHO: thay cho người (chủ ngữ hoặc tân ngữ)\n- WHOM: thay cho người (chỉ làm tân ngữ: Whom + S + V)\n- WHICH: thay cho vật (chủ ngữ hoặc tân ngữ)\n- THAT: thay cho who, whom, which trong mệnh đề xác định\n- WHOSE + Noun: chỉ sở hữu (người hoặc vật)\n2. Trạng từ quan hệ:\n- WHERE = in / at which (thay thế trạng từ nơi chốn)\n- WHEN = in / on / at which (thay thế trạng từ thời gian)\n- WHY = for which (thay thế lý do: the reason why)",
        "essence": "Kết nối hai câu đơn thành một câu phức, thay thế cho danh từ hoặc trạng từ đứng trước để tránh lặp từ.",
        "examples": [
            {
                "en": "The boy whose mother is a renowned neurosurgeon won the national science fair.",
                "vi": "Cậu bé có mẹ là một bác sĩ phẫu thuật thần kinh nổi tiếng đã giành giải nhất hội thi khoa học quốc gia.",
                "breakdown": "Whose + Noun (whose mother): sở hữu."
            },
            {
                "en": "That was the memorable summer when we volunteered in the highlands.",
                "vi": "Đó là mùa hè đáng nhớ khi chúng tôi đi làm tình nguyện ở vùng cao.",
                "breakdown": "When = in which (thay cho thời gian the summer)."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The passionate environmentalist ________ organization planted one million trees was honored at the summit.",
                "options": ["A. whose", "B. who", "C. whom", "D. which"],
                "answer": 0,
                "explanation": "Chỉ sở hữu 'tổ chức CỦA nhà môi trường' (whose organization) -> Dùng 'whose'."
            },
            {
                "question": "This is the hospital ________ the clinical trials for the new vaccine were conducted.",
                "options": ["A. where", "B. which", "C. when", "D. why"],
                "answer": 0,
                "explanation": "Chỉ nơi chốn nơi sự việc diễn ra (in the hospital) -> Dùng trạng từ quan hệ 'where'."
            }
        ]
    },
    {
        "order": 42,
        "id": "g42-relative-prepositions",
        "number": "#42",
        "title": "Mệnh đề quan hệ với giới từ (Relative Clauses with Prepositions: Prep + Whom/Which)",
        "category": "relative_clauses",
        "categoryLabel": "5. Mệnh đề quan hệ",
        "sectionTitle": "Phần 5: Mệnh Đề Quan Hệ Toàn Diện",
        "formula": "1. Đưa giới từ lên trước đại từ quan hệ:\n- Với người: PREPOSITION + WHOM (tuyệt đối KHÔNG dùng who hoặc that sau giới từ)\n- Với vật: PREPOSITION + WHICH (tuyệt đối KHÔNG dùng that sau giới từ)\n2. Cụm từ chỉ số lượng / định lượng:\n- all of / none of / neither of / both of / either of / most of / some of / each of / one of + WHOM / WHICH",
        "essence": "Phong cách học thuật chuẩn mực trong tiếng Anh trang trọng; rất thường xuyên xuất hiện trong các câu hỏi phân loại 8+ và 9+ của đề thi THPT Quốc Gia.",
        "examples": [
            {
                "en": "The academic supervisor under whom she conducted research was a distinguished professor.",
                "vi": "Người hướng dẫn học thuật mà dưới sự hướng dẫn của thầy cô ấy đã làm nghiên cứu là một vị giáo sư ưu tú.",
                "breakdown": "Giới từ UNDER đứng trước đại từ chỉ người: under WHOM."
            },
            {
                "en": "The university library acquired 500 new textbooks, all of which were imported from the UK.",
                "vi": "Thư viện trường đại học đã mua thêm 500 cuốn giáo trình mới, tất cả số đó đều được nhập khẩu từ Vương quốc Anh.",
                "breakdown": "Định lượng chỉ vật: all of WHICH."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The foreign diplomat to ________ the ambassador presented the credential credentials was warmly welcomed.",
                "options": ["A. whom", "B. who", "C. that", "D. which"],
                "answer": 0,
                "explanation": "Sau giới từ 'to' chỉ người, bắt buộc dùng 'whom' -> Dùng 'to whom'."
            },
            {
                "question": "The tech firm recruited twenty young engineers, most of ________ held degrees from prestigious universities.",
                "options": ["A. whom", "B. which", "C. that", "D. who"],
                "answer": 0,
                "explanation": "Chỉ số lượng chỉ người 'most of...' -> Bắt buộc dùng 'most of whom'."
            }
        ]
    },
    {
        "order": 43,
        "id": "g43-reduced-relative",
        "number": "#43",
        "title": "Rút gọn mệnh đề quan hệ (Reduced Relative Clauses: V-ing, V3/ed, To-V, Cụm danh từ)",
        "category": "relative_clauses",
        "categoryLabel": "5. Mệnh đề quan hệ",
        "sectionTitle": "Phần 5: Mệnh Đề Quan Hệ Toàn Diện",
        "formula": "1. Rút gọn bằng V-ING khi mệnh đề mang nghĩa CHỦ ĐỘNG:\n   The boy who sits next to me -> The boy SITTING next to me\n2. Rút gọn bằng V3/ED khi mệnh đề mang nghĩa BỊ ĐỘNG:\n   The books which were published in 2020 -> The books PUBLISHED in 2020\n3. Rút gọn bằng TO V_INF khi có từ bổ nghĩa: the first, the second, the last, the only, so sánh nhất:\n   Yuri Gagarin was the first man who flew into space -> Yuri Gagarin was the first man TO FLY into space\n4. Rút gọn bằng Cụm danh từ (Appositive):\n   Ha Long Bay, which is a natural wonder -> Ha Long Bay, A NATURAL WONDER...",
        "essence": "Chuyên đề cốt lõi số 1 trong bài thi THPTQG giúp biến câu phức rườm rà thành câu súc tích, ngắn gọn và tự nhiên.",
        "examples": [
            {
                "en": "Candidates arriving after the test commencement time will not be admitted.",
                "vi": "Những thí sinh đến sau giờ bắt đầu làm bài sẽ không được vào phòng thi.",
                "breakdown": "Chủ động: Candidates who arrive... -> Candidates arriving..."
            },
            {
                "en": "Neil Armstrong was the first human to set foot on the Moon in 1969.",
                "vi": "Neil Armstrong là con người đầu tiên đặt chân lên Mặt Trăng vào năm 1969.",
                "breakdown": "Sau 'the first' -> rút gọn bằng TO V: to set foot."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The scientific paper ________ by our research team was published in a prestigious international journal.",
                "options": ["A. writing", "B. written", "C. to write", "D. was written"],
                "answer": 1,
                "explanation": "Bài báo khoa học được viết (bị động: which was written) -> Rút gọn bằng Quá khứ phân từ: 'written'."
            },
            {
                "question": "Marie Curie was the first woman ________ two Nobel Prizes in distinct scientific fields.",
                "options": ["A. winning", "B. to win", "C. won", "D. was won"],
                "answer": 1,
                "explanation": "Có từ thứ tự 'the first woman' mang nghĩa chủ động -> Rút gọn bằng 'to win'."
            }
        ]
    }
]

print(f"Part 5 ready with {len(RELATIVE_ITEMS)} items.")

