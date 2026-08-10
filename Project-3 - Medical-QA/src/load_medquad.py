# ==========================================================
# Project: Medical Q&A Chatbot
# File: load_medquad.py
# Author: Vijayalakshmi Narayanan
# Description:
# Loads the processed MedQuAD dataset for deployment.
# Falls back to the original XML dataset on the local machine.
# ==========================================================

import os
import json
import gzip
import xml.etree.ElementTree as ET


def load_medquad():

    current_dir = os.path.dirname(os.path.abspath(__file__))

    # ------------------------------------------------------
    # First choice: processed dataset for deployment
    # ------------------------------------------------------

    processed_path = os.path.join(
        current_dir,
        "..",
        "data",
        "medquad_processed.json.gz"
    )

    processed_path = os.path.abspath(processed_path)

    if os.path.exists(processed_path):

        print("\nLoading processed MedQuAD dataset...\n")

        with gzip.open(
            processed_path,
            "rt",
            encoding="utf-8"
        ) as file:

            medical_data = json.load(file)

        print("\n===================================")
        print(
            f"Total Q&A pairs loaded: {len(medical_data)}"
        )
        print("===================================\n")

        return medical_data

    # ------------------------------------------------------
    # Fallback: original local MedQuAD XML dataset
    # ------------------------------------------------------

    dataset_path = r"C:\AI_Datasets\MedQuAD\MedQuAD-master"

    if not os.path.exists(dataset_path):

        raise FileNotFoundError(
            "MedQuAD dataset was not found. "
            "Expected either the processed dataset at "
            f"'{processed_path}' or the local dataset at "
            f"'{dataset_path}'."
        )

    medical_data = []

    print("\nLoading MedQuAD Dataset from XML files...\n")

    for folder in os.listdir(dataset_path):

        folder_path = os.path.join(
            dataset_path,
            folder
        )

        if not os.path.isdir(folder_path):
            continue

        print(f"Reading Folder: {folder}")

        for file in os.listdir(folder_path):

            if not file.endswith(".xml"):
                continue

            xml_file = os.path.join(
                folder_path,
                file
            )

            try:

                tree = ET.parse(xml_file)
                root = tree.getroot()

                qa_pairs = root.find("QAPairs")

                if qa_pairs is None:
                    continue

                for qa in qa_pairs.findall("QAPair"):

                    question = qa.findtext("Question")
                    answer = qa.findtext("Answer")

                    if question and answer:

                        medical_data.append(
                            {
                                "question": question.strip(),
                                "answer": answer.strip(),
                                "source": folder
                            }
                        )

            except Exception as error:

                print(
                    f"Error reading {file}: {error}"
                )

    print("\n===================================")
    print(
        f"Total Q&A pairs loaded: {len(medical_data)}"
    )
    print("===================================\n")

    return medical_data


# ----------------------------------------------------------
# Test the loader when this file is run directly
# ----------------------------------------------------------

if __name__ == "__main__":

    data = load_medquad()

    print("\nFirst 5 Question-Answer Pairs:\n")

    for item in data[:5]:

        print("Source :", item["source"])
        print("Question:", item["question"])
        print(
            "Answer:",
            item["answer"][:120],
            "..."
        )
        print("-" * 70)
