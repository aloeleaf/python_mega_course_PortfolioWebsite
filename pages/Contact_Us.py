import streamlit as st
from send_mail import send_mail

st.header("Contact Me")

with st.form(key="emil_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    #message = message + "\n" + user_email
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_mail(message.encode("utf-8"), user_email)
        st.info("Your email was sent successfully")