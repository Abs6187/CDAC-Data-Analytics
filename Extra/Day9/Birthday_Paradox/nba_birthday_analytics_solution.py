"""
Title: NBA Player Biographical & Birthday Paradox Analysis (Complete Solution)
Description: A modular Python script for loading, sanitizing, and analyzing 
             NBA player birth dates to explore shared birthdays and player lookups.

"""

import pandas as pd
import datetime

# ==========================================
# SUB-STEP FUNCTIONS (The Lifecycle Phases)
# ==========================================

def phase_1_discovery_and_sanitization(file_path):
    """
    [Phase 1] Data Discovery, Column Standardization & Sanitization (5 Marks)
    - Load the NBA player CSV file.
    - Standardize column names (snake_case, lowercased).
    - Sanitize player names (remove trailing asterisks) and parse birth dates.

    """
    print("\n[PHASE 1] Discovery, Column Standardization & Sanitization (5 Marks)")
    print("-" * 65)
    
    try:
        df = pd.read_csv(file_path)
        print(f"-> Successfully loaded dataset from: '{file_path}'")
    except FileNotFoundError:
        print(f"-> Error: File '{file_path}' not found. Please ensure the CSV file is present.")
        raise
        
    # Standardize column headers: strip whitespace, lowercase, replace spaces with underscores
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    print(f"-> Standardized Columns: {list(df.columns)}")
    
    # Sanitize player names (remove Hall of Fame asterisk '*' if present)
    if 'player' in df.columns:
        df['player'] = df['player'].str.replace('*', '', regex=False).str.strip()
        
    # Sanitize and parse 'birth_date' into standard datetime format
    if 'birth_date' in df.columns:
        df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')
        
    print(f"-> Dataset Shape: {df.shape[0]} players, {df.shape[1]} attributes")
    
    # Check for missing birth dates
    missing_births = df['birth_date'].isnull().sum()
    print(f"-> Missing Birth Dates Found: {missing_births}")
    
    return df


def phase_2_birthday_paradox_analysis(df):
    """
    [Phase 2] Birthday Paradox & Date Distribution (10 Marks)
    - Extract month and day components to analyze date frequencies.
    - Identify shared birthdays across the dataset.

    """
    print("\n[PHASE 2] Birthday Paradox & Date Distribution (10 Marks)")
    print("-" * 65)
    
    # Extract Month-Day string format ('MM-DD') for birthday matching
    df['birth_month_day'] = df['birth_date'].dt.strftime('%m-%d')
    
    # Find shared birthdays (duplicate month-day combinations across players)
    shared_birthdays = df[df.duplicated(subset=['birth_month_day'], keep=False)].sort_values('birth_month_day')
    
    unique_birthdays = df['birth_month_day'].nunique()
    total_players = df.shape[0]
    
    print(f"-> Total Players Analyzed: {total_players}")
    print(f"-> Unique Birthday Combinations (Month-Day): {unique_birthdays}")
    print(f"-> Players sharing a birthday with at least one other player: {len(shared_birthdays)}")
    
    if not shared_birthdays.empty:
        print("\n   Sample Shared Birthdays (First 5 matches):")
        print(shared_birthdays[['player', 'birth_date', 'colleges']].head(5).to_string(index=False))
        
    return df


def phase_3_player_lookup_system(df, player_name):
    """
    [Phase 3] Player Detail Retrieval (10 Marks)
    - Search for a specific player by name (case-insensitive substring match).
    - Retrieve biographical details.

    """
    print(f"\n[PHASE 3] Player Lookup: Searching for '{player_name}' (10 Marks)")
    print("-" * 65)
    
    # Filter dataframe for matching player names
    match = df[df['player'].str.contains(player_name, case=False, na=False)]
    
    if match.empty:
        print(f"-> No player found matching '{player_name}'.")
        return None
        
    print(f"-> Found {len(match)} matching record(s):")
    for idx, row in match.iterrows():
        b_date_str = row['birth_date'].strftime('%B %d, %Y') if pd.notnull(row['birth_date']) else 'Unknown'
        print(f"   * Player: {row['player']}")
        print(f"     Position: {row['pos']} | Height: {row['ht']} | Weight: {row['wt']} lbs")
        print(f"     College: {row['colleges']} | Career Active: {row['from']} - {row['to']}")
        print(f"     Birth Date: {b_date_str}")
        
    return match.iloc[0]


def phase_4_shared_birthday_cohort(df, player_name):
    """
    [Phase 4] Shared Birthday Peer Finder (10 Marks)
    - Identify the target player's birth date.
    - List all other NBA players sharing that exact birth date.

    """
    print(f"\n[PHASE 4] Shared Birthday Cohort for '{player_name}' (10 Marks)")
    print("-" * 65)
    
    match = df[df['player'].str.contains(player_name, case=False, na=False)]
    if match.empty:
        print("-> Target player not found for cohort matching.")
        return
        
    target_player_row = match.iloc[0]
    target_birth_date = target_player_row['birth_date']
    
    if pd.isnull(target_birth_date):
        print(f"-> Target player '{target_player_row['player']}' has an invalid birth date.")
        return
        
    target_month_day = target_player_row['birth_month_day']
    target_date_formatted = target_birth_date.strftime('%B %d')
    
    # Find all players sharing the exact same Month and Day
    peers = df[(df['birth_month_day'] == target_month_day) & (df['player'] != target_player_row['player'])]
    
    print(f"-> Target Player: {target_player_row['player']} (Born: {target_birth_date.strftime('%B %d, %Y')})")
    print(f"-> Other NBA players born on {target_date_formatted} (regardless of year): {len(peers)}")
    
    if not peers.empty:
        print("\n   Peer Players with Matching Birthdays:")
        for idx, row in peers.iterrows():
            year_born = row['birth_date'].strftime('%Y') if pd.notnull(row['birth_date']) else 'Unknown'
            print(f"   - {row['player']} (Born: {year_born}, College: {row['colleges']}, Active: {row['from']}-{row['to']})")
    else:
        print(f"-> No other players in the dataset share this exact birthday ({target_date_formatted}).")


def phase_5_evaluation_and_summary(df):
    """

    - Summarize statistical findings on birthday distributions and dataset hygiene.

    """
    print("\n[PHASE 5] Evaluation & Summary Reporting (5 Marks)")
    print("-" * 65)
    
    total_records = df.shape[0]
    valid_dates = df['birth_date'].notnull().sum()
    duplicate_days_count = df['birth_month_day'].duplicated().sum()
    
    print(f"-> Summary Metrics:")
    print(f"   * Total Records Processed: {total_records}")
    print(f"   * Successfully Parsed Birth Dates: {valid_dates}")
    print(f"   * Coinciding Birthday Instances (Birthday Paradox occurrences): {duplicate_days_count}")
    print("\n-> Analytical Conclusion: Even in relatively small subsets of biographical data, shared calendar birthdays emerge frequently, illustrating the core probabilistic principles of the Birthday Paradox.")


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_analytics_lifecycle():
    """
    Facade function coordinating the NBA analytics and birthday lookup workflow.
    """
    print("=" * 65)
    print("STARTING NBA BIRTHDAY & BIOGRAPHICAL LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)
    
    # File path for NBA dataset
    file_path = 'nba_players.csv'  # Replace with actual CSV path if named differently
    
    # Target player for lookup and cohort matching demonstration
    target_player = "Kareem Abdul-Jabbar"
    
    # Executing phases chronologically
    df = phase_1_discovery_and_sanitization(file_path)
    df = phase_2_birthday_paradox_analysis(df)
    phase_3_player_lookup_system(df, target_player)
    phase_4_shared_birthday_cohort(df, target_player)
    phase_5_evaluation_and_summary(df)
    
    print("\n" + "=" * 65)
    print("NBA BIRTHDAY ANALYTICS LIFECYCLE COMPLETED SUCCESSFULLY")
    print("=" * 65)


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_analytics_lifecycle()