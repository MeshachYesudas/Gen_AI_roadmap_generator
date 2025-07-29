import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get response from LLaMA
def getLlamaresponse(skill):
    try:
        llm = CTransformers(
            model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
            model_type='llama',
            config={
                'max_new_tokens': 512,
                'temperature': 0.7,
            }
        )

        template = """
        You are an expert in {skill}. I want to learn it from scratch.
        Give me a step-by-step roadmap to master it with free resources.
        Format it as clear numbered steps.
        """

        prompt = PromptTemplate(input_variables=["skill"], template=template)
        final_prompt = prompt.format(skill=skill)
        response = llm(final_prompt)

        return response
    except Exception as e:
        return f"❌ Error: {e}"

# Streamlit UI setup
st.set_page_config(page_title='THE SKILL ROADMAP', layout='centered')

st.header("🎯 SKILL JOURNEY")

skill = st.text_input("Enter the skill you wish to learn:")

submit = st.button('Generate Roadmap')

if submit and skill:
    with st.spinner("Generating roadmap..."):
        output = getLlamaresponse(skill)
        st.subheader("🧭 Your Roadmap")
        st.markdown(output)  # This formats steps nicely if in Markdown
