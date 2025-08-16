# ⚽ Football Datasets Downloader

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data Source](https://img.shields.io/badge/Data%20Source-football--data.co.uk-green.svg)](http://www.football-data.co.uk/)

A comprehensive Python tool to automatically download historical football (soccer) datasets from **football-data.co.uk** spanning **1993–2025**. Get match results, detailed statistics, and betting odds for Europe's top leagues in minutes!

---

## 🎯 Features

- **🏆 Complete Coverage**: Download 30+ years of football data (1993-2025)
- **⚡ Automated Downloads**: One command downloads everything
- **📊 Rich Statistics**: Match results, team stats, referee data, and more
- **💰 Betting Odds**: Historical odds from multiple bookmakers
- **🔄 Resume Support**: Skip already downloaded files
- **📁 Auto-Organization**: Data sorted by league and season
- **🛡️ Error Handling**: Robust download with retry mechanism

---

## 📈 Perfect For

| Use Case | Description |
|----------|-------------|
| **Sports Analytics** | Analyze team performance, trends, and patterns |
| **Machine Learning** | Train models for match prediction and analysis |
| **Data Science Projects** | Football statistics research and visualization |
| **Betting Research** | Historical odds analysis and modeling |
| **Academic Research** | Sports science and performance studies |

---

## 🏆 Available Leagues

| League | Country | Code | Years Available | Matches per Season |
|--------|---------|------|-----------------|-------------------|
| **Premier League** | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 England | E0 | 1993-2025 | ~380 |
| **Ligue 1** | 🇫🇷 France | F1 | 1993-2025 | ~380 |
| **Bundesliga** | 🇩🇪 Germany | D1 | 1993-2025 | ~306 |
| **Serie A** | 🇮🇹 Italy | I1 | 1993-2025 | ~380 |

**Total**: 32+ seasons × 4 leagues = **~48,000+ matches** with complete statistics!

---

## 📊 Data Features

### Match Information
- **Basic Data**: Date, teams, final score, half-time score
- **Match Officials**: Referee assignments
- **Attendance**: Stadium attendance figures
- **Result Categories**: Home win (H), Draw (D), Away win (A)

### Detailed Statistics
- **Shots**: Total shots, shots on target
- **Corners**: Corner kicks for both teams  
- **Cards**: Yellow and red cards
- **Fouls**: Fouls committed by each team

### Betting Odds (Multiple Bookmakers)
- **1X2 Odds**: Home win, Draw, Away win
- **Asian Handicap**: Spread betting odds
- **Over/Under**: Total goals betting lines
- **Bookmakers**: Bet365, Pinnacle, William Hill, and more

---

## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.6 or higher
python --version

# Install required packages
pip install requests
```

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/sosthene14/footballdataset.git
cd footballdataset
```

2. **Run the downloader**:
```bash
python download_all_datasets.py
```

3. **Access your data**:
```bash
# Data will be organized in the datasets/ folder
ls datasets/
```

---

## 📁 Project Structure

```
football-datasets-downloader/
├── 📄 README.md                    # This comprehensive guide
├── 🐍 download_all_datasets.py     # Main download script
├── 📄 requirements.txt             # Python dependencies
├── 📄 LICENSE                      # MIT License
├── 📂 datasets/                    # Downloaded data (created automatically)
│   ├── 🏴󠁧󠁢󠁥󠁮󠁧󠁿 premier_league_data/
│   │   ├── premier_league_1993-94.csv
│   │   ├── premier_league_1994-95.csv
│   │   └── ... (all seasons)
│   ├── 🇫🇷 ligue1_match_data/
│   ├── 🇩🇪 bundesliga1_statistics/
│   ├── 🇮🇹 seriea_historical_data/
│   └── 📄 column_descriptions.txt  # Detailed data dictionary
└── 📂 examples/                    # Usage examples (optional)
    ├── basic_analysis.py
    └── visualization_example.py
```

---

## 🔧 Configuration Options

### Custom League Selection
```python
# Modify in download_all_datasets.py
LEAGUES = {
    'E0': 'premier_league_data',      # Enable/disable leagues
    'F1': 'ligue1_match_data',        # by commenting out lines
    'D1': 'bundesliga1_statistics',
    'I1': 'seriea_historical_data'
}
```
 
## 📈 Data Analysis Examples

 
```

### Top Scorers Analysis
```python
# Analyze high-scoring matches
high_scoring = df[(df['FTHG'] + df['FTAG']) >= 5]
print(f"Matches with 5+ goals: {len(high_scoring)}")
```

---

## 📋 Data Dictionary

| Column | Description | Example |
|--------|-------------|---------|
| `Date` | Match date | 14/08/2023 |
| `HomeTeam` | Home team name | Arsenal |
| `AwayTeam` | Away team name | Man City |
| `FTHG` | Full time home goals | 2 |
| `FTAG` | Full time away goals | 1 |
| `FTR` | Full time result (H/D/A) | H |
| `HTHG` | Half time home goals | 1 |
| `HTAG` | Half time away goals | 0 |
| `HTR` | Half time result | H |
| `HS` | Home team shots | 15 |
| `AS` | Away team shots | 8 |
| `HST` | Home shots on target | 7 |
| `AST` | Away shots on target | 3 |
| `HC` | Home team corners | 6 |
| `AC` | Away team corners | 4 |
| `HF` | Home team fouls | 12 |
| `AF` | Away team fouls | 18 |
| `HY` | Home team yellow cards | 2 |
| `AY` | Away team yellow cards | 4 |
| `HR` | Home team red cards | 0 |
| `AR` | Away team red cards | 1 |
| `B365H` | Bet365 home win odds | 2.10 |
| `B365D` | Bet365 draw odds | 3.40 |
| `B365A` | Bet365 away win odds | 3.75 |

**📄 Complete data dictionary available in `datasets/column_descriptions.txt`**

---

## ⚙️ Requirements

Create a `requirements.txt` file:

```txt
requests>=2.25.1
tqdm>=4.62.0
pandas>=1.3.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 Bug Reports
- Use GitHub Issues to report bugs
- Include Python version and error messages
- Provide steps to reproduce

### ✨ Feature Requests
- Additional leagues (Championship, La Liga, etc.)
- Data export formats (JSON, SQLite)
- Advanced filtering options
- Data validation tools

### 🔧 Pull Requests
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push to branch: `git push origin feature-name`
5. Open a Pull Request

---

  

### Getting Help
- 📖 Check existing [GitHub Issues](https://github.com/your-username/football-datasets-downloader/issues)
- 💬 Create a new issue with detailed information
- 📧 Contact: sosthenemounsambote14@gmail.com

---

## 📊 Data Source & Credits

**Data Source**: [football-data.co.uk](http://www.football-data.co.uk/)
- Trusted provider of historical football data
- Updated regularly with latest match results
- Includes comprehensive betting odds from major bookmakers

**Acknowledgments**:
- Football-Data.co.uk for providing free historical data
- The Python community for excellent libraries
- Contributors and users of this project

---

## ⚖️ Legal & Usage

### License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### Data Usage Policy
- ✅ Personal analysis and research
- ✅ Academic and educational purposes  
- ✅ Open source projects
- ⚠️ Commercial use: Check football-data.co.uk terms
- ❌ Redistribution without attribution

### Disclaimer
This tool downloads publicly available data from football-data.co.uk. Users are responsible for complying with the source website's terms of service.

---

 

### Version History
- **v1.0.0** (2025): Initial release with 5 major leagues
- **v1.1.0** (planned): Additional leagues and export formats

---

## 🌟 Star History

If this project helps you, please consider giving it a ⭐ on GitHub!

 ## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=sosthene14/footballdataset&type=Date)](https://www.star-history.com/#sosthene14/footballdataset&Date)
---

## 📞 Contact

**Project Maintainer**: Sosthene Mounsambote 
**Email**: sosthenemounsambote14@gmail.com  
**GitHub**: [@sosthene14](https://github.com/sosthene14)  
**LinkedIn**: [sosthene mounsambote](https://sn.linkedin.com/in/sosthene-mounsambote-311171248)

---

<div align="center">

**⚽ Happy Data Analysis! ⚽**

*Built with ❤️ for the football data community*

[⬆ Back to Top](#-footballdataset)

</div>