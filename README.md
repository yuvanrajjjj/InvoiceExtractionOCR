# Invoice Extraction with LLM

This project extracts specific information from invoices in PDF format using a language model (LLM). The extracted information includes the invoice number, total amount, address, and account number.

## Project Structure

- `Invoice.pdf`: The PDF file containing the invoice to be processed.
- `Extraction.py`: The main script for loading the PDF, extracting information, and saving the results.
- `extracted_output.txt`: The file where the extracted information is saved.

## Requirements

- Python 3.7+
- langchain
- langchain-community
- warnings
- OllamaFunctions

## Installation

1. **Clone the repository**
    ```bash
    git clone (https://github.com/yuvanrajjjj/InvoiceExtractionOCR.git)
    cd InvoiceExtractionWithLLM
    ```

2. **Create a virtual environment and activate it**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Place your invoice PDF in the project directory**
    Ensure your invoice PDF file is named `Invoice.pdf` or update the script with your PDF file's name.

2. **Run the extraction script**
    ```bash
    python extracted_output.txt
    ```

3. **Check the extracted output**
    The extracted information will be saved in `extracted_output.txt` in the project directory.

## Example Output
{
"invoice no": 12345,
"Total": 67890,
"Address": "123 Main St, Anytown, USA",
"Account No": 987654321
}
