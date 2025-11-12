with open('streamlit_app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
print(f"Total lines: {len(lines)}")
print("\nSearching for key locations...")

for i, line in enumerate(lines, 1):
    if 'def main(' in line:
        print(f"Line {i}: {line.strip()}")
    elif 'with tab' in line:
        print(f"Line {i}: {line.strip()}")
    elif 'st.tabs(' in line:
        print(f"Line {i}: {line.strip()}")
        # Print next 10 lines
        for j in range(i, min(i+10, len(lines))):
            print(f"Line {j+1}: {lines[j].rstrip()}")
        break

