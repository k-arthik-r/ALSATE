<div align="center">
<image src="https://github.com/user-attachments/assets/454e05ec-e34a-47d5-a513-b8858fa88211"/>
</div>

------------------------

<div align="center">
  <a><img src="https://img.shields.io/badge/Llama 3.2 3B Instruct-0467DF?style=for-the-badge&logo=meta&logoColor=white"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Transformer-gold?style=for-the-badge&logo=package&logoColor=black"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/PEFT-99EDC3?style=for-the-badge&logo=randforest"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/LoRA-53AC56?style=for-the-badge&logo=minetest&logoColor=000000"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Streamlit-000000?style=for-the-badge&logo=streamlit"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Journalctl-51BB7B?style=for-the-badge&logo=local&logoColor=white"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/WSL-68BC71?style=for-the-badge&logo=ubuntu&logoColor=black"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/VirtualBox-2F61B4?style=for-the-badge&logo=virtualbox&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Ngrok-1F1E37?style=for-the-badge&logo=ngrok&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/W and B-FFBE00?style=for-the-badge&logo=weightsandbiases&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Quantization-Q4-red?style=for-the-badge"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/GGML_ORG-000000?style=for-the-badge&logo=ggml-org"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/CURL-073551?style=for-the-badge&logo=curl&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Homebrew-FBB040?style=for-the-badge&logo=homebrew&logoColor=ffdd54"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Google Sheets-34A853?style=for-the-badge&logo=googlesheets&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Google Apps Script-4285F4?style=for-the-badge&logo=googleappsscript&logoColor=white"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Huggingface-FF9D00?style=for-the-badge&logo=huggingface-logo"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white"></a> &nbsp;
</div>

------------------------

ALSATE an acronym for "Analysis of Linux System Logs for Active Threat detection and Evaluation" is an automated log monitoring system that continuously analyzes Linux sys-logs for threat levels 4 and below, leveraging a fine-tuned Large Language Model (LLM) to detect issues, provide explanations, and recommend actionable remediation measures to enhance system security and efficiency.

ALSATE prioritizes the following five levels of system logs:
- L0 - EMERGENCY
- L1 - ALERT
- L2 - CRITICAL
- L3 - ERROR
- L4 - WARNING

Logs at levels 5 and above (such as Notice or Info) are not analyzed, as they typically indicate no significant threat.

------------------------

## Requirments

### Web Level Requirements
- Huggingface Account
  
  <a href="https://www.huggingface.co/" alt="huggingface">
      <img src="https://custom-icon-badges.demolab.com/badge/Huggingface-FF9D00?style=for-the-badge&logo=huggingface-logo"></a>
<br>

### System Level Requirements (Only for Windows and MAC)

- Oracle Virtual Box 7.1.4 (Recommended) (Any Virtual Engine with latest the lersions can also be used)

  <a href="https://download.virtualbox.org/virtualbox/7.1.4/Oracle_VirtualBox_Extension_Pack-7.1.4.vbox-extpack" alt="huggingface">
      <img src="https://img.shields.io/badge/VirtualBox-2F61B4?style=for-the-badge&logo=virtualbox&logoColor=white"></a>
<br>

### Virtal Machine Level Requirements

- Ubuntu 24.04.1 (Recommended) (Any other Linux Distribution or any other latest version of the Ubuntu can also be used)

  <a href="https://ubuntu.com/download/desktop/thank-you?version=24.04.1&architecture=amd64&lts=true" alt="huggingface">
      <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"></a>
<br>

### Linux Distribution Level Requirements

- Python 3.12.3 (Recommended) 

  <a href="https://www.python.org/downloads/release/python-3123/" alt="python">
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>
<br>

- python-pip 24.0 (Recommended)

  <a href="https://pypi.org/project/pip/" alt="python">
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>
        
  To Install python-pip, open a bash terminal and execute this,
  
  ```bash
  sudo apt-get install python-pip
  ```
  
<br>

- cURL 8.11.0 (Recommended)

  <a href="https://curl.se/" alt="curl">
        <img src="https://img.shields.io/badge/CURL-073551?style=for-the-badge&logo=curl&logoColor=white" /></a>

  To Install cURL, open a bash terminal and execute this,

  ```bash
  sudo apt-get install curl
  ```
  
<br>

- git 2.43.0 (Recommended)

  <a href="https://www.python.org/downloads/release/python-3913/" alt="python">
        <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" /></a>

  To Install git, open a bash terminal and execute this,
  ```bash
  sudo apt install git-all
  ```
  
<br>

- Homebrew 4.4.8 (Recommended)

  <a href="https://www.python.org/downloads/release/python-3913/" alt="python">
        <img src="https://img.shields.io/badge/Homebrew-FBB040?style=for-the-badge&logo=homebrew&logoColor=ffdd54" /></a>

  To Install Homebrew, open a bash terminal and execute these,
  
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
  ```bash
  test -d ~/.linuxbrew && eval "$(~/.linuxbrew/bin/brew shellenv)"
  ```
  ```bash
  test -d /home/linuxbrew/.linuxbrew && eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
  ```
  ```bash
  echo "eval \"\$($(brew --prefix)/bin/brew shellenv)\"" >> ~/.bashrc
  ```

---------------------------

## Modules/Libraries Used

All The Modules/Libraries Used in the project can be installed using [requirements.txt](requirements.txt)
- `re`
- `time`
- `json`
- `requests`
- `streamlit`
- `subprocess`
- `streamlit.components.v1`

----------------------------

## Setup

### Step 1 : Restrict the System to produce only Level 4 and below logs.

- Since we are focussing only on Level 4 and below sys-logs as level 5 and above sys-logs produce no potential threat, we are required to access only level 4 and below sys-logs and ignore level 5 and level 6 logs. we can achive this by changing the journalctl configuration in the linux systems.
- To set the system to syore only level 4 and below logs, open your operating system and navigate to,
  
  ```bash
  /etc/systemd/journald.conf
  ```
- open the journald.conf in editable mode and scroll down in that file.
- in the configuration list you can notice two fields such as:
  - MaxLevelStore and
  - MaxLevelSyslog
- now set both of them to *warning*
  ```bash
  #MaxLevelStore = warning
  #MaxLevelSyslog = warning
  ```
- save the file and restart the operating system.
  
### Step 2 : Download the Quantized Model

- Fine Tuned and Quantized Model: k-arthik-r/llama-3.2-3b-sys-log-analysis-alsate-Q4_K_M-GGUF
- Download the Fine tuned and quantized model by clicking [Here](https://huggingface.co/k-arthik-r/llama-3.2-3b-sys-log-analysis-alsate-Q4_K_M-GGUF/resolve/main/llama-3.2-3b-sys-log-analysis-alsate-q4_k_m.gguf?download=true)
- To Know More about Quantized Model Click [Here]().

### Step 3 : Setup the Repository

- Inside in your Linux Distribution, select a location for the project in any easily accessible location(Like Desktop).
- Open a bash terminal in the selected location, Initialize an empty git repository and clone the repository using,
  
  ```bash
  git init
  ```
  
  ```bash
  https://github.com/k-arthik-r/ALSATE.git
  ```
- A folder with name "ALSATE" will be created.
- Move the downloaded model(From Step 2) into the ALSATE Folder. 
- Navigate to the ALSATE Folder.
 
### Step 4 : Create a Python Virtual Env and install the requirements.
- Inside ALSATE folder open a bash terminal.
- Install virtualenv,
  
  ```bash
  pip3 install virtualenv
  ```
- create a python virtual environment with the name *env*.
  
  ```bash
  python3 -m venv env
  ```
- Activate the Virtual Environment.
    
  ```bash
  source env/bin/activate
  ```
- Install the requirments from the [requirements.txt](requirements.txt)
  
  ```bash
  pip3 install -r requirements.txt
  ```

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

  ![Screenshot 2024-12-04 220654](https://github.com/user-attachments/assets/684ccbc7-9b9a-4d88-a176-050b24ac7cb8)

- or by sending a curl request,
  ```bash
  curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer no-key" \
  -d '{
  "messages": [
  {
          "role": "system",
          "content": "Your name is ALSATE,you are an advanced syslog parsing and analysis tool. Your task is to analyze provided system logs, identify potential causes of their generation, and detect any security threats or anomalies. If threats are found, suggest precise remediation steps. Respond only when the input is a valid system log; otherwise, reply with: Input does not appear to be a valid system log. Unable to assist."
      },
      {
          "role": "user",
          "content": "Nov 05 22:28:18 ubuntu kernel: workqueue: blk_mq_requeue_work hogged CPU for >10000us 16 times, consider switching to WQ_UNBOUND"
      }
    ]
  }'
  ```
  Note: if you use a curl request method, you may have to wait for 2 to 3 Minutes before you get any response depending on your current system status. you will get a     responce similar to the snapshot provided below.

  ![Screenshot 2024-12-04 214110](https://github.com/user-attachments/assets/8dd7369b-c54b-454b-8107-8c67fc79318d)
  
  Disclaimer* - This is only when the llm is activated in http://localhost:8080, you may need to change the link if your LLM is activated in any other address.

- After Successfully activating the LLM Server, Add its location where its active in the .env file located at the root.
  ```text
  URL = http://localhost:8080
  ```

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

### Step 3 : Fetch Sys-Logs from dynamic text file, analyse it using the fine tuned llm and display it in the streamlit interface along with its cause and remediation.

- Within the current directory open a new bash terminal.
- activate python virtual environment,
  
  ```bash
  source env/bin/activate
  ```
- execute main.py,
  
  ```bash
  sreamlit run main.py
  ```
- After the Execution of this you could see a Streamlit Application running in localhost.

----------------------------

## Working 

#### 1. Extract Logs with Specific Threat Level:
Use journalctl, a command-line tool for querying and displaying logs from the systemd journal, to filter logs based on a specific threat level. In this case, you're looking for logs with threat levels 4 and below. This helps in narrowing down the logs to a particular set of interest based on severity.

#### 2. Dump Extracted Logs into Live Logs File:
Once you have filtered the logs, redirect or save them into a "live logs" file. This file serves as a real-time repository of logs that can be monitored, analyzed, and processed further.

#### 3. Fetch the First Log from the Live Logs File:
After the live logs file is populated, extract the first log entry. This log entry will be the starting point for further analysis.

#### 4. Query the Log with Llama-3.2-3B Fine-Tuned Model:
Pass the fetched log to a fine-tuned machine learning model (Llama-3.2-3B in this case) for analysis. The model is expected to process the log and generate a response that contains key insights, such as the heading, log content, possible cause, and recommended remediation.

#### 5. Receive and Parse the Response:
After receiving the model's response, use predefined regular expressions to parse the response. The goal here is to extract specific details such as:
- **Heading:** A brief title or summary of the log's content.
- **Log:** The main content or description of the log entry.
- **Cause:** The potential reason behind the issue or event recorded in the log.
- **Remediation:** Suggested actions to resolve or mitigate the problem identified in the log.

#### 6. Append the Parsed Details to the Live Logs List:
After parsing the response, append the extracted details (heading, log, cause, and remediation) to the live logs list. This allows you to continuously build and maintain a collection of structured log information for further analysis.

#### 7. Delete(Update) the Fetched Log from the Live Log File:
Once the first log entry has been processed and its details have been extracted and stored, delete it from the live logs file. This ensures that only unprocessed logs remain in the file for future querying and analysis.

#### 8. Represent the Records in Streamlit Interface:
Use Streamlit, a Python library for creating interactive web applications, to visualize and display the records. The live logs list, which now contains structured and parsed information, can be shown in a user-friendly interface, allowing users to easily view and interact with the log records, including their heading, content, cause, and remediation.

![alsate-working-drawio](https://github.com/user-attachments/assets/c34b8842-5f85-4430-b802-c573a917a000)

---------------------------------

## Key Features

- **Automated Syslog Monitoring**  
   - Real-time tracking of Linux sys-logs, focusing on high-severity threats (levels 4 and below).  
   - Continuous analysis without requiring manual intervention.

- **AI-Driven Analysis**  
   - Utilizes a fine-tuned Large Language Model (LLM) for log analysis.  
   - Identifies vulnerabilities, determines root causes, and suggests actionable remediation steps.  

- **Proactive Threat Management**  
   - Provides early detection of potential threats to prevent escalation.  
   - Generates actionable insights to prioritize responses effectively.  

- **Efficient Log Management**  
   - Reduces operational overhead with automated log processing.  
   - Enhances security and operational efficiency by minimizing manual efforts.

- **Low Infrastructure Requirements**  
   - Optimized to run efficiently on resource-constrained hardware, such as devices with minimal RAM, storage, and processing power.  
   - Eliminates the need for expensive components or high-end systems, making it accessible for organizations with limited budgets.

- **User-Friendly Interface**  
   - Presents processed log data and insights through an intuitive dashboard for easy decision-making.  

- **Scalability and Adaptability**  
   - Capable of handling logs from multiple Linux systems.  
   - Designed to adapt to various enterprise environments and applications.  

- **Optimization Features**  
   - Fine-tuned using Llama 3.2 3B Instruct Base Model with Low Rank Adaptation (LoRA) for resource efficiency.  
   - Quantization techniques enable deployment on devices with constrained resources.  

- **Expected Outcomes**  
   - Enhanced security posture and operational efficiency.  
   - Automated log management with proactive issue resolution.  
   - Data-driven insights for informed decision-making.


---------------------------------

## Recording

[demo.webm](https://github.com/user-attachments/assets/012f759d-1423-48a7-aa87-40e05fae3318)

----------------------------

## License

[![Licence](https://img.shields.io/badge/LICENSE-Contributor_Consent_License(CCL)-red?style=for-the-badge)](./LICENSE)

----------------------------

## Feedback
If you have any feedback, please reach out to us at voidex.developer@gmail.com .
You are also welcomed to add new features by creating Pull Requests.
