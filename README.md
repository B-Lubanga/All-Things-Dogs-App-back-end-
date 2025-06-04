# 🐶 Dog Adoption Platform - CLI & ORM Backend Project

## Overview

This is a command-line interface (CLI) application for managing a Dog Adoption platform. It allows users to interact with dog adoption data, rescue centers, dog owners, and veterinarians through a Python CLI backed by a SQLAlchemy ORM and SQLite database.

This is a brief description of the project.

<img src="assets/Schemer%20diagram.png" alt="Schemer Diagram">

## Features

- View and manage adoptable dogs, rescue dogs, or dogs for sale
- Register dogs (adoptable, rescued, for sale)
- Assign owners, rescue centers, and vets
- Filter dogs by breed, location, or status
- Simple command-line interface
- CRUD operations for dogs, owners, and vets
- Relationship management between entities using SQLAlchemy ORM

## Tech Stack

- Python 3.8+
- SQLAlchemy
- Pipenv (for virtual environment and dependency management)
- SQLite

## Installation

```bash
git clone https://github.com/yourusername/dog-adoption-cli.git
cd dog-adoption-cli
pipenv install
pipenv shell
python seed.py
python main.py
```
