import streamlit as st

# ایپ کی بیسک سیٹنگز
st.set_page_config(
    page_title="AI News & Tech Hub (Cloud)",
    page_icon="🤖",
    layout="wide"
)

# اسٹائلنگ اور ڈیزائن
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 18px;
        color: #4B5563;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: #F3F4F6;
        border-left: 5px solid #2563EB;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ہیڈر سیکشن
st.markdown('<div class="main-title">🤖 AI News & Tech Updates (Cloud Edition)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">دسمبر/جنوری تک بغیر کسی لوکل کمپیوٹر کے 100% کلاؤڈ پر چلنے والا بلاگنگ اور آرٹیکل جنریٹر ٹول</div>', unsafe_allow_html=True)

# سائیڈ بار (مینو)
st.sidebar.title("کلاؤڈ مینو")
menu = st.sidebar.selectbox("آپشن منتخب کریں:", [
    "ڈیش بورڈ (Dashboard)", 
    "نیا آرٹیکل جنریٹ کریں (AI Writer)", 
    "پبلشڈ پوسٹس (Published Logs)"
])

# 1. ڈیش بورڈ سیکشن
if menu == "ڈیش بورڈ (Dashboard)":
    st.subheader("خوش آمدید، موئز!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="کل کلاؤڈ پوسٹس", value="0", delta="آج نئی: 0")
    with col2:
        st.metric(label="زبانیں (Languages)", value="English & Urdu", delta="موجود")
    with col3:
        st.metric(label="سسٹم اسٹیٹس", value="آن لائن (Cloud)", delta="محفوظ")

    st.markdown("---")
    st.markdown("""
    ### 📌 اس پراجیکٹ کے اہم اصول:
    1. **100% کلاؤڈ بیسڈ:** اس کے لیے فی الحال کسی لوکل پی سی کی ضرورت نہیں ہے۔
    2. **ڈوئل لینگویج:** ہر خبر انگلش اور اردو دونوں زبانوں میں تیار ہوگی۔
    3. **مستقبل کی تیاری:** جنوری میں کمپیوٹر ملنے پر یہ سارا کوڈ GitHub کے ذریعے آپ کے سسٹم میں شفٹ ہو جائے گا۔
    """)

# 2. نیا آرٹیکل جنریٹ کرنے کا سیکشن (AI Writer)
elif menu == "نیا آرٹیکل جنریٹ کریں (AI Writer)":
    st.subheader("✍️ کلاؤڈ AI آرٹیکل جنریٹر")
    st.markdown("یہاں آپ اپنی خام خبر (Raw News) درج کریں گے اور AI اسے انگلش اور اردو بلاگ پوسٹ میں بدل دے گا۔")

    news_input = st.text_area("خام خبر یا ٹائٹل یہاں درج کریں:", placeholder="مثلاً: OpenAI announced a breakthrough new model...")
    
    if st.button("آرٹیکل جنریٹ کریں"):
        if news_input.strip() != "":
            st.success("خبر کامیابی سے پراسیس ہو گئی ہے!")
            
            # یہاں سیمپل کے طور پر آؤٹ پٹ دکھا رہے ہیں (بعد میں یہاں OpenAI/Gemini API لگ جائے گی)
            st.markdown("### 🇬🇧 English Version")
            st.info(f"**Title:** The Future of AI: Insights on {news_input[:30]}...\n\n**Content:** This is an automated cloud-generated English article based on your input.")
            
            st.markdown("### 🇵🇰 اردو ورژن")
            st.warning(f"**عنوان:** مصنوعی ذہانت کا مستقبل: ایک نئی تبدیلی...\n\n**تفصیل:** یہ آپ کی فراہم کردہ خبر کا خودکار اردو ترجمہ اور بلاگ پوسٹ ہے۔")
        else:
            st.error("براہ کرم پہلے کوئی خبر یا ٹائٹل درج کریں!")

# 3. پبلشڈ پوسٹس سیکشن
elif menu == "پبلشڈ پوسٹس (Published Logs)":
    st.subheader("📂 کلاؤڈ آڈٹ لاگز اور پوسٹس")
    st.write("ابھی تک کوئی پوسٹ کلاؤڈ پر سیو نہیں کی گئی۔ جب آپ میک (Make.com) یا اس ایپ سے پوسٹس پبلش کریں گے، تو ان کا ریکارڈ یہاں نظر آئے گا۔")
