import os
import re
import time
import json
import requests
import streamlit as st
from dotenv import load_dotenv
import streamlit.components.v1 as components

load_dotenv()
URL = os.getenv("URL")

def extract_heading(log):
    pattern = r"^\w+\s+\d+\s+\d+:\d+:\d+\s+(.*?:.*?):"
    match = re.search(pattern, log)
    if match:
        result = match.group(1)
        return result
    else:
        pattern = r"^\w+\s+\d+\s+\d+:\d+:\d+\s+([^:]+):"
        match = re.search(pattern, log)
        if match:
            result = match.group(1)
            return result
        else:
            return "line_break::"


def extract_cause_and_remediation(response):
    content = re.sub(r"(Cause\s*-\s*.*?)(\\n)", r"\1", response, count=1)

    cause_pattern = r"Cause\s*-\s*(.*?)(?=\s*Remediation|$)"
    remediation_pattern = r"Remediation\s*-\s*(.*?)(?=$)"

    cause_match = re.search(cause_pattern, content)
    remediation_match = re.search(remediation_pattern, content)

    cause = cause_match.group(1).strip() if cause_match else None
    remediation = remediation_match.group(1).strip() if remediation_match else None

    return cause, remediation


def request_files(query):

    url = URL + "v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer no-key"}

    data = {
        "messages": [
            {
                "role": "system",
                "content": "Your name is ALSATE, you are an advanced syslog parsing and analysis tool. Your task is to analyze provided system logs, identify potential causes of their generation, and detect any security threats or anomalies. If threats are found, suggest precise remediation steps. Respond only when the input is a valid system log; otherwise, reply with: Input does not appear to be a valid system log. Unable to assist.",
            },
            {"role": "user", "content": query},
        ]
    }

    return (url, headers, data)


def process_first_line(file_path):
    try:
        with open(file_path, "r+") as file:
            lines = file.readlines()

            if lines:
                first_line = lines.pop(0)
                file.seek(0)
                file.writelines(lines)
                file.truncate()
                return first_line.strip()
            else:
                return None
    except FileNotFoundError:
        return "ERROR 400"
    except Exception as e:
        return "ERROR"


def expander(Heading, Log, Cause, Remediation):
    with st.expander(f"**{Heading}**"):
        st.divider()
        st.markdown("**:blue[Log]**")
        st.write(Log)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**:orange[Cause]**")
        st.write(Cause)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**:green[Remediation]**")
        st.write(Remediation)
        st.markdown("<br>", unsafe_allow_html=True)


st.set_page_config(
    page_title="ALSATE",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="https://github.com/user-attachments/assets/6290a8fd-b30b-4a6b-96a2-1a2e1313c4db",
)

col1, col2 = st.columns([5, 1])
with col1:
    st.markdown("<h1 style='margin-bottom: 0;'>ALSATE</h1>", unsafe_allow_html=True)
with col2:
    st.markdown(
        """
        <div style='padding-top: 20px; text-align: right;'>
            <img src='https://github.com/user-attachments/assets/6290a8fd-b30b-4a6b-96a2-1a2e1313c4db' style='width: 70px;' alt='Logo'>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

content = []

placeholder = st.empty()
while True:

    if len(content) > 200:
        content.clear()

    with placeholder.container():
        log = process_first_line("live_logs.txt")
     
        if log is None:
            time.sleep(5)
            continue

        url, headers, data = request_files(log)
        try:
            response = requests.post(url, headers=headers, json=data)
            response_json = response.json()
        except Exception as e:
            print(e, "ISE 500")

        _Heading_ = extract_heading(log)
        _Cause_, _Remediation_ = extract_cause_and_remediation(response_json["choices"][0]["message"]["content"])
        _Log_ = log

        data = {
            "Heading": _Heading_,
            "Log": _Log_,
            "Cause": _Cause_,
            "Remediation": _Remediation_,
        }
        content.append(data)
        for item in content:
            with st.container():
                expander(item["Heading"], item["Log"], item["Cause"], item["Remediation"])

# {
    #     "Heading": "ubuntu kernel: workqueue",
    #     "Log": "Nov 05 22:28:18 ubuntu kernel: workqueue: blk_mq_requeue_work hogged CPU for >10000us 16 times, consider switching to WQ_UNBOUND",
    #     "Cause": "The blk_mq_requeue_work function is consuming excessive CPU time, likely due to heavy I/O operations.",
    #     "Remediation": "Consider switching to WQ_UNBOUND work queues to distribute the load across multiple CPUs and prevent CPU bottlenecks.",
    # },
    # {
    #     "Heading": "ubuntu systemd[1]: systemd-logind.service",
    #     "Log": "Nov 07 08:58:01 ubuntu systemd[1]: systemd-logind.service: Watchdog timeout (limit 3min)!",
    #     "Cause": "The systemd-logind service did not respond within the allowed timeout period, possibly due to high system load or a deadlock.",
    #     "Remediation": "Investigate the service logs and check for performance issues. Restart the service with systemctl restart systemd-logind.",
    # },
    # {
    #     "Heading": "ubuntu systemd[1]: kerneloops.service",
    #     "Log": "Nov 07 13:56:53 ubuntu systemd[1]: kerneloops.service: Found left-over process 1218 (kerneloops) in control group while starting unit. Ignoring.",
    #     "Cause": "The kerneloops service detected an orphaned process.",
    #     "Remediation": "Clean up orphaned processes and ensure proper service shutdowns.",
    # },
