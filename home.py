from libraries import *

def home():

    st.markdown("<h1 style='text-align: center; color: white;'>The Yoga Guru</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>An AI based Yoga Pose Detection and Pose Grading Application</p>", unsafe_allow_html=True)
    def load_animation(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None

        return r.json()

    animation = load_animation("https://assets1.lottiefiles.com/packages/lf20_kkflmtur.json")


        
    return st_lottie(animation,height = 500)



    