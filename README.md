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

## Usage

### Add Item

1. Click on the "Add Item" page.

2. Fill out all fields in the form:

- Name: Name of the item
- Price: Price of the item it has to be positive number
- MAC Address: the format of this field is a valid MAC address example: 00:0a:95:9d:68:16
- Serial Number: serial number of the item that has to be unique.
- Manufacturer: The manufacturer company.
- Description: Description of the item.

3. Press the "Add Item" to submit this item to the inventory.

### Edit an Item

1. Click on the view of the inventory.

2. Click the "Edit" button next to the item you would like to edit.

3. Update the fields as needed and click the "Update Item" button to save changes.

### Viewing Items

To view all the items within the inventory click on the main inventory page.

Each item will list information such as, but not limited to name, price, and MAC address.
