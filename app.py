import streamlit as st
import subprocess, os, re
from datetime import datetime

st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖", layout="wide")
st.title("🤖 AI Code Reviewer")
st.write("Analyze Python code using Flake8, Black and Radon.")

code = st.text_area("Paste Python code", height=250)
uploaded = st.file_uploader("Or upload a .py file", type=["py"])
analyze = st.button("Analyze Code")

code_text=""
if uploaded:
    code_text=uploaded.read().decode("utf-8")
elif code.strip():
    code_text=code

if analyze:
    if not code_text:
        st.warning("Please enter or upload Python code.")
        st.stop()

    os.makedirs("temp", exist_ok=True)
    temp_file=os.path.join("temp","temp_code.py")
    with open(temp_file,"w",encoding="utf-8") as f:
        f.write(code_text)

    st.subheader("Original Code")
    st.code(code_text,language="python")

    flake=subprocess.run(["python","-m","flake8",temp_file],capture_output=True,text=True)
    flake_out=flake.stdout.strip()
    st.subheader("Flake8 Analysis")
    if flake_out:
        st.error("Style Issues Found")
        st.code(flake_out)
    else:
        st.success("No style issues found.")

    subprocess.run(["python","-m","black",temp_file],capture_output=True,text=True)

    with open(temp_file,"r",encoding="utf-8") as f:
        formatted=f.read()

    st.subheader("Formatted Code")
    st.code(formatted,language="python")

    radon=subprocess.run(["python","-m","radon","cc",temp_file],capture_output=True,text=True)
    st.subheader("Radon Complexity")
    st.code(radon.stdout if radon.stdout else "No report.")

    flake_count=0 if not flake_out else len(flake_out.splitlines())
    m=re.search(r"\b([A-F])\b",radon.stdout)
    grade=m.group(1) if m else "N/A"

    st.subheader("Summary")
    st.write(f"Flake8 Issues: {flake_count}")
    st.write(f"Complexity Grade: {grade}")

    report=f"""AI CODE REVIEW REPORT

Date: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
Flake8 Issues: {flake_count}
Complexity Grade: {grade}

Original Code
{code_text}

Formatted Code
{formatted}

Flake8 Output
{flake.stdout}

Radon Output
{radon.stdout}
"""

    os.makedirs("reports",exist_ok=True)
    filename=os.path.join("reports",f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(filename,"w",encoding="utf-8") as f:
        f.write(report)

    st.success(f"Report saved to {filename}")

    st.download_button("📄 Download Report",report,os.path.basename(filename),"text/plain")
