from libraries import *
from home import *

from TadaAsana import *
from VrikshAsana import *
from TrikonaAsana import *
from ShavaAsana import *
from SetuBandhAsana import *
from PadahastAsana import *
from BhujangAsana import *
from ArdhChakrAsana import *
import threading 

#loading the holistic model into our code
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

#defining the demo image which will be displayed as default
DEMO_IMAGE = 'demo.jpg'

c = conn.cursor()

def view_all_data():
	c.execute('SELECT * FROM taskstable')
	data = c.fetchall()
	return data

#resizing the images
@st.cache()
def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized

#main Navigation of our application
with st.sidebar:
    selected = option_menu(
        menu_title="Free Your Chakras",
        options=["Home","Yoga Pose Grading","result","Meet the team",],
        icons=["house","bar-chart","pie-chart","person"],
        menu_icon='cast'

    )


if selected=='Home':
    home()  #function made in home.py
    expander_faq = st.expander("More About Our Project")
    expander_faq.write("Hi there! If you have any questions about our project, or simply want to check out the source code, please visit our github repo: https://github.com/Shubhmeep/The-Yoga-Guru.git")

elif selected=='result':
    result = view_all_data()
    # st.write(result)
    st.info('All your previous results are recorded here')
    clean_df = pd.DataFrame(result,columns=["Name","Accuracy","Status","Asana","Date","Input by"])
    st.dataframe(clean_df)
    



elif selected=='Yoga Pose Grading':

    app_mode = st.sidebar.selectbox('Choose the pose to perform',
    ['Tada Asana','Vriksha Asana','Trikona Asana','Shava Asana','SetuBandh Asana','Padahast Asana','Bhujanga Asana','Dhanur Asana'],)

    detection_mode = st.sidebar.selectbox('Grade through ',
        ['Image','Take Picture','Real Time Webcam'])


    if app_mode =='Tada Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            tadaAsanaImage()  #function in TadaAsana.py
                        
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')
                        

            

        if detection_mode == "Real Time Webcam":
            tadaVideo()  #function in TadaAsana.py
           
        if detection_mode == "Take Picture":

            tadaPicture()
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')


    
    elif app_mode =='Vriksha Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            treeAsanaImage()  #function in TadaAsana.py
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')


            

        if detection_mode == "Real Time Webcam":
            treeVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            treePicture()
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')


    elif app_mode =='Trikona Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            trikonaAsanaImage()  #function in TadaAsana.py
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')


            

        if detection_mode == "Real Time Webcam":
            trikonaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            trikonaPicture()
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')



    elif app_mode =='Shava Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            shavaAsanaImage()  #function in TadaAsana.py
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')


            

        if detection_mode == "Real Time Webcam":
            shavaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            shavaPicture()
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')


    elif app_mode =='SetuBandh Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            SetuBandhAsanaImage()  #function in TadaAsana.py
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')


            

        if detection_mode == "Real Time Webcam":
            SetuBandhAsanaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            SetuBandhAsanaPicture()
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')

        

    elif app_mode =='Padahast Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            PadahastAsanaImage()  #function in TadaAsana.py
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')


            

        if detection_mode == "Real Time Webcam":
            PadahastAsanaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            PadahastAsanaPicture()
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')



    elif app_mode =='Bhujanga Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            BhujangAsanaImage()  #function in TadaAsana.py
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')


        if detection_mode == "Real Time Webcam":
            BhujangAsanaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            BhujangAsanaPicture()
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')


    else:

        st.title("Welcome !")
        st.title(f"Let's see how well you can perform Dhanur Asana")
        st.markdown('---')

        if detection_mode == "Image":
            ArdhChakrAsanaImage()  #function in TadaAsana.py
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')


            

        if detection_mode == "Real Time Webcam":
            ArdhChakrAsanaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            ArdhChakrAsanaPicture()
             
            st.sidebar.info('PRIVACY POLICY: uploaded images are never saved or stored. They are held entirely within memory for prediction \
                        and discarded after the final results are displayed. ')







        

else:
        import os
        st.sidebar.write(" ------ ")
        st.subheader("We are NUtons !!")
        first_column, second_column, third_column, forth_column,  = st.columns(4)
        first_column.image(os.path.join('meet_team/shubh.jpeg'),    use_column_width = True, caption = "Shubh Sehgal ")
        second_column.image(os.path.join('meet_team/manu.jpeg'),    use_column_width = True, caption = "Manu Gupta")
        third_column.image(os.path.join('meet_team/WhatsApp Image 2022-04-22 at 3.57.55 PM.jpeg'),  use_column_width = True, caption = "Piyush Kalyani")
        forth_column.image(os.path.join('meet_team/ayush.jpg'),  use_column_width = True, caption = "Aayush Pandey")
      
      
       
      
    

        st.sidebar.write('Please feel free to connect with us')
        st.sidebar.success('Hope you had a great time :)')

        expandar_linkedin = st.expander('Contact Information')
        expandar_linkedin.write('Shubh: shubh.sehgal2506@gmail.com')
        expandar_linkedin.write('Manu: manu.gupta19@st.niituniversity.in')
        expandar_linkedin.write('Piyush: piyush.kalyani19@st.niituniversity.in')
        expandar_linkedin.write('Aayush: aayush.pandey19@st.niituniversity.in')
       

        expander_faq = st.expander("More About Our Project")
        expander_faq.write("Hi there! If you have any questions about our project, or simply want to check out the source code, please visit our github repo: https://github.com/Shubhmeep/The-Yoga-Guru.git")



   

         



            
            
            
            



            
                                            
                    

                    

                    

            

          

            
