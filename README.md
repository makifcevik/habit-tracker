# Habit Tracker

This Habit Tracker project is a Python script that interacts with the Pixela API, allowing you to create and update custom graphs to track and visualize your data over time. 
Whether you want to monitor daily reading time, exercise minutes, or any other metric, Pixela provides a simple and customizable solution.

## Features

- Create and manage custom graphs to visualize your data.
- Post, update, and delete data points (pixels) on your graphs.
- Integration with the Pixela API.

## Prerequisites

Before using the Pixela Data Tracker, ensure you have the following prerequisites:

- **Python**: The script was developed using Python 3.11+.
- **Pixela Account**: Register for an account at [Pixela](https://pixe.la/).

## Getting Started

### User Registration

1. Visit [Pixela](https://pixe.la/).
2. Register for an account.
3. Retrieve your Pixela token.

### Graph Creation

1. Uncomment the `register_user_token()` and after you register (meaning that you need to run the script once) uncomment `post_graph()` line in the script.
2. Replace `"TOKEN HERE"` with your Pixela token and `"USERNAME HERE"` with your Pixela username.
3. Run the script to create your user and graph.

## Usage

### Posting a Pixel

1. Use the `post_pixel(date, quantity)` function to post a data point on your graph.
2. Replace `date` with the date in `yyyyMMdd` format and `quantity` with your data value.
3. Example: `post_pixel("20231104", "70")`.

### Updating a Pixel

1. Use the `update_pixel(date, quantity)` function to update an existing data point.
2. Replace `date` with the date to update and `quantity` with the new data value.
3. Example: `update_pixel(today, "80")`.

### Deleting a Pixel

1. Use the `delete_pixel(date)` function to delete an existing data point.
2. Replace `date` with the date to delete.
3. Example: `delete_pixel(today)`.

## Viewing Your Progress

1. You can view the changes you made on https://pixe.la/v1/users/USERNAME/graphs/graph1.html
2. Place your registered username in the `USERNAME` part

## Dependencies

- [requests](https://pypi.org/project/requests/): For making API requests to Pixela.
