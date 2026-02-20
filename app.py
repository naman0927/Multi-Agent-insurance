import streamlit as st
from services.llm_services import LLMService
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent

# Initialize
llm_service = LLMService(model_name="llama3")
researcher = ResearcherAgent(llm_service)
writer = WriterAgent(llm_service)

st.title("Multi-Agent Insurance System")

user_query = st.text_area("Enter your insurance query:")

if st.button("Run Query"):
    if user_query:
        state = {"user_query": user_query}

        # Research Agent
        st.info("Research Agent Working...")
        state = researcher.run(state)

        st.success("Research Completed")

        # Show JSON Output
        st.subheader("Research JSON Output")

        if isinstance(state["research_data"], dict):
            st.json(state["research_data"])
        else:
            st.warning("JSON formatting issue")
            st.write(state["research_data"])

        # Writer Agent
        st.info("Writer Agent Working...")
        state = writer.run(state)

        final_report = state.get("final_report", "Report failed")

        st.success("Final Report Generated")

        st.subheader("Final Insurance Report")
        st.write(final_report)

        # Save report
        with open("final_insurance_report.txt", "w", encoding="utf-8") as f:
            f.write(final_report)

        st.success("Report saved as final_insurance_report.txt")
