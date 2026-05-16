import streamlit as st
import pymongo



st.title("SignIn")
t1=st.text_input("Username")
t2=st.text_input("Password")
if st.button("SIGNIN"):
       conn=pymongo.MongoClient("mongodb+srv://ranjanayush31765_db_user:EW9kHFHIlxV79Akj@cluster0.bnmawun.mongodb.net/?appName=Cluster0")
       mydb=conn["cv"]
       my=mydb["user_info"]
       res=my.find({"username":t1,"password":t2})
       v=0
       for data in res:
              v=v+1
              st.session_state["username"]=data["username"]
              st.switch_page("pages/profile.py")
              
       if v==0:
              st.success("Invalid Login !!!")
