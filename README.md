Inventory Management Application

## Overview

The Inventory Management Application is a web-based application for the management of inventory items. It provides an interface for adding, editing, and viewing items within the inventory. Product details will be stored in an efficient manner so as to keep track of the product name, price, MAC address, serial number, manufacturer, and description.

## Features

- Easy interface for adding, editing, and viewing items in the inventory.
- Input validation to ensure that data integrity is maintained, for example, making certain fields required and proper format of the MAC address.
- Error handling from the submission of invalid input and server-side validation

## Technologies Used

![Flask-web drawio](https://github.com/user-attachments/assets/aa3a3d64-7e77-462e-95d5-ec1b69057dbb)

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy with a relational database (e.g., SQLite, PostgreSQL)
- **Frontend**: HTML, CSS, JavaScript (Bootstrap for styling)
- **Environment**: Python 3.x, Flask framework
- **Containerization**: Docker and Docker Compose

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Docker
- Docker Compose

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. **Build and run the application using Docker Compose:**:
   ```bash
   docker-compose up --build

> [!NOTE]    
> The application will be accessible at http://127.0.0.1:5000.
