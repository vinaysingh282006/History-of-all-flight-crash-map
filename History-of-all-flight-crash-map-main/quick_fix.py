with open('streamlit_app.py', 'r', encoding='utf-8') as f:
    content = f.read()

print("Original file length:", len(content))

# Step 1: Fix tab definition
content = content.replace('# FIVE TABS', '# SIX TABS')
content = content.replace('tab1, tab2, tab3, tab4, tab5 = st.tabs([', 'tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([')

# Step 2: Add 6th tab name
old_tabs = '''        "💰 **COST BREAKDOWN**"
    ])'''
new_tabs = '''        "💰 **COST BREAKDOWN**",
        "🌦️ **WEATHER CORRELATION**"
    ])'''
content = content.replace(old_tabs, new_tabs)

print("Steps 1 & 2 complete: Tab definition updated")

# Step 3: Add tab6 content before if __name__
tab6_content = '''
    # Tab 6: Weather Correlation Dashboard
    with tab6:
        st.markdown('<h2 class="tab-header">🌦️ Weather Correlation Dashboard</h2>', unsafe_allow_html=True)
        st.markdown("""
        ### 📊 Understanding Weather's Impact on Aviation Safety
        
        This dashboard analyzes weather correlations with aviation crashes.
        """)
        
        with st.spinner('🌤️ Analyzing weather patterns...'):
            weather_df = enrich_crash_data_with_weather(df)
        
        st.markdown("### 📈 Key Weather Statistics")
        col1, col2, col3, col4 = st.columns(4)
        
        weather_related_count = weather_df['has_weather_mention'].sum()
        weather_percentage = (weather_related_count / len(weather_df)) * 100
        fog_crashes = weather_df['fog'].sum()
        storm_crashes = weather_df['storm'].sum()
        
        with col1:
            st.metric("Weather-Related", f"{weather_related_count:,}")
        with col2:
            st.metric("Impact Rate", f"{weather_percentage:.1f}%")
        with col3:
            st.metric("Fog Crashes", f"{fog_crashes:,}")
        with col4:
            st.metric("Storm Crashes", f"{storm_crashes:,}")
        
        st.markdown("### 🌍 Weather Impact Overview")
        col1, col2 = st.columns(2)
        
        with col1:
            pie_fig = create_weather_pie_chart(weather_df)
            st.plotly_chart(pie_fig, use_container_width=True)
        
        with col2:
            type_fig = create_weather_type_analysis(weather_df)
            st.plotly_chart(type_fig, use_container_width=True)
        
        st.markdown("### 🔬 Correlation Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            scatter_fig = create_weather_scatter_plot(weather_df)
            st.plotly_chart(scatter_fig, use_container_width=True)
        
        with col2:
            visibility_fig = create_visibility_wind_heatmap(weather_df)
            st.plotly_chart(visibility_fig, use_container_width=True)
        
        st.markdown("### 📅 Temporal Weather Patterns")
        col1, col2 = st.columns(2)
        
        with col1:
            monthly_fig = create_monthly_weather_pattern(weather_df)
            st.plotly_chart(monthly_fig, use_container_width=True)
        
        with col2:
            heatmap_fig = create_weather_correlation_heatmap(weather_df)
            st.plotly_chart(heatmap_fig, use_container_width=True)
        
        st.markdown("### 📈 Long-Term Weather Trends")
        decade_fig = create_decade_weather_trend(weather_df)
        st.plotly_chart(decade_fig, use_container_width=True)

'''

content = content.replace('\nif __name__ == "__main__":', tab6_content + '\nif __name__ == "__main__":')

with open('streamlit_app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Step 3 complete: Tab6 content added")
print("New file length:", len(content))
print("\n" + "="*60)
print("SUCCESS! Weather Correlation tab has been added!")
print("="*60)
print("\nRestart Streamlit to see the changes:")
print("  streamlit run streamlit_app.py")
print("\nYou should now see 6 tabs with Weather Correlation as the 6th tab!")

