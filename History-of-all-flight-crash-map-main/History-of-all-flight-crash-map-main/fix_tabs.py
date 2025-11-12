#!/usr/bin/env python3
"""
Script to add tab6 (Weather Correlation) to streamlit_app.py
"""

with open('streamlit_app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Replace "FIVE TABS" with "SIX TABS" and add tab6 to the definition
old_tabs_def = '''    # FIVE TABS
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🌍 **3D GLOBE**", 
        "🏁 **RACING STICKS**", 
        "🎯 **CRASH REASONS**", 
        "💀 **FATALITY TRENDS**",
        "💰 **COST BREAKDOWN**"
    ])'''

new_tabs_def = '''    # SIX TABS
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🌍 **3D GLOBE**", 
        "🏁 **RACING STICKS**", 
        "🎯 **CRASH REASONS**", 
        "💀 **FATALITY TRENDS**",
        "💰 **COST BREAKDOWN**",
        "🌦️ **WEATHER CORRELATION**"
    ])'''

if old_tabs_def in content:
    content = content.replace(old_tabs_def, new_tabs_def)
    print("✓ Step 1: Updated tab definition to include tab6")
else:
    print("✗ Step 1: Could not find the old tabs definition")
    print("Searching for variations...")
    if "tab1, tab2, tab3, tab4, tab5 = st.tabs" in content:
        print("  Found st.tabs with 5 tabs, but exact match failed. Manual edit needed.")
    exit(1)

# Step 2: Add tab6 content before "if __name__"
tab6_content = '''    
    # Tab 6: Weather Correlation Dashboard
    with tab6:
        st.markdown('<h2 class="tab-header">🌦️ Weather Correlation Dashboard</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        ### 📊 Understanding Weather's Impact on Aviation Safety
        
        This dashboard analyzes the correlation between weather conditions and aviation crashes throughout history.
        By examining crash summaries for weather-related keywords, we can identify patterns and understand how
        environmental factors have influenced aviation accidents.
        
        **Analysis Methods:**
        - **Keyword Analysis**: Extracting weather conditions from crash summaries
        - **Pattern Recognition**: Identifying seasonal and temporal trends
        - **Correlation Studies**: Linking weather severity with crash outcomes
        - **Visual Analytics**: Heatmaps, scatter plots, and trend analysis
        """)
        
        # Enrich data with weather information
        with st.spinner('🌤️ Analyzing weather patterns in crash data...'):
            weather_df = enrich_crash_data_with_weather(df)
        
        st.markdown("---")
        
        # Key Weather Metrics
        st.markdown("### 📈 Key Weather Statistics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        weather_related_count = weather_df['has_weather_mention'].sum()
        weather_percentage = (weather_related_count / len(weather_df)) * 100
        fog_crashes = weather_df['fog'].sum()
        storm_crashes = weather_df['storm'].sum()
        
        with col1:
            st.markdown(f\'\'\'
            <div class="metric-card">
                <div class="metric-number">{weather_related_count:,}</div>
                <div class="metric-label">🌩️ Weather-Related Crashes</div>
            </div>
            \'\'\', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f\'\'\'
            <div class="metric-card">
                <div class="metric-number">{weather_percentage:.1f}%</div>
                <div class="metric-label">📊 Weather Impact Rate</div>
            </div>
            \'\'\', unsafe_allow_html=True)
        
        with col3:
            st.markdown(f\'\'\'
            <div class="metric-card">
                <div class="metric-number">{fog_crashes:,}</div>
                <div class="metric-label">🌫️ Fog-Related Crashes</div>
            </div>
            \'\'\', unsafe_allow_html=True)
        
        with col4:
            st.markdown(f\'\'\'
            <div class="metric-card">
                <div class="metric-number">{storm_crashes:,}</div>
                <div class="metric-label">⛈️ Storm-Related Crashes</div>
            </div>
            \'\'\', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Weather Overview Section
        st.markdown("### 🌍 Weather Impact Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Weather vs Non-Weather Crashes")
            pie_fig = create_weather_pie_chart(weather_df)
            st.plotly_chart(pie_fig, use_container_width=True)
        
        with col2:
            st.markdown("#### Weather Condition Types")
            type_fig = create_weather_type_analysis(weather_df)
            st.plotly_chart(type_fig, use_container_width=True)
        
        st.markdown("---")
        
        # Correlation Analysis Section
        st.markdown("### 🔬 Correlation Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Weather Severity vs Fatalities")
            scatter_fig = create_weather_scatter_plot(weather_df)
            st.plotly_chart(scatter_fig, use_container_width=True)
            
            # Calculate correlation
            correlation = weather_df[['weather_severity', 'Fatalities']].corr().iloc[0, 1]
            st.info(f"📊 **Correlation Coefficient**: {correlation:.3f} - " + 
                   ("Strong positive correlation" if abs(correlation) > 0.7 else 
                    "Moderate correlation" if abs(correlation) > 0.4 else 
                    "Weak correlation"))
        
        with col2:
            st.markdown("#### Visibility vs Wind Speed Impact")
            visibility_fig = create_visibility_wind_heatmap(weather_df)
            st.plotly_chart(visibility_fig, use_container_width=True)
            
            st.info("🌫️ **Key Insight**: Low visibility combined with strong winds creates " +
                   "the most hazardous conditions for aviation, as shown in the darker regions of the heatmap.")
        
        st.markdown("---")
        
        # Temporal Analysis Section
        st.markdown("### 📅 Temporal Weather Patterns")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Seasonal Weather Crash Patterns")
            monthly_fig = create_monthly_weather_pattern(weather_df)
            st.plotly_chart(monthly_fig, use_container_width=True)
        
        with col2:
            st.markdown("#### Weather Conditions Heatmap")
            heatmap_fig = create_weather_correlation_heatmap(weather_df)
            st.plotly_chart(heatmap_fig, use_container_width=True)
        
        st.markdown("---")
        
        # Long-term Trends
        st.markdown("### 📈 Long-Term Weather Trends")
        
        decade_fig = create_decade_weather_trend(weather_df)
        st.plotly_chart(decade_fig, use_container_width=True)
        
        st.markdown("---")
        
        # Insights and Recommendations
        st.markdown("### 💡 Key Insights & Recommendations")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="crash-details">
                <h4>🌫️ Visibility Concerns</h4>
                <p>Low visibility conditions (fog, heavy rain, snow) are consistently associated 
                with higher crash rates. Modern instrument landing systems (ILS) have significantly 
                improved safety in these conditions.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="crash-details">
                <h4>💨 Wind Impact</h4>
                <p>Strong winds and wind shear remain critical factors in aviation accidents. 
                Advanced weather radar and wind shear detection systems are essential for 
                modern aircraft safety.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="crash-details">
                <h4>⛈️ Storm Avoidance</h4>
                <p>Thunderstorms and severe weather systems can be avoided with proper planning 
                and real-time weather monitoring. Modern meteorological services provide crucial 
                support for flight safety.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Data Source Information
        st.markdown("---")
        st.markdown("""
        ### 📚 Data Analysis Methodology
        
        **Weather Detection**: Weather conditions are identified by analyzing crash summary descriptions 
        for specific keywords related to meteorological phenomena (fog, storm, wind, ice, rain, snow, etc.).
        
        **Severity Index**: A weather severity index (0-10) is calculated based on the presence and 
        intensity of weather-related keywords in crash descriptions.
        
        **Historical Context**: This analysis covers over 100 years of aviation history (1908-2009), 
        providing valuable insights into how weather preparedness and technology have evolved.
        
        **Note**: For production deployments, integration with real weather APIs (Open-Meteo, NOAA) 
        would provide actual historical weather data for enhanced accuracy.
        """)

'''

# Find where to insert tab6 content (before "if __name__")
if_name_marker = '\nif __name__ == "__main__":\n'

if if_name_marker in content:
    # Insert tab6 content before the if __name__ block
    content = content.replace(if_name_marker, tab6_content + if_name_marker)
    print("✓ Step 2: Added tab6 content before 'if __name__'")
else:
    print("✗ Step 2: Could not find 'if __name__' marker")
    exit(1)

# Write the updated content
with open('streamlit_app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n" + "="*60)
print("✓ SUCCESS! streamlit_app.py has been updated!")
print("="*60)
print("\n📊 Changes made:")
print("  1. Updated st.tabs() definition to include tab6")
print("  2. Added Weather Correlation tab name")
print("  3. Added complete tab6 content (187 lines)")
print("\n🚀 Next steps:")
print("  1. Restart Streamlit: streamlit run streamlit_app.py")
print("  2. You should now see 6 tabs including Weather Correlation")
print("  3. Click on the 6th tab to view the weather dashboard")
print("="*60)

