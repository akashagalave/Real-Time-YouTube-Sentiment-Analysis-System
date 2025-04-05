# 🔍 YouTube Comment Sentiment Analyzer – Real-Time Chrome Extension

🚀 A next-gen, **AI-powered Chrome plugin** that brings YouTube comment sentiment analysis **directly to your browser – in real time**!  
This project fuses **Machine Learning**, **MLOps**, and **Cloud Deployment** into one slick and interactive user experience.

---

## 🎯 Why This Project?

Every day, millions engage through YouTube comments — some supportive, some critical, some downright toxic. But creators, marketers, and researchers face a major problem:

> ❓ How do we **quickly understand audience sentiment** at scale and in real time?

---

### ✅ Our Solution

The plugin **automatically reads YouTube comments**, runs them through a trained **ML model**, and injects real-time sentiment tags into the YouTube UI itself.

💬 Each comment is analyzed live and marked as:
- ✅ **Positive**
- ⚪ **Neutral**
- ❌ **Negative**

> 🧠 **Result:** Creators, brands, and researchers get instant audience intelligence **without scrolling endlessly**.

---

## 🔥 Real-World Use Cases

| 👥 User Type         | 💡 Value Delivered                                                |
|---------------------|-------------------------------------------------------------------|
| 🎥 **Content Creators** | Instantly track fan reactions & early criticism on uploads        |
| 📈 **Marketers**         | Monitor brand perception & campaign feedback in real time        |
| 🧠 **Researchers**        | Study public sentiment at scale across multiple niches/videos    |

---

## 📽️ Live Demo

▶️ **See It in Action!**  
👉 [Watch the Demo Video](Demo_Video/YT-Plugin.mp4)

---

## 🧠 Full Tech Stack

| **Layer**      | **Stack**                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------|
| **ML & NLP**   | `LightGBM`, `TfidfVectorizer`, `Optuna`                                                            |
| **MLOps**      | `DVC` (data & pipeline versioning), `MLflow`, `Docker`, `AWS EC2`, `ECR`, `CodeDeploy`, `S3`      |
| **Frontend**   | Chrome Extension using `HTML`, `CSS`, `JavaScript`, `Manifest v3`                                  |
| **Backend**    | `Flask` API serving the ML model via `Docker`, deployed on **AWS EC2**                             |

---

## ✨ Key Features

✅ **Real-time Sentiment Detection**  
→ Tags comments as **Positive**, **Neutral**, or **Negative** — live, as you scroll.

🧠 **ML-Powered Predictions**  
→ Built using a fine-tuned `LightGBM` classifier, optimized via `Optuna`.

🌩️ **Cloud-Native Deployment**  
→ Hosted on AWS using:
- **EC2** + **Docker** for scalable backend
- **ECR** for container registry
- **S3** + **MLflow** for model tracking
- **CodeDeploy** + **AutoScaling** for zero-downtime deployment

---

## 📁 Repositories

| Component         | GitHub Repo                                                                 |
|------------------|------------------------------------------------------------------------------|
| 🤖 **Backend + Model**   | [`YouTube-Comment-Sentiment-Analysis`](https://github.com/akashagalave/YouTube-Comment-Sentiment-Analysis) |
| 🧩 **Chrome Plugin**     | [`YT-CHROME-PLUGIN`](https://github.com/akashagalave/YT-CHROME-PLUGIN)                                    |

---

## ⚙️ Run It Locally – In Just Minutes!

### 🛠️ Backend Setup

```bash
git clone https://github.com/akashagalave/YouTube-Comment-Sentiment-Analysis.git
cd YouTube-Comment-Sentiment-Analysis
pip install -r requirements.txt
python app.py


The Flask server will start and serve the ML model at http://127.0.0.1:5000.


### 🧩 Step 2: Load the Chrome Extension

```bash
git clone https://github.com/akashagalave/YT-CHROME-PLUGIN.git



Then follow these steps in your browser:

1.  Open chrome://extensions
2.  Enable Developer Mode (toggle at the top-right)
3.  Click Load Unpacked
4.  Select the YT-CHROME-PLUGIN directory


Built with ❤️ by [Akash Agalave](https://github.com/akashagalave)




