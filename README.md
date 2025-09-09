# Distracted Driver Detection System

An AI-powered web application built with Streamlit and Google's Gemini Pro Vision model to analyze images of drivers and classify whether they are distracted or alert. This project provides a user-friendly interface for real-time driver safety analysis.

## 📋 Table of Contents
Overview

Features

Tech Stack

Project Structure

Setup and Installation

How to Run

Usage

## 🌟 Overview
Driver distraction is a leading cause of traffic accidents. This application leverages the powerful multimodal capabilities of the Gemini Pro Vision AI to analyze visual data and identify common signs of distraction, such as phone use, looking away from the road, or interacting with passengers.

The goal is to provide a tool that can be used for driver safety monitoring, research, or fleet management, offering immediate and actionable insights into driver behavior.

## ✨ Features
Interactive UI: A clean and professional multi-page interface built with Streamlit.

AI-Powered Analysis: Utilizes Google's Gemini Pro Vision model for accurate image analysis.

Sample Images: Includes pre-loaded sample images for users to quickly test the application's functionality.

File Uploader: Allows users to upload their own images (.jpg, .jpeg, .png) for analysis.

Two-Column Layout: A modern UI that displays the image on one side and the AI's analysis on the other.

Detailed Feedback: The AI provides a clear classification ("Alert" or "Distracted") along with a detailed reasoning for its conclusion.

Multi-Language Support: Basic setup for English and Japanese language options.

## 🛠️ Tech Stack
Backend: Python

Frontend Framework: Streamlit

AI Model: Google Gemini 1.5 Flash

Core Libraries: google-generativeai, Pillow, streamlit-option-menu

## 📁 Project Structure
Here is the folder and file structure required to run this project correctly:

your_project_folder/
├── .streamlit/
│   └── secrets.toml        # For storing the API key securely
├── css/
│   └── style.css           # Custom CSS styles
├── ui_assets/
│   └── images/
│       ├── samples/
│       │   ├── sample1.jpg
│       │   ├── sample2.jpg
│       │   └── sample3.jpg
│       ├── driver_1.jpg      # Homepage feature images
│       ├── driver_2.jpg
│       ├── driver_3.jpg
│       └── algo-logo.png
        ├── facebook.png
        ├── instagram.png
        ├── linkedin.png
        └── location.png
|__ utils
    └── load.py             # Utility functions
├── app.py                  # Main application router
├── dashboard.py            # Logic for the "Demo" page
├── homepage.py             # Logic for the "Overview" page
└── requirements.txt        # Python dependencies


## ⚙️ Setup and Installation
Follow these steps to set up and run the project on your local machine.

1. Prerequisites
Python 3.8 or higher installed on your system.

2. Clone the Repository
Clone this repository to your local machine:

git clone https://github.com/SnehaSalunke20/ALGO-Distracted-Driver-Detection
cd <your-repository-folder>

3. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

## For macOS/Linux
python3 -m venv venv
source venv/bin/activate

## For Windows
python -m venv venv
venv\Scripts\activate

4. Install Dependencies
Install all the required Python libraries from the requirements.txt file.

pip install -r requirements.txt

5. Set Up Your API Key
The application uses Streamlit's secrets management to handle your Google Gemini API key securely.

Create a folder named .streamlit in the root of your project folder.

Inside the .streamlit folder, create a new file named secrets.toml.

Open secrets.toml and add your API key in the following format:

## .streamlit/secrets.toml
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY_HERE"

Important: Make sure to add .streamlit/secrets.toml to your .gitignore file to prevent your key from being uploaded to GitHub.

🚀 How to Run
Once you have completed the setup, you can run the application using the following command in your terminal:

streamlit run app.py

A new tab should automatically open in your web browser with the application running.

usage
Overview Page: The application opens to an overview page describing the features and use cases.

Navigate to Demo: Click on the "Demo" tab in the navigation bar.

Select an Image:

Click on one of the Sample buttons to load a pre-configured image.

Or, use the file uploader to upload your own image of a driver.

Analyze: Click the "Analyze Image" button.

View Results: The AI's classification and reasoning will appear in the analysis box on the right-hand side.

This project was developed to showcase the capabilities of multimodal AI models in real-world safety applications.
