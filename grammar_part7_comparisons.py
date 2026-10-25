# -*- coding: utf-8 -*-
"""
Part 7: 6 Comparisons Structures (Items 48-53)
"""

COMPARISONS_ITEMS = [
    {
        "order": 48,
        "id": "g48-equal-comparison",
        "number": "#48",
        "title": "So sánh bằng và không bằng (Equal Comparison)",
        "category": "comparisons",
        "categoryLabel": "7. Cấu trúc so sánh",
        "sectionTitle": "Phần 7: Các Cấu Trúc So Sánh",
        "formula": "1. Khẳng định (Bằng nhau):\n   S1 + V + AS + adj / adv + AS + S2 / O\n   (Ví dụ: as diligent as, as fluently as)\n2. Phủ định (Không bằng nhau):\n   S1 + V(phủ định) + NOT AS / NOT SO + adj / adv + AS + S2 / O\n3. So sánh danh từ giống nhau:\n   S1 + V + THE SAME + (Noun) + AS + S2\n   (Ví dụ: the same age as, the same height as)",
        "essence": "So sánh sự tương đồng hoặc khác biệt về tính chất, mức độ hoặc khả năng giữa hai người, hai sự vật hoặc hai hành động.",
        "examples": [
            {
                "en": "Lan speaks English as fluently as a native speaker.",
                "vi": "Lan nói tiếng Anh lưu loát như một người bản xứ.",
                "breakdown": "So sánh trạng từ 'fluently' đi với động từ 'speaks': as fluently as."
            },
            {
                "en": "Living in a quiet countryside village is not as stressful as living in a crowded metropolis.",
                "vi": "Sống ở làng quê yên bình không căng thẳng bằng sống ở đại đô thị đông đúc.",
                "breakdown": "So sánh không bằng: not as stressful as."
            }
        ],
        "practiceQuestions": [
            {
                "question": "This newly developed algorithm does not process massive data sets ________ that older program.",
                "options": ["A. as slow as", "B. so slowly as", "C. more slowly", "D. slower than"],
                "answer": 1,
                "explanation": "Động từ 'process' cần trạng từ 'slowly'; câu phủ định (does not) dùng 'so slowly as' (hoặc as slowly as)."
            },
            {
                "question": "Minh is the same age ________ my elder brother; both were born in 2006.",
                "options": ["A. as", "B. like", "C. with", "D. to"],
                "answer": 0,
                "explanation": "Cấu trúc so sánh: the same + N + AS -> Dùng 'as'."
            }
        ]
    },
    {
        "order": 49,
        "id": "g49-comparative",
        "number": "#49",
        "title": "So sánh hơn (Comparative)",
        "category": "comparisons",
        "categoryLabel": "7. Cấu trúc so sánh",
        "sectionTitle": "Phần 7: Các Cấu Trúc So Sánh",
        "formula": "1. Tính từ / Trạng từ ngắn (1 âm tiết, hoặc 2 âm tiết tận cùng -y, -le, -ow, -er):\n   S1 + V + Adj/Adv-ER + THAN + S2 / O\n   (Ví dụ: faster than, earlier than, simpler than)\n2. Tính từ / Trạng từ dài (2 âm tiết trở lên):\n   S1 + V + MORE + Adj/Adv + THAN + S2 / O\n   (Ví dụ: more convenient than, more diligently than)\n3. Từ nhấn mạnh mức độ chênh lệch (đứng trước so sánh hơn):\n   MUCH / FAR / A LOT / SIGNIFICANTLY (nhiều) | SLIGHTLY / A BIT (chút ít)\n   (Ví dụ: much more expensive, far better than)",
        "essence": "Dùng để so sánh sự hơn kém giữa hai đối tượng về một đặc điểm hoặc một hành động cụ thể.",
        "examples": [
            {
                "en": "Travelling by high-speed bullet train is far more convenient than taking a conventional bus.",
                "vi": "Đi lại bằng tàu cao tốc tiện lợi hơn nhiều so với việc đi xe buýt thông thường.",
                "breakdown": "Nhấn mạnh mức độ 'far' + so sánh hơn tính từ dài: far more convenient than."
            }
        ],
        "practiceQuestions": [
            {
                "question": "Solar energy is becoming ________ cheaper and more accessible than traditional fossil fuels.",
                "options": ["A. much", "B. more", "C. very", "D. so"],
                "answer": 0,
                "explanation": "Từ bổ nghĩa nhấn mạnh cho tính từ so sánh hơn (cheaper) là 'much' (hoặc far, a lot) -> Dùng 'much cheaper'."
            },
            {
                "question": "The living expenses in Tokyo are significantly higher than ________ in rural towns.",
                "options": ["A. that", "B. those", "C. these", "D. this"],
                "answer": 1,
                "explanation": "So sánh đối tượng số nhiều (living expenses) thay bằng đại từ 'those of / those in' -> Dùng 'those'."
            }
        ]
    },
    {
        "order": 50,
        "id": "g50-superlative",
        "number": "#50",
        "title": "So sánh nhất (Superlative)",
        "category": "comparisons",
        "categoryLabel": "7. Cấu trúc so sánh",
        "sectionTitle": "Phần 7: Các Cấu Trúc So Sánh",
        "formula": "1. Tính từ / Trạng từ ngắn:\n   S + V + THE + Adj/Adv-EST + (in / of / among...)\n   (Ví dụ: the highest mountain in Vietnam)\n2. Tính từ / Trạng từ dài:\n   S + V + THE MOST + Adj/Adv + (in / of / among...)\n   (Ví dụ: the most influential scientist of our era)\n3. Thứ hạng (Thứ hai, thứ ba...):\n   S + V + the second / third / fourth + most Adj / Adj-est\n4. Một trong những... nhất:\n   one of the most Adj + N(số nhiều)",
        "essence": "Dùng để so sánh một đối tượng vượt trội nhất trong một nhóm gồm từ ba đối tượng trở lên.",
        "examples": [
            {
                "en": "Fansipan is celebrated as the highest mountain peak in Indochina.",
                "vi": "Phan Xi Păng được ca ngợi là đỉnh núi cao nhất tại Đông Dương.",
                "breakdown": "Tính từ ngắn: the highest + in Indochina (phạm vi nơi chốn dùng IN)."
            },
            {
                "en": "Artificial intelligence is considered one of the most transformative technologies in human history.",
                "vi": "Trí tuệ nhân tạo được coi là một trong những công nghệ mang tính biến đổi mạnh mẽ nhất trong lịch sử nhân loại.",
                "breakdown": "One of the most transformative + N_plural (technologies)."
            }
        ],
        "practiceQuestions": [
            {
                "question": "Da Nang is frequently cited as one of the most ________ cities to live in Southeast Asia.",
                "options": ["A. livable", "B. more livable", "C. most livable", "D. livably"],
                "answer": 0,
                "explanation": "Đã có 'one of the most' nên phía sau là tính từ nguyên mẫu: 'one of the most livable cities'."
            },
            {
                "question": "Russia is by far ________ country in the world in terms of geographical land area.",
                "options": ["A. the largest", "B. larger", "C. largest", "D. more large"],
                "answer": 0,
                "explanation": "So sánh nhất thế giới đi kèm từ nhấn mạnh 'by far' -> Bắt buộc có mạo từ THE: 'by far the largest'."
            }
        ]
    },
    {
        "order": 51,
        "id": "g51-progressive-comparison",
        "number": "#51",
        "title": "So sánh lũy tiến / càng ngày càng (Comparative + and + Comparative)",
        "category": "comparisons",
        "categoryLabel": "7. Cấu trúc so sánh",
        "sectionTitle": "Phần 7: Các Cấu Trúc So Sánh",
        "formula": "1. Tính từ / Trạng từ ngắn:\n   Adj/Adv-ER + AND + Adj/Adv-ER\n   (Ví dụ: faster and faster, hotter and hotter, higher and higher)\n2. Tính từ / Trạng từ dài:\n   MORE AND MORE + Adj/Adv\n   (Ví dụ: more and more expensive, more and more complicated)",
        "essence": "Diễn tả một tính chất, trạng thái đang tăng dần hoặc giảm dần liên tục theo thời gian (càng ngày càng...).",
        "examples": [
            {
                "en": "As the final exam approaches, students feel more and more anxious.",
                "vi": "Khi kỳ thi cuối kỳ đến gần, các học sinh cảm thấy càng ngày càng lo lắng.",
                "breakdown": "Tính từ dài (anxious): more and more anxious."
            },
            {
                "en": "Owing to global warming, summer temperatures are becoming hotter and hotter.",
                "vi": "Do sự nóng lên toàn cầu, nhiệt độ mùa hè đang trở nên ngày càng nóng hơn.",
                "breakdown": "Tính từ ngắn (hot): hotter and hotter."
            }
        ],
        "practiceQuestions": [
            {
                "question": "With the continuous inflation rate, essential living commodities are becoming ________ expensive.",
                "options": ["A. more and more", "B. much and more", "C. most and most", "D. as and as"],
                "answer": 0,
                "explanation": "Cấu trúc so sánh lũy tiến với tính từ dài (expensive): 'more and more expensive'."
            },
            {
                "question": "The athlete ran ________ as he neared the finish line of the race.",
                "options": ["A. faster and faster", "B. more fast and fast", "C. fast and faster", "D. fast and fast"],
                "answer": 0,
                "explanation": "Trạng từ ngắn 'fast' đổi thành 'faster and faster' (càng ngày càng nhanh)."
            }
        ]
    },
    {
        "order": 52,
        "id": "g52-double-comparative",
        "number": "#52",
        "title": "So sánh kép / càng... thì càng... (Double Comparative: The more... the more...)",
        "category": "comparisons",
        "categoryLabel": "7. Cấu trúc so sánh",
        "sectionTitle": "Phần 7: Các Cấu Trúc So Sánh",
        "formula": "THE + Comparative + S1 + V1 , THE + Comparative + S2 + V2\n1. Với tính từ/trạng từ ngắn:\n   THE + Adj/Adv-er + S + V, THE + Adj/Adv-er + S + V\n2. Với tính từ/trạng từ dài:\n   THE MORE + Adj/Adv + S + V, THE MORE + Adj/Adv + S + V\n3. Với danh từ:\n   THE MORE + Noun + S + V, THE MORE + Noun + S + V\n4. Với động từ:\n   THE MORE + S + V, THE MORE + S + V",
        "essence": "Diễn tả mối quan hệ nhân quả tương hỗ: Khi một vế biến đổi tăng/giảm thì vế kia cũng lập tức biến đổi theo mức độ tương ứng.",
        "examples": [
            {
                "en": "The more diligently you practice English every day, the more fluently you can speak.",
                "vi": "Bạn càng luyện tập tiếng Anh chăm chỉ mỗi ngày bao nhiêu, bạn càng nói lưu loát bấy nhiêu.",
                "breakdown": "The more diligently S1 + V1, the more fluently S2 + V2."
            },
            {
                "en": "The more congested the urban traffic becomes, the higher the citizens' stress level is.",
                "vi": "Giao thông đô thị càng tắc nghẽn, mức độ căng thẳng của người dân càng tăng cao.",
                "breakdown": "The more congested S1 + V1, the higher S2 + V2."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The more qualifications you possess, ________ job opportunities you will be offered.",
                "options": ["A. the more", "B. the most", "C. more", "D. the greater"],
                "answer": 0,
                "explanation": "The more + Noun (qualifications)..., THE MORE + Noun (job opportunities)... -> Dùng 'the more'."
            },
            {
                "question": "The harder you work on this project, ________ the final results will be.",
                "options": ["A. better", "B. the best", "C. the better", "D. the more good"],
                "answer": 2,
                "explanation": "The harder + S + V, THE BETTER + S + V -> Bắt buộc có mạo từ 'the' và dạng so sánh hơn 'the better'."
            }
        ]
    },
    {
        "order": 53,
        "id": "g53-multiple-numbers-comparison",
        "number": "#53",
        "title": "So sánh gấp bội / số lần (Multiple Numbers Comparison: twice as... as, three times as... as)",
        "category": "comparisons",
        "categoryLabel": "7. Cấu trúc so sánh",
        "sectionTitle": "Phần 7: Các Cấu Trúc So Sánh",
        "formula": "S + V + MULTIPLE NUMBER + AS + adj / adv / much / many + AS + O\n* Từ chỉ số lần:\n- twice (gấp đôi - KHÔNG dùng two times)\n- three times / four times / five times... (gấp ba, gấp bốn...)\n- half (bằng một nửa)\n* Danh từ đếm được: AS MANY + N(số nhiều) + AS\n* Danh từ không đếm được: AS MUCH + N(không đếm được) + AS",
        "essence": "Diễn tả một đối tượng có kích thước, số lượng, trọng lượng hoặc giá trị gấp bao nhiêu lần (hoặc bằng một nửa) so với đối tượng kia.",
        "examples": [
            {
                "en": "The new luxury electric car costs twice as much as the standard model.",
                "vi": "Chiếc xe điện hạng sang mới có giá đắt gấp đôi so với mẫu xe tiêu chuẩn.",
                "breakdown": "Twice + as much as: gấp hai lần chi phí."
            },
            {
                "en": "This modern warehouse holds three times as many goods as the old facility.",
                "vi": "Nhà kho hiện đại này chứa lượng hàng hóa nhiều gấp ba lần so với cơ sở cũ.",
                "breakdown": "Three times + as many goods as (hàng hóa đếm được)."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The tuition fee at this international school is ________ that of local public schools.",
                "options": ["A. three times as high as", "B. as three times high as", "C. higher three times than", "D. three times higher as"],
                "answer": 0,
                "explanation": "Cấu trúc so sánh gấp bội: S + V + multiple number (three times) + AS + adj (high) + AS + O -> Dùng 'three times as high as'."
            },
            {
                "question": "This newly developed solar battery stores ________ electricity as the previous prototype.",
                "options": ["A. twice as much", "B. twice as many", "C. two times much", "D. as twice much"],
                "answer": 0,
                "explanation": "'electricity' là danh từ không đếm được, dùng 'twice as much electricity as' -> Dùng 'twice as much'."
            }
        ]
    }
]

print(f"Part 7 ready with {len(COMPARISONS_ITEMS)} items.")

