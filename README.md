# Multimodal AI Agent System

Welcome to the **Multimodal AI Agent System** repository! This project integrates advanced AI technologies to handle a variety of multimodal tasks including image generation, text-to-speech conversion, image description, and web searching. This README provides an overview of the system, setup instructions, and usage guidelines.

## Overview

The Multimodal AI Agent System leverages CrewAI, Replicate AI models, Groq accelerators, and Tavily-Python to provide a scalable and efficient solution for handling complex AI tasks. The system is designed to process user instructions through various agents and helper functions, ensuring seamless execution of multimodal tasks.

### Key Components

1. **CrewAI Framework**
   - Central management for coordinating agents and their workflows.
   - Handles task lifecycle, agent interactions, and overall orchestration.

2. **Replicate AI**
   - Provides pre-trained models for:
     - **Text-to-Speech:** Converts text into spoken words.
     - **Image Generation:** Creates images from textual descriptions.
     - **Image Captioning:** Provides textual descriptions for images.

3. **Groq Hardware Accelerators**
   - Speeds up AI model inference with optimized performance and energy efficiency.

4. **Tavily-Python**
   - Facilitates web searches and information retrieval, summarizing relevant web content.

### Helper Functions

1. **Web Search Tool Helper Function**
   - Utilizes Tavily-Python to perform search queries and generate summaries.

2. **Text-to-Speech Tool Helper Function**
   - Uses the Replicate AI text-to-speech model to produce audio from text.

3. **Image Generation Helper Function**
   - Leverages Replicate AI’s image generation model to create images from text.

4. **Process Image for Description Helper Function**
   - Uses Replicate AI’s image captioning model to describe the contents of images.

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repo/multimodal-ai-agent.git
   cd multimodal-ai-agent
   ```

2. **Install Dependencies**

   Ensure you have Python 3.x installed. Install the required packages using:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**

   Set up your API keys for Replicate AI and Tavily-Python in the configuration file (`config/config.json`):

   ```json
   {
     "replicate_api_key": "YOUR_REPLICATE_API_KEY",
     "tavily_api_key": "YOUR_TAVILY_API_KEY"
   }
   ```

4. **Setup Groq Accelerators**

   Follow the [Groq documentation](https://www.groq.com/docs) to configure and integrate Groq hardware accelerators with your system.

5. **Initialize the System**

   Run the setup script to initialize the system components:

   ```bash
   python setup.py
   ```

### Usage

1. **Start the Crew System**

   ```bash
   python start_crew.py
   ```

2. **Send User Instructions**

   Interact with the system through the provided user interface or API. Examples of user instructions include:
   - "Generate an image of a futuristic city skyline."
   - "Describe the image I just uploaded."
   - "Convert this text into speech."
   - "Find information about the latest advancements in AI."

3. **Monitor and Debug**

   Monitor system performance and logs through the provided monitoring tools. Refer to the `logs/` directory for detailed logs.

### Example Workflow

1. **Generate an Image:**

   - **Instruction:** "Generate an image of a futuristic city skyline."
   - **System Response:** The Image Generation Agent creates and displays the image.

2. **Describe an Image:**

   - **Instruction:** "Describe the image I just uploaded."
   - **System Response:** The Image Description Agent provides a textual description of the uploaded image.

3. **Convert Text to Speech:**

   - **Instruction:** "Convert this text into speech."
   - **System Response:** The Text-to-Speech Agent generates and provides an audio file.

4. **Perform Web Search:**

   - **Instruction:** "Find information about the latest advancements in AI."
   - **System Response:** The Web Search Agent performs the search and provides a summary.

### Contribution

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) for details on how to contribute to the project.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Contact

For questions or support, please contact (mailto:samad.ali.hulikunte@gmail.com ).

abdul samad a 
7795738104
