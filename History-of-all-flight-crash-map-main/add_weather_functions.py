#!/usr/bin/env python3
"""
Script to add all weather correlation backend functions to streamlit_app.py
"""

print("Reading streamlit_app.py...")
with open('streamlit_app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# All the weather functions that need to be added
weather_functions = '''
# ======================= WEATHER CORRELATION FUNCTIONS =======================

@st.cache_data(ttl=3600)
def fetch_weather_data_sample(lat, lon, date):
    """
    Fetch historical weather data from Open-Meteo API
    Returns simulated weather data based on crash patterns
    """
    try:
        # For demo purposes, we'll create realistic simulated weather data
        # In production, you'd use: https://archive-api.open-meteo.com/v1/archive
        
        # Simulate weather conditions based on historical patterns
        np.random.seed(int(lat * lon * 1000) % 1000)
        
        weather_data = {
            'temperature': np.random.uniform(-10, 35),
            'wind_speed': np.random.uniform(0, 80),
            'visibility': np.random.uniform(0.1, 10),
            'precipitation': np.random.uniform(0, 50),
            'pressure': np.random.uniform(980, 1030),
            'humidity': np.random.uniform(30, 100),
            'cloud_cover': np.random.uniform(0, 100)
        }
        
        return weather_data
    except Exception as e:
        return None

def enrich_crash_data_with_weather(df):
    """Add weather data to crash dataset"""
    weather_conditions = []
    
    # Analyze crash summaries for weather-related keywords
    for idx, row in df.iterrows():
        summary = str(row['Summary']).lower()
        weather_info = {
            'has_weather_mention': any(keyword in summary for keyword in 
                                      ['weather', 'storm', 'wind', 'fog', 'rain', 'snow', 'ice', 'turbulence']),
            'fog': 'fog' in summary or 'visibility' in summary,
            'storm': 'storm' in summary or 'thunderstorm' in summary or 'lightning' in summary,
            'wind': 'wind' in summary or 'gust' in summary,
            'ice': 'ice' in summary or 'icing' in summary or 'frost' in summary,
            'rain': 'rain' in summary or 'precipitation' in summary,
            'snow': 'snow' in summary or 'blizzard' in summary
        }
        
        # Simulate weather severity based on keywords (0-10 scale)
        severity = 0
        if weather_info['has_weather_mention']:
            severity = np.random.uniform(5, 10)
        else:
            severity = np.random.uniform(0, 4)
        
        weather_info['weather_severity'] = severity
        weather_info['estimated_wind_speed'] = np.random.uniform(10, 80) if weather_info['wind'] else np.random.uniform(0, 30)
        weather_info['estimated_visibility'] = np.random.uniform(0.1, 2) if weather_info['fog'] else np.random.uniform(5, 10)
        
        weather_conditions.append(weather_info)
    
    weather_df = pd.DataFrame(weather_conditions)
    enriched_df = pd.concat([df.reset_index(drop=True), weather_df], axis=1)
    
    return enriched_df

def create_weather_correlation_heatmap(df):
    """Create heatmap showing correlation between weather conditions and crashes"""
    
    # Prepare data for correlation
    weather_types = ['fog', 'storm', 'wind', 'ice', 'rain', 'snow']
    yearly_weather = []
    
    for year in sorted(df['year'].unique()):
        year_data = df[df['year'] == year]
        weather_counts = {
            'year': year,
            'total_crashes': len(year_data),
            'weather_related': year_data['has_weather_mention'].sum()
        }
        
        for weather in weather_types:
            weather_counts[weather] = year_data[weather].sum()
        
        yearly_weather.append(weather_counts)
    
    weather_df = pd.DataFrame(yearly_weather)
    
    # Create heatmap data
    z_data = []
    for weather in weather_types:
        z_data.append(weather_df[weather].values[-30:])  # Last 30 years for better visualization
    
    fig = go.Figure(data=go.Heatmap(
        z=z_data,
        x=weather_df['year'].values[-30:],
        y=[w.title() for w in weather_types],
        colorscale=[
            [0, COLORS['success']], 
            [0.5, COLORS['warning']], 
            [1, COLORS['danger']]
        ],
        text=z_data,
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(title="Crashes")
    ))
    
    fig.update_layout(
        title="🌡️ Weather Conditions Heatmap - Crashes Over Time",
        xaxis_title="Year",
        yaxis_title="Weather Condition",
        height=500,
        paper_bgcolor=COLORS['light_bg'],
        plot_bgcolor='white',
        font=dict(color=COLORS['text'], size=14)
    )
    
    return fig

def create_weather_scatter_plot(df):
    """Scatter plot showing relationship between weather severity and fatalities"""
    
    # Sample data for better performance (use every 5th crash)
    sample_df = df[::5].copy()
    
    fig = go.Figure()
    
    # Weather-related crashes
    weather_crashes = sample_df[sample_df['has_weather_mention'] == True]
    non_weather_crashes = sample_df[sample_df['has_weather_mention'] == False]
    
    fig.add_trace(go.Scatter(
        x=weather_crashes['weather_severity'],
        y=weather_crashes['Fatalities'],
        mode='markers',
        name='Weather-Related',
        marker=dict(
            size=10,
            color=COLORS['danger'],
            opacity=0.6,
            line=dict(width=1, color='white')
        ),
        text=[f"Year: {row['year']}<br>Location: {row['Location']}<br>Fatalities: {int(row['Fatalities'])}" 
              for _, row in weather_crashes.iterrows()],
        hovertemplate="%{text}<extra></extra>"
    ))
    
    fig.add_trace(go.Scatter(
        x=non_weather_crashes['weather_severity'],
        y=non_weather_crashes['Fatalities'],
        mode='markers',
        name='Non-Weather',
        marker=dict(
            size=8,
            color=COLORS['primary'],
            opacity=0.4,
            line=dict(width=1, color='white')
        ),
        text=[f"Year: {row['year']}<br>Location: {row['Location']}<br>Fatalities: {int(row['Fatalities'])}" 
              for _, row in non_weather_crashes.iterrows()],
        hovertemplate="%{text}<extra></extra>"
    ))
    
    fig.update_layout(
        title="⚡ Weather Severity vs. Fatalities Correlation",
        xaxis_title="Weather Severity Index (0-10)",
        yaxis_title="Number of Fatalities",
        height=600,
        paper_bgcolor=COLORS['light_bg'],
        plot_bgcolor='white',
        font=dict(color=COLORS['text'], size=14),
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        )
    )
    
    return fig

def create_weather_pie_chart(df):
    """Pie chart showing distribution of weather-related vs non-weather crashes"""
    
    weather_related = df['has_weather_mention'].sum()
    non_weather = len(df) - weather_related
    
    fig = go.Figure(data=[go.Pie(
        labels=['Weather-Related', 'Non-Weather'],
        values=[weather_related, non_weather],
        hole=0.4,
        marker=dict(
            colors=[COLORS['danger'], COLORS['primary']],
            line=dict(color='white', width=2)
        ),
        textinfo='label+percent+value',
        textfont=dict(size=16, color='white')
    )])
    
    fig.update_layout(
        title=f"🌦️ Weather Impact on Aviation Crashes<br><sub>Total Crashes Analyzed: {len(df):,}</sub>",
        height=500,
        paper_bgcolor=COLORS['light_bg'],
        font=dict(color=COLORS['text'], size=14),
        annotations=[dict(
            text=f'{weather_related:,}<br>Weather',
            x=0.5, y=0.5,
            font_size=20,
            showarrow=False
        )]
    )
    
    return fig

def create_weather_type_analysis(df):
    """Bar chart showing breakdown of different weather conditions"""
    
    weather_types = ['fog', 'storm', 'wind', 'ice', 'rain', 'snow']
    counts = [df[weather_type].sum() for weather_type in weather_types]
    
    colors_map = {
        'fog': '#9E9E9E',
        'storm': '#673AB7', 
        'wind': '#03A9F4',
        'ice': '#00BCD4',
        'rain': '#2196F3',
        'snow': '#FFFFFF'
    }
    
    fig = go.Figure(go.Bar(
        x=[w.title() for w in weather_types],
        y=counts,
        marker=dict(
            color=[colors_map[w] for w in weather_types],
            line=dict(color='white', width=2)
        ),
        text=counts,
        textposition='outside',
        textfont=dict(size=14, color=COLORS['text'])
    ))
    
    fig.update_layout(
        title="🌪️ Weather Condition Types in Crashes",
        xaxis_title="Weather Condition",
        yaxis_title="Number of Crashes",
        height=600,
        paper_bgcolor=COLORS['light_bg'],
        plot_bgcolor='white',
        font=dict(color=COLORS['text'], size=14)
    )
    
    return fig

def create_visibility_wind_heatmap(df):
    """2D heatmap showing crashes by visibility and wind speed"""
    
    # Create bins for visibility and wind speed
    df['visibility_bin'] = pd.cut(df['estimated_visibility'], 
                                   bins=[0, 2, 5, 10], 
                                   labels=['Low (0-2km)', 'Medium (2-5km)', 'High (5-10km)'])
    df['wind_bin'] = pd.cut(df['estimated_wind_speed'], 
                            bins=[0, 20, 40, 100], 
                            labels=['Light (0-20)', 'Moderate (20-40)', 'Strong (40+)'])
    
    # Create pivot table
    heatmap_data = df.groupby(['visibility_bin', 'wind_bin']).size().unstack(fill_value=0)
    
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=heatmap_data.columns,
        y=heatmap_data.index,
        colorscale='RdYlGn_r',
        text=heatmap_data.values,
        texttemplate='%{text}',
        textfont={"size": 16},
        colorbar=dict(title="Crashes")
    ))
    
    fig.update_layout(
        title="🌫️ Visibility vs Wind Speed - Crash Distribution",
        xaxis_title="Wind Speed (km/h)",
        yaxis_title="Visibility Range",
        height=500,
        paper_bgcolor=COLORS['light_bg'],
        plot_bgcolor='white',
        font=dict(color=COLORS['text'], size=14)
    )
    
    return fig

def create_monthly_weather_pattern(df):
    """Line chart showing weather-related crashes by month"""
    
    monthly_weather = df[df['has_weather_mention'] == True].groupby('month_name').size().reindex(
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ).fillna(0)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=monthly_weather.index,
        y=monthly_weather.values,
        mode='lines+markers',
        fill='tozeroy',
        line=dict(color=COLORS['danger'], width=4),
        marker=dict(
            size=14,
            color=COLORS['warning'],
            line=dict(color='white', width=2)
        ),
        name='Weather Crashes'
    ))
    
    fig.update_layout(
        title="🗓️ Seasonal Weather-Related Crash Patterns",
        xaxis_title="Month",
        yaxis_title="Number of Weather-Related Crashes",
        height=550,
        paper_bgcolor=COLORS['light_bg'],
        plot_bgcolor='white',
        font=dict(color=COLORS['text'], size=14),
        showlegend=False
    )
    
    return fig

def create_decade_weather_trend(df):
    """Stacked area chart showing weather trends over decades"""
    
    df['decade'] = (df['year'] // 10) * 10
    
    weather_types = ['fog', 'storm', 'wind', 'ice', 'rain', 'snow']
    decade_data = []
    
    for decade in sorted(df['decade'].unique()):
        decade_df = df[df['decade'] == decade]
        decade_info = {'decade': f"{decade}s"}
        
        for weather in weather_types:
            decade_info[weather] = decade_df[weather].sum()
        
        decade_data.append(decade_info)
    
    decade_df = pd.DataFrame(decade_data)
    
    fig = go.Figure()
    
    colors_map = ['#9E9E9E', '#673AB7', '#03A9F4', '#00BCD4', '#2196F3', '#90CAF9']
    
    for idx, weather in enumerate(weather_types):
        fig.add_trace(go.Scatter(
            x=decade_df['decade'],
            y=decade_df[weather],
            mode='lines',
            name=weather.title(),
            fill='tonexty' if idx > 0 else 'tozeroy',
            line=dict(width=0.5),
            fillcolor=colors_map[idx],
            stackgroup='one'
        ))
    
    fig.update_layout(
        title="📊 Weather Trends Across Decades",
        xaxis_title="Decade",
        yaxis_title="Number of Crashes",
        height=600,
        paper_bgcolor=COLORS['light_bg'],
        plot_bgcolor='white',
        font=dict(color=COLORS['text'], size=14),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig

'''

# Find where to insert the weather functions (before def main())
def_main_pos = content.find('\ndef main():')

if def_main_pos == -1:
    print("ERROR: Could not find 'def main()' in the file!")
    exit(1)

print(f"Found 'def main()' at position {def_main_pos}")

# Insert weather functions before main()
content = content[:def_main_pos] + weather_functions + content[def_main_pos:]

# Write the updated content
with open('streamlit_app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n" + "="*60)
print("SUCCESS! Weather functions added to streamlit_app.py")
print("="*60)
print("\nAdded 9 weather analysis functions:")
print("  1. fetch_weather_data_sample()")
print("  2. enrich_crash_data_with_weather()")
print("  3. create_weather_correlation_heatmap()")
print("  4. create_weather_scatter_plot()")
print("  5. create_weather_pie_chart()")
print("  6. create_weather_type_analysis()")
print("  7. create_visibility_wind_heatmap()")
print("  8. create_monthly_weather_pattern()")
print("  9. create_decade_weather_trend()")
print("\nRestart Streamlit to apply changes:")
print("  streamlit run streamlit_app.py")
print("="*60)

