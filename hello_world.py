# -*- coding=utf-8-*-
"""
@File:hello world.py
@Author:Created by Han X.Y
@Date:on 2024/5/23 9:05
@PythonVersion: Python3.8.5
@desc:
@log:
"""
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.write("Hello world")

# st.button会显示一个按钮组件
# 应用标题的文字
st.header("st.button",divider="blue")
st.header("st.button",divider="green")
st.header("st.button",divider="orange")
st.header("st.button",divider="gray")
st.header("st.button",divider="grey")
st.header("st.button",divider="violet")

# 接受一个值为Say hello的label参数，会作为显示在按钮上的文字
if st.button("Say hello"):
    # st.write:用作显示文字消息，取决于是按钮是否按下
    st.write("why Hello there")
else:
    st.write("Goodbye")
st.markdown("# 标题1")
st.markdown("# 标题2")
st.write("Hello,*World!* :sunglasses:")
df = pd.DataFrame({
        "first column" : [1, 2, 3, 4],
        "second column": [10, 20, 30, 40]
        })
st.write(df)

st.write("Below is a Dataframe:", df, "Above is a dataframe")
df2 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
        x="a",
        y="b",
        size='c',
        color='c',
        tooltip=['a', 'b', 'c']
        )
st.write(c)


st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
"""
使用小号字体显示文本。

这应该用于字幕、旁白、脚注、旁注和其他解释性文本。
"""


st.subheader('This is a subheader with a divider', divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')


st.text('This is some text.')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')



code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='c')
