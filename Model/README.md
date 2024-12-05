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

## Platform used to fine tune the model

- Kaggle Account
  
  <a href="https://www.kaggle.com" alt="kaggle">
      <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white"></a>
      
---------------------------

## Base Model

- Llama 3.2 3B
  
  <a href="https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/" alt="llama"><img src="https://img.shields.io/badge/Llama 3.2 3B-0467DF?style=for-the-badge&logo=meta&logoColor=white"></a> &nbsp;

  Why Llama 3.2 3B?
  - Llama 3.2 Quantized Models (3B) are highly optimized versions of Meta’smultilingual large language models.
  - They feature 3 billion parameters and are tailored for instruction-following tasks.
  - Designed for deployment on resource-constrained devices, such as smartphones and tablets.
  - These models reduce memory usage and power consumption while preserving nearly the same accuracy as their non-quantized counterparts.

- Llama 3.2 3B Instruct

  <a href="https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct" alt="llama"><img src="https://img.shields.io/badge/Llama 3.2 3B Instruct-0467DF?style=for-the-badge&logo=meta&logoColor=white"></a> &nbsp;
  
  The fine-tuned **Llama 3.2 3B Instruct** model is a cornerstone of the system, meticulously tailored to excel in conversational tasks. Leveraging the **Instructor template**, it crafts highly contextual, precise, and coherent responses. This fine-tuning not only enhances its ability to interpret complex inputs but also ensures adaptability across diverse conversational scenarios, making it an indispensable component for effective interaction and response generation.

-------------------------------

## Dataset

The Original Dataset consist of 3 counter parts namely
  - Log
  - Cause
  - Remediation

#### Logs
- Source : Ubuntu System
- The log data was collected using **Journalctl**, with a focus on **system logs of level 4 and below**. To streamline this, we modified the **Journalctl configuration file** to restrict the system to produce only the required log levels (details available in the Main README). This approach ensured the data remained precise and aligned with the project's objectives. The collected logs were then temporarily stored in **Google Sheets**, organized by log level separations, allowing for efficient preprocessing and analysis in later stages.

#### Cause and Remediation

- Source: The causes and remediation steps were derived from multiple credible and practical resources:

Troubleshooting Methodologies:
Common practices followed by system administrators and hardware experts for diagnosing and resolving issues.
Official Documentation:
Authoritative resources from organizations such as Red Hat and Ubuntu, providing detailed guides for system management and troubleshooting.
Hands-On Experiments:
Practical experiments conducted in virtual environments, leveraging official documentation and guides to simulate real-world issues and their resolutions.
Key References:

Red Hat Enterprise Linux System Administrator’s Guide:
Covers essential tasks for managing Linux systems, such as file system issues and system recovery.
Explore it here.

Red Hat Enterprise Linux Diagnostics and Troubleshooting:
Focused on diagnosing and resolving system issues, including disk failures, kernel panics, and memory errors.

These sources ensured that the dataset’s cause and remediation components were well-informed, practical, and grounded in real-world scenarios, enhancing their reliability and applicability.






