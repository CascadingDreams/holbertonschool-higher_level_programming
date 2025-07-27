#!/usr/bin/env python3
"""
Database setup script for the products database.
This script creates the SQLite database file and populates it with sample data.
Run this once before starting your Flask application.
"""

import os
import sqlite3

def create_database():
    """
    Creates the products database and populates it with sample data.
    Removes any existing database file first to ensure clean creation.
    """
    # Remove existing database file if it exists
    if os.path.exists('products.db'):
        os.remove('products.db')
        print("Removed existing database file")
    
    # Create new database connection
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create the Products table structure
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS Products (
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           category TEXT NOT NULL,
           price REAL NOT NULL
       )
    ''')
    
    # Insert sample data into the table
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    print("Database created successfully with sample data!")
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

# This block must be at module level (no indentation)
if __name__ == '__main__':
    create_database()