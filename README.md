# ✈️ Planify – Travel Booking System

<p align="center">
  <b>Your All-in-One Travel Companion (Hotels + Flights)</b><br>
  Built with Python + JSON Storage
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Storage-JSON-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Working-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Made%20By-Jithin%20Mathew-purple?style=for-the-badge">
</p>

---

## 🌍 Overview

**Planify** is a **CLI-based travel booking system** that allows users to:

* 🏨 Book hotels
* ✈️ Book flights
* 📋 Manage bookings
* 🚖 Access travel services

Unlike traditional systems, Planify uses **JSON files instead of databases**, making it lightweight and easy to run anywhere.

---

## 🚀 Features

### 👤 User System

* Guest registration & login
* Password input with hidden dialog (Tkinter)
* Guest archiving & reactivation

---

### 🏨 Hotel Booking

* Search hotels by:

  * City
  * Room type
  * Price range
* Real-time availability tracking
* Automatic discount (10% for >3 nights)

---

### ✈️ Flight Booking

* Search flights by:

  * Route (From → To)
  * Airline
  * Price
* Seat availability management
* 🎫 Auto-generated **PNR numbers**

---

### 📋 Booking Management

* View hotel bookings
* View flight bookings
* Cancel bookings
* Auto-update availability

---

### 🌟 Additional Services

* 🍽️ Meal booking
* 🚖 Taxi booking
* 🎡 Experience booking

---

### 🎁 Smart Features

* Combo offers (hotel + flight discounts)
* Active booking validation before services
* Data persistence using JSON files

---

## 🛠️ Tech Stack

| Technology | Purpose       |
| ---------- | ------------- |
| Python     | Core logic    |
| JSON       | Data storage  |
| Tkinter    | Password UI   |
| datetime   | Date handling |

---

## 📂 Project Structure

```bash
travel-booking-system.py   # Main application
guests.json               # User data
hotels.json               # Hotel data
flights.json              # Flight data
bookings.json             # Booking records
archives.json             # Archived users
README.md                 # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jithin2007/Python-Based-Travel-Booking-System.git
cd Python-Based-Travel-Booking-System
```

---

### 2️⃣ Run the Project

```bash
python travel-booking-system.py
```

---

## 🧠 How It Works

```text
Register/Login → Search Hotels/Flights → Book → Manage → Add Services
```

* JSON files act as a database
* Data is automatically created on first run
* Availability updates in real-time
* Users are archived when inactive

---

## 📸 Demo (CLI Preview)

```text
****Welcome to Planify****
1. Register Guest
2. Login
3. Exit
```

```text
Available Flights:
Flight ID: 1, Airline: Air India, Route: Mumbai → Delhi
Price: ₹3500
```

```text
Flight booked successfully!
PNR: PNR123456
Total bill: ₹7000
```

---

## ⚠️ Limitations

* CLI-based (no GUI yet)
* Passwords are stored in plain text
* No online deployment (local only)

---

## 🔮 Future Improvements

* 🌐 Convert to Flask/Django web app
* 🔐 Add password hashing
* 💳 Payment gateway integration
* 📱 GUI or mobile app
* ☁️ Cloud deployment

---

## 👨‍💻 Author

**Jithin Mathew**

---

## 🌟 Show Your Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🚀 Build on it

---

<p align="center">
  Built for learning, scaling, and flexing 🚀
</p>
