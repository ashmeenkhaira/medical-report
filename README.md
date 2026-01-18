# Medical-report
<div align="center">

<h1>🫁 Multimodal Chest X-Ray Report Generation</h1>

<p>
<strong>An end-to-end medical AI system that predicts chest diseases and generates radiology reports from X-ray images</strong>
</p>

<p>
<img src="https://img.shields.io/badge/TensorFlow-2.20-orange" />
<img src="https://img.shields.io/badge/Streamlit-Cloud-red" />
<img src="https://img.shields.io/badge/HuggingFace-Model-yellow" />
<img src="https://img.shields.io/badge/Python-3.13-blue" />
</p>

<hr/>

<p>
🚀 <strong><a href="https://medical-report-ld4ooptgda2ndwohgrhpch.streamlit.app/">Live Demo</a></strong> &nbsp; | &nbsp;
🤗 <strong><a href="https://huggingface.co/AshuKaur/medical-report/tree/main">Hugging Face Model</a></strong>
</p>

</div>

---

<h2>🧠 Overview</h2>

<p>
This project is a <strong>multimodal medical AI system</strong> that takes <strong>frontal and lateral chest X-ray images</strong> as input and produces:
</p>

<ul>
  <li>✅ <strong>Multi-label disease predictions</strong></li>
  <li>📝 <strong>Automatically generated radiology-style reports</strong></li>
</ul>

<p>
The system combines <strong>computer vision</strong> and <strong>natural language processing</strong> using a CNN-Transformer architecture and is fully deployed using <strong>Streamlit Cloud</strong>.
</p>

---

<h2>📥 Inputs & 📤 Outputs</h2>

<table>
<tr>
<th>Type</th>
<th>Description</th>
</tr>
<tr>
<td><strong>Input</strong></td>
<td>Frontal + Lateral Chest X-ray Images</td>
</tr>
<tr>
<td><strong>Output</strong></td>
<td>Disease probabilities + Generated medical report</td>
</tr>
</table>

<h3>🦠 Predicted Diseases</h3>

<ul>
  <li>Pneumonia</li>
  <li>Edema</li>
  <li>Effusion</li>
  <li>Cardiomegaly</li>
  <li>Atelectasis</li>
</ul>

---

<h2>🏗 Model Architecture</h2>

<pre>
Frontal X-ray ─┐
               ├─ CNN (ResNet50) ─┐
Lateral X-ray ─┘                  ├─ Feature Fusion ──┐
                                                     ├─ Disease Classifier
                                                     └─ Transformer Decoder ──► Report
</pre>

<h3>Key Components</h3>

<ul>
  <li><strong>Visual Encoder:</strong> Shared ResNet50 backbone</li>
  <li><strong>Feature Fusion:</strong> Concatenation of multi-view embeddings</li>
  <li><strong>Disease Head:</strong> Multi-label classifier (sigmoid)</li>
  <li><strong>Text Decoder:</strong> Transformer with cross-attention</li>
</ul>

---

<h2>📊 Dataset</h2>

<p>
<strong>Indiana University Chest X-Ray Dataset (IU-Xray)</strong>
</p>

<ul>
  <li>Paired frontal & lateral views</li>
  <li>Expert radiology reports</li>
  <li>Tokenized vocabulary for supervised text generation</li>
</ul>

<p>
<i>Used strictly for research and educational purposes.</i>
</p>

---

<h2>🧪 Training Details</h2>

<ul>
  <li>Multi-task learning (classification + report generation)</li>
  <li>Teacher forcing during training</li>
  <li>Greedy decoding during inference</li>
  <li>Joint loss optimization</li>
</ul>

---

<h2>🚀 Deployment</h2>

<h3>🤗 Model Hosting</h3>

<ul>
  <li>Trained model hosted on <strong>Hugging Face</strong></li>
  <li>Downloaded dynamically at runtime</li>
</ul>

<h3>🖥 App Hosting</h3>

<ul>
  <li>Built with <strong>Streamlit</strong></li>
  <li>Deployed on <strong>Streamlit Cloud</strong></li>
  <li>Compatible with <strong>Python 3.13 + TensorFlow 2.20</strong></li>
</ul>

---

<h2>📁 Project Structure</h2>

<pre>
medical-report/
├── app.py
├── requirements.txt
├── pyproject.toml
├── utils/
│   ├── image_utils.py
│   └── inference.py
├── model/
│   └── vocab.txt
└── README.md
</pre>

---

<h2>⚠️ Medical Disclaimer</h2>

<p style="color:red;">
<strong>This application is for research and educational purposes only.</strong><br/>
It is <strong>NOT</strong> intended for clinical diagnosis or medical decision-making.
</p>

---

<h2>🌟 Highlights</h2>

<ul>
  <li>End-to-end multimodal ML pipeline</li>
  <li>Vision + Language fusion</li>
  <li>Real-world deployment challenges solved</li>
  <li>Hugging Face + Streamlit integration</li>
</ul>

---

<h2>🔮 Future Work</h2>

<ul>
  <li>Beam search decoding</li>
  <li>Attention visualization</li>
  <li>Model quantization</li>
  <li>Single-view inference support</li>
</ul>

---

<h2>👩‍💻 Author</h2>

<p>
<strong>Ashmeen Khaira</strong><br/>
Machine Learning & AI Enthusiast
</p>

<hr/>

<div align="center">
<p><strong>⭐ If you like this project, consider starring the repository!</strong></p>
</div>
