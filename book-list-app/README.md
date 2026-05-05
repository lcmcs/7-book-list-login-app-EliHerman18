# MCON 504 Week 6: Book List Login App

## Overview
This is a small Flask web application built for MCON 504 Week 6. It demonstrates the use of Flask-WTF for form validation, session-gated access control, and the Post/Redirect/Get (PRG) pattern. 

Users must log in with hardcoded credentials to access the library. Once authenticated, they can view a list of books and add new books to the temporary server-side list.

## Features Implemented
- **Session Gating:** Unauthenticated users are automatically redirected to the login page.
- **Flask-WTF Forms:** Secure, validated forms for logging in and adding books (including CSRF protection).
- **Inline Validation Errors:** Form inputs missing required data or exceeding length limits display specific error messages next to the relevant field.
- **Post/Redirect/Get Pattern:** Prevents duplicate form submissions upon browser refresh.
- **Flash Messages:** Dynamic success and error notifications configured across the application layout.

## Prerequisites
- Python 3.8+
- [Flask](https://flask.palletsprojects.com/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)
- Gunicorn

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd book-list-app