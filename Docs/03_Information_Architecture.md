# Information Architecture

Project: CampusQR

Platform: Digital Place Platform

Version: 1.0

---

# Platform Architecture

Digital Place Platform is designed as a modular system where every physical location has its own digital experience.

Instead of showing an entire city, the platform provides information and services only for the place the user has entered.

Examples include:

- Campus
- Hospital
- Shopping Mall
- Airport
- Museum
- Tourist Attraction
- Railway Station

Each location is accessed by scanning its QR code.

---

# User Flow

Arrival at Location

↓

Scan QR Code

↓

Load Location Profile

↓

Welcome Screen

↓

Home Dashboard

↓

Choose Service

↓

Complete Task

---

# Home Dashboard

Every location follows the same dashboard structure.

Home

├── Navigate

├── Explore

├── Services

├── Emergency

├── Information

└── Settings

The content changes depending on the location type.

---

# Navigation Module

Navigation

├── Search Destination

├── Route

├── Destination Details

└── Navigation Instructions

---

# Explore Module

Campus Example

├── Departments

├── Library

├── Laboratories

├── Cafeteria

├── Hostel

├── Auditorium

Hospital Example

├── OPD

├── Emergency

├── Pharmacy

├── Laboratory

├── ICU

Airport Example

├── Gates

├── Lounges

├── Restaurants

├── Baggage Claim

├── Security

---

# Services Module

Campus

- Events
- Timetable
- Transport

Hospital

- Appointment
- Doctor Directory

Mall

- Offers
- Store Directory

Airport

- Flight Information

---

# Emergency Module

Emergency Contacts

Nearest Help Desk

Medical Support

Security

Fire Safety

---

# Information Module

Description

Operating Hours

Contact Information

FAQs

Announcements

---

# Settings

Language

Theme

Accessibility

Notifications

---

# Administration

Admin Login

↓

Dashboard

├── Manage Locations

├── Manage QR Codes

├── Manage Information

├── Manage Users

└── Analytics

---

# Campus Module (MVP)

Version 1 includes only the Campus module.

Campus

├── Navigation

├── Building Information

├── Departments

├── Emergency Contacts

└── Campus Information

Future modules will reuse the same platform architecture.

---

# Design Principles

- Modular
- Scalable
- Location-aware
- Easy to use
- Fast access through QR
- Consistent user experience

---

# Future Expansion

Digital Place Platform

├── CampusQR

├── HospitalQR

├── MallQR

├── AirportQR

├── MuseumQR

├── TourismQR

└── Smart City QR