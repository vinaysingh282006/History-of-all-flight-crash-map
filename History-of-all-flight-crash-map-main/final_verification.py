#!/usr/bin/env python3
"""Final verification that all weather components are present"""

with open('streamlit_app.py', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.split('\n')

print("="*60)
print("FINAL VERIFICATION - Weather Correlation Feature")
print("="*60)
print()

# Check file stats
print(f"File Statistics:")
print(f"  Total lines: {len(lines)}")
print(f"  File size: {len(content):,} bytes")
print()

# Check backend functions
backend_functions = [
    'fetch_weather_data_sample',
    'enrich_crash_data_with_weather',
    'create_weather_correlation_heatmap',
    'create_weather_scatter_plot',
    'create_weather_pie_chart',
    'create_weather_type_analysis',
    'create_visibility_wind_heatmap',
    'create_monthly_weather_pattern',
    'create_decade_weather_trend'
]

print("Backend Functions (9 required):")
missing_functions = []
for func in backend_functions:
    exists = f'def {func}(' in content
    status = "[OK]" if exists else "[MISSING]"
    print(f"  {status} {func}()")
    if not exists:
        missing_functions.append(func)

if missing_functions:
    print(f"\nERROR: {len(missing_functions)} functions missing!")
    exit(1)

print()

# Check frontend components
print("Frontend Components:")
checks = {
    "SIX TABS comment": "# SIX TABS" in content,
    "tab6 in definition": "tab6 = st.tabs" in content,
    "Weather tab name": "WEATHER CORRELATION" in content,
    "with tab6 block": "with tab6:" in content,
    "enrich_crash_data call": "enrich_crash_data_with_weather(df)" in content,
    "create_weather_pie_chart call": "create_weather_pie_chart(weather_df)" in content,
}

all_checks_passed = True
for check_name, result in checks.items():
    status = "[OK]" if result else "[MISSING]"
    print(f"  {status} {check_name}")
    if not result:
        all_checks_passed = False

print()

if all_checks_passed and not missing_functions:
    print("="*60)
    print("[SUCCESS] All components verified!")
    print("="*60)
    print()
    print("The Weather Correlation feature is fully installed!")
    print()
    print("Next steps:")
    print("  1. Restart Streamlit: streamlit run streamlit_app.py")
    print("  2. Refresh browser: Ctrl+Shift+R")
    print("  3. Click on the 6th tab: Weather Correlation")
    print()
    print("The error should now be resolved!")
else:
    print("="*60)
    print("[ERROR] Some components are missing!")
    print("="*60)
    exit(1)

