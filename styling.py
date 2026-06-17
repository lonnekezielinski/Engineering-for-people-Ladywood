import pathlib
import streamlit as st
from translations import apply_rtl_css

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def apply_text_size():
    if "text_size" in st.query_params:
        url_text_size = st.query_params["text_size"]

        if url_text_size in ["S", "M", "L"]:
            st.session_state["text_size"] = url_text_size

    if "text_size" not in st.session_state:
        st.session_state["text_size"] = "S"

    text_size = st.session_state["text_size"]

    if text_size == "S":
        title_size = "68px"
        subtitle_size = "21px"
        page_title_size = "58px"
        heading_size = "28px"
        body_size = "18px"
        small_body_size = "16px"

        mobile_title_size = "38px"
        mobile_subtitle_size = "18px"
        mobile_page_title_size = "40px"
        mobile_heading_size = "22px"
        mobile_body_size = "16px"

    elif text_size == "M":
        title_size = "80px"
        subtitle_size = "24px"
        page_title_size = "70px"
        heading_size = "34px"
        body_size = "22px"
        small_body_size = "19px"

        mobile_title_size = "44px"
        mobile_subtitle_size = "21px"
        mobile_page_title_size = "48px"
        mobile_heading_size = "28px"
        mobile_body_size = "20px"

    elif text_size == "L":
        title_size = "87px"
        subtitle_size = "27px"
        page_title_size = "82px"
        heading_size = "40px"
        body_size = "26px"
        small_body_size = "23px"

        mobile_title_size = "50px"
        mobile_subtitle_size = "24px"
        mobile_page_title_size = "56px"
        mobile_heading_size = "34px"
        mobile_body_size = "24px"

    st.markdown(f"""
    <style>
    :root {{
        --title-size: {title_size};
        --subtitle-size: {subtitle_size};
        --page-title-size: {page_title_size};
        --heading-size: {heading_size};
        --body-size: {body_size};
        --small-body-size: {small_body_size};

        --mobile-title-size: {mobile_title_size};
        --mobile-subtitle-size: {mobile_subtitle_size};
        --mobile-page-title-size: {mobile_page_title_size};
        --mobile-heading-size: {mobile_heading_size};
        --mobile-body-size: {mobile_body_size};
    }}
    </style>
    """, unsafe_allow_html=True)

def apply_style(lang):
    apply_text_size()
    css_path = pathlib.Path("assets/styles.css")
    load_css(css_path)

    # Right to left for some languages 
    st.markdown(apply_rtl_css(lang), unsafe_allow_html=True)