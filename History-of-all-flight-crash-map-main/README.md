# ✈️ BUDDHA PROJECT - Aviation Crash Analytics Dashboard

> **Interactive analytics dashboard for historical aviation accident data from 1908 to 2022**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.15%2B-3F4F75.svg)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🚀 Project Overview

The **BUDDHA PROJECT** is a comprehensive aviation safety analytics dashboard that visualizes over **100 years of historical airplane crash data**. Built with Streamlit and Plotly, it provides researchers, analysts, and aviation professionals with powerful tools to explore trends, causes, and patterns in aviation accidents.

### 🎯 Key Features

- **🌍 3D Interactive Globe**: Geospatial visualization of crashes worldwide
- **🏁 Racing Stick Animation**: Dual transparent animated charts (purple crashes vs blue fatalities)
- **🎯 Multi-Dimensional Analysis**: Crash reasons, trends, and patterns
- **💰 Cost Breakdown**: Financial impact analysis ($50M per crash + $1.5M per fatality)
- **📊 Multiple Chart Types**: Pie, bar, line, area, and stacked visualizations
- **🎮 Interactive Controls**: Year range selectors, speed controls, and real-time filtering

## 📸 Screenshots

### Dashboard Overview
The dashboard features 5 main tabs with comprehensive analytics:

1. **3D Globe Tab**: Interactive Earth visualization with clickable crash markers
2. **Racing Sticks Tab**: Animated purple (crashes) vs blue (fatalities) racing bars
3. **Crash Reasons Tab**: Multi-colored stick charts and categorical analysis
4. **Fatality Trends Tab**: Time-series analysis with area charts
5. **Cost Breakdown Tab**: Financial impact and airline risk assessment

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Python web framework
- **Visualization**: [Plotly](https://plotly.com/) - Interactive charts and graphs
- **Data Processing**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Mapping**: [Folium](https://folium.readthedocs.io/) - 3D geographic visualization

## 📋 Prerequisites

- **Python 3.8 or higher**
- **pip** package manager
- **Git** (for cloning the repository)

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/buddha-aviation-dashboard.git
cd buddha-aviation-dashboard
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Dashboard
```bash
streamlit run streamlit_app.py
```

### 4. Open in Browser
The dashboard will automatically open at: `http://localhost:8501`

## 📁 Project Structure

```
BUDDHA PROJECT/
├── streamlit_app.py        # Main application entry point
├── dataset.csv.csv         # Historical aviation crash data (1908-2022)
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## 🎮 Usage Guide

### Navigation
The dashboard is organized into **5 main tabs**:

#### 🌍 3D Globe Tab
- **Interactive Earth**: Click on markers to see crash details
- **Year Selector**: Filter data by specific years
- **Color Coding**: Marker size and color represent fatality count

#### 🏁 Racing Sticks Tab
- **Animated Racing**: Watch purple (crashes) vs blue (fatalities) bars race through time
- **Speed Controls**: Adjust animation speed (Fast: 0.8s, Normal: 2s, Slow: 4s)
- **Timeline Slider**: Navigate through years manually
- **Play/Pause**: Full control over animation playback

#### 🎯 Crash Reasons Tab
- **Multi-Colored Stick Chart**: Color-coded by crash causes (Weather, Mechanical, Human Error, Fire, Other)
- **Interactive Filtering**: Year range slider affects all visualizations
- **Multiple Views**: Pie charts, bar charts, line graphs, and aircraft type analysis

#### 💀 Fatality Trends Tab
- **Time-Series Analysis**: Area charts showing fatality trends over time
- **Pattern Recognition**: Identify peaks and valleys in aviation safety

#### 💰 Cost Breakdown Tab
- **Financial Impact**: Estimated costs per airline and crash
- **Risk Analysis**: Scatter plots showing crash count vs fatality rates
- **Year Filtering**: Analyze costs for specific time periods

### Interactive Features
- **Real-Time Filtering**: All charts update dynamically with user selections
- **Responsive Design**: Works on desktop and mobile devices
- **Professional Styling**: Light blue gradient theme with modern aesthetics
- **Smooth Animations**: Cubic-in-out easing for professional transitions

## 📊 Data Information

The dashboard analyzes **historical aviation crash data** including:
- **Time Range**: 1908 - 2022 (114+ years)
- **Geographic Coverage**: Worldwide incidents
- **Data Points**: Date, Location, Operator, Aircraft Type, Casualties, Crash Summary
- **Records**: 5,000+ aviation incidents

## 🌟 Check Out My Live Project! 🌟

I’ve built an interactive web app to explore global flight crash data! 🚀  

**🔗 [Flight Crash Mapped](https://flightcrashmapped.streamlit.app/)**  

### 🔹 Project Preview
Click to see screenshots from the app:

![Preview 1](https://raw.githubusercontent.com/vinaysingh282006/History-of-all-flight-crash-map/main/webpreview1.png)
![Preview 2](https://raw.githubusercontent.com/vinaysingh282006/History-of-all-flight-crash-map/main/webpreview2.png)
![Preview 3](https://raw.githubusercontent.com/vinaysingh282006/History-of-all-flight-crash-map/main/webpreview3.png)
![Preview 4](https://raw.githubusercontent.com/vinaysingh282006/History-of-all-flight-crash-map/main/webpreview4.png)


> Built with **Streamlit** for interactive maps, data visualization, and insights. Explore, analyze, and visualize flight crash data globally. 🌍📊


### Data Fields
- `Date`: Incident date
- `Location`: Geographic location of crash
- `Operator`: Airline or operator involved
- `Type`: Aircraft model/type
- `Aboard`: Total people on board
- `Fatalities`: Number of fatalities
- `Summary`: Incident description and probable cause

## 🎨 Customization

### Color Themes
The dashboard uses a professional color palette:
- **Primary**: `#2E86AB` (Blue)
- **Secondary**: `#A23B72` (Purple)
- **Accent**: `#F18F01` (Orange)
- **Success**: `#4CAF50` (Green)
- **Warning**: `#FF9800` (Orange)
- **Danger**: `#F44336` (Red)

### Chart Sizing
All visualizations follow large sizing standards:
- **Standard Charts**: 600-700px height
- **Featured Charts**: 800px height
- **Racing Animation**: 800px height
- **Full-width displays** for maximum impact

## 🔧 Development

### Adding New Features
The dashboard follows a modular architecture:
1. **Data Functions**: Add new data processing in the load_data() function
2. **Visualization Functions**: Create new chart functions following existing patterns
3. **Tab Integration**: Add new tabs in the main() function
4. **Styling**: Maintain consistent color schemes and sizing

### Performance Optimization
- **Data Caching**: Uses `@st.cache_data` for efficient data loading
- **Selective Rendering**: Charts update only when necessary
- **Memory Management**: Efficient data structures and processing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Data Source**: Historical aviation accident records
- **Streamlit Community**: For the excellent web framework
- **Plotly Team**: For powerful visualization capabilities
- **Open Source Contributors**: For the amazing Python ecosystem

## 📞 Support

For questions, issues, or contributions:
- **GitHub Issues**: [Report bugs or request features](https://github.com/yourusername/buddha-aviation-dashboard/issues)
- **Documentation**: Check this README for detailed usage instructions
- **Community**: Join discussions in the GitHub repository

---

**Made with ❤️ for aviation safety research and data analysis**

> *"In aviation, every accident teaches us something new. This dashboard helps us learn from history to build a safer future."*
