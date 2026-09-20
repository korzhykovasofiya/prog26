import gradio as gr
from datetime import datetime

def greet(name: str, timestamp: float) -> str:
    date = datetime.fromtimestamp(timestamp)

    return date.strftime("%d %B %y") + " Hello " + name + "!"

demo = gr.Interface(
    fn=greet,
    title="Hello World Application",
    description="This is <b>Hello World Application</b> to print \"Hello World\"",
    article="yay",
    inputs=[
        gr.Textbox(label="Enter name", placeholder="Name we want to greet"),
        gr.DateTime(label="Select date")
    ], 
    outputs=[
        gr.Textbox(label="Greeting")
    ],
    submit_btn="Transform",
    flagging_mode="never"
)

demo.launch()