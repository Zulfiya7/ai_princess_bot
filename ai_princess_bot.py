
import streamlit as st

# 🌸 Бет баптауы
st.set_page_config(page_title="AI Princess Chatbot", page_icon="👑", layout="centered")

# 🌟 Стильді CSS
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .main {
        background-color: #fdf6ff;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e0c7f3;
    }
    h1 {
        color: #b23be3;
        font-family: 'Georgia', serif;
        text-align: center;
    }
    .stTextInput > div > div > input {
        background-color: #fdf6ff;
    }
    </style>
""", unsafe_allow_html=True)

# 👑 Бет мазмұны
st.title("👑 AI Princess")
st.markdown("### 🤖 Жасанды интеллект туралы білгің келсе – ханшайымнан сұра!")

st.image("https://cdn-icons-png.flaticon.com/512/3468/3468213.png", width=120)  # Кішкентай ханшайым иконкасы

# 📝 Сұрақ енгізу
user_input = st.text_input("🧠 Сұрағыңызды осында жазыңыз:")

# 📚 Дайын жауаптар
responses = {
    "жасанды интеллект": "Жасанды интеллект – адам сияқты ойлап, шешім қабылдай алатын бағдарламалар жиынтығы.",
    "нейрондық желі": "Нейрондық желі – мидағы нейрондар тәрізді жұмыс істейтін алгоритмдер жүйесі.",
    "машиналық оқыту": "Бұл компьютерлердің деректер арқылы өздігінен үйренуіне мүмкіндік беретін әдіс.",
    "чатбот": "Чатбот – қолданушымен сөйлесетін бағдарлама. Ол сұрақтарға жауап береді, көмек көрсетеді.",
    "ai не үшін керек": "AI медицина, білім, қаржы, өнеркәсіп, тіпті шығармашылықта да қолданылады!"
}

# 🔍 Жауап табу
if user_input:
    matched = False
    for key in responses:
        if key in user_input.lower():
            st.success("👑 AI Princess: " + responses[key])
            matched = True
            break
    if not matched:
        st.warning("👑 AI Princess: Кешір, мен бұл сұраққа әлі жауап бере алмаймын... Бірақ үйреніп жатырмын!")

# 🌸 Аяқ
st.markdown("---")
st.markdown("🌟 *AI Queens жобасы үшін әзірленген. Жасанды интеллект – біздің тәжіміз!*")
