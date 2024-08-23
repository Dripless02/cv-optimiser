from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=API_KEY)
def generate_optimized_cv(cv_text, job_description):
    prompt = (
        f"Given the following resume:\n\n{cv_text}\n\n"
        f"And the following job description:\n\n{job_description}\n\n"
        f"Please create an optimized resume that aligns with the job description. "
        f"Include necessary keywords and rephrase where necessary to match the qualifications."
        f" Do not include false information, exaggerate qualifications, or overly increase the length of the CV."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in HR and resume optimization."},
            {"role": "user", "content": prompt},
        ],

    )

    optimized_cv = response.choices[0].message.content

    return optimized_cv

def main():
    cv_file_path = input("Enter the path to your CV file: ")
    job_file_path = input("Enter the path to the job description file: ")

    with open(cv_file_path, 'r', encoding = "utf8") as cv_file:
        cv_text = cv_file.read()

    with open(job_file_path, 'r', encoding = "utf8") as job_file:
        job_description = job_file.read()

    optimized_cv = str(generate_optimized_cv(cv_text, job_description))

    output_file_path = 'optimized_cv.txt'
    with open(output_file_path, 'w') as f:
        f.write(optimized_cv)

    print(f"Optimized CV saved to {output_file_path}")

if __name__ == '__main__':
    main()