import gradio as gr
from data_loader import PDFTextProcessor
from Agent import agent as create_agent

def process_file(file):
    try:
        if file:
            processor = PDFTextProcessor(file.name)
            original_resume = processor.process()
            return original_resume, original_resume  # Return for both original and transformed
    except Exception as e:
        return f"Error: {str(e)}", ""
    return "", ""

def process_resume_and_chat(user_input, original_resume, previous_transformed):
    try:
        if not original_resume:
            return "Please upload a resume first."

        if user_input:
            # Use the previous transformed resume if it exists, otherwise use original
            input_resume = previous_transformed if previous_transformed else original_resume
            input_data = f"{input_resume}\n\n{user_input}"
            transformed_resume = create_agent(input_data)
            return transformed_resume
        return previous_transformed
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    with gr.Blocks(css="""
        #resume-containers {
            margin-bottom: 20px;
        }
        #chat-section {
            margin-top: 20px;
            border-top: 1px solid #ccc;
            padding-top: 20px;
        }
        .resume-box {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 20px;
            height: 600px;
            overflow-y: auto;
            background-color: #f9f9f9;
            font-family: monospace;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        """) as app:
        gr.Markdown("# Resume Editor and Chat Agent")

        with gr.Row(elem_id="resume-containers"):
            with gr.Column(scale=1):
                gr.Markdown("### Original Resume")
                original_resume = gr.Markdown(
                    value="Upload a resume to see the content here.",
                    elem_id="original_resume",
                    elem_classes="resume-box"
                )

            with gr.Column(scale=1):
                gr.Markdown("### Transformed Resume")
                transformed_resume = gr.Markdown(
                    value="",
                    elem_id="transformed_resume",
                    elem_classes="resume-box"
                )

        with gr.Row(elem_id="chat-section"):
            with gr.Column(scale=2):
                file_input = gr.File(
                    label="Upload Resume (PDF)",
                    elem_id="file_input"
                )
                user_input = gr.Textbox(
                    label="Edit Request or Prompt",
                    placeholder="E.g., 'Improve the summary section'",
                    elem_id="user_input",
                    lines=4
                )
                submit_button = gr.Button(
                    "Submit",
                    elem_id="submit_button",
                    size="lg"
                )

        # State variable to store the latest transformed resume
        state = gr.State("")

        file_input.upload(
            process_file,
            inputs=[file_input],
            outputs=[original_resume, transformed_resume]
        )

        submit_button.click(
            process_resume_and_chat,
            inputs=[user_input, original_resume, transformed_resume],
            outputs=[transformed_resume]
        )

    app.launch()

if __name__ == "__main__":
    main()