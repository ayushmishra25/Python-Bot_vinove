# Python Agent Test

## Overview
This Python-based desktop agent monitors employee activity, capturing user inputs and screenshots. It runs in the background, ensuring efficient activity tracking, robust error handling, and secure data upload to cloud storage like AWS S3.

## Core Features

### 1. **Activity Tracking**
- Monitors user activity, capturing inputs such as mouse and keyboard usage.
- Detects scripted activity (e.g., irregular mouse movements, unnatural keyboard inputs) and flags it.
- Configurable options for capturing screenshots (blurred/unblurred) and the ability to enable/disable screenshot capture.

### 2. **Configurable Screenshot Intervals**
- Screenshots can be captured at customizable intervals (e.g., every 5 or 10 minutes).
- The agent listens for configuration updates from a web application and applies them in real-time.

### 3. **Time Zone Management**
- Automatically detects and adjusts for time zone changes.
- Logs user activity with accurate timestamps reflecting the time zone.

### 4. **Data Upload**
- Automatically uploads screenshots and activity logs to Amazon S3 or similar cloud storage.
- Efficiently handles large file uploads with compression and chunking.
- Data transmission is securely encrypted.

### 5. **Error Handling and Resilience**
- **No Internet Connection:** Queues uploads and retries when the connection is restored.
- **Abrupt Disconnection:** Handles unexpected shutdowns gracefully, ensuring data integrity.
- **Firewall Restrictions:** Detects firewall issues and provides error messaging.

### 6. **Instance Management**
- Ensures only one instance of the application is running to prevent multiple instances.

## Best Practices

### 1. **Memory and Performance Optimization**
- Lightweight with minimal impact on system resources.
- Optimized for efficient memory usage and minimal CPU consumption.

### 2. **File Size Management**
- Compresses screenshots to reduce file sizes before upload.
- Logic for deleting or archiving old screenshots to manage local storage effectively.

### 3. **Modular and Object-Oriented Design**
- Structured in a modular, object-oriented manner.
- Extensively commented for clarity and maintainability.

### 4. **Security**
- Handles AWS credentials securely.
- Follows best practices for encrypted file uploads via SSL/TLS.

## Optional Features (Future Enhancements)
- **Auto-Update Mechanism:** Automatic updates without user intervention.
- **Low Battery Detection:** Suspends tracking when low battery is detected on laptops.
- **Enhanced Security:** Multi-factor authentication (MFA) for configuration changes.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/employee-monitoring-app.git
   cd employee-monitoring-app

2. **Install Dependencies Install the required libraries listed in requirements.txt:**
   ```bash
   pip install -r requirements.txt

3. **Set AWS Credentials Set up your AWS credentials in the environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID='your-access-key'
    export AWS_SECRET_ACCESS_KEY='your-secret-key'

4. **Run the Application**
   ```bash
   python monitor.py

## Testing

1. **Unit Tests**
Core functionality tests for activity tracking, file upload, and instance management.
Includes tests for error scenarios (e.g., network disconnections).

2. **Integration Tests** 
Validates interaction between agent components (e.g., configuration updates, upload handling).


## Thank you, Vinove, for providing us with this incredible opportunity to deepen our understanding of these concepts 

