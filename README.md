# Sales Data Analyzer

A simple Python project that reads product sales data from a CSV file and displays useful sales summaries in the terminal.

## Features

- Reads product, price, and quantity information from `dados.csv`.
- Calculates the total sales amount.
- Displays each product's sales details.
- Groups and displays the total quantity sold for each product.

## Project Structure

```text
.
├── dados.csv   # Sales data
├── teste.py    # Analysis script
└── README.md   # Project documentation
```

## CSV Format

The input file must contain the following columns:

```csv
produto,preco,quantidade
Mouse,50,10
Teclado,120,5
Monitor,900,2
```

- `produto`: Product name
- `preco`: Unit price
- `quantidade`: Number of units sold

## How to Run

Make sure Python is installed, then run the following command from the project directory:

```bash
python teste.py
```

The script prints the details for each product, the total sales amount, and the total quantity sold per product.

## Requirements

This project uses only Python's standard library, so no external packages are required.
