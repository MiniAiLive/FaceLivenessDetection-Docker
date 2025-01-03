import gradio as gr
import os
import requests

def check_liveness(frame):
    url = "http://127.0.0.1:8092/api/check_liveness"
    files = {'image': open(frame, 'rb')}
    r = requests.post(url=url, files=files)

    html = None
    table_value = ""

    for key, value in r.json().items():
        row_value = ("<tr>"
                        "<td>{key}</td>"
                        "<td>{value}</td>"
                    "</tr>".format(key=key, value=value))
        table_value = table_value + row_value

    html = ("<table>"
                "<tr>"
                    "<th style=""width:30%"">Field</th>"
                    "<th style=""width:50%"">Value</th>"
                "</tr>"
                "{table_value}"
                "</table>".format(table_value=table_value))
    
    return html

# APP Interface
with gr.Blocks() as MiniAIdemo:
    gr.Markdown(
        """
        <a href="https://miniai.live" style="display: flex; align-items: center;">
            <img src="https://miniai.live/wp-content/uploads/2024/02/logo_name-1-768x426-1.png" style="width: 18%; margin-right: 15px;"/>
            <div>
                <p style="font-size: 50px; font-weight: bold; margin-right: 20px;">Face Liveness Detection Web Online Demo</p>
            </div>
        </a>

        <br/>
        <ul>
            <li style="font-size: 18px;">Visit and learn more about our Service : <a href="https://miniai.live" target="_blank" style="font-size: 18px;">https://www.miniai.live</a></li>
            <li style="font-size: 18px;">Check our SDK for cross-platform from Github : <a href="https://github.com/MiniAiLive" target="_blank" style="font-size: 18px;">https://github.com/MiniAiLive</a></li>
            <li style="font-size: 18px;">Quick view our Youtube Demo Video : <a href="https://www.youtube.com/@miniailive" target="_blank" style="font-size: 18px;">MiniAiLive Youtube Channel</a></li>
            <li style="font-size: 18px;">Demo with Android device from Google Play : <a href="https://play.google.com/store/apps/dev?id=5831076207730531667" target="_blank" style="font-size: 18px;">MiniAiLive Google Play</a></li>
        </ul>
        <br/>
        """
    )
    with gr.Tabs():
        with gr.TabItem("Face Liveness Detection"):
            with gr.Row():
                with gr.Column():
                    im_live_input = gr.Image(type='filepath', height=300)
                    gr.Examples(
                        [
                            os.path.join(os.path.dirname(__file__), "images/f_fake_andr_mask.jpg"),
                            os.path.join(os.path.dirname(__file__), "images/f_fake_andr_mask3d.jpg"),
                            os.path.join(os.path.dirname(__file__), "images/f_fake_andr_monitor.jpg"),
                            os.path.join(os.path.dirname(__file__), "images/f_fake_andr_outline.jpg"),
                            os.path.join(os.path.dirname(__file__), "images/f_fake_andr_outline3d.jpg"),
                            os.path.join(os.path.dirname(__file__), "images/old-1.jpg"),
                            os.path.join(os.path.dirname(__file__), "images/old-4.jpg"),
                        ],
                        inputs=im_live_input
                    )
                    btn_f_live = gr.Button("Check Liveness", variant='primary')
                with gr.Column():
                    txt_live_output = gr.HTML()
            btn_f_live.click(check_liveness, inputs=im_live_input, outputs=txt_live_output)

if __name__ == "__main__":
    MiniAIdemo.launch(server_port=8083, server_name="0.0.0.0")