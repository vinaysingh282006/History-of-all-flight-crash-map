with open('streamlit_app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}\n")

# Find st.tabs
for i, line in enumerate(lines):
    if 'st.tabs' in line:
        print(f"=== Found st.tabs at line {i+1} (offset {i}) ===")
        start = max(0, i-2)
        end = min(len(lines), i+8)
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"{marker} {j+1:4d}: {lines[j].rstrip()}")
        print()

# Find where tab content starts
for i, line in enumerate(lines):
    if line.strip().startswith('with tab'):
        print(f"Line {i+1}: {line.strip()}")

# Find main function
for i, line in enumerate(lines):
    if 'def main()' in line:
        print(f"\n=== Main function at line {i+1} ===")
        break

# Find if __name__
for i, line in enumerate(lines):
    if '__name__' in line:
        print(f"=== Program entry at line {i+1} ===")
        break

