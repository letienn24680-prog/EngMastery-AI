# -*- coding: utf-8 -*-
"""
Part 1: 13 Tenses & Near Future (Items 1-13)
"""

TENSES_ITEMS = [
    {
        "order": 1,
        "id": "g01-present-simple",
        "number": "#01",
        "title": "Hiện tại đơn (Present Simple)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + V(s/es) | S + am/is/are + N/Adj\n(-) S + do/does not + V_inf | S + am/is/are not + N/Adj\n(?) Do/Does + S + V_inf? | Am/Is/Are + S + N/Adj?\n* Dấu hiệu: always, usually, often, sometimes, rarely, never, every day/week, once a year...",
        "essence": "Diễn tả một chân lý, sự thật hiển nhiên; thói quen, hành động lặp đi lặp lại ở hiện tại; hoặc lịch trình, thời gian biểu cố định (tàu xe, máy bay, lịch học).",
        "examples": [
            {
                "en": "Water freezes at 0 degrees Celsius and boils at 100 degrees Celsius.",
                "vi": "Nước đóng băng ở 0 độ C và sôi ở 100 độ C.",
                "breakdown": "Chân lý khoa học hiển nhiên -> chia Hiện tại đơn số ít: freezes, boils."
            },
            {
                "en": "The express train to Da Nang departs at 7:30 tomorrow morning.",
                "vi": "Chuyến tàu hỏa tốc hành đi Đà Nẵng khởi hành lúc 7h30 sáng mai.",
                "breakdown": "Lịch trình tàu xe cố định -> dùng Hiện tại đơn (departs) diễn đạt tương lai."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The Earth ________ around the Sun, which takes approximately 365 days.",
                "options": ["A. revolves", "B. is revolving", "C. revolved", "D. has revolved"],
                "answer": 0,
                "explanation": "Chân lý tự nhiên hiển nhiên -> Dùng thì Hiện tại đơn: 'revolves' (Chủ ngữ ngôi thứ 3 số ít)."
            },
            {
                "question": "Our final English exam ________ at 8:00 AM next Monday according to the school schedule.",
                "options": ["A. will start", "B. is starting", "C. starts", "D. started"],
                "answer": 2,
                "explanation": "Lịch thi theo thời gian biểu của nhà trường -> Dùng thì Hiện tại đơn: 'starts'."
            }
        ]
    },
    {
        "order": 2,
        "id": "g02-present-continuous",
        "number": "#02",
        "title": "Hiện tại tiếp diễn (Present Continuous)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + am/is/are + V-ing\n(-) S + am/is/are not + V-ing\n(?) Am/Is/Are + S + V-ing?\n* Dấu hiệu: now, right now, at the moment, at present, Look!, Listen!, Be quiet!...",
        "essence": "Diễn tả hành động đang diễn ra ngay tại thời điểm nói; kế hoạch dự định chắc chắn sẽ thực hiện trong tương lai gần; hoặc sự phàn nàn về một thói quen xấu (đi kèm always, continually).",
        "examples": [
            {
                "en": "Listen! The teacher is explaining an important grammar rule.",
                "vi": "Hãy lắng nghe kìa! Giáo viên đang giải thích một quy tắc ngữ pháp quan trọng.",
                "breakdown": "Mệnh lệnh gây chú ý 'Listen!' -> hành động đang diễn ra: is explaining."
            },
            {
                "en": "He is always leaving his dirty dishes in the sink, which annoys his roommate.",
                "vi": "Anh ấy cứ luôn để bát đĩa bẩn trong bồn rửa, khiến bạn cùng phòng rất bực mình.",
                "breakdown": "Phàn nàn thói quen lặp đi lặp lại gây khó chịu: is always leaving."
            }
        ],
        "practiceQuestions": [
            {
                "question": "Please lower your voice! The baby ________ soundly in the next room.",
                "options": ["A. sleeps", "B. is sleeping", "C. slept", "D. has slept"],
                "answer": 1,
                "explanation": "Lời nhắc nhở 'Please lower your voice!' chứng tỏ hành động đang diễn ra -> dùng 'is sleeping'."
            },
            {
                "question": "We ________ to Nha Trang this weekend; our flight tickets and resort rooms have already been booked.",
                "options": ["A. fly", "B. are flying", "C. flew", "D. were flying"],
                "answer": 1,
                "explanation": "Kế hoạch đã chuẩn bị đầy đủ vé và phòng nghỉ -> dùng thì Hiện tại tiếp diễn chỉ tương lai có sắp đặt: 'are flying'."
            }
        ]
    },
    {
        "order": 3,
        "id": "g03-present-perfect",
        "number": "#03",
        "title": "Hiện tại hoàn thành (Present Perfect)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + have/has + V3/ed\n(-) S + have/has not (haven't/hasn't) + V3/ed\n(?) Have/Has + S + V3/ed?\n* Dấu hiệu: already, yet, just, ever, never, recently, so far, up to now, since + mốc tg, for + khoảng tg, this is the first time...",
        "essence": "Diễn tả hành động bắt đầu trong quá khứ kéo dài đến hiện tại; hành động vừa mới xảy ra; trải nghiệm tính đến hiện tại; hoặc hành động đã xảy ra không rõ thời gian nhưng kết quả quan trọng ở hiện tại.",
        "examples": [
            {
                "en": "They have lived in this metropolitan city for over fifteen years.",
                "vi": "Họ đã sinh sống tại thành phố đại đô thị này được hơn mười lăm năm.",
                "breakdown": "Bắt đầu 15 năm trước và hiện vẫn đang ở đó: have lived + for 15 years."
            },
            {
                "en": "This is the third time that she has won the national scholarship.",
                "vi": "Đây là lần thứ ba cô ấy giành được học bổng quốc gia.",
                "breakdown": "Cấu trúc 'This is the first/second/third time' + Present Perfect: has won."
            }
        ],
        "practiceQuestions": [
            {
                "question": "Dr. Minh ________ at this specialized hospital since he returned from Germany in 2018.",
                "options": ["A. worked", "B. is working", "C. has worked", "D. had worked"],
                "answer": 2,
                "explanation": "Cấu trúc: S + have/has V3/ed + since + S + V2/ed -> Dùng 'has worked'."
            },
            {
                "question": "This is the most challenging examination that I ________.",
                "options": ["A. ever took", "B. have ever taken", "C. was taking", "D. had ever taken"],
                "answer": 1,
                "explanation": "Cấu trúc so sánh nhất (the most challenging) + Present Perfect: 'have ever taken'."
            }
        ]
    },
    {
        "order": 4,
        "id": "g04-present-perfect-continuous",
        "number": "#04",
        "title": "Hiện tại hoàn thành tiếp diễn (Present Perfect Continuous)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + have/has + been + V-ing\n(-) S + have/has not + been + V-ing\n(?) Have/Has + S + been + V-ing?\n* Dấu hiệu: all day, all morning, for [hours/days] now, how long...",
        "essence": "Nhấn mạnh tính liên tục và kéo dài không gián đoạn của hành động từ quá khứ đến hiện tại; hoặc hành động vừa mới dứt nhưng để lại hậu quả/dấu vết rất rõ ràng ở hiện tại.",
        "examples": [
            {
                "en": "Her eyes are exhausted because she has been reading medical documents all day.",
                "vi": "Mắt cô ấy mệt mỏi vì cô ấy đã đọc tài liệu y khoa liên tục cả ngày.",
                "breakdown": "Dấu vết hiện tại (eyes are exhausted) + quá trình liên tục (all day) -> has been reading."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The ground is completely soaked because it ________ heavily for three hours.",
                "options": ["A. has been raining", "B. is raining", "C. rained", "D. was raining"],
                "answer": 0,
                "explanation": "Hậu quả hiện tại (ground is soaked) và quá trình mưa liên tục suốt 3 giờ -> Dùng 'has been raining'."
            },
            {
                "question": "How long ________ for the job interview results? - For nearly two weeks!",
                "options": ["A. have you been waiting", "B. do you wait", "C. did you wait", "D. are you waiting"],
                "answer": 0,
                "explanation": "Câu hỏi 'How long' nhấn mạnh quá trình chờ đợi kéo dài đến nay -> Dùng 'have you been waiting'."
            }
        ]
    },
    {
        "order": 5,
        "id": "g05-past-simple",
        "number": "#05",
        "title": "Quá khứ đơn (Past Simple)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + V2/ed | S + was/were + N/Adj\n(-) S + did not + V_inf | S + was/were not + N/Adj\n(?) Did + S + V_inf? | Was/Were + S + N/Adj?\n* Dấu hiệu: yesterday, ago, last week/month/year, in 1995, in the past, when S + V2...",
        "essence": "Diễn tả hành động đã bắt đầu, xảy ra và kết thúc hoàn toàn tại một thời điểm xác định trong quá khứ; hoặc một chuỗi các hành động liên tiếp trong quá khứ.",
        "examples": [
            {
                "en": "He stepped out of the taxi, paid the driver, and walked straight into the office.",
                "vi": "Anh ấy bước ra khỏi taxi, trả tiền cho tài xế và đi thẳng vào văn phòng.",
                "breakdown": "Chuỗi hành động liên tiếp trong quá khứ: stepped -> paid -> walked."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The World Health Organization ________ the eradication of smallpox in 1980.",
                "options": ["A. declares", "B. declared", "C. has declared", "D. was declaring"],
                "answer": 1,
                "explanation": "Có mốc thời gian xác định trong quá khứ 'in 1980' -> Dùng Quá khứ đơn: 'declared'."
            },
            {
                "question": "My grandparents ________ in a quiet countryside village before moving to the city in 2005.",
                "options": ["A. live", "B. lived", "C. are living", "D. have lived"],
                "answer": 1,
                "explanation": "Hành động đã hoàn toàn kết thúc trước năm 2005 -> Dùng Quá khứ đơn: 'lived'."
            }
        ]
    },
    {
        "order": 6,
        "id": "g06-past-continuous",
        "number": "#06",
        "title": "Quá khứ tiếp diễn (Past Continuous)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + was/were + V-ing\n(-) S + was/were not + V-ing\n(?) Was/Were + S + V-ing?\n* Cấu trúc: While + S + was/were + V-ing, S + V2/ed | S + was/were + V-ing WHEN + S + V2/ed | At [thời điểm cụ thể] yesterday",
        "essence": "Diễn tả hành động đang diễn ra tại một thời điểm chính xác trong quá khứ; hoặc một hành động đang diễn ra thì một hành động ngắn khác xen vào.",
        "examples": [
            {
                "en": "At 8:30 PM last night, we were revising for the national mock examination.",
                "vi": "Vào lúc 8h30 tối hôm qua, chúng tôi đang ôn tập cho kỳ thi thử quốc gia.",
                "breakdown": "Thời điểm cụ thể trong quá khứ 'At 8:30 PM last night' -> were revising."
            },
            {
                "en": "While the laboratory team was conducting the experiment, the power suddenly went out.",
                "vi": "Trong khi đội ngũ phòng thí nghiệm đang tiến hành thí nghiệm thì đột ngột mất điện.",
                "breakdown": "Đang diễn ra (was conducting) thì bị xen vào (went out)."
            }
        ],
        "practiceQuestions": [
            {
                "question": "While the tourists ________ through the national reserve, they spotted a rare snow leopard.",
                "options": ["A. trekked", "B. were trekking", "C. have trekked", "D. trek"],
                "answer": 1,
                "explanation": "Mệnh đề sau 'While' diễn tả hành động đang diễn ra trong quá khứ -> Dùng 'were trekking'."
            },
            {
                "question": "What ________ you doing at 10 PM yesterday when the emergency siren rang?",
                "options": ["A. did", "B. were", "C. had", "D. are"],
                "answer": 1,
                "explanation": "Hành động đang diễn ra tại thời điểm cụ thể 'at 10 PM yesterday' -> Dùng 'were you doing'."
            }
        ]
    },
    {
        "order": 7,
        "id": "g07-past-perfect",
        "number": "#07",
        "title": "Quá khứ hoàn thành (Past Perfect)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + had + V3/ed\n(-) S + had not (hadn't) + V3/ed\n(?) Had + S + V3/ed?\n* Cấu trúc liên kết:\n1. By the time + S + V2/ed, S + had + V3/ed\n2. S + had + V3/ed + BEFORE + S + V2/ed\n3. AFTER + S + had + V3/ed, S + V2/ed",
        "essence": "Diễn tả hành động xảy ra và hoàn tất trước một hành động khác trong quá khứ, hoặc trước một mốc thời gian trong quá khứ.",
        "examples": [
            {
                "en": "By the time the firefighter squad arrived, the neighbors had put out the fire.",
                "vi": "Trước khi đội lính cứu hỏa đến nơi, hàng xóm đã dập tắt đám cháy.",
                "breakdown": "Dập cháy xong trước (had put out) -> lính cứu hỏa đến sau (arrived)."
            }
        ],
        "practiceQuestions": [
            {
                "question": "By the time the rescue team reached the isolated mountain village, villagers ________ all flood victims.",
                "options": ["A. evacuated", "B. had evacuated", "C. have evacuated", "D. were evacuating"],
                "answer": 1,
                "explanation": "By the time + S + V2/ed, S + had + V3/ed -> Dùng 'had evacuated'."
            },
            {
                "question": "After she ________ the master's dissertation, she received a scholarship offer from Oxford.",
                "options": ["A. defended", "B. had defended", "C. was defending", "D. defends"],
                "answer": 1,
                "explanation": "After + S + had + V3/ed, S + V2/ed -> Dùng 'had defended'."
            }
        ]
    },
    {
        "order": 8,
        "id": "g08-past-perfect-continuous",
        "number": "#08",
        "title": "Quá khứ hoàn thành tiếp diễn (Past Perfect Continuous)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + had + been + V-ing\n(-) S + had not + been + V-ing\n(?) Had + S + been + V-ing?\n* Dấu hiệu: had been V-ing for [duration] before + S + V2/ed",
        "essence": "Nhấn mạnh khoảng thời gian kéo dài liên tục của một hành động trước khi có một hành động khác xảy ra trong quá khứ.",
        "examples": [
            {
                "en": "He had been driving for six straight hours before he decided to take a rest.",
                "vi": "Anh ấy đã lái xe liên tục suốt sáu tiếng đồng hồ trước khi quyết định dừng lại nghỉ ngơi.",
                "breakdown": "Lái xe liên tục 6 tiếng (had been driving) trước khi quyết định (decided)."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The marathon runner collapsed because he ________ for three hours under the scorching sun.",
                "options": ["A. has run", "B. had been running", "C. was running", "D. ran"],
                "answer": 1,
                "explanation": "Nguyên nhân dẫn đến kiệt sức trong quá khứ (collapsed) là hành động chạy liên tục trong 3 giờ trước đó -> Dùng 'had been running'."
            }
        ]
    },
    {
        "order": 9,
        "id": "g09-future-simple",
        "number": "#09",
        "title": "Tương lai đơn (Future Simple)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + will + V_inf\n(-) S + will not (won't) + V_inf\n(?) Will + S + V_inf?\n* Dấu hiệu: tomorrow, next week/year, in the future, I think, I hope, I believe, probably...",
        "essence": "Diễn tả quyết định tức thời nảy sinh ngay lúc nói; lời hứa, lời cảnh báo, đe dọa; hoặc dự đoán chủ quan về tương lai không có căn cứ hiện tại.",
        "examples": [
            {
                "en": "I think the government will implement stricter laws on carbon emissions.",
                "vi": "Tôi nghĩ rằng chính phủ sẽ áp dụng các đạo luật nghiêm ngặt hơn về lượng phát thải carbon.",
                "breakdown": "Dự đoán chủ quan cá nhân sau 'I think' -> will implement."
            },
            {
                "en": "Don't carry that heavy luggage alone; I will assist you.",
                "vi": "Đừng xách hành lý nặng một mình; tôi sẽ giúp bạn.",
                "breakdown": "Quyết định tức thì ngay lúc nói để giúp đỡ -> will assist."
            }
        ],
        "practiceQuestions": [
            {
                "question": "I am so tired. - Sit down and relax, I ________ you a cup of hot tea.",
                "options": ["A. am making", "B. will make", "C. made", "D. have made"],
                "answer": 1,
                "explanation": "Quyết định đưa ra ngay lúc nói -> Dùng thì Tương lai đơn: 'will make'."
            },
            {
                "question": "Experts predict that renewable energy ________ fossil fuels in the near future.",
                "options": ["A. replaces", "B. replaced", "C. will replace", "D. is replacing"],
                "answer": 2,
                "explanation": "Dự đoán tương lai sau 'predict that' -> Dùng 'will replace'."
            }
        ]
    },
    {
        "order": 10,
        "id": "g10-future-continuous",
        "number": "#10",
        "title": "Tương lai tiếp diễn (Future Continuous)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + will + be + V-ing\n(-) S + will not + be + V-ing\n(?) Will + S + be + V-ing?\n* Dấu hiệu: at this time tomorrow, at [specific time] next week...",
        "essence": "Diễn tả một hành động sẽ đang diễn ra tại một thời điểm hoặc một khoảng thời gian xác định trong tương lai.",
        "examples": [
            {
                "en": "At 9 o'clock tomorrow morning, thousands of students will be sitting for the national entrance exam.",
                "vi": "Vào lúc 9 giờ sáng mai, hàng ngàn học sinh sẽ đang ngồi làm bài thi tuyển sinh quốc gia.",
                "breakdown": "Thời điểm cụ thể trong tương lai 'At 9 o'clock tomorrow' -> will be sitting."
            }
        ],
        "practiceQuestions": [
            {
                "question": "This time next month, we ________ across Europe on our graduation trip.",
                "options": ["A. will travel", "B. will be travelling", "C. travelled", "D. are travelling"],
                "answer": 1,
                "explanation": "'This time next month' chỉ thời điểm xác định trong tương lai -> Dùng thì Tương lai tiếp diễn: 'will be travelling'."
            },
            {
                "question": "Don't call her at 8 PM tonight because she ________ an important board meeting.",
                "options": ["A. will attend", "B. will be attending", "C. attended", "D. attends"],
                "answer": 1,
                "explanation": "Hành động sẽ đang diễn ra vào lúc 8h tối nay -> Dùng 'will be attending'."
            }
        ]
    },
    {
        "order": 11,
        "id": "g11-future-perfect",
        "number": "#11",
        "title": "Tương lai hoàn thành (Future Perfect)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + will + have + V3/ed\n(-) S + will not + have + V3/ed\n(?) Will + S + have + V3/ed?\n* Cấu trúc liên kết:\n1. By the time + S + V(s/es) (hiện tại đơn), S + will have + V3/ed\n2. By + mốc thời gian tương lai (by 2030, by next June), S + will have + V3/ed",
        "essence": "Diễn tả hành động sẽ được hoàn tất trước một thời điểm cụ thể hoặc trước một hành động khác trong tương lai.",
        "examples": [
            {
                "en": "By the time you graduate from high school, you will have mastered English grammar.",
                "vi": "Trước khi bạn tốt nghiệp cấp ba, bạn sẽ hoàn thành việc nắm vững ngữ pháp tiếng Anh.",
                "breakdown": "By the time + S + V(hiện tại) -> vế chính dùng will have mastered."
            }
        ],
        "practiceQuestions": [
            {
                "question": "By the end of this year, the construction workers ________ the trans-national highway.",
                "options": ["A. will complete", "B. will have completed", "C. completed", "D. have completed"],
                "answer": 1,
                "explanation": "By + mốc thời gian tương lai (By the end of this year) -> Dùng Tương lai hoàn thành: 'will have completed'."
            },
            {
                "question": "By the time my brother returns from Australia, I ________ my university graduation thesis.",
                "options": ["A. will finish", "B. will have finished", "C. finished", "D. have finished"],
                "answer": 1,
                "explanation": "By the time + S + V(s/es), S + will have V3/ed -> Dùng 'will have finished'."
            }
        ]
    },
    {
        "order": 12,
        "id": "g12-future-perfect-continuous",
        "number": "#12",
        "title": "Tương lai hoàn thành tiếp diễn (Future Perfect Continuous)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + will + have + been + V-ing\n(-) S + will not + have + been + V-ing\n(?) Will + S + have + been + V-ing?\n* Dấu hiệu: By + mốc tương lai, S + will have been V-ing for [duration]",
        "essence": "Nhấn mạnh tính liên tục của một hành động tính tới một mốc thời gian xác định trong tương lai.",
        "examples": [
            {
                "en": "By next November, Professor Smith will have been lecturing at this university for 25 years.",
                "vi": "Tính đến tháng 11 tới, Giáo sư Smith sẽ giảng dạy tại trường đại học này tròn 25 năm liên tục.",
                "breakdown": "Nhấn mạnh quá trình 25 năm liên tục tính tới mốc tương lai: will have been lecturing."
            }
        ],
        "practiceQuestions": [
            {
                "question": "By next month, the environmentalist team ________ researching climate impacts for a decade.",
                "options": ["A. will conduct", "B. will have been conducting", "C. conducted", "D. is conducting"],
                "answer": 1,
                "explanation": "Nhấn mạnh độ dài thời gian liên tục 'for a decade' tính đến mốc 'By next month' -> Dùng 'will have been conducting'."
            }
        ]
    },
    {
        "order": 13,
        "id": "g13-near-future",
        "number": "#13",
        "title": "Tương lai gần (Near Future: Be going to)",
        "category": "tenses",
        "categoryLabel": "1. Hệ thống các thì",
        "sectionTitle": "Phần 1: 13 Thì & Tương Lai Gần",
        "formula": "(+) S + am/is/are + going to + V_inf\n(-) S + am/is/are not + going to + V_inf\n(?) Am/Is/Are + S + going to + V_inf?\n* Dấu hiệu: có kế hoạch từ trước, hoặc có dấu hiệu/chứng cứ rõ ràng ở hiện tại",
        "essence": "Diễn tả dự định/kế hoạch đã được cân nhắc từ trước thời điểm nói; hoặc dự đoán tương lai dựa trên dấu hiệu/bằng chứng khách quan nhìn thấy ngay lúc nói.",
        "examples": [
            {
                "en": "Look at those thick dark clouds in the sky! It is going to rain heavily.",
                "vi": "Hãy nhìn những đám mây đen dày đặc trên bầu trời kìa! Trời sắp mưa to rồi đấy.",
                "breakdown": "Dự đoán dựa trên bằng chứng hiện tại (mây đen) -> is going to rain."
            },
            {
                "en": "I have saved money for months; I am going to buy a new laptop next week.",
                "vi": "Tôi đã tiết kiệm tiền suốt mấy tháng; tôi dự định sẽ mua một chiếc máy tính xách tay mới vào tuần tới.",
                "breakdown": "Kế hoạch đã chuẩn bị tiền từ trước -> am going to buy."
            }
        ],
        "practiceQuestions": [
            {
                "question": "Be careful! The ladder is wobbling; you ________ fall!",
                "options": ["A. will", "B. are going to", "C. were", "D. have"],
                "answer": 1,
                "explanation": "Dự đoán có bằng chứng trực quan rõ rệt (thang đang rung lắc) -> Dùng 'are going to fall'."
            },
            {
                "question": "We have already made hotel reservations; we ________ spend our vacation in Da Nang.",
                "options": ["A. are going to", "B. will", "C. would", "D. shall"],
                "answer": 0,
                "explanation": "Kế hoạch đã chuẩn bị trước (đã đặt phòng) -> Dùng 'are going to spend'."
            }
        ]
    }
]

print(f"Part 1 ready with {len(TENSES_ITEMS)} items.")

