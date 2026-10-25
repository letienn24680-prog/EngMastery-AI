# -*- coding: utf-8 -*-
"""
Part 2: 6 Passive Voice Structures (Items 14-19)
"""

PASSIVE_ITEMS = [
    {
        "order": 14,
        "id": "g14-basic-passive",
        "number": "#14",
        "title": "Bị động cơ bản theo các thì (Basic Passive Voice)",
        "category": "passive",
        "categoryLabel": "2. Thể bị động",
        "sectionTitle": "Phần 2: Thể Bị Động Toàn Diện",
        "formula": "Quy tắc chung: S + BE (chia theo thì) + V3/ed + (by O)\n1. Hiện tại đơn: S + am/is/are + V3/ed\n2. Quá khứ đơn: S + was/were + V3/ed\n3. Tiếp diễn: S + am/is/are/was/were + BEING + V3/ed\n4. Hoàn thành: S + have/has/had + BEEN + V3/ed\n5. Tương lai đơn: S + will + BE + V3/ed",
        "essence": "Dùng khi chủ ngữ là đối tượng chịu tác động của hành động, hoặc khi người thực hiện hành động không quan trọng, không rõ danh tính, hoặc đã quá hiển nhiên.",
        "examples": [
            {
                "en": "The national high school exam papers are strictly sealed and confidential.",
                "vi": "Đề thi THPT Quốc gia được niêm phong nghiêm ngặt và bảo mật.",
                "breakdown": "Hiện tại đơn bị động: are sealed (chủ ngữ số nhiều exam papers)."
            },
            {
                "en": "A new modern bridge is being built across the Red River.",
                "vi": "Một cây cầu hiện đại mới đang được xây dựng bắc qua sông Hồng.",
                "breakdown": "Hiện tại tiếp diễn bị động: is being built."
            }
        ],
        "practiceQuestions": [
            {
                "question": "Millions of smartphones ________ by tech companies every month.",
                "options": ["A. manufacture", "B. are manufactured", "C. were manufactured", "D. are manufacturing"],
                "answer": 1,
                "explanation": "Chủ ngữ 'Millions of smartphones' là vật chịu tác động, thói quen lặp lại ở hiện tại -> Dùng bị động hiện tại đơn: 'are manufactured'."
            },
            {
                "question": "The historical monument ________ by a severe storm last September.",
                "options": ["A. damaged", "B. was damaged", "C. is damaged", "D. had damaged"],
                "answer": 1,
                "explanation": "Có mốc thời gian quá khứ 'last September' và chủ ngữ bị động -> Dùng 'was damaged'."
            }
        ]
    },
    {
        "order": 15,
        "id": "g15-passive-modals",
        "number": "#15",
        "title": "Bị động với động từ khuyết thiếu (Passive with Modals)",
        "category": "passive",
        "categoryLabel": "2. Thể bị động",
        "sectionTitle": "Phần 2: Thể Bị Động Toàn Diện",
        "formula": "1. Hiện tại / Tương lai: S + modal (can, must, should, may, might, have to) + BE + V3/ed\n2. Quá khứ (phỏng đoán/tiếc nuối): S + modal + HAVE BEEN + V3/ed",
        "essence": "Chuyển câu chứa động từ khuyết thiếu sang dạng bị động để nhấn mạnh quyền hạn, nghĩa vụ, sự bắt buộc hoặc phỏng đoán đối với đối tượng bị tác động.",
        "examples": [
            {
                "en": "All plastic waste must be sorted before recycling.",
                "vi": "Tất cả rác thải nhựa phải được phân loại trước khi đem tái chế.",
                "breakdown": "Modal 'must' + be + V3/ed: must be sorted."
            },
            {
                "en": "The report should have been submitted yesterday.",
                "vi": "Bản báo cáo lẽ ra đã phải được nộp từ ngày hôm qua.",
                "breakdown": "Bị động quá khứ với modal tiếc nuối: should have been submitted."
            }
        ],
        "practiceQuestions": [
            {
                "question": "Strict environmental regulations must ________ to preserve national parks.",
                "options": ["A. enforce", "B. be enforced", "C. to enforce", "D. being enforced"],
                "answer": 1,
                "explanation": "Cấu trúc bị động với modal verb: must + be + V3/ed -> Dùng 'be enforced'."
            },
            {
                "question": "This rare artifact ought to ________ with extreme care in the museum.",
                "options": ["A. be preserved", "B. preserve", "C. have preserved", "D. preserving"],
                "answer": 0,
                "explanation": "Ought to + be + V3/ed -> Dùng 'be preserved'."
            }
        ]
    },
    {
        "order": 16,
        "id": "g16-causative-form",
        "number": "#16",
        "title": "Bị động thể nhờ bảo / sai khiến (Causative Form: Have / Get sth done)",
        "category": "passive",
        "categoryLabel": "2. Thể bị động",
        "sectionTitle": "Phần 2: Thể Bị Động Toàn Diện",
        "formula": "1. Thể chủ động:\n- HAVE + sb + V_inf (nhờ ai làm gì)\n- GET + sb + TO V_inf (thuyết phục/nhờ ai làm gì)\n2. Thể bị động (cực hay thi):\n- S + HAVE / GET + sth + V3/ed (bởi ai: by sb)",
        "essence": "Dùng khi người nói không tự mình làm một việc gì đó mà thuê, nhờ, hoặc yêu cầu một người khác thực hiện cho mình.",
        "examples": [
            {
                "en": "My father had his car repaired by a certified mechanic yesterday.",
                "vi": "Bố tôi đã nhờ một thợ cơ khí lành nghề sửa chiếc xe ô tô của ông vào ngày hôm qua.",
                "breakdown": "S + had + sth (his car) + V3/ed (repaired)."
            },
            {
                "en": "She got her university application translated into English.",
                "vi": "Cô ấy đã nhờ người dịch hồ sơ ứng tuyển đại học của mình sang tiếng Anh.",
                "breakdown": "S + got + sth (her application) + V3/ed (translated)."
            }
        ],
        "practiceQuestions": [
            {
                "question": "I am going to have my air conditioner ________ before the summer heatwave begins.",
                "options": ["A. servicing", "B. to service", "C. serviced", "D. service"],
                "answer": 2,
                "explanation": "Cấu trúc bị động nhờ bảo: have + sth + V3/ed -> Dùng 'serviced'."
            },
            {
                "question": "The manager got his secretary ________ all the meeting documents for the directors.",
                "options": ["A. to prepare", "B. prepare", "C. prepared", "D. preparing"],
                "answer": 0,
                "explanation": "Cấu trúc chủ động của GET: get + sb + TO V_inf -> Dùng 'to prepare'."
            }
        ]
    },
    {
        "order": 17,
        "id": "g17-impersonal-passive",
        "number": "#17",
        "title": "Bị động khách quan / tường thuật ý kiến (Impersonal Passive: It is said that...)",
        "category": "passive",
        "categoryLabel": "2. Thể bị động",
        "sectionTitle": "Phần 2: Thể Bị Động Toàn Diện",
        "formula": "Chủ động: People/They + say/believe/think/report/rumor + that + S2 + V2...\n-> Cách 1: It + is/was + said/believed/thought + that + S2 + V2...\n-> Cách 2 (Chuyển S2 lên đầu):\n- Cùng thì: S2 + is/are/was/were said + TO V_inf\n- Khác thì (V2 xảy ra trước V1): S2 + is/are/was/were said + TO HAVE V3/ed",
        "essence": "Dùng để truyền đạt thông tin, dư luận hoặc ý kiến của số đông một cách khách quan, trang trọng mà không cần chỉ đích danh ai nói.",
        "examples": [
            {
                "en": "It is reported that the global temperature has risen by 1.1 degrees Celsius.",
                "vi": "Người ta báo cáo rằng nhiệt độ toàn cầu đã tăng 1,1 độ C.",
                "breakdown": "Dạng bị động giả: It is reported that..."
            },
            {
                "en": "Thomas Edison is believed to have invented the phonograph in 1877.",
                "vi": "Thomas Edison được tin là đã phát minh ra máy hát đĩa vào năm 1877.",
                "breakdown": "Tin ở hiện tại (is believed) nhưng phát minh trong quá khứ (1877) -> TO HAVE V3: to have invented."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The ancient fortress is believed ________ by Roman architects centuries ago.",
                "options": ["A. to build", "B. to be built", "C. to have been built", "D. building"],
                "answer": 2,
                "explanation": "Pháo đài được xây trong quá khứ (centuries ago) trước thời điểm hiện tại (is believed) và mang nghĩa bị động -> Dùng 'to have been built'."
            },
            {
                "question": "It ________ that the newly discovered drug could cure rare viral infections.",
                "options": ["A. is said", "B. says", "C. has said", "D. is saying"],
                "answer": 0,
                "explanation": "Cấu trúc bị động khách quan: It is said that + S + V -> Dùng 'is said'."
            }
        ]
    },
    {
        "order": 18,
        "id": "g18-passive-perception",
        "number": "#18",
        "title": "Bị động với động từ chỉ giác quan / tri giác (Passive with verbs of perception)",
        "category": "passive",
        "categoryLabel": "2. Thể bị động",
        "sectionTitle": "Phần 2: Thể Bị Động Toàn Diện",
        "formula": "1. Chủ động:\n- S + see / hear / watch / notice + O + V_inf (chứng kiến toàn bộ hành động)\n- S + see / hear / watch / notice + O + V-ing (chứng kiến hành động đang diễn ra)\n2. Bị động:\n- S(O) + be + seen / heard / noticed + TO V_inf (toàn bộ hành động: thêm 'to')\n- S(O) + be + seen / heard / noticed + V-ing (hành động đang diễn ra: giữ nguyên V-ing)",
        "essence": "Diễn tả một đối tượng được người khác nhìn thấy, nghe thấy hoặc nhận thấy đang làm gì hoặc làm xong việc gì.",
        "examples": [
            {
                "en": "The suspect was seen to enter the jewelry store through the back door.",
                "vi": "Kẻ tình nghi được nhìn thấy đã đi vào cửa hàng trang sức qua cửa sau.",
                "breakdown": "Chủ động: People saw the suspect enter -> Bị động thêm 'to': was seen TO ENTER."
            },
            {
                "en": "The young girl was heard singing a traditional lullaby in the garden.",
                "vi": "Người ta nghe thấy cô bé đang hát một bài hát ru truyền thống trong vườn.",
                "breakdown": "Chủ động: Heard her singing -> Bị động giữ nguyên V-ing: was heard singing."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The thief was seen ________ the perimeter wall and escape into the dark forest.",
                "options": ["A. climb", "B. to climb", "C. climbed", "D. to be climbed"],
                "answer": 1,
                "explanation": "Bị động của động từ giác quan (see sb do sth) chuyển sang bị động thêm 'to' -> 'was seen to climb'."
            },
            {
                "question": "Children were noticed ________ football in the school playground during the afternoon break.",
                "options": ["A. playing", "B. to be played", "C. played", "D. having played"],
                "answer": 0,
                "explanation": "Chứng kiến hành động đang diễn ra: be noticed + V-ing -> Dùng 'playing'."
            }
        ]
    },
    {
        "order": 19,
        "id": "g19-passive-two-objects",
        "number": "#19",
        "title": "Bị động kép và bị động có hai tân ngữ (Passive with two objects)",
        "category": "passive",
        "categoryLabel": "2. Thể bị động",
        "sectionTitle": "Phần 2: Thể Bị Động Toàn Diện",
        "formula": "Chủ động: S + V + O1 (người: tân ngữ gián tiếp) + O2 (vật: tân ngữ trực tiếp)\n(Ví dụ: give, send, lend, offer, teach, buy, pay...)\n-> Bị động 1 (đưa tân ngữ người lên đầu - tự nhiên nhất):\n   O1 + BE + V3/ed + O2 + (by S)\n-> Bị động 2 (đưa tân ngữ vật lên đầu - cần thêm giới từ to/for):\n   O2 + BE + V3/ed + TO / FOR + O1 + (by S)",
        "essence": "Khi câu chủ động có hai tân ngữ (tân ngữ chỉ người và tân ngữ chỉ vật), có thể tạo thành 2 câu bị động tương ứng tùy thuộc vào thông tin muốn nhấn mạnh.",
        "examples": [
            {
                "en": "The outstanding student was awarded a full scholarship by the university.",
                "vi": "Học sinh xuất sắc đã được trường đại học trao một suất học bổng toàn phần.",
                "breakdown": "Bị động 1 (đưa người O1 lên làm chủ ngữ): The student was awarded a scholarship."
            },
            {
                "en": "A generous scholarship was awarded TO the outstanding student.",
                "vi": "Một suất học bổng hào phóng đã được trao cho người học sinh xuất sắc.",
                "breakdown": "Bị động 2 (đưa vật O2 lên làm chủ ngữ): thêm giới từ TO."
            }
        ],
        "practiceQuestions": [
            {
                "question": "All newly hired employees were offered ________ by the company director.",
                "options": ["A. a lucrative contract", "B. to a lucrative contract", "C. for a lucrative contract", "D. with a lucrative contract"],
                "answer": 0,
                "explanation": "Cấu trúc bị động: S (người) + be offered + O (vật) -> Dùng trực tiếp danh từ 'a lucrative contract'."
            },
            {
                "question": "A prestigious medal was presented ________ the war veteran by the President.",
                "options": ["A. for", "B. to", "C. with", "D. at"],
                "answer": 1,
                "explanation": "Khi đưa tân ngữ vật lên trước (A medal was presented), giới từ đi với người là TO -> 'presented to the war veteran'."
            }
        ]
    }
]

print(f"Part 2 ready with {len(PASSIVE_ITEMS)} items.")

