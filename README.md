# CampusQR Backend

> **Scan. Discover. Navigate.**

CampusQR is a QR-powered navigation platform designed to help users navigate complex physical locations.

The first implementation focuses on **campuses**, where users can scan QR codes to identify a campus, building, floor, or location and access location information and navigation.

This repository contains the **CampusQR backend**, built with FastAPI, PostgreSQL, and Redis.

---

## 🎯 Current Goal

Build a scalable backend for campus navigation that supports:

* Campus management
* Building management
* Floor management
* Location management
* QR-based location identification
* Location search
* Recent accessed locations
* Navigation-related location data

The system is designed so that it can later be extended beyond campuses.

---

## 🏗️ Backend Architecture

```text
                    CampusQR Android App
                            │
                         Retrofit
                            │
                            ▼
                       FastAPI API
                       /          \
                      /            \
                     ▼              ▼
               PostgreSQL         Redis
                    │                │
                    │                └── Recent Locations
                    │
                    ├── Campus
                    ├── Building
                    ├── Floor
                    └── Location
```

---

## 📍 Location Hierarchy

CampusQR uses a hierarchical location structure:

```text
Campus
  │
  └── Building
        │
        └── Floor
              │
              └── Location
```

Example:

```text
Sant Gajanan Maharaj College
        │
        └── Main Building
              │
              └── Ground Floor
                    │
                    ├── Computer Department
                    ├── Admin Office
                    └── Canteen
```

This structure allows the system to represent both outdoor and indoor locations.

---

## 🔲 QR Architecture

QR codes identify different levels of the location hierarchy.

### Campus

```text
CAMPUSQR:CAMPUS:C001
```

### Building

```text
CAMPUSQR:BUILDING:B001
```

### Floor

```text
CAMPUSQR:FLOOR:F001
```

### Location

```text
CAMPUSQR:LOCATION:L001
```

The QR code contains an identifier rather than storing all location information.

The backend resolves the identifier and returns the corresponding data.

---

## ⚡ Redis — Recent Locations

Redis is used for fast access to a user's recently accessed locations.

Example Redis key:

```text
recent_locations:{user_id}
```

Example:

```text
recent_locations:25

L001
L023
L008
L011
L015
```

When a user accesses a location, the backend updates Redis.

The system maintains a limited number of recent locations and removes duplicate entries.

This allows the Android Home screen to quickly display:

```text
Recent Locations

Computer Department
Library
Main Building
Admin Office
```

---

## 🗄️ PostgreSQL

PostgreSQL stores the permanent location data.

### Main entities

```text
Campus
Building
Floor
Location
```

Relationships:

```text
Campus
  │
  └── 1:N Buildings
            │
            └── 1:N Floors
                      │
                      └── 1:N Locations
```

---

## 🔌 API Modules

The backend will be organized into modular routers.

```text
routers/
│
├── campus.py
├── buildings.py
├── floors.py
├── locations.py
├── qr.py
└── recent_locations.py
```

Planned API structure:

```text
Campus
GET     /campuses
POST    /campuses
GET     /campuses/{campus_code}
PUT     /campuses/{campus_code}
DELETE  /campuses/{campus_code}

Buildings
GET     /buildings
POST    /buildings
GET     /buildings/{building_code}
PUT     /buildings/{building_code}
DELETE  /buildings/{building_code}

Floors
GET     /floors
POST    /floors
GET     /floors/{floor_code}

Locations
GET     /locations
POST    /locations
GET     /locations/{location_code}
GET     /locations/search

QR
POST    /qr/resolve

Recent Locations
GET     /recent-locations
POST    /recent-locations/{location_code}
```

Endpoints will be added incrementally as development progresses.

---

## 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Database

* PostgreSQL
* SQLAlchemy
* AsyncPG

### Caching / Fast Data

* Redis

### API Communication

* REST API
* JSON

### Development

* Git
* GitHub
* Docker — planned

---

## 📂 Project Structure

```text
CampusQR-Backend/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── dependencies.py
│
├── routers/
│   ├── campus.py
│   ├── buildings.py
│   ├── floors.py
│   ├── locations.py
│   ├── qr.py
│   └── recent_locations.py
│
├── crud/
│   ├── campus.py
│   ├── buildings.py
│   ├── floors.py
│   └── locations.py
│
├── redis/
│   └── client.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

The structure may evolve as new modules are implemented.

---

## 🚧 Current Development Status

### Completed

* FastAPI backend setup
* PostgreSQL connection
* SQLAlchemy async database setup
* Campus model
* Campus CRUD APIs
* Campus retrieval using `campus_code`

### In Progress

* Building management
* Floor management
* Location management
* QR resolution
* Redis integration
* Recent location API

### Future

* Authentication integration
* Location search improvements
* Navigation APIs
* Indoor navigation support
* Admin APIs
* Multi-location support

---

## 🚀 Running the Backend

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

API documentation:

```text
/docs
```

The backend can then be accessed locally at:

```text
http://127.0.0.1:8000
```

---

## 🔗 Android Integration

The CampusQR Android application communicates with this backend using **Retrofit**.

Development architecture:

```text
CampusQR Android
       │
       │ Retrofit
       ▼
CampusQR FastAPI
       │
       ├── PostgreSQL
       │
       └── Redis
```

The Android application is maintained separately from this repository.

---

## 🌱 Future Expansion

Although the MVP focuses on campuses, the backend architecture is intended to support other physical environments in the future:

```text
Campus
Hospital
Airport
Shopping Mall
Museum
Tourist Destination
Public Spaces
City
```

The long-term goal is to provide a common backend architecture for location-aware digital experiences.

---

## 📌 Project Status

🚧 **Active Development**

CampusQR is currently being developed as a campus navigation MVP, starting with the backend foundation and gradually expanding toward QR-based navigation and indoor location support.

---

## 📄 License

This project is currently under active development.
