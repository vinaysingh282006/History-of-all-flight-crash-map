#!/usr/bin/env python3
# Script to add Weather Correlation tab to streamlit_app.py

print("Reading streamlit_app.py...")
with open('streamlit_app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Current file has {len(lines)} lines")

# Find the line with tab definitions
tab_def_line = None
for i, line in enumerate(lines):
    if 'tab1, tab2, tab3, tab4, tab5 = st.tabs' in line:
        tab_def_line = i
        break

if tab_def_line is None:
    print("ERROR: Could not find tab definition line!")
    exit(1)

print(f"Found tab definition at line {tab_def_line + 1}")

# Replace line 746 (# FIVE TABS) with # SIX TABS
if tab_def_line > 0 and 'FIVE TABS' in lines[tab_def_line - 1]:
    lines[tab_def_line - 1] = lines[tab_def_line - 1].replace('FIVE TABS', 'SIX TABS')
    print("Updated comment to SIX TABS")

# Replace the tab definition line to include tab6
lines[tab_def_line] = lines[tab_def_line].replace(
    'tab1, tab2, tab3, tab4, tab5 = st.tabs',
    'tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs'
)
print("Updated tab definition to include tab6")

# Find the line with the closing bracket for st.tabs
closing_bracket_line = None
for i in range(tab_def_line + 1, min(tab_def_line + 15, len(lines))):
    if ']' in lines[i] and ')' in lines[i]:
        closing_bracket_line = i
        break

if closing_bracket_line is None:
    print("ERROR: Could not find closing bracket for st.tabs!")
    exit(1)

# Insert the weather tab name before the closing bracket
weather_tab_line = '        "🌦️ **WEATHER CORRELATION**"\\n'
lines[closing_bracket_line] = lines[closing_bracket_line].replace(
    '    ])',
    ',\\n' + weather_tab_line + '    ])'
)
print("Added Weather Correlation tab name")

# Find where to insert tab6 content (before if __name__)
if_name_line = None
for i, line in enumerate(lines):
    if 'if __name__ == "__main__":' in line:
        if_name_line = i
        break

if if_name_line is None:
    print("ERROR: Could not find 'if __name__' line!")
    exit(1)

print(f"Found 'if __name__' at line {if_name_line + 1}")

# Create tab6 content
tab6_lines = [
    '\\n',
    '    # Tab 6: Weather Correlation Dashboard\\n',
    '    with tab6:\\n',
    '        st.markdown(\\'<h2 class="tab-header">🌦️ Weather Correlation Dashboard</h2>\\', unsafe_allow_html=True)\\n',
    '        \\n',
    '        st.markdown("""\\n',
    '        ### 📊 Understanding Weather\\'s Impact on Aviation Safety\\n',
    '        \\n',
    '        This dashboard analyzes the correlation between weather conditions and aviation crashes throughout history.\\n',
    '        By examining crash summaries for weather-related keywords, we can identify patterns and understand how\\n',
    '        environmental factors have influenced aviation accidents.\\n',
    '        \\n',
    '        **Analysis Methods:**\\n',
    '        - **Keyword Analysis**: Extracting weather conditions from crash summaries\\n',
    '        - **Pattern Recognition**: Identifying seasonal and temporal trends\\n',
    '        - **Correlation Studies**: Linking weather severity with crash outcomes\\n',
    '        - **Visual Analytics**: Heatmaps, scatter plots, and trend analysis\\n',
    '        """)\\n',
    '        \\n',
    '        # Enrich data with weather information\\n',
    '        with st.spinner(\\'🌤️ Analyzing weather patterns in crash data...\\'):\\n',
    '            weather_df = enrich_crash_data_with_weather(df)\\n',
    '        \\n',
    '        st.markdown("---")\\n',
    '        \\n',
    '        # Key Weather Metrics\\n',
    '        st.markdown("### 📈 Key Weather Statistics")\\n',
    '        \\n',
    '        col1, col2, col3, col4 = st.columns(4)\\n',
    '        \\n',
    '        weather_related_count = weather_df[\\'has_weather_mention\\'].sum()\\n',
    '        weather_percentage = (weather_related_count / len(weather_df)) * 100\\n',
    '        fog_crashes = weather_df[\\'fog\\'].sum()\\n',
    '        storm_crashes = weather_df[\\'storm\\'].sum()\\n',
    '        \\n',
    '        with col1:\\n',
    '            st.markdown(f\\'\\'\\'\\n',
    '            <div class="metric-card">\\n',
    '                <div class="metric-number">{weather_related_count:,}</div>\\n',
    '                <div class="metric-label">🌩️ Weather-Related Crashes</div>\\n',
    '            </div>\\n',
    '            \\'\\'\\'

, unsafe_allow_html=True)\\n',
    '        \\n',
    '        with col2:\\n',
    '            st.markdown(f\\'\\'\\'\\n',
    '            <div class="metric-card">\\n',
    '                <div class="metric-number">{weather_percentage:.1f}%</div>\\n',
    '                <div class="metric-label">📊 Weather Impact Rate</div>\\n',
    '            </div>\\n',
    '            \\'\\'\\'

, unsafe_allow_html=True)\\n',
    '        \\n',
    '        with col3:\\n',
    '            st.markdown(f\\'\\'\\'\\n',
    '            <div class="metric-card">\\n',
    '                <div class="metric-number">{fog_crashes:,}</div>\\n',
    '                <div class="metric-label">🌫️ Fog-Related Crashes</div>\\n',
    '            </div>\\n',
    '            \\'\\'\\'

, unsafe_allow_html=True)\\n',
    '        \\n',
    '        with col4:\\n',
    '            st.markdown(f\\'\\'\\'\\n',
    '            <div class="metric-card">\\n',
    '                <div class="metric-number">{storm_crashes:,}</div>\\n',
    '                <div class="metric-label">⛈️ Storm-Related Crashes</div>\\n',
    '            </div>\\n',
    '            \\'\\'\\'

, unsafe_allow_html=True)\\n',
    '        \\n',
    '        st.markdown("---")\\n',
    '        st.markdown("### 🌍 Weather Impact Overview")\\n',
    '        col1, col2 = st.columns(2)\\n',
    '        with col1:\\n',
    '            st.markdown("#### Weather vs Non-Weather Crashes")\\n',
    '            pie_fig = create_weather_pie_chart(weather_df)\\n',
    '            st.plotly_chart(pie_fig, use_container_width=True)\\n',
    '        with col2:\\n',
    '            st.markdown("#### Weather Condition Types")\\n',
    '            type_fig = create_weather_type_analysis(weather_df)\\n',
    '            st.plotly_chart(type_fig, use_container_width=True)\\n',
    '        st.markdown("---")\\n',
    '        st.markdown("### 🔬 Correlation Analysis")\\n',
    '        col1, col2 = st.columns(2)\\n',
    '        with col1:\\n',
    '            st.markdown("#### Weather Severity vs Fatalities")\\n',
    '            scatter_fig = create_weather_scatter_plot(weather_df)\\n',
    '            st.plotly_chart(scatter_fig, use_container_width=True)\\n',
    '            correlation = weather_df[[\\'weather_severity\\', \\'Fatalities\\']].corr().iloc[0, 1]\\n',
    '            st.info(f"📊 **Correlation Coefficient**: {correlation:.3f}")\\n',
    '        with col2:\\n',
    '            st.markdown("#### Visibility vs Wind Speed Impact")\\n',
    '            visibility_fig = create_visibility_wind_heatmap(weather_df)\\n',
    '            st.plotly_chart(visibility_fig, use_container_width=True)\\n',
    '        st.markdown("---")\\n',
    '        st.markdown("### 📅 Temporal Weather Patterns")\\n',
    '        col1, col2 = st.columns(2)\\n',
    '        with col1:\\n',
    '            monthly_fig = create_monthly_weather_pattern(weather_df)\\n',
    '            st.plotly_chart(monthly_fig, use_container_width=True)\\n',
    '        with col2:\\n',
    '            heatmap_fig = create_weather_correlation_heatmap(weather_df)\\n',
    '            st.plotly_chart(heatmap_fig, use_container_width=True)\\n',
    '        st.markdown("### 📈 Long-Term Weather Trends")\\n',
    '        decade_fig = create_decade_weather_trend(weather_df)\\n',
    '        st.plotly_chart(decade_fig, use_container_width=True)\\n',
]

# Insert tab6 content before if __name__
lines[if_name_line:if_name_line] = tab6_lines

print(f"Inserted tab6 content ({len(tab6_lines)} lines) before 'if __name__'")

# Write the modified file
with open('streamlit_app.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

new_total = len(lines)
print(f"\\nFile updated! New total: {new_total} lines (was {len(lines) - len(tab6_lines)} lines)")
print("\\n✓ SUCCESS! The Weather Correlation tab has been added!")
print("\\nNext step: Restart your Streamlit app:")
print("  streamlit run streamlit_app.py")

