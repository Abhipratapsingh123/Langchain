from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)


st.header('Research Tool')

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers",
                           "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis",
                           "T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer",
                           "RoBERTa: A Robustly Optimized BERT Pretraining Approach",
                           "Word2Vec: Efficient Estimation of Word Representations in Vector Space",
                           "GloVe: Global Vectors for Word Representation",
                           "ImageNet Classification with Deep Convolutional Neural Networks",
                           "Very Deep Convolutional Networks for Large-Scale Image Recognition",
                           "YOLO: You Only Look Once",
                           "Visual Transformers (ViT)",
                           "Diffusion Models Beat GANs on Image Synthesis",
                           "A Few Useful Things to Know About Machine Learning",
                           "Gradient-Based Learning Applied to Document Recognition"])

style_input = st.selectbox("Select Explanation Style", [
                           "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", [
                            "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

template = load_prompt('Prompts\\template.json')

# fill the placeholders
#  prompt = template.invoke(
#         {'paper_input': paper_input,
#          'style_input': style_input,
#          'length_input': length_input

#          }
#     )

# both the prompt and model can be invoked through a single chain

if st.button("Summarize"):
    chain = template | model

    result = chain.invoke(
        {'paper_input': paper_input,
         'style_input': style_input,
         'length_input': length_input
         }
    )
    # result = model.invoke(paper_input) no need because of chain
    st.write(result.content)
