import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_story(theme, genre, length):
    """Generate a story using OpenAI API based on user inputs"""
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        prompt = f"Write a {length} story in the {genre} genre about {theme}. Make it engaging and creative."
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative story writer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating story: {str(e)}"

def main():
    st.set_page_config(
        page_title="AI Story Generator",
        page_icon="📚",
        layout="wide"
    )
    
    st.title("🌟 AI Story Generator")
    st.markdown("### Create unique stories from your ideas!")
    
    # User inputs
    theme = st.text_input("Enter your story theme or main idea:", 
                         placeholder="e.g., 'a magical forest', 'time travel', 'lost treasure'")
    
    genre = st.selectbox(
        "Choose your story genre:",
        ["Fantasy", "Science Fiction", "Mystery", "Romance", "Adventure", "Horror"]
    )
    
    length = st.select_slider(
        "Select story length:",
        options=["Very Short", "Short", "Medium", "Long"],
        value="Short"
    )
    
    if st.button("Generate Story ✨"):
        if theme:
            with st.spinner("Creating your story... Please wait..."):
                story = generate_story(theme, genre, length)
                st.markdown("### Your Story:")
                st.write(story)
        else:
            st.warning("Please enter a theme for your story!")
    
    st.markdown("---")
    st.markdown("### How to use:")
    st.markdown("""
    1. Enter a theme or main idea for your story
    2. Select your preferred genre
    3. Choose the desired length
    4. Click 'Generate Story' and watch the magic happen!
    """)

if __name__ == "__main__":
    main()
