Installation and Usage Instructions
===================================

This guide explains how to set up and run the Accommodation Booking System project.

Installation
------------
Follow these steps to install and set up the project on your local machine:

1. **Clone the Repository:**
   Clone the project's repository from GitHub using the following command:
   .. code-block:: bash

       git clone https://github.com/YourRepo/AccomodationBookingSystem.git

2. **Set Up a Virtual Environment:**
   Create and activate a virtual environment for the project:
   - On Windows:
     .. code-block:: bash

         python -m venv venv
         venv\Scripts\activate

   - On macOS/Linux:
     .. code-block:: bash

         python3 -m venv venv
         source venv/bin/activate

3. **Install Dependencies:**
   Install the required dependencies listed in the `requirements.txt` file:
   .. code-block:: bash

       pip install -r requirements.txt

4. **Database Setup:**
   Perform the necessary database migrations:
   .. code-block:: bash

       python manage.py makemigrations
       python manage.py migrate

5. **Run the Server:**
   Start the development server:
   .. code-block:: bash

       python manage.py runserver

6. **Access the Application:**
   Open a web browser and navigate to:



Usage
-----
Once the project is running, you can perform the following actions:

1. **Register a New User:**
- Use the registration page to create a new user account.

2. **Log In:**
- Use your registered credentials to log in.

3. **Book a Room:**
- Navigate to the booking page and select a room.

4. **Make a Payment:**
- Simulate a payment using the provided form.

5. **Manage Bookings:**
- View, cancel, or reschedule your bookings from your profile page.

