import tkinter as tk
from tkinter import scrolledtext
from services.llm_services import LLMService
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
import threading
import time

llm_service = LLMService(model_name="llama3")
researcher = ResearcherAgent(llm_service)
writer = WriterAgent(llm_service)

def run_query_thread():
    user_query = query_entry.get("1.0", tk.END).strip()
    if not user_query:
        return

    output_text.delete("1.0", tk.END)
    loading_label.config(text="🔄 Generating... please wait")

    def process():
        state = {"user_query": user_query}

        # Researcher
        try:
            loading_label.config(text="🔍 Research Agent Working...")
            state = researcher.run(state)
            research_data = state.get("research_data", "Error in research")

            output_text.insert(tk.END, "=== Research Output ===\n", "blue")
            output_text.insert(tk.END, research_data + "\n\n", "blue")

        except Exception as e:
            output_text.insert(tk.END, f"Researcher Error: {e}\n", "red")

        # Writer
        try:
            loading_label.config(text="🖋 Writer Agent Working... please wait")

            state = writer.run(state)
            final_report = state.get("final_report", "Report generation failed")

            output_text.insert(tk.END, "=== Final Insurance Report ===\n", "green")

            for sentence in final_report.split(". "):
                output_text.insert(tk.END, sentence.strip() + ".\n", "green")
                output_text.see(tk.END)
                output_text.update()
                time.sleep(0.03)

            with open("final_insurance_report.txt", "w", encoding="utf-8") as f:
                f.write(final_report)

            loading_label.config(text="✅ Done! Report saved")

        except Exception as e:
            output_text.insert(tk.END, f"Writer Error: {e}\n", "red")

    threading.Thread(target=process).start()


# GUI Setup
root = tk.Tk()
root.title("Multi-Agent Insurance System - Mac")
root.geometry("800x600")

tk.Label(root, text="Enter your insurance query:").pack(anchor="w", padx=10)
query_entry = tk.Text(root, height=4, width=95)
query_entry.pack(padx=10, pady=5)

tk.Button(root, text="Run Query", command=run_query_thread).pack(pady=5)

loading_label = tk.Label(root, text="", font=("Arial", 10, "italic"))
loading_label.pack()

output_text = scrolledtext.ScrolledText(root, height=25, width=95)
output_text.pack(padx=10, pady=5)

output_text.tag_config("blue", foreground="blue")
output_text.tag_config("green", foreground="green")
output_text.tag_config("red", foreground="red")

root.mainloop()