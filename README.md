# 🏆 NBA Game Win Predictor: 2025 Finals Edition  
### *"Predicting Playoff Outcomes, One Game at a Time — Again."*

Ever watched tip-off and wondered: *"Who's actually going to win this?"*  
This project uses real-time NBA data and machine learning to predict the outcome of each **2025 NBA Finals** game between the **Indiana Pacers** and the **Oklahoma City Thunder**.

> 📈 *Follow-up to the Eastern Conference Finals project (66.7% accuracy!). This time, we're running it back for the championship.*

---

## 📦 What This Repo Contains

This repo includes prediction files for **Games 1 through 7** of the 2025 NBA Finals.

Each `.py` file:
- Pulls updated game stats via [`nba_api`](https://github.com/swar/nba_api)
- Computes rolling team averages over the last `n` games (FG%, REB, AST, STL, etc.)
- Trains a `RandomForestClassifier` model per team based on win history
- Outputs **normalized win probabilities** for each game
- Includes visualizations (in select files) to track stat trends and playoff momentum

---

## 🧠 Why I Built This

After predicting the 2025 Eastern Conference Finals, I wanted to continue exploring:
- **How stats reflect team performance under extreme pressure**
- **Whether machine learning can help fans predict outcomes with more insight**
- **How far predictive modeling can go using just team-level stats + momentum**


---

## 🔮 How It Works

Each game prediction script:
1. Pulls season stats for each team
2. Filters for games after the season start (e.g., `2024-10-21`)
3. Calculates recent averages over the last 18 playoff games
4. Trains a `RandomForestClassifier` to model win outcomes
5. Predicts and normalizes win probabilities per matchup
6. *(Optional)* Generates plots using `matplotlib` / `seaborn`

---

## 📊 Game Predictions: 2025 NBA Finals

*This section will be updated as each game is predicted and played.*  

| Game | Thunder Win % | Pacers Win % | Predicted Winner | Actual Outcome | Prediction Accuracy |
|------|----------------|----------------|------------------|----------------|---------------------|
| 1    | TBD            | TBD            | TBD              | TBD            | —                   |
| 2    | TBD            | TBD            | TBD              | TBD            | —                   |
| 3    | TBD            | TBD            | TBD              | TBD            | —                   |
| 4    | TBD            | TBD            | TBD              | TBD            | —                   |
| 5    | TBD            | TBD            | TBD              | TBD            | —                   |
| 6    | TBD            | TBD            | TBD              | TBD            | —                   |
| 7    | TBD            | TBD            | TBD              | TBD            | —                   |

> Results will be filled in as the series progresses. Final model accuracy will be reported after the last game.

---

## 📊 Visuals (in select files)

- FG% and 3PT% over recent games  
- Turnovers, Assists, and Rebounds  
- Plus/Minus momentum indicators  

> *Note: Not every script includes graphs yet — stay tuned as the series unfolds.*

---

## ⚙️ Tech Stack

- Python  
- `nba_api` for pulling game data  
- `pandas`, `numpy` for data wrangling  
- `scikit-learn` for modeling  
- `matplotlib`, `seaborn` for visualizations

---

## 📌 Future Goals

- Add a **Tableau dashboard** to explore series predictions interactively  
- Include **player-level data** for more detailed modeling  
- Add **Monte Carlo simulations** to predict full series outcomes probabilistically  
- Generalize this system for **season-long or bracket-wide** prediction tooling
