# -*- coding: utf-8 -*-
"""
Part 3: 11 Conditionals & Subjunctive Structures (Items 20-30)
"""

CONDITIONALS_ITEMS = [
    {
        "order": 20,
        "id": "g20-zero-conditional",
        "number": "#20",
        "title": "Câu điều kiện loại 0 (Zero Conditional)",
        "category": "conditionals_subjunctive",
        "categoryLabel": "3. Điều kiện & Giả định",
        "sectionTitle": "Phần 3: Câu Điều Kiện & Thể Giả Định",
        "formula": "If / When + S + V(s/es) (Hiện tại đơn), S + V(s/es) (Hiện tại đơn)",
        "essence": "Diễn tả sự thật khoa học hiển nhiên, quy luật tự nhiên, hoặc thói quen chắc chắn xảy ra nếu điều kiện được đáp ứng.",
        "examples": [
            {
                "en": "If you heat ice, it melts into water.",
                "vi": "Nếu bạn đun nóng băng, nó sẽ tan chảy thành nước.",
                "breakdown": "Cả 2 mệnh đề đều chia Hiện tại đơn: heat -> melts."
            }
        ],
        "practiceQuestions": [
            {
                "question": "If you mix red and blue paint, you ________ purple.",
                "options": ["A. get", "B. will get", "C. got", "D. are getting"],
                "answer": 0,
                "explanation": "Quy luật pha màu tự nhiên hiển nhiên -> Dùng câu điều kiện loại 0: 'get'."
            }
        ]
    },
    {
        "order": 21,
        "id": "g21-first-conditional",
        "number": "#21",
        "title": "Câu điều kiện loại 1 (First Conditional)",
        "category": "conditionals_subjunctive",
        "categoryLabel": "3. Điều kiện & Giả định",
        "sectionTitle": "Phần 3: Câu Điều Kiện & Thể Giả Định",
        "formula": "If + S + V(s/es) (Hiện tại đơn), S + will / can / may / must + V_inf\n(Mệnh lệnh: If + S + V(s/es), (please) + V_inf / Don't + V_inf)",
        "essence": "Diễn tả điều kiện có thể xảy ra ở hiện tại hoặc tương lai và kết quả có thật tương ứng.",
        "examples": [
            {
                "en": "If she studies diligently every evening, she will pass the entrance exam with flying colours.",
                "vi": "Nếu cô ấy học tập chăm chỉ mỗi buổi tối, cô ấy sẽ thi đỗ kỳ thi tuyển sinh với kết quả xuất sắc.",
                "breakdown": "Mệnh đề If chia hiện tại đơn (studies), mệnh đề chính dùng will + pass."
            }
        ],
        "practiceQuestions": [
            {
                "question": "If the weather ________ favorable tomorrow morning, we will go on a field trip.",
                "options": ["A. is", "B. will be", "C. was", "D. would be"],
                "answer": 0,
                "explanation": "Trong mệnh đề IF loại 1, động từ chia ở Hiện tại đơn -> Dùng 'is'."
            },
            {
                "question": "If you encounter any technical issues with the system, ________ the hotline immediately.",
                "options": ["A. calling", "B. call", "C. called", "D. will call"],
                "answer": 1,
                "explanation": "Mệnh đề chính dạng câu mệnh lệnh -> Dùng động từ nguyên thể 'call'."
            }
        ]
    },
    {
        "order": 22,
        "id": "g22-second-conditional",
        "number": "#22",
        "title": "Câu điều kiện loại 2 (Second Conditional)",
        "category": "conditionals_subjunctive",
        "categoryLabel": "3. Điều kiện & Giả định",
        "sectionTitle": "Phần 3: Câu Điều Kiện & Thể Giả Định",
        "formula": "If + S + V2/ed (To be: WERE cho mọi ngôi), S + would / could / might + V_inf",
        "essence": "Diễn tả điều kiện giả định trái ngược với thực tế ở hiện tại, hoặc tình huống không có thật ở hiện tại; dùng đưa ra lời khuyên (If I were you).",
        "examples": [
            {
                "en": "If I had more leisure time, I would volunteer at the wildlife sanctuary.",
                "vi": "Nếu tôi có nhiều thời gian rảnh hơn, tôi sẽ đi làm tình nguyện viên tại khu bảo tồn động vật hoang dã.",
                "breakdown": "Hiện tại không có rảnh: If I had (V2) -> would volunteer."
            },
            {
                "en": "If I were in your position, I would accept that prestigious scholarship immediately.",
                "vi": "Nếu tôi ở vị trí của bạn, tôi sẽ nhận ngay suất học bổng danh giá đó.",
                "breakdown": "Lời khuyên giả định: If I were in your position -> would accept."
            }
        ],
        "practiceQuestions": [
            {
                "question": "If he ________ fluent in French, he could apply for the diplomatic position in Paris.",
                "options": ["A. is", "B. were", "C. has been", "D. will be"],
                "answer": 1,
                "explanation": "Điều kiện trái ngược với thực tế hiện tại (loại 2), to be dùng 'were' cho mọi ngôi -> Dùng 'were'."
            },
            {
                "question": "If my family lived closer to the city center, we ________ so much time commuting every day.",
                "options": ["A. won't spend", "B. wouldn't spend", "C. didn't spend", "D. haven't spent"],
                "answer": 1,
                "explanation": "Mệnh đề chính của câu điều kiện loại 2: would + V_inf -> Dùng 'wouldn't spend'."
            }
        ]
    },
    {
        "order": 23,
        "id": "g23-third-conditional",
        "number": "#23",
        "title": "Câu điều kiện loại 3 (Third Conditional)",
        "category": "conditionals_subjunctive",
        "categoryLabel": "3. Điều kiện & Giả định",
        "sectionTitle": "Phần 3: Câu Điều Kiện & Thể Giả Định",
        "formula": "If + S + had + V3/ed (Quá khứ hoàn thành), S + would / could / might + HAVE + V3/ed",
        "essence": "Diễn tả điều kiện giả định trái ngược hoàn toàn với thực tế đã xảy ra trong quá khứ, thường dùng để bày tỏ sự tiếc nuối hoặc trách móc.",
        "examples": [
            {
                "en": "If the rescue team had arrived fifteen minutes earlier, they could have saved the climbers.",
                "vi": "Nếu đội cứu hộ đến sớm hơn 15 phút, họ đã có thể cứu được những người leo núi.",
                "breakdown": "Thực tế trong quá khứ đội cứu hộ đến muộn: had arrived -> could have saved."
            }
        ],
        "practiceQuestions": [
            {
                "question": "If you ________ your seatbelt, you would not have sustained severe injuries in the crash.",
                "options": ["A. fasten", "B. had fastened", "C. were fastening", "D. fastened"],
                "answer": 1,
                "explanation": "Mệnh đề chính là 'would not have sustained' (loại 3) -> Mệnh đề If chia Quá khứ hoàn thành: 'had fastened'."
            },
            {
                "question": "If Minh had prepared more thoroughly for the interview, he ________ the job offer.",
                "options": ["A. would get", "B. will get", "C. would have got", "D. got"],
                "answer": 2,
                "explanation": "Mệnh đề If có 'had prepared' (loại 3) -> Mệnh đề chính: 'would have got'."
            }
        ]
    },
    {
        "order": 24,
        "id": "g24-mixed-conditionals",
        "number": "#24",
        "title": "Câu điều kiện hỗn hợp (Mixed Conditionals: loại 2 & 3)",
        "category": "conditionals_subjunctive",
        "categoryLabel": "3. Điều kiện & Giả định",
        "sectionTitle": "Phần 3: Câu Điều Kiện & Thể Giả Định",
        "formula": "1. Dạng 1 (Giả thiết quá khứ -> Kết quả hiện tại: Loại 3 + Loại 2):\n   If + S + had + V3/ed, S + would / could + V_inf (now / today)\n2. Dạng 2 (Bản chất hiện tại -> Kết quả quá khứ: Loại 2 + Loại 3):\n   If + S + were / V2/ed, S + would / could + HAVE + V3/ed",
        "essence": "Kết hợp giữa điều kiện ở một thời điểm (quá khứ/hiện tại) và kết quả ở một thời điểm khác (hiện tại/quá khứ). Dấu hiệu quan trọng nhất là các từ chỉ thời gian: now, today, yesterday...",
        "examples": [
            {
                "en": "If I had accepted the scholarship last year, I would be studying in London right now.",
                "vi": "Nếu năm ngoái tôi nhận học bổng, thì bây giờ tôi đang học tập ở London rồi.",
                "breakdown": "Giả thiết quá khứ (last year: had accepted) -> kết quả hiện tại (right now: would be studying)."
            },
            {
                "en": "If she weren't so afraid of flying, she would have travelled to Japan with us last summer.",
                "vi": "Nếu cô ấy không sợ đi máy bay (bản chất luôn thế), cô ấy đã đi du lịch Nhật Bản cùng chúng tôi vào mùa hè năm ngoái.",
                "breakdown": "Bản chất hiện tại (weren't) -> kết quả quá khứ (last summer: would have travelled)."
            }
        ],
        "practiceQuestions": [
            {
                "question": "If Nam had taken my advice yesterday, he ________ in such a dilemma now.",
                "options": ["A. won't be", "B. wouldn't be", "C. wouldn't have been", "D. isn't"],
                "answer": 1,
                "explanation": "Giả thiết quá khứ (yesterday: had taken) nhưng kết quả ở hiện tại (now) -> Dùng điều kiện hỗn hợp: 'wouldn't be'."
            },
            {
                "question": "If she ________ English fluently, she would have secured that foreign investment deal last month.",
                "options": ["A. spoke", "B. had spoken", "C. speaks", "D. will speak"],
                "answer": 0,
                "explanation": "Bản chất năng lực hiện tại (If she spoke) dẫn đến kết quả trong quá khứ (last month: would have secured) -> Dùng 'spoke'."
            }
        ]
    },
    {
        "order": 25,
        "id": "g25-inversion-conditionals",
        "number": "#25",
        "title": "Đảo ngữ câu điều kiện (Inversion in Conditionals: Should, Were, Had)",
        "category": "conditionals_subjunctive",
        "categoryLabel": "3. Điều kiện & Giả định",
        "sectionTitle": "Phần 3: Câu Điều Kiện & Thể Giả Định",
        "formula": "Bỏ 'IF' và đảo trợ động từ lên đầu câu:\n1. Loại 1: SHOULD + S + V_inf, S + will + V_inf\n2. Loại 2: WERE + S + to V_inf / WERE + S + Adj/Noun, S + would + V_inf\n3. Loại 3: HAD + S + V3/ed, S + would have + V3/ed\n* Phủ định: để 'NOT' sau chủ ngữ (Ví dụ: Had he not noticed...)",
        "essence": "Tăng tính trang trọng (formal), học thuật cho câu văn; xuất hiện với tần suất cực kỳ cao trong các đề thi tuyển sinh và THPT Quốc Gia.",
        "examples": [
            {
                "en": "Should you require further assistance, please contact our support team.",
                "vi": "Nếu quý khách cần thêm sự hỗ trợ, xin vui lòng liên hệ với đội ngũ chăm sóc khách hàng.",
                "breakdown": "= If you should require / If you require."
            },
            {
                "en": "Had we invested in renewable technology earlier, our operating costs would have reduced significantly.",
                "vi": "Nếu chúng ta đầu tư vào công nghệ tái tạo sớm hơn, chi phí vận hành đã giảm đáng kể.",
                "breakdown": "= If we had invested..."
            }
        ],
        "practiceQuestions": [
            {
                "question": "________ anyone call for me while I am out, please take a message.",
                "options": ["A. Should", "B. Were", "C. Had", "D. If should"],
                "answer": 0,
                "explanation": "Đảo ngữ câu điều kiện loại 1: Should + S + V_inf -> Dùng 'Should'."
            },
            {
                "question": "________ more financial capital, the company would expand into overseas markets.",
                "options": ["A. Were the company to possess", "B. Had the company possessed", "C. If the company possesses", "D. Should the company possess"],
                "answer": 0,
                "explanation": "Mệnh đề chính là 'would expand' (loại 2) -> Đảo ngữ loại 2: Were + S + to V -> Dùng 'Were the company to possess'."
            },
            {
                "question": "________ the safety protocols carefully, the industrial accident would not have occurred.",
                "options": ["A. Had the workers followed", "B. Did the workers follow", "C. Were the workers to follow", "D. Should the workers follow"],
                "answer": 0,
                "explanation": "Mệnh đề chính là 'would not have occurred' (loại 3) -> Đảo ngữ loại 3: Had + S + V3/ed -> Dùng 'Had the workers followed'."
            }
        ]
    },
    {
        "order": 26,
        "id": "g26-if-alternatives",
        "number": "#26",
        "title": "Biến thể thay thế \"If\" (Unless, Provided that, As long as, In case, But for, Without)",
        "category": "conditionals_subjunctive",
        "categoryLabel": "3. Điều kiện & Giả định",
        "sectionTitle": "Phần 3: Câu Điều Kiện & Thể Giả Định",
        "formula": "1. UNLESS = If... not (Trừ khi / Nếu không)\n2. PROVIDED THAT / PROVIDING THAT / AS LONG AS / SO LONG AS = If (Miễn là)\n3. IN CASE + Clause (Phòng khi / Đề phòng)\n4. BUT FOR / WITHOUT + Noun/V-ing:\n- Loại 2: But for / Without + N, S + would + V_inf\n- Loại 3: But for / Without + N, S + would have + V3/ed (Nếu không vì / Nếu không nhờ có)",
        "essence": "Các liên từ và cụm giới từ tương đương với mệnh đề điều kiện, giúp diễn đạt linh hoạt các sắc thái dự phòng, ràng buộc điều kiện hoặc lòng biết ơn.",
        "examples": [
            {
                "en": "Unless you register before midnight, your application will be disqualified.",
                "vi": "Trừ khi bạn đăng ký trước nửa đêm, bằng không hồ sơ của bạn sẽ bị loại (= If you do not register...).",
                "breakdown": "Unless + S + V khẳng định = If + S + V phủ định."
            },
            {
                "en": "But for his timely warning, we would have driven into the flooded road.",
                "vi": "Nếu không nhờ có lời cảnh báo kịp thời của anh ấy, chúng tôi đã lái xe vào con đường ngập lụt.",
                "breakdown": "But for + N (warning) -> câu điều kiện loại 3: would have driven."
            }
        ],
        "practiceQuestions": [
            {
                "question": "You can borrow my personal laptop ________ you promise to handle it with utmost care.",
                "options": ["A. as long as", "B. unless", "C. in case", "D. but for"],
                "answer": 0,
                "explanation": "'as long as' = miễn là mang nghĩa điều kiện tích cực: Miễn là bạn hứa giữ gìn cẩn thận."
            },
            {
                "question": "________ the unconditional support of my parents, I would never have succeeded in this business.",
                "options": ["A. But for", "B. Provided that", "C. As long as", "D. Unless"],
                "answer": 0,
                "explanation": "But for + Noun phrase (hỗ trợ của cha mẹ), S + would have V3 -> Dùng 'But for' (nếu không nhờ có)."
            }
        ]
    },
    {
        "order": 27,
        "id": "g27-present-subjunctive",
        "number": "#27",
        "title": "Thể giả định hiện tại / Bàng thái cách (Present Subjunctive: suggest, demand, vital that...)",
        "category": "conditionals_subjunctive",
        "categoryLabel": "3. Điều kiện & Giả định",
        "sectionTitle": "Phần 3: Câu Điều Kiện & Thể Giả Định",
        "formula": "1. Với động từ yêu cầu/đề xuất:\nS1 + suggest / recommend / demand / insist / request / require / advise + that + S2 + (should) + V_inf\n2. Với tính từ quan trọng/cấp thiết:\nIt is essential / vital / imperative / crucial / necessary / mandatory + that + S + (should) + V_inf\n* Dạng bị động: (should) BE + V3/ed",
        "essence": "Động từ trong mệnh đề 'that' LUÔN Ở DẠNG NGUYÊN THỂ KHÔNG CHIA (không chia theo thì, không chia số ít, không chia ngôi), kể cả khi S2 là he, she, it.",
        "examples": [
            {
                "en": "The doctor strongly recommended that the patient quit smoking immediately.",
                "vi": "Bác sĩ khuyến nghị mạnh mẽ rằng bệnh nhân nên bỏ thuốc lá ngay lập tức.",
                "breakdown": "Recommended that + the patient + QUIT (nguyên thể, không thêm -s)."
            },
            {
                "en": "It is vital that all national cultural heritage be preserved for future generations.",
                "vi": "Điều thiết yếu là tất cả di sản văn hóa quốc gia phải được bảo tồn cho các thế hệ tương lai.",
                "breakdown": "Vital that + S + BE PRESERVED (bị động nguyên thể)."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The board of directors demanded that the financial director ________ an explanation immediately.",
                "options": ["A. gives", "B. give", "C. gave", "D. has given"],
                "answer": 1,
                "explanation": "Cấu trúc giả định thức: demand that + S + (should) V_inf -> Dùng 'give' nguyên thể không chia."
            },
            {
                "question": "It is essential that every candidate ________ strictly by the examination regulations.",
                "options": ["A. abides", "B. abide", "C. abided", "D. is abiding"],
                "answer": 1,
                "explanation": "It is essential that + S + V_inf -> Dùng 'abide' nguyên thể."
            }
        ]
    },
    {
        "order": 28,
        "id": "g28-wish-if-only",
        "number": "#28",
        "title": "Giả định với mong ước (Wish / If only ở hiện tại, quá khứ, tương lai)",
        "category": "conditionals_subjunctive",
        "categoryLabel": "3. Điều kiện & Giả định",
        "sectionTitle": "Phần 3: Câu Điều Kiện & Thể Giả Định",
        "formula": "1. Ước cho Hiện tại (trái ngược hiện tại):\n   S + wish / If only + S + V2/ed (To be: WERE cho mọi ngôi)\n2. Ước cho Quá khứ (tiếc nuối quá khứ):\n   S + wish / If only + S + HAD + V3/ed\n3. Ước cho Tương lai (mong muốn thay đổi/phàn nàn):\n   S + wish / If only + S + WOULD / COULD + V_inf",
        "essence": "Diễn tả những mong muốn, ước nguyện không có thật ở hiện tại, quá khứ hoặc tương lai. Quy tắc bất biến là luôn lùi một thì so với thời điểm được ước.",
        "examples": [
            {
                "en": "I wish I were more confident when speaking English in front of an audience.",
                "vi": "Tôi ước gì mình tự tin hơn khi nói tiếng Anh trước đám đông.",
                "breakdown": "Ước hiện tại: wish I WERE."
            },
            {
                "en": "If only we had reserved our train tickets earlier; now all seats are booked.",
                "vi": "Giá như chúng tôi đặt vé tàu sớm hơn; giờ thì tất cả chỗ đã kín rồi.",
                "breakdown": "Ước quá khứ: had reserved."
            }
        ],
        "practiceQuestions": [
            {
                "question": "He lives far from his workplace. He wishes he ________ closer to his office.",
                "options": ["A. lives", "B. lived", "C. has lived", "D. had lived"],
                "answer": 1,
                "explanation": "Ước trái ngược thực tế hiện tại (He lives far) -> Lùi về Quá khứ đơn: 'lived'."
            },
            {
                "question": "I regret not attending the seminar yesterday. If only I ________ there!",
                "options": ["A. was", "B. had been", "C. were", "D. would be"],
                "answer": 1,
                "explanation": "Tiếc nuối sự việc trong quá khứ (yesterday) -> Dùng Quá khứ hoàn thành: 'had been'."
            }
        ]
    },
    {
        "order": 29,
        "id": "g29-its-time-would-rather",
        "number": "#29",
        "title": "Giả định với cấu trúc thời gian và sở thích (It's time / It's high time, Would rather)",
        "category": "conditionals_subjunctive",
        "categoryLabel": "3. Điều kiện & Giả định",
        "sectionTitle": "Phần 3: Câu Điều Kiện & Thể Giả Định",
        "formula": "1. Cấu trúc It's time:\n- IT IS TIME / IT IS HIGH TIME / IT IS ABOUT TIME + S + V2/ed (Đã đến lúc ai phải làm gì)\n- IT IS TIME + (for sb) + TO V_inf\n2. Cấu trúc Would rather:\n- Cùng chủ ngữ: S + would rather + V_inf + THAN + V_inf\n- Hai chủ ngữ khác nhau:\n  + Hiện tại / Tương lai: S1 + would rather + S2 + V2/ed\n  + Quá khứ: S1 + would rather + S2 + HAD + V3/ed",
        "essence": "Diễn tả tính cấp bách cần làm ngay một việc đã trễ (It's time), hoặc diễn tả mong muốn ai đó làm điều gì theo ý mình (Would rather có 2 chủ ngữ).",
        "examples": [
            {
                "en": "It is high time municipal authorities took effective measures against air pollution.",
                "vi": "Đã đến lúc chính quyền đô thị phải áp dụng các biện pháp hiệu quả chống ô nhiễm không khí.",
                "breakdown": "It is high time + S + V2/ed: took."
            },
            {
                "en": "I would rather you didn't smoke inside the study room.",
                "vi": "Tôi muốn bạn không hút thuốc bên trong phòng học hơn.",
                "breakdown": "Hai chủ ngữ khác nhau ở hiện tại: would rather you DIDN'T SMOKE."
            }
        ],
        "practiceQuestions": [
            {
                "question": "It is about time our government ________ stricter laws to combat wildlife trafficking.",
                "options": ["A. enacted", "B. enacts", "C. enact", "D. has enacted"],
                "answer": 0,
                "explanation": "Cấu trúc: It is about time + S + V2/ed -> Dùng 'enacted'."
            },
            {
                "question": "I would rather you ________ anyone about our confidential meeting yesterday.",
                "options": ["A. don't tell", "B. didn't tell", "C. hadn't told", "D. not tell"],
                "answer": 2,
                "explanation": "Would rather có 2 chủ ngữ nói về sự việc trong quá khứ (yesterday) -> Dùng Quá khứ hoàn thành: 'hadn't told'."
            }
        ]
    },
    {
        "order": 30,
        "id": "g30-as-if-as-though",
        "number": "#30",
        "title": "Giả định như thể là (As if / As though)",
        "category": "conditionals_subjunctive",
        "categoryLabel": "3. Điều kiện & Giả định",
        "sectionTitle": "Phần 3: Câu Điều Kiện & Thể Giả Định",
        "formula": "1. Giả định không có thật ở hiện tại:\n   S + V(hiện tại) + AS IF / AS THOUGH + S + V2/ed (were)\n2. Giả định không có thật ở quá khứ:\n   S + V(quá khứ) + AS IF / AS THOUGH + S + HAD + V3/ed\n3. Sự việc có thật / khả năng cao là đúng: chia theo thì thực tế",
        "essence": "Diễn tả hành động hoặc trạng thái diễn ra 'như thể là', so sánh một tình huống với một giả thiết không có thật.",
        "examples": [
            {
                "en": "He talks about artificial intelligence as if he were an expert in the field.",
                "vi": "Anh ta nói về trí tuệ nhân tạo như thể anh ta là một chuyên gia trong lĩnh vực này vậy (thực tế anh ta không phải).",
                "breakdown": "Giả thiết không có thật ở hiện tại: as if he WERE."
            }
        ],
        "practiceQuestions": [
            {
                "question": "She acts as though she ________ the director of the entire multinational corporation.",
                "options": ["A. is", "B. were", "C. has been", "D. will be"],
                "answer": 1,
                "explanation": "Giả định không có thật ở hiện tại sau 'as though' -> Dùng 'were' cho mọi ngôi."
            }
        ]
    }
]

print(f"Part 3 ready with {len(CONDITIONALS_ITEMS)} items.")

