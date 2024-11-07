import streamlit as st
from scrape import scrape_website, extract_content_body, clean_body_content

st.title("Web Scraper")
url = st.text_input("Enter URL")

if st.button("Scrape this"):
    st.write("scraping...")
    scraped_website = scrape_website(url)
    extracted_content_body = extract_content_body(scraped_website)
    cleaned_body_content = clean_body_content(extracted_content_body)

    st.session_state.dom_content = cleaned_body_content

    st.text_area("DOM Content", cleaned_body_content, height=300)
