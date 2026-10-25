# -*- coding: utf-8 -*-
"""
Part 6: 4 Reported Speech Structures (Items 44-47)
"""

REPORTED_ITEMS = [
    {
        "order": 44,
        "id": "g44-reported-statements",
        "number": "#44",
        "title": "Tường thuật câu trần thuật (Reported Statements)",
        "category": "reported_speech",
        "categoryLabel": "6. Câu tường thuật",
        "sectionTitle": "Phần 6: Câu Gián Tiếp & Tường Thuật",
        "formula": "S + SAID (THAT) + S' + V (lùi thì)...\nS + TOLD SB (THAT) + S' + V (lùi thì)...\n* 3 Quy tắc biến đổi bắt buộc:\n1. LÙI THÌ:\n- Hiện tại đơn -> Quá khứ đơn\n- Hiện tại tiếp diễn -> Quá khứ tiếp diễn\n- Hiện tại hoàn thành -> Quá khứ hoàn thành\n- Quá khứ đơn -> Quá khứ hoàn thành\n- Will -> Would | Can -> Could | Must -> Had to\n2. ĐỔI ĐẠI TỪ: phù hợp với chủ ngữ và tân ngữ\n3. ĐỔI TRẠNG NGỮ:\n- here -> there | now -> then | today -> that day\n- yesterday -> the day before / the previous day\n- tomorrow -> the next day / the following day\n- this/these -> that/those | ago -> before",
        "essence": "Thuật lại lời nói của một người khác dưới dạng gián tiếp, bảo đảm tính logic về thời gian và góc nhìn xưng hô.",
        "examples": [
            {
                "en": "Direct: 'I am completing my final graduation project,' said Nam.\n-> Reported: Nam said that he was completing his final graduation project.",
                "vi": "Nam nói rằng cậu ấy đang hoàn thành đồ án tốt nghiệp cuối khóa của mình.",
                "breakdown": "Lùi thì: am completing -> was completing; đổi đại từ: I -> he, my -> his."
            }
        ],
        "practiceQuestions": [
            {
                "question": "'I finished the university application yesterday,' said Lan.\n-> Lan said that she ________ the university application the previous day.",
                "options": ["A. finished", "B. had finished", "C. has finished", "D. was finishing"],
                "answer": 1,
                "explanation": "Quá khứ đơn (finished) lùi một thì thành Quá khứ hoàn thành -> Dùng 'had finished'."
            },
            {
                "question": "The meteorologist announced that the tropical cyclone ________ landfall the following morning.",
                "options": ["A. will make", "B. would make", "C. makes", "D. has made"],
                "answer": 1,
                "explanation": "Câu tường thuật gián tiếp trong quá khứ (announced) có 'the following morning' -> Lùi will thành 'would make'."
            }
        ]
    },
    {
        "order": 45,
        "id": "g45-reported-questions",
        "number": "#45",
        "title": "Tường thuật câu hỏi Yes/No và Wh-questions (Reported Questions)",
        "category": "reported_speech",
        "categoryLabel": "6. Câu tường thuật",
        "sectionTitle": "Phần 6: Câu Gián Tiếp & Tường Thuật",
        "formula": "1. Câu hỏi Yes/No:\n   S + ASKED (SB) / WONDERED / WANTED TO KNOW + IF / WHETHER + S' + V (lùi thì, trật tự KHẲNG ĐỊNH)\n2. Câu hỏi có từ để hỏi (Wh-questions):\n   S + ASKED (SB) + WH-WORD (What/Where/When/Why/How) + S' + V (lùi thì, trật tự KHẲNG ĐỊNH)\n* QUY TẮC CỐT LÕI: KHÔNG dùng trợ động từ đảo ngữ (do/does/did) và KHÔNG còn dấu chấm hỏi (?).",
        "essence": "Chuyển câu hỏi trực tiếp thành một mệnh đề danh từ tường thuật gián tiếp, giữ nguyên trật tự xuôi: Chủ ngữ + Động từ.",
        "examples": [
            {
                "en": "Direct: 'Do you study abroad?' the interviewer asked.\n-> Reported: The interviewer asked me IF / WHETHER I studied abroad.",
                "vi": "Người phỏng vấn hỏi tôi liệu tôi có đi du học hay không.",
                "breakdown": "Dùng 'if/whether', bỏ trợ động từ do, lùi thì study -> studied."
            },
            {
                "en": "Direct: 'Where did you purchase that dictionary?' asked Mai.\n-> Reported: Mai asked me WHERE I had purchased that dictionary.",
                "vi": "Mai hỏi tôi nơi tôi đã mua cuốn từ điển đó.",
                "breakdown": "Trật tự xuôi: Where + I + had purchased (không dùng Where did I buy)."
            }
        ],
        "practiceQuestions": [
            {
                "question": "The immigration officer asked the traveller ________ a return flight ticket.",
                "options": ["A. if did he have", "B. if he had", "C. whether had he", "D. that he had"],
                "answer": 1,
                "explanation": "Tường thuật câu hỏi Yes/No: asked + if + S + V (trật tự khẳng định, lùi thì) -> Dùng 'if he had'."
            },
            {
                "question": "She asked her supervisor ________ to solve the software system malfunction.",
                "options": ["A. how could they", "B. how they could", "C. that how they could", "D. how did they"],
                "answer": 1,
                "explanation": "Tường thuật câu hỏi Wh-question: asked + Wh-word + S + V -> Dùng 'how they could'."
            }
        ]
    },
    {
        "order": 46,
        "id": "g46-reported-imperatives",
        "number": "#46",
        "title": "Tường thuật câu mệnh lệnh, yêu cầu, lời khuyên (Reported Imperatives / Requests)",
        "category": "reported_speech",
        "categoryLabel": "6. Câu tường thuật",
        "sectionTitle": "Phần 6: Câu Gián Tiếp & Tường Thuật",
        "formula": "1. Khẳng định:\n   S + TOLD / ASKED / ORDERED / REQUESTED / WARNED / ADVISED + O + TO V_inf\n2. Phủ định (Đừng làm gì):\n   S + TOLD / ASKED / ORDERED / WARNED + O + NOT TO V_inf\n(Ví dụ: 'Don't open the door' -> told me NOT TO OPEN the door)",
        "essence": "Tường thuật một mệnh lệnh, yêu cầu lịch sự hoặc lời cảnh báo bằng cách sử dụng động từ nguyên mẫu có 'to' hoặc 'not to'.",
        "examples": [
            {
                "en": "Direct: 'Please turn off your mobile devices during the exam,' the proctor said.\n-> Reported: The proctor asked all candidates TO TURN OFF their mobile devices during the exam.",
                "vi": "Giám thị yêu cầu tất cả thí sinh tắt thiết bị di động trong giờ thi.",
                "breakdown": "Asked + O + TO V_inf: asked all candidates to turn off."
            },
            {
                "en": "Direct: 'Don't touch that live electric wire!' shouted the electrician.\n-> Reported: The electrician warned us NOT TO TOUCH that live electric wire.",
                "vi": "Người thợ điện cảnh báo chúng tôi không được chạm vào sợi dây điện hở đó.",
                "breakdown": "Warned + O + NOT TO V_inf."
            }
        ],
        "practiceQuestions": [
            {
                "question": "'Please fasten your seatbelts,' the flight attendant said to the passengers.\n-> The flight attendant told the passengers ________ their seatbelts.",
                "options": ["A. fasten", "B. to fasten", "C. fastening", "D. fastened"],
                "answer": 1,
                "explanation": "Cấu trúc tường thuật câu mệnh lệnh: tell sb + TO V_inf -> Dùng 'to fasten'."
            },
            {
                "question": "The police officer warned the speeding motorist ________ so recklessly in residential areas.",
                "options": ["A. not to drive", "B. to not drive", "C. not driving", "D. don't drive"],
                "answer": 0,
                "explanation": "Cấu trúc: warn sb + NOT TO V_inf -> Dùng 'not to drive'."
            }
        ]
    },
    {
        "order": 47,
        "id": "g47-reporting-verbs-special",
        "number": "#47",
        "title": "Tường thuật dùng động từ chỉ dẫn đặc biệt đi kèm To-V hoặc V-ing (Reporting Verbs)",
        "category": "reported_speech",
        "categoryLabel": "6. Câu tường thuật",
        "sectionTitle": "Phần 6: Câu Gián Tiếp & Tường Thuật",
        "formula": "1. V + TO V_inf:\n   - agree, refuse, offer, promise, threaten + TO V_inf\n2. V + O + TO V_inf:\n   - advise, invite, remind, encourage, urge, forbid + O + TO V_inf\n3. V + V-ing:\n   - admit, deny, suggest + V-ing\n4. V + PREPOSITION + V-ing:\n   - apologize (to sb) for + V-ing (xin lỗi vì đã làm gì)\n   - accuse sb of + V-ing (buộc tội ai vì đã làm gì)\n   - congratulate sb on + V-ing (chúc mừng ai vì đã làm gì)\n   - thank sb for + V-ing (cảm ơn ai vì đã làm gì)\n   - insist on + V-ing (khăng khăng đòi làm gì)",
        "essence": "Thay vì lặp lại 'said that' nhàm chán, các động từ chỉ dẫn đặc biệt tóm lược chính xác hành động giao tiếp và thái độ của người nói một cách súc tích.",
        "examples": [
            {
                "en": "Direct: 'I am so sorry for arriving late to the staff meeting,' said Peter.\n-> Reported: Peter apologized for arriving late to the staff meeting.",
                "vi": "Peter đã xin lỗi vì đã đến muộn cuộc họp nhân viên.",
                "breakdown": "Apologized for + V-ing."
            },
            {
                "en": "Direct: 'Congratulations on winning first prize in the national contest!'\n-> Reported: The teacher congratulated Lan on winning first prize in the national contest.",
                "vi": "Giáo viên đã chúc mừng Lan vì đã giành giải nhất trong kỳ thi quốc gia.",
                "breakdown": "Congratulated + sb + ON + V-ing."
            }
        ],
        "practiceQuestions": [
            {
                "question": "'I definitely didn't leak the confidential exam paper,' said the teaching assistant.\n-> The teaching assistant denied ________ the confidential exam paper.",
                "options": ["A. to leak", "B. leaking", "C. of leaking", "D. to have leaked"],
                "answer": 1,
                "explanation": "Động từ 'deny' đi kèm trực tiếp với danh động từ: deny + V-ing (phủ nhận đã làm gì) -> Dùng 'leaking'."
            },
            {
                "question": "The principal congratulated all twelfth graders ________ passing their graduation exams with high distinction.",
                "options": ["A. on", "B. for", "C. at", "D. with"],
                "answer": 0,
                "explanation": "Cấu trúc: congratulate sb ON V-ing (chúc mừng ai về việc gì) -> Giới từ bắt buộc là 'on'."
            }
        ]
    }
]

print(f"Part 6 ready with {len(REPORTED_ITEMS)} items.")

