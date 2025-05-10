# 📚 Smart Study Scheduler

A smart and simple web app built with **Streamlit** to help students generate an optimized study schedule based on the subjects they want to study and the time they have available. It also provides motivational quotes and allows you to **export your schedule as a PDF**.

---

## 🔧 Features

* ✅ User input for subjects and study hours
* 📊 Automatic adjustment of schedule based on total available time
* 📄 Export your personalized schedule as a downloadable PDF
* 💬 Motivational quotes for study encouragement
* ⚡ Built using Python and Streamlit for fast deployment

---

## 💽 Demo

Try the app live on [Streamlit Cloud](#)
*(Replace the `#` with your actual Streamlit deployment link)*

---

## 🚀 How It Works

1. Enter your subjects and how many hours you'd like to study each.
2. Specify your total available study time for the day.
3. The app will calculate and adjust your schedule proportionally.
4. Click a button to **export your study plan as a PDF**.
5. Get inspired with a random motivational quote!

---

## 🛠 Installation

### Prerequisites:

* Python 3.x
* pip

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-study-scheduler.git
cd smart-study-scheduler
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run study_scheduler.py
```

---

## 📦 Dependencies

```
streamlit
fpdf
```

Make sure they are listed in `requirements.txt` for deployment.

---

## 📁 Project Structure

```
smart-study-scheduler/
│
├── study_scheduler.py     # Main Streamlit app
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---
## 💻Screenshots
![WhatsApp Image 2025-05-10 at 07 55 14_2b0a1da5](https://github.com/user-attachments/assets/37de24ad-a126-41d1-add9-c3730d468fdf)
![WhatsApp Image 2025-05-10 at 07 55 55_3b3e3b56](https://github.com/user-attachments/assets/46aef16e-2d1c-41a8-8737-0ddae2c347cf)
![WhatsApp Image 2025-05-10 at 07 55 35_7eab6bf7](https://github.com/user-attachments/assets/34b5fa73-aa4b-4f80-983b-740ea009667c)



## 📄 Example PDF Output

> The exported PDF includes:
>
> * Subject names
> * Allocated hours
> * Title & formatting for readability

---

## 🙌 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 🧑‍💻 Author

**Vishal Singh Kashyap**
[LinkedIn](https://linkedin.com/in/your-profile)
[GitHub](https://github.com/yourusername)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Future Improvements

* Add drag-and-drop study calendar view
* Save schedules for different dates
* Notify users via email
