with open('streamlit_app.py', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.split('\n')

print(f"Total lines: {len(lines)}")
print(f"File size: {len(content)} bytes")
print()
print("Checking for weather tab components:")
print(f"  - 'tab6' in definition: {'tab6 = st.tabs' in content}")
print(f"  - 'with tab6:' block: {'with tab6:' in content}")
print(f"  - Weather tab name: {'WEATHER CORRELATION' in content}")
print(f"  - SIX TABS comment: {'SIX TABS' in content}")
print(f"  - Weather dashboard header: {'Weather Correlation Dashboard' in content}")
print()

# Count tabs
with_tabs = [i+1 for i, line in enumerate(lines) if line.strip().startswith('with tab') and ':' in line]
print(f"Number of 'with tab' blocks found: {len(with_tabs)}")
print(f"Tab block lines: {with_tabs}")
print()

if len(with_tabs) == 6:
    print("✓ SUCCESS: All 6 tabs are present!")
else:
    print(f"⚠ WARNING: Found {len(with_tabs)} tabs instead of 6")

