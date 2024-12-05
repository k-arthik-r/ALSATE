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

The Model and the Dataset used has a very strict LICENSING Policy, we suggest you to read and understand all the aspects of the LICENSE before you read further. 

[![Licence](https://img.shields.io/badge/LICENSE-Contributor_Consent_License(CCL)-red?style=for-the-badge)](./LICENSE)

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

## Modules/Libraries Used

All The Modules/Libraries Used in the project can be installed using [requirements.txt](requirements.txt)
- `transformers`
- `bitsandbytes`
- `peft`
- `os`
- `torch`
- `wandb`
- `datasets`
- `trl`

----------------------------

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

The Original Dataset consist of 2 counter parts namely
  - Log
  - Cause and Remediation

#### Logs
- Source : Ubuntu System
- The log data was collected using **Journalctl**, with a focus on **system logs of level 4 and below**. To streamline this, we modified the **Journalctl configuration file** to restrict the system to produce only the required log levels (details available in the Main README). This approach ensured the data remained precise and aligned with the project's objectives. The collected logs were then temporarily stored in **Google Sheets**, organized by log level separations, allowing for efficient preprocessing and analysis in later stages.

#### Cause and Remediation

- Source: The causes and remediation steps were derived from multiple credible and practical resources:

  - Troubleshooting Methodologies: Common practices followed by system administrators and hardware experts for diagnosing and resolving issues.
  - Official Documentation:Authoritative resources from organizations such as Red Hat and Ubuntu, providing detailed guides for system management and troubleshooting.
  - Hands-On Experiments: Practical experiments conducted in virtual environments, leveraging official documentation and guides to simulate real-world issues and their resolutions.
    
- Key References:
  
  - Red Hat Enterprise Linux System Administrator’s Guide: Covers essential tasks for managing Linux systems, such as file system issues and system recovery.
  
  - Red Hat Enterprise Linux Diagnostics and Troubleshooting: Focused on diagnosing and resolving system issues, including disk failures, kernel panics, and memory errors.
  
  These sources ensured that the dataset’s cause and remediation components were well-informed, practical, and grounded in real-world scenarios, enhancing their reliability and applicability.

A sample from google sheets: 

| **Logs** | **Cause and Remediation** |
|----------|----------------------------|
| **Nov 07 10:11:20 ubuntu gdm3[1175]: GLib: Source ID 181 was not found when attempting to remove it** | **Cause**: GLib attempted to remove a non-existent resource, which could indicate a logic error or race condition in the GDM code. <br> **Remediation**: Review the GDM logs for related issues. Update GDM and GLib to the latest versions to ensure bug fixes. |


Llama 3.2 requires the input data to adhere to a specific template for effective fine-tuning and inference. To meet this requirement, we rephrased the entire dataset using a Transformer Template.


```markdown
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Cutting Knowledge Date: December 2023  
Today Date: 26 Nov 2024  

Your name is "ALSATE", you are an advanced syslog parsing and analysis tool. Your task is to analyze provided system logs, identify potential causes of their generation, and detect any security threats or anomalies. If threats are found, suggest precise remediation steps. Respond only when the input is a valid system log; otherwise, reply with: 'Input does not appear to be a valid system log. Unable to assist.'  
<|eot_id|><|start_header_id|>user<|end_header_id|>

Nov 24 00:49:54: Critical system failure: Network driver unable to initialize, system cannot access the network.  
<|eot_id|><|start_header_id|>assistant<|end_header_id|>

Cause - The network driver failed to load, preventing system connectivity.  
Remediation -  
1. Reinstall or update the network driver.  
2. Check and replace hardware like the network adapter if necessary.  
3. Verify network configurations for errors.  
<|eot_id|>
```

--------------------------------------------

## Fine Tuning

We have used **LoRA (Low-Rank Adaptation)** to fine-tune the **Llama 3.2 3B Instruct** model effectively and efficiently. LoRA is a powerful fine-tuning technique designed to optimize the performance of large language models while reducing resource consumption.

### What is LoRA?
**LoRA (Low-Rank Adaptation)** is a fine-tuning method that focuses on updating only a small subset of parameters in a pre-trained model, rather than all the parameters. It introduces low-rank matrices into specific layers of the model (usually attention layers), allowing significant computational and memory efficiency.

### Why LoRA?  
- **Efficiency**: Fine-tuning only a few parameters drastically reduces the memory and computational cost, making it suitable for large models like Llama 3.2.  
- **Adaptability**: LoRA allows the base model to retain its general knowledge while specializing in a specific domain or task through efficient parameter updates.  
- **Low Hardware Requirements**: LoRA reduces the GPU and memory requirements, enabling fine-tuning even on resource-constrained hardware.  
- **Parameter Efficiency**: By introducing low-rank matrices, the number of trainable parameters is minimized while still achieving high performance.

### How LoRA Works:
1. **Decomposition**: In LoRA, weight updates are decomposed into low-rank matrices (e.g., `A` and `B`), where the rank is significantly smaller than the full size of the weight matrix.  
2. **Optimization**: During training, only the low-rank matrices are updated, leaving the original model weights unchanged.  
3. **Integration**: At inference, the updates from LoRA are combined with the pre-trained weights, producing predictions as if the entire model had been fine-tuned.  

### Advantages of Using LoRA:
- **Speed**: Speeds up the fine-tuning process, as fewer parameters need to be trained.  
- **Storage**: Only the low-rank matrices need to be stored for task-specific fine-tuning, reducing storage requirements.  
- **Scalability**: LoRA is scalable and can be used to fine-tune large models on a variety of tasks without re-training the entire model.  

LoRA enabled us to efficiently adapt the Llama 3.2 model for syslog analysis, allowing it to detect causes and provide actionable remediation steps without requiring significant computational resources.

To Know More About LoRA Click [Here](https://arxiv.org/pdf/2106.09685)

-------------------------

## Execution

The code and its execution history used for fine-tuning the model are available in [alsate.ipynb](alsate.ipynb).

--------------------------

## Training Hyperparameters

| **Hyperparameter**          | **Value**            | **Description**                                                                              |
|------------------------------|----------------------|----------------------------------------------------------------------------------------------|
| `output_dir`                | `new_model`         | Directory to save the trained model.                                                        |
| `per_device_train_batch_size` | `1`                | Batch size per device during training.                                                      |
| `per_device_eval_batch_size` | `1`                | Batch size per device during evaluation.                                                    |
| `gradient_accumulation_steps` | `2`               | Number of steps to accumulate gradients before performing an optimizer step.                |
| `optim`                     | `paged_adamw_32bit` | Optimizer used during training.                                                             |
| `num_train_epochs`           | `2`                | Total number of training epochs.                                                            |
| `eval_strategy`             | `steps`             | Evaluation strategy to use.                                                                 |
| `eval_steps`                | `0.05`             | Number of steps between evaluations.                                                        |
| `save_steps`                | `0.05`             | Number of steps between saving checkpoints.                                                 |
| `save_total_limit`           | `3`                | Maximum number of checkpoints to keep.                                                      |
| `logging_steps`             | `1`                | Number of steps between logging outputs.                                                    |
| `warmup_steps`              | `1000`             | Number of warmup steps for the learning rate scheduler.                                      |
| `logging_strategy`           | `steps`             | Logging strategy used.                                                                      |
| `learning_rate`             | `2e-4`             | Initial learning rate.                                                                      |
| `fp16`                      | `False`            | Whether to use 16-bit floating-point precision.                                             |
| `bf16`                      | `False`            | Whether to use bfloat16 precision.                                                          |
| `group_by_length`           | `True`             | Whether to group sequences of similar lengths during training.                              |
| `max_grad_norm`             | `0.8`              | Maximum gradient norm for gradient clipping.                                                |
| `weight_decay`              | `0.1`              | Weight decay for the optimizer.                                                             |
| `load_best_model_at_end`    | `True`             | Whether to load the best model at the end of training.                                       |
| `report_to`                 | `wandb`            | Reporting tool for training logs.                                                           |
| `r`                         | `16`               | Rank of the LoRA layers.                                                                    |
| `lora_alpha`                | `32`               | Scaling factor for LoRA updates.                                                            |
| `lora_dropout`              | `0.05`             | Dropout rate applied to the LoRA layers.                                                    |
| `bias`                      | `none`             | Whether to include bias terms in LoRA updates.                                              |
| `task_type`                 | `CAUSAL_LM`        | Type of task for which LoRA is configured.                                                  |
| `target_modules`            | `modules`          | Modules targeted by the LoRA adapter.                                                      |
| `max_seq_length`            | `512`              | Maximum sequence length for inputs.                                                         |
| `dataset_text_field`         | `text`             | Field in the dataset that contains the input text.                                          |
| `packing`                   | `False`            | Whether to pack multiple sequences into a single input example during training.             |

-------------------------------

## Quantization

For our use case, where we aimed to run the model locally on a low-performance machine, we needed to reduce the model's resource consumption. To achieve this, we quantized the model to **Q4 Small** and **Q4 Medium** (we chose **Q4 Medium** for optimal performance).

To quantize the model, we used GGML-ORG's repository, which you can access here.

  <a href="https://huggingface.co/spaces/ggml-org/gguf-my-repo" alt="ggml">
      <img src="https://custom-icon-badges.demolab.com/badge/GGML_ORG-000000?style=for-the-badge&logo=ggml-org"></a>

-------------------------------

## Model Tree

![model tree](https://github.com/user-attachments/assets/dfaa13bc-d2ac-413b-af67-76a17ce2d0a3)

-------------------------------

## Modle and Model Card

Access the model and model card here:

- **Base Model** : *meta-llama/Llama-3.2-3B* : [here](https://huggingface.co/meta-llama/Llama-3.2-3B)

- **Finetuned Model v1** : *meta-llama/Llama-3.2-3B-Instruct* : [here](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)

- **Finetuned Model v2** : *k-arthik-r/llama-3.2-3b-sys-log-analysis-alsate* : [here](https://huggingface.co/k-arthik-r/llama-3.2-3b-sys-log-analysis-alsate)

- **Quantized Model v1** : *k-arthik-r/llama-3.2-3b-sys-log-analysis-alsate-Q4_K_S-GGUF* : [here](https://huggingface.co/k-arthik-r/llama-3.2-3b-sys-log-analysis-alsate-Q4_K_S-GGUF)

- **Quantized Model v2** : *k-arthik-r/llama-3.2-3b-sys-log-analysis-alsate-Q4_K_M-GGUF* : [here](https://huggingface.co/k-arthik-r/llama-3.2-3b-sys-log-analysis-alsate-Q4_K_M-GGUF)
  
Note* - Focus on **Finetuned Model v2** and **Quantized Model v2**

-------------------------------

## Hardware Used

Nvidia T4 x 2 - GPU

  <a href="https://www.nvidia.com/en-in/data-center/tesla-t4" alt="nvidia">
      <img src="https://img.shields.io/badge/nVIDIA-%2376B900.svg?style=for-the-badge&logo=nVIDIA&logoColor=white"></a>

-------------------------------

## Results

We used **Weights & Biases** to track the training progress, which you can access [here](https://wandb.ai/vvce/ALSATE/runs/w7rii5yb?nw=nwuserkarthikr).

### Train Loss

![W B Chart 12_4_2024, 12_35_25 PM](https://github.com/user-attachments/assets/e3a26c34-20e9-4a92-be65-47161d9b0966)

### Evalution Loss

![W B Chart 12_4_2024, 12_35_11 PM](https://github.com/user-attachments/assets/16c30475-a292-42af-8238-d05d777a70e1)

### Training status table

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6575ccbb177b3b46636f3a42/modXs7vn78yMvygz1spFA.png)

----------------------------

## License

[![Licence](https://img.shields.io/badge/LICENSE-Contributor_Consent_License(CCL)-red?style=for-the-badge)](./LICENSE)

----------------------------

## Feedback
If you have any feedback or need access to the model, please reach out to us at voidex.developer@gmail.com .
