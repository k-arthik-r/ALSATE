<div align="center">
<image src="https://github.com/user-attachments/assets/454e05ec-e34a-47d5-a513-b8858fa88211"/>
</div>

------------------------

<div align="center">
  <a><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/google colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Huggingface-FF9D00?style=for-the-badge&logo=huggingface-logo"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Llama 3.2 3B-0467DF?style=for-the-badge&logo=meta&logoColor=white"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Transformer-gold?style=for-the-badge&logo=package&logoColor=black"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Langchain-FBEEE9?style=for-the-badge&logo=ln"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Chroma DB-999999?style=for-the-badge&logo=chroma-logo"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Samantara-FFFFFF?style=for-the-badge&logo=sam"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Innosetup-FAEBD7?style=for-the-badge&logo=innosetup"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/PEFT-99EDC3?style=for-the-badge&logo=randforest"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/LoRA-7BD3EA?style=for-the-badge&logo=randforest"></a> &nbsp;

</div>

------------------------

ALSATE an acronym for "Analysis of Linux System Logs for Active Threat detection and Evaluation" is an automated log monitoring system that continuously analyzes Linux sys-logs for threat levels 4 and below, leveraging a fine-tuned Large Language Model (LLM) to detect issues, provide explanations, and recommend actionable remediation measures to enhance system security and efficiency.

The Project Focus on 5 Levels of System Logs, namely:
- L0 - EMERGENCY
- L1 - ALERT
- L2 - CRITICAL
- L3 - ERROR
- L4 - WARNING

------------------------

## Requirments
Python 3.9.13 (Recommended) 

<a href="https://www.python.org/downloads/release/python-3913/" alt="python">
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>

<br>
<br>

Huggingface Account

<a href="https://www.huggingface.co/" alt="huggingface">
      <img src="https://custom-icon-badges.demolab.com/badge/Huggingface-FF9D00?style=for-the-badge&logo=huggingface-logo"></a>

<br>
<br>

A Linux Distribution (UBUNTU on Oracle Virtual Box is Preffered) 

Run a Linux Disrtibution on your PC Using a VM Engine such as Oracle Virual Box, VMware, etc,.. or using WSL on windows or using Dual Boot Mode.

<a href="https://ubuntu.com/download/desktop/thank-you?version=24.04.1&architecture=amd64&lts=true" alt="huggingface">
      <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"></a>

<a href="https://download.virtualbox.org/virtualbox/7.1.4/Oracle_VirtualBox_Extension_Pack-7.1.4.vbox-extpack" alt="huggingface">
      <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"></a>

We have used Ubuntu 24.04.1 LTS and Oracle VirtualBox 7.1.4 to run this application.
        
---------------------------

## Modules/Libraries Used

All The Modules/Libraries Used in the Project can be installed using [requirements.txt](requirements.txt)

LLM Finetuning
- transformers
- bitsandbytes
- peft
- os
- torch
- wandb
- datasets
- trl

Project Execution
- re
- time
- json
- requests
- streamlit
- streamlit.components.v1

----------------------------

## Setup



----------------------------

## How to Run?

The execution of this project involves 3 Steps:

### Step 1 : Activate LLM Server
To Activate the LLM Server we need a package called llama.cpp, 

#### About llama.cpp
Llama.cpp allows you to download and run inference on a GGUF simply by providing a path to the Hugging Face repo path and the file name. llama.cpp downloads the model checkpoint and automatically caches it. The location of the cache is defined by LLAMA_CACHE environment variable; read more about it [here](https://github.com/ggerganov/llama.cpp/pull/7826).

You can install llama.cpp through brew (works on Mac and Linux), or you can build it from source. There are also pre-built binaries and Docker images that you can [check in the official documentation](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage).

#### Follow the below steps provided
- Within the Current directory open a new bash terminal.
- Install llama.cpp using brew,
  ```bash
    brew install llama.cpp
  ```
- Activate the LLM Server Using,
  ```bash
    llama-server -m llama-3.2-3b-sys-log-analysis-alsate-q4_k_m.gguf
  ```
  Note: After Executing the above command you may have to wait for 10-15 min to get the model completely activated and get running.
-  You can check the activation of the model either by visiting the link where the model is being running - Usually in the port 8080 or 8081, so visit http://127.0.0.1:8080 or http://127.0.0.1:8081, which will redirect you to a chat interface like the below snapshot.

- or by sending a curl request,
  ```bash
    curl http://localhost:8080/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer no-key" \
    -d '{
    "messages": [
    {
            "role": "system",
            "content": "Your name is "ALSATE",you are an advanced syslog parsing and analysis tool. Your task is to analyze provided system logs, identify potential causes               of their generation, and detect any security threats or anomalies. If threats are found, suggest precise remediation steps. Respond only when the input is a                 valid system log; otherwise, reply with: 'Input does not appear to be a valid system log. Unable to assist.'"
        },
        {
            "role": "user",
            "content": "Nov 05 22:28:18 ubuntu kernel: workqueue: blk_mq_requeue_work hogged CPU for >10000us 16 times, consider switching to WQ_UNBOUND"
        }
      ]
    }'
  ```
  Note: if you use a curl request method, you may have to wait for 2 to 3 Minutes before you get any response depending on your current system status. you will get a     responce similar to the snapshot provided below. Disclaimer* - This is only when the llm is activated in http://localhost:8080, you may need to change the link if your LLM is activated in any other address.

### Step 2 : Read Sys-Logs and save it in a dynamic text file.

- Within the Current directory open a new bash terminal.
- activate python virtual environment,
  
  ```bash
    source bin/activate
  ```
- execute read.py,
  
  ```bash
    python3 read.py
  ```

- After the Execution of this you could see a new text file with name *live_logs.txt* being created and sys-logs being added in that file. 

### Step 3 : Fetch Sys-Logs from dynamic text file, analyse it using the fine tuned llm and display it in the streamlit interface.

- Within the Current directory open a new bash terminal.
- activate python virtual environment,
  
  ```bash
    source bin/activate
  ```
- execute main.py,
  
  ```bash
    python3 main.py
  ```
- After the Execution of this you could see a Streamlit Application running in local host.

----------------------------
