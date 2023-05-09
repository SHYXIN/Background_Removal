import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="背景去除器")

st.write("## 从图像中删除背景")
st.write(
    ":dog: 尝试上传图片以观看神奇地删除的背景。可以从边栏下载完整质量的图像。此代码是开源的，可在 GitHub上获取。"
)
st.sidebar.write("## 上传图像和下载图像:gear:")


# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("原始图像 :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("去除背景图像: wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("下载 去除背景图像", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./zebra.jpg")
