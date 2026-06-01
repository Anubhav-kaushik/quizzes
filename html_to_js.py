import os
import re
import json
from bs4 import BeautifulSoup

# Global schema matching the requested pattern to embed at the top of data.js
EXAM_SCHEMA = {
    "title": "string",
    "exam_level": {
        "Tier-I": {
            "sections": {
                "General Intelligence and Reasoning": {
                    "question_count": 25,
                    "marking_schema": {"correct": 2, "incorrect": -0.5, "unattempted": 0},
                    "time_allotted": 15
                },
                "General Awareness": {
                    "question_count": 25,
                    "marking_schema": {"correct": 2, "incorrect": -0.5, "unattempted": 0},
                    "time_allotted": 15
                },
                "Quantitative Aptitude": {
                    "question_count": 25,
                    "marking_schema": {"correct": 2, "incorrect": -0.5, "unattempted": 0},
                    "time_allotted": 15
                },
                "English Language": {
                    "question_count": 25,
                    "marking_schema": {"correct": 2, "incorrect": -0.5, "unattempted": 0},
                    "time_allotted": 15
                }
            }
        },
        "Tier-II": {
            "sections": {
                "General Intelligence and Reasoning": {
                    "question_count": 30,
                    "marking_schema": {"correct": 3, "incorrect": -1, "unattempted": 0},
                    "time_allotted": 30
                },
                "Quantitative Aptitude": {
                    "question_count": 30,
                    "marking_schema": {"correct": 3, "incorrect": -1, "unattempted": 0},
                    "time_allotted": 30
                },
                "English Language": {
                    "question_count": 45,
                    "marking_schema": {"correct": 3, "incorrect": -1, "unattempted": 0},
                    "time_allotted": 30
                },
                "General Awareness": {
                    "question_count": 25,
                    "marking_schema": {"correct": 3, "incorrect": -1, "unattempted": 0},
                    "time_allotted": 30
                },
                "Computer Knowledge": {
                    "question_count": 15,
                    "marking_schema": {"correct": 3, "incorrect": -1, "unattempted": 0},
                    "time_allotted": 15
                }
            }
        }
    }
}

def extract_linked_files_from_index(index_path):
    linked_files = []
    if not os.path.exists(index_path):
        print(f"Warning: {index_path} not found.")
        return linked_files

    with open(index_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    buttons = soup.find_all('button', onclick=True)
    for btn in buttons:
        match = re.search(r"hyperlinkTo\(['\"]([^'\"]+)['\"]\)", btn['onclick'])
        if match:
            linked_files.append(match.group(1))
            
    return list(set(linked_files))

def clean_normalize_and_update_images(soup_element, html_file_path):
    if not soup_element:
        return ""
    
    element_copy = BeautifulSoup(str(soup_element), "html.parser")
    file_base_without_ext, _ = os.path.splitext(html_file_path)
    asset_folder_path = f"{file_base_without_ext}_files".replace(os.sep, '/')

    for img in element_copy.find_all("img"):
        src_attr = img.get("src", "")
        src_lower = src_attr.lower()
        
        if "tick.png" in src_lower or "cross.png" in src_lower:
            img.decompose()
            continue
            
        if src_attr and not src_attr.startswith(('http://', 'https://', 'data:')):
            clean_filename = os.path.basename(src_attr)
            combined_path = f"{asset_folder_path}/{clean_filename}"
            img['src'] = combined_path

    inner_html = element_copy.decode_contents().strip()
    inner_html = re.sub(r'^\s*\d+\.\s*(&nbsp;)?\s*', '', inner_html)
    normalized_html = re.sub(r'\s+', ' ', inner_html).strip()
    return normalized_html

def parse_html_question_paper(file_path, original_raw_path):
    if not os.path.exists(file_path):
        return None

    normalized_file_path = original_raw_path.replace(os.sep, '/')
    
    # Auto-detect Tier level from path string
    exam_level = "Tier-I"
    if "tier-2" in normalized_file_path.lower() or "tier2" in normalized_file_path.lower():
        exam_level = "Tier-II"

    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    exam_title = "Combined Graduate Level Examination"
    exam_date = ""
    exam_sch_time = ""

    main_info = soup.find("div", class_="main-info-pnl")
    if main_info:
        strong_title = main_info.find("strong")
        if strong_title:
            exam_title = strong_title.text.strip()
            
        # Extract exam date and time strings safely from info table labels
        for tr in main_info.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) == 2:
                key_text = tds[0].text.strip().lower()
                val_text = tds[1].text.strip()
                if "exam date" in key_text:
                    exam_date = val_text
                elif "exam time" in key_text:
                    exam_sch_time = val_text

    questions_list = []
    sections = soup.find_all("div", class_="section-cntnr")

    for idx_sec, section in enumerate(sections):
        section_lbl = section.find("div", class_="section-lbl")
        section_name = f"Section {idx_sec + 1}"
        if section_lbl:
            bold_span = section_lbl.find("span", class_="bold")
            if bold_span:
                section_name = bold_span.text.replace("Section :", "").replace("\xa0", " ").strip()

        question_panels = section.find_all("div", class_="question-pnl")
        for panel in question_panels:
            row_tbl = panel.find("table", class_="questionRowTbl")
            if not row_tbl:
                continue

            q_text_cell = row_tbl.find("td", class_="bold", style=lambda s: s and "text-align: left" in s) or \
                          row_tbl.find("td", style=lambda s: s and "text-align: left" in s)

            if not q_text_cell:
                continue

            question_html = clean_normalize_and_update_images(q_text_cell, normalized_file_path)
            
            q_id = ""
            menu_tbl = panel.find("table", class_="menu-tbl")
            if menu_tbl:
                for tr in menu_tbl.find_all("tr"):
                    tds = tr.find_all("td")
                    if len(tds) == 2 and "Question ID" in tds[0].text:
                        q_id = tds[1].text.strip()

            if not q_id:
                q_id = str(len(questions_list) + 1)

            options_html_list = []
            correct_answer_html = ""

            ans_cells = row_tbl.find_all("td", class_=["wrngAns", "rightAns"])
            for cell in ans_cells:
                cleaned_option_html = clean_normalize_and_update_images(cell, normalized_file_path)
                options_html_list.append(cleaned_option_html)

                if "rightAns" in cell.get("class", []):
                    correct_answer_html = cleaned_option_html

            questions_list.append({
                "id": q_id,
                "section": section_name,
                "category": [section_name],
                "question": question_html,
                "options": options_html_list,
                "correct_answer": correct_answer_html
            })

    return {
        "title": exam_title,
        "exam_level": exam_level,
        "exam_date": exam_date,
        "exam_sch_time": exam_sch_time,
        "questions": questions_list
    }

def build_exam_database():
    index_file = "index.html"
    linked_paths = extract_linked_files_from_index(index_file)
    database = {}

    if not linked_paths:
        print("No paths discovered in index.html. Checking fallback root entries...")
        linked_paths = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

    for raw_path in linked_paths:
        local_path = raw_path.replace('/', os.sep)
        actual_path = local_path if os.path.exists(local_path) else os.path.basename(local_path)
        
        if os.path.exists(actual_path):
            # Compute file key identifier format slug (e.g., '2023-07-14-900-1000-E')
            slug = os.path.basename(actual_path).replace('.html', '')
            print(f"Scraping file payload: {actual_path}...")
            parsed_paper = parse_html_question_paper(actual_path, raw_path)
            if parsed_paper and parsed_paper["questions"]:
                database[slug] = parsed_paper
        else:
            print(f"Skipping: File path not found -> {actual_path}")

    output_js_file = "data.js"
    with open(output_js_file, 'w', encoding='utf-8') as out:
        out.write("const EXAM_SCHEMA = ")
        json.dump(EXAM_SCHEMA, out, indent=4, ensure_ascii=False)
        out.write(";\n\n")
        out.write("const EXAM_DATABASE = ")
        json.dump(database, out, indent=4, ensure_ascii=False)
        out.write(";\n")

    print(f"\nGenerated database array successfully inside: '{output_js_file}'")

if __name__ == "__main__":
    build_exam_database()