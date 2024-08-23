# Project Name

## Description

This project is a CV optimiser that extracts relevant information from a Job description and applies it to a CV. The CV parser uses the OpenAI API to generate a summary of the CV and Job description. The parser then extracts the relevant information from the Job description and applies it to the CV. The optimised CV is then generated and stored in the output folder.

## Installation

To install and run the CV parser, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/cv-parser.git`
2. Navigate to the project directory: `cd cv-parser`
3. Install the required dependencies: `npm install openai` `npm install python-dotenv`
4. Run the application: `python3 cv_parser.py`

## Usage

To use the CV parser, follow these steps:
1. Create a .env file in the root directory of the project with a valid OpenAI API key.
2. Place the CV document in the folder `x.txt`.
2. Place the Job description in the folder `y.txt`.
3. The parsed information will be generated and stored in the output folder `optimized_cv.txt`.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.


