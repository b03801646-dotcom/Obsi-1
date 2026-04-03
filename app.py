import streamlit as st
import requests
import time

st.set_page_config(page_title="My Rush Tool", page_icon="⚡")
st.title("⚡ أداة الرشق الخاصة بي")

# خانة إدخال الرابط في التطبيق
video_url = st.text_input("🔗 الصق رابط فيديو التيك توك هنا:")

if st.button("بدء الهجوم المكثف 🔥"):
    if video_url:
        st.success("بدأ العمل.. راقب النتائج في حسابك!")
        progress = st.progress(0)
        status = st.empty()
        
        # الرابط المباشر للسيرفر
        api_url = "https://alloush-python-u3vewnba7fyjqivh8odxdr.streamlit.app"
        
        for i in range(1, 101):
            try:
                # طلب المشاهدات
                requests.post(api_url, data={"url": video_url, "action": "views"})
                # طلب اللايكات كل 5 مرات
                if i % 5 == 0:
                    requests.post(api_url, data={"url": video_url, "action": "likes"})
                
                # تحديث شريط التقدم في واجهة التطبيق
                progress.progress(i / 100)
                status.text(f"✅ جاري إرسال الدفعة رقم {i}...")
                time.sleep(0.1)
            except:
                continue
        st.balloons()
        st.success("🎯 تم الانتهاء بنجاح!")
    else:
        st.error("⚠️ يرجى وضع الرابط أولاً")
