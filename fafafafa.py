import streamlit as st
st.title("number")
st.write("your fat" " and u smelly"" and u stink")
thing=st.text_input("first number", "goon")
thing2=st.text_input("second number", "goon")
if thing == thing2:
    st.write("2 numbers are the same")
elif thing > thing2:
    st.write("first number is larger")
else:
    st.write("second number is larger")
st.title("check ur name length")
name =st.text_input("input name rharhagrhagr")
st.title("buttons that u can press :D")
if st.button("don't click this button"):
    st.write("hi did i scare you? i'm a job application lol")
    st.write((len(name)))
if st.button("click this button"):
    st.balloons()
    st.success("yippee you actually listened X3")
