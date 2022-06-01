from distutils.command.upload import upload
from libraries import *
import time
from time import sleep
import sqlite3
from datetime import date

conn = sqlite3.connect('data.db',check_same_thread=False)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# loading the holistic model into our code
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
DEMO_IMAGE = 'demo.jpg'



c = conn.cursor()
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS taskstable(name TEXT,acuu TEXT,passFail TEXT,asan TEXT,date DATE,inputby)')

def add_data(name,acuu,passFail,asan,inputby):

	c.execute('INSERT INTO taskstable(name,acuu,passFail,asan,date,inputby) VALUES (?,?,?,?,?,?)',(name,acuu,passFail,asan,date.today(),inputby))
	conn.commit()

# def view_all_data():
# 	c.execute('SELECT * FROM taskstable')
# 	data = c.fetchall()
# 	return data


def tadaAsanaImage():
    #drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=1)
    st.sidebar.markdown('---')

    st.markdown(
        """
            <style>
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                width: 400px;
            }
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 400px;
                margin-left: -400px;
            }
            </style>
            """,
        unsafe_allow_html=True,
    )

    img_file_buffer = st.sidebar.file_uploader(
        "Upload an image", type=["jpg", "jpeg", 'png'])
    if img_file_buffer is not None:
        image = np.array(Image.open(img_file_buffer))

    else:
        demo_image = DEMO_IMAGE
        image = np.array(Image.open(demo_image))
    st.sidebar.text('Demo Input Image')
    st.sidebar.image(image)

    name = "TadaAsana"
    acc = []
    inputby = "image upload"

    username = st.text_input('Full name')

    with mp_holistic.Holistic(static_image_mode=True,
                              min_detection_confidence=0.6,
                              min_tracking_confidence=0.6) as holistic:

          # Make Detections
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = holistic.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        outimage = image.copy()

        mp_drawing.draw_landmarks(outimage, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(
                                      color=(245, 117, 66), thickness=2, circle_radius=4),
                                  mp_drawing.DrawingSpec(
                                      color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )

        st.subheader('Output Image')
        st.image(outimage, use_column_width=True)

        try:
            pose = results.pose_landmarks.landmark
            pose_row = list(np.array(
                [[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose]).flatten())
              # Concate rows
            row = pose_row
            X = pd.DataFrame([row])
            body_language_class = model.predict(X)[0]
            body_language_prob = model.predict_proba(X)[0]
            curruntasan = 'TadaAsana'
              # print(body_language_class, body_language_prob)
            if body_language_class == name:
                acc.append(
                    str(round(body_language_prob[np.argmax(body_language_prob)], 2)*100))
                for i in acc:
                    var = i

                st.markdown(
                    f"<h5 style='text-align: left; color: white;'>Accuracy Score : {var} %</h5>", unsafe_allow_html=True)

                if float(var) > 60.0:
                    passfail='perfromed sucessfully'
                    st.markdown(
                        "<h5 style='text-align: left; color: green;'> You have Successfully performed Tada Asana</h5>", unsafe_allow_html=True)
                else:
                    passfail='unsucessfull in performing'
                    st.markdown(
                        "<h5 style='text-align: left; color: red;'> You have failed in performing Tada Asana</h5>", unsafe_allow_html=True)
                    st.markdown(
                        "<h5 style='text-align: left; color: red;'> Try getting and Accuracy score > 60 %</h5>", unsafe_allow_html=True)
                if st.button('add record'):
                    create_table()
                    add_data(username,var,passfail,name,inputby)
                    st.success('sucessfully added the record')

            else:
                st.subheader(
                    f'You are currently not performing Tada Asana')

        except:
            pass


def tadaVideo():

    class VideoTransformer(VideoTransformerBase):
        def __init__(self) -> None:
            self.acc = []

        def transform(self, image):
            name = "TadaAsana"

            with mp_holistic.Holistic(min_detection_confidence=0.6, min_tracking_confidence=0.6) as holistic:
                image = image.to_ndarray(format="bgr24")
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                results = holistic.process(image)

                # Recolor image back to BGR for rendering
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # 4. Pose Detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                        mp_drawing.DrawingSpec(
                                            color=(245, 117, 66), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(
                                            color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

                try:

                    pose = results.pose_landmarks.landmark
                    pose_row = list(np.array(
                        [[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose]).flatten())

                    # Concate rows
                    row = pose_row

                    X = pd.DataFrame([row])
                    body_language_class = model.predict(X)[0]
                    body_language_prob = model.predict_proba(X)[0]
                    #print(body_language_class, body_language_prob)
                    if body_language_class == name:
                        # Get status box

                        cv2.putText(image, 'Accuracy :', (20, 12),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                        cv2.putText(image, str(round(body_language_prob[np.argmax(body_language_prob)], 2)), (
                            20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, 	(0, 128, 0),  2, cv2.LINE_AA)

                        self.acc.append(
                            str(round(body_language_prob[np.argmax(body_language_prob)], 2)*100))

                    else:

                        cv2.putText(image, 'Please Perform the Pose', (10, 40),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),  2, cv2.LINE_AA)
                except:
                    pass

            return image

    webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)


def tadaPicture():
    name = "TadaAsana"
    acc = []
    inputby="snapshot"
  
    

    def main():
            class VideoTransformer(VideoTransformerBase):
                # `transform()` is running in another thread, then a lock object is used here for thread-safety.
                frame_lock: threading.Lock
                in_image: Union[np.ndarray, None]
                out_image: Union[np.ndarray, None]

                def __init__(self) -> None:
                    self.frame_lock = threading.Lock()
                    self.in_image = None
                    self.out_image = None

                def transform(self, frame: av.VideoFrame) -> np.ndarray:
                    in_image = frame.to_ndarray(format="bgr24")

                    # Simple flipping for example.
                    out_image = in_image[:, ::-1, :]

                    with self.frame_lock:
                        self.in_image = in_image
                        self.out_image = out_image

                    return out_image

            ctx = webrtc_streamer(
                key="snapshot", video_transformer_factory=VideoTransformer)

            username = st.text_input('Full name')

            Mytimer =st.slider('timer input', 15, 120, 30)

            if ctx.video_transformer:
                if st.button("Snapshot"):

                    
                    ph = st.empty()
                    N = Mytimer
                    for secs in range(N,0,-1):
                        mm, ss = secs//60, secs%60
                        ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
                        time.sleep(1)
                    # # sleep(Mytimer-15)
                    with ctx.video_transformer.frame_lock:
                        in_image = ctx.video_transformer.in_image
                        out_image = ctx.video_transformer.out_image

                    if in_image is not None and out_image is not None:
                        st.write("Output image:")
                        with mp_holistic.Holistic(static_image_mode=True,
                                                  min_detection_confidence=0.6,
                                                  min_tracking_confidence=0.6) as holistic:
                            out_image = cv2.cvtColor(
                                out_image, cv2.COLOR_BGR2RGB)
                            out_image.flags.writeable = False

                            results = holistic.process(out_image)
                            out_image.flags.writeable = True
                            out_image = cv2.cvtColor(
                                out_image, cv2.COLOR_RGB2BGR)

                            #outimage = out_image.copy()
                            mp_drawing.draw_landmarks(out_image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                        mp_drawing.DrawingSpec(
                                            color=(245, 117, 66), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(
                                            color=(245, 66, 230), thickness=2, circle_radius=2)
                                                      )


                            st.subheader('Output Image')
                            st.image(out_image, channels="BGR", use_column_width=True)
                            try:
                                pose = results.pose_landmarks.landmark
                                pose_row = list(np.array(
                                    [[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose]).flatten())
                                # Concate rows
                                row = pose_row
                                X = pd.DataFrame([row])
                                body_language_class = model.predict(X)[0]
                                body_language_prob = model.predict_proba(X)[0]
                                #print(body_language_class, body_language_prob)
                                if body_language_class == name:
                                    acc.append(
                                        str(round(body_language_prob[np.argmax(body_language_prob)], 2)*100))
                                    for i in acc:
                                        var = i

                                    st.markdown(
                                        f"<h5 style='text-align: left; color: white;'>Accuracy Score : {var} %</h5>", unsafe_allow_html=True)

                                    if float(var) > 60.0:
                                        
                                        create_table()
                                        add_data(username,var,passfail,name,inputby)
                                        st.success('sucessfully added the record')
                                        passfail="sucessfull"
                                        st.markdown(
                                            "<h5 style='text-align: left; color: green;'> You have Successfully performed Tada Asana</h5>", unsafe_allow_html=True)

                                    else:
                                        passfail="unsucessfull"
                                        create_table()
                                        add_data(username,var,passfail,name,inputby)
                                        st.success('sucessfully added the record')
                                        st.markdown(
                                            "<h5 style='text-align: left; color: red;'> You have failed in performing Tada Asana</h5>", unsafe_allow_html=True)
                                        st.markdown(
                                            "<h5 style='text-align: left; color: red;'> Try getting and Accuracy score > 60 %</h5>", unsafe_allow_html=True)



                                else:
                                    passfail="unsucessfull"
                                    create_table()
                                    add_data(username,0,passfail,name,inputby)
                                    st.success('sucessfully added the record')
                                    st.subheader(
                                        f'You are currently not performing Tada Asana')

                            except:
                                pass

                        # st.image(out_image, channels="BGR")


                    else:
                        st.warning("No frames available yet.")

    
    main()
