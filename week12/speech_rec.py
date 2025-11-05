import re, speech_recognition as sr
import sys
r = sr.Recognizer()
activated = False

with sr.Microphone() as mic:
    r.adjust_for_ambient_noise(mic, duration=0.4)
    print("พูด 'สวัสดีครับ' เพื่อเริ่มใช้งาน")

    while True: 
        try:
            audio = r.listen(mic, timeout=6, phrase_time_limit=10)
            text = r.recognize_google(audio, language="th-TH")
            print("ได้ยิน :", text)

            

            if text.strip() == "สวัสดีปิด":
                print("ปิดโปรแกรมแล้วครับ 👋")
                sys.exit(0)
                
            if not activated:
                if text.strip() == "สวัสดีครับ":
                    activated = True
                    print("ระบบพร้อมทำงานแล้ว ✅")
                else:
                    print("กรุณาพูด 'สวัสดีครับ' ก่อนครับ")
                continue    

            # ทุกคำสั่งต้องเริ่มด้วย "สวัสดี"
            if text.startswith("สวัสดีครับ"):
                cmd = text.replace("สวัสดีครับ", "", 1).strip()

                # ---------- ตรวจจับความเร็ว ----------
                if "ความเร็ว" in cmd or cmd.lower().startswith("speed"):
                    m = re.search(r"(\d+)", cmd)
                    speed = int(m.group(1)) if m else None
                    if speed is not None and 0 <= speed <= 100:
                        print(":", cmd, "| SPEED :", speed)
                    else:
                        print("กรุณาพูดความเร็วระหว่าง 0–100")


        except sr.WaitTimeoutError:
            print("ไม่มีเสียงพูดมาเลยค่ะ")
        
        except sr.UnknownValueError:
            print("พูดมาได้เลยค่ะ.........")
